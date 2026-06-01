from __future__ import annotations

from typing import Any, Dict, List


class IncompleteTruthReasoner:
    """Detects weak truth, not just missing files.

    Incomplete truth includes duplicated functional truths, placeholder-like files,
    conflict candidates, missing local standards, weak single-source evidence, and
    high-similarity artifacts that represent different functional paths.
    """

    def detect(self, requirement: Dict[str, Any], artifact_matrix: Dict[str, Any] | None = None, truth_store: Dict[str, Any] | None = None, semantics: Dict[str, Any] | None = None) -> Dict[str, Any]:
        matrix = artifact_matrix or {}
        semantics = semantics or {}
        issues: List[Dict[str, Any]] = []

        for item in semantics.get('empty_declared_targets', [])[:100]:
            issues.append({
                'code': 'empty_declared_target_truth',
                'severity': 'maturity',
                'path': item.get('path'),
                'reason': 'Empty governed artifact is a declared construction target, not completed truth.',
                'interpretation': 'Keep it visible as a target to mature. Do not ignore it and do not invent its missing logic.',
                'decision': 'MATURE',
            })

        for item in semantics.get('declared_missing_artifacts', [])[:100]:
            issues.append({
                'code': 'declared_but_missing_artifact',
                'severity': 'maturity',
                'path': item.get('declared_in'),
                'missing_path': item.get('normalized_path'),
                'reason': 'A governed artifact declares a related/child artifact that is not present.',
                'interpretation': 'This is a broken truth promise. Create, defer, or repair the declared artifact before relying on that branch.',
                'decision': 'MATURE',
            })

        duplicates = matrix.get('duplicate_scan') or {}
        for item in duplicates.get('duplicates', [])[:50]:
            paths = item.get('paths') or []
            if len(paths) < 2:
                continue
            functional_divergence = self._functional_divergence(paths)
            issues.append({
                'code': 'duplicate_or_near_duplicate_truth',
                'severity': 'maturity',
                'paths': paths,
                'reason': 'Multiple artifacts share very similar content.',
                'interpretation': 'If paths represent different functional truths, this is not reusable truth; it is likely placeholder, copy, or underdeveloped truth.',
                'functional_divergence_hint': functional_divergence,
                'decision': 'MATURE',
            })

        conflict_scan = matrix.get('conflict_scan') or {}
        for item in conflict_scan.get('conflicts', [])[:50]:
            issues.append({
                'code': 'conflict_candidate',
                'severity': 'maturity',
                'paths': item.get('paths') or [],
                'reason': item.get('reason') or 'Conflict candidate found.',
                'decision': 'MATURE',
            })

        diagnostics = matrix.get('diagnostics') or {}
        for item in diagnostics.get('issues', [])[:100]:
            if item.get('code') in {'placeholder_content', 'placeholder_file', 'weak_layer_identity', 'duplicate_content'} or item.get('severity') in {'maturity','blocker'}:
                issues.append({
                    'code': f"diagnostic_{item.get('code')}",
                    'severity': item.get('severity','maturity'),
                    'path': item.get('path'),
                    'reason': item.get('message') or item.get('recommendation') or 'Diagnostic indicates incomplete truth.',
                    'decision': 'BLOCK' if item.get('severity') == 'blocker' else 'MATURE',
                })

        records = matrix.get('records') or []
        placeholder_records = [r for r in records if any('placeholder' in str(i).lower() for i in (r.get('issues') or []))]
        for r in placeholder_records[:50]:
            issues.append({
                'code': 'placeholder_artifact_truth',
                'severity': 'maturity',
                'path': r.get('path'),
                'reason': 'Artifact carries placeholder markers and cannot be treated as complete truth.',
                'decision': 'MATURE',
            })

        depth = int(requirement.get('truth_depth') or 2)
        if depth >= 3:
            relationship = self._relationship_signal(matrix, semantics)
            if not relationship.get('has_relational_evidence'):
                issues.append({
                    'code': 'insufficient_relational_truth',
                    'severity': 'maturity',
                    'reason': 'Intent requires relational truth but artifact evidence lacks enough relationship signals.',
                    'decision': 'MATURE',
                })

        truth_store = truth_store or {}
        if depth >= 4 and not any(truth_store.get(k) for k in ('facts','decisions','conflicts','assumptions')):
            issues.append({
                'code': 'missing_truth_store_context',
                'severity': 'maturity',
                'reason': 'Higher-depth request has no recorded local truth store facts/decisions/assumptions.',
                'decision': 'MATURE',
            })

        blockers = [i for i in issues if i.get('decision') == 'BLOCK']
        maturity = [i for i in issues if i.get('decision') == 'MATURE']
        return {
            'status': 'blocked' if blockers else ('mature_required' if maturity else 'clear'),
            'issue_count': len(issues),
            'blocking_count': len(blockers),
            'maturity_issue_count': len(maturity),
            'issues': issues,
        }

    def _functional_divergence(self, paths: List[str]) -> Dict[str, Any]:
        # Generic, project-neutral divergence detection. AOS must not hardcode
        # active-project domain names or sample payload concepts here. It only
        # compares path structure signatures to detect that duplicate content is
        # appearing under distinct functional branches.
        signatures = []
        for p in paths:
            parts = [x for x in p.replace('\\', '/').split('/') if x]
            functional_parts = [
                x.lower() for x in parts[-5:]
                if not x.lower().endswith(('.md', '.yaml', '.json', '.py'))
            ]
            signatures.append({'path': p, 'functional_signature': functional_parts})
        token_sets = {tuple(x['functional_signature']) for x in signatures}
        return {'divergent_functional_paths': len(token_sets) > 1, 'path_signatures': signatures}

    def _relationship_signal(self, matrix: Dict[str, Any], semantics: Dict[str, Any] | None = None) -> Dict[str, Any]:
        signals = 0
        for key in ['call_graph','import_graph','symbol_graph','api_intelligence','database_intelligence','impact_map']:
            v = matrix.get(key) or {}
            if isinstance(v, dict) and any(v.values()):
                signals += 1
        if (semantics or {}).get('declared_edges'):
            signals += 1
        return {'relationship_signal_count': signals, 'has_relational_evidence': signals >= 2}
