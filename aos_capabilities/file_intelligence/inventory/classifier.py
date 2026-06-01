from __future__ import annotations
from typing import Any, Dict, List
from aos_capabilities.file_intelligence.common import CONCEPT_GROUPS

class ContentClassifier:
    def classify(self, text: str) -> Dict[str, Any]:
        low = (text or '').lower()
        concepts: Dict[str, Dict[str, Any]] = {}
        for name, terms in CONCEPT_GROUPS.items():
            hits = [term for term in terms if term.lower() in low]
            if hits:
                concepts[name] = {'hits': hits[:10], 'score': len(hits)}
        placeholder_terms = ['todo','tbd','placeholder','not implemented','coming soon','stub','لاحقاً','لاحقا','مسودة','فارغ','قيد الكتابة']
        readiness_terms = ['acceptance','api','endpoint','database','entity','state','event','permission','test','contract','decision','risk','قبول','واجهة','كيان','حالة','حدث','صلاحية','اختبار','قرار','خطر']
        return {
            'concepts': concepts,
            'placeholder_hits': [t for t in placeholder_terms if t in low],
            'readiness_hits': [t for t in readiness_terms if t in low],
            'content_state': self.content_state(text, concepts),
        }

    def content_state(self, text: str, concepts: Dict[str, Any]) -> str:
        stripped = (text or '').strip()
        if not stripped:
            return 'empty'
        if len(stripped) < 80:
            return 'thin'
        if concepts:
            return 'conceptual_or_implementation_signal'
        return 'content_present_unclassified'
