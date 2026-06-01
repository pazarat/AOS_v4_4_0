from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict


@dataclass(frozen=True)
class PerformanceBudget:
    profile: str
    max_target_ms: int
    artifact_policy: str
    project_truth_policy: str
    second_pass_policy: str
    reason: str

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


class PerformanceBudgetPlanner:
    """Defines hot-path budgets before layer calls.

    The budget is not a timer after the fact; it is a governance decision that
    prevents expensive scans from entering normal answers unless explicitly asked.
    """

    DIAGNOSTIC_TERMS = {'تقرير', 'تشخيص', 'تفاصيل', 'أرقام', 'ارقام', 'audit', 'metrics', 'diagnostic', 'inspect', 'doctor', 'trace'}
    MODIFY_TERMS = {'اصلح', 'أصلح', 'نفذ', 'عدّل', 'عدل', 'patch', 'fix', 'repair', 'implement', 'refactor'}

    def plan(self, surface: str, request_text: str) -> PerformanceBudget:
        text = (request_text or '').lower()
        explicit_diag = any(t in text for t in self.DIAGNOSTIC_TERMS)
        may_modify = any(self._has_term(text, t) for t in self.MODIFY_TERMS)
        if surface == 'aos_environment':
            if explicit_diag or may_modify:
                return PerformanceBudget(
                    profile='runtime_controlled_diagnostic',
                    max_target_ms=5000,
                    artifact_policy='scoped_runtime_fast_value_only',
                    project_truth_policy='forbidden',
                    second_pass_policy='truth_only_no_payload_refocus',
                    reason='runtime diagnostics may inspect scoped runtime files but never active payload truth',
                )
            return PerformanceBudget(
                profile='runtime_hot_answer',
                max_target_ms=2500,
                artifact_policy='skip_artifact_scan_use_truth_context',
                project_truth_policy='forbidden',
                second_pass_policy='disabled_unless_blocker',
                reason='runtime identity/governance answers must be fast and payload-isolated',
            )
        if surface == 'workshop_general_truth':
            return PerformanceBudget(
                profile='workshop_hot_or_scoped',
                max_target_ms=2500,
                artifact_policy='skip_or_scoped_workshop_only',
                project_truth_policy='forbidden',
                second_pass_policy='disabled_unless_blocker',
                reason='workshop questions do not need active payload loading',
            )
        return PerformanceBudget(
            profile='project_normal',
            max_target_ms=4000,
            artifact_policy='fast_value_by_default_deep_only_if_explicit',
            project_truth_policy='allowed_when_loaded',
            second_pass_policy='enabled_for_project_contradictions',
            reason='project answers may load project truth but should still avoid deep diagnostics by default',
        )

    def _has_term(self, text: str, term: str) -> bool:
        if term.isascii():
            return term in text
        # Arabic substring matching is dangerous here: e.g. 'طبق' is inside 'طبقة'.
        return term in text.split()
