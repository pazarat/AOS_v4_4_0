from __future__ import annotations

from typing import Any, Dict, List


class ResponseContractEnforcer:
    """Final visible-response guard.

    This guard does not force a template. It enforces identity truth: the visible
    identity in AOS work is the operational engineer identity, not the generic
    model identity, and project-facing answers must not expose internal paths or
    runtime implementation unless explicitly requested.
    """

    GENERIC_IDENTITY_TERMS = (
        'أنا GPT', 'انا GPT', 'I am GPT', "I'm GPT", 'أنا ChatGPT', 'انا ChatGPT', 'I am ChatGPT',
        'GPT-5.5', 'GPT-4', 'GPT-5', 'OpenAI model', 'نموذج لغوي من OpenAI', 'تقنياً أنا GPT', 'تقنيا أنا GPT'
    )
    AOS_INTERNAL_TERMS = (
        'aos_core', 'aos_capabilities', 'StateGraph', 'IntentEngine', 'SurfaceResolver',
        'operation_packet', 'file intelligence', 'طبقة intent', 'طبقة surface', 'self-check',
        'RUN_TESTS.py', 'Python compile', '.zip', 'AOS_v', 'اختبار الصحة', 'Thought for'
    )
    INTERNAL_PATH_TERMS = (
        'workshop/active_project/PROJECT', 'workshop/active_project', 'aos_identity/',
        'aos_core/', 'aos_capabilities/', 'runtime_state/', 'reports/last_operation_packet.json', 'file_matrix_report', 'doctor_report'
    )
    AOS_AS_PROJECT_TERMS = (
        'فحصت الملف المتاح عندي فعليًا: AOS_', 'فحصت النسخة المتاحة عندي: AOS_',
        'AOS v', 'AOS_v', 'تقييمي الحالي لوضع AOS', 'AOS حاليًا', 'AOS نفسه يبدو',
        'إذا كان قصدك هو تطوير AOS', 'إن كان قصدك هو تطوير AOS', 'تطوير AOS نفسه'
    )

    def enforce(self, text: str, packet: Dict[str, Any]) -> Dict[str, Any]:
        intent = packet.get('intent', {})
        surface = intent.get('surface')
        violations: List[str] = []
        stripped = (text or '').strip()
        lower = stripped.lower()
        first_chunk = stripped[:900]

        for term in self.GENERIC_IDENTITY_TERMS:
            if term.lower() in first_chunk.lower():
                violations.append('generic_model_identity_leak')
                break

        if surface == 'active_project_payload':
            active_state = (((packet.get('scope') or {}).get('active_project_state')) or {}).get('state')
            if active_state == 'no_project_loaded':
                project_claim_terms = ['المشروع الحالي يحتوي', 'المشروع الحالي يبدو', 'داخل المشروع الحالي', 'ملفات المشروع الحالية', 'حسب ملفات مشروعك']
                if any(t in stripped for t in project_claim_terms) and 'لا يوجد مشروع' not in stripped:
                    violations.append('project_claim_without_loaded_project_payload')
            for term in self.AOS_INTERNAL_TERMS:
                if term.lower() in lower:
                    violations.append(f'aos_internal_exposure:{term}')
                    break
            for term in self.INTERNAL_PATH_TERMS:
                if term.lower() in lower:
                    violations.append(f'raw_internal_path_exposure:{term}')
                    break
            for term in self.AOS_AS_PROJECT_TERMS:
                if term.lower() in lower:
                    violations.append('aos_evaluated_as_project')
                    break
            if 'sample_payload' in lower or 'sample_projects' in lower:
                violations.append('sample_path_leaked_into_project_answer')
            if 'aos حاليًا' in lower or 'aos نفسه' in lower or 'تقييمي الحالي لوضع aos' in lower:
                violations.append('aos_evaluated_as_project')
            if 'مشروعك الفعلي' in lower and 'لا يوجد مشروع' not in lower:
                violations.append('claims_user_project_without_loaded_project')

        return {
            'passed': not violations,
            'violations': violations,
            'surface': surface,
            'rule': 'operational_identity_truth_and_silent_surface_contract',
            'truth_grounding_required': True,
            'allowed_claim_grades': ['verified', 'derived', 'assumption', 'unknown', 'blocked'],
        }
