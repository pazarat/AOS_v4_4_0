from __future__ import annotations
import hashlib
from typing import Any, Dict, List
from aos_capabilities.file_intelligence.common import tokenize

class SemanticFingerprinter:
    def fingerprint_text(self, text: str) -> Dict[str, Any]:
        tokens = tokenize(text)
        unique = sorted(set(tokens))
        joined = ' '.join(unique[:5000])
        return {
            'semantic_sha1': hashlib.sha1(joined.encode('utf-8')).hexdigest(),
            'token_count': len(tokens),
            'unique_token_count': len(unique),
            'top_terms': self.top_terms(tokens),
        }

    def top_terms(self, tokens: List[str], n: int = 20) -> List[Dict[str, Any]]:
        counts = {}
        for t in tokens:
            if len(t) < 3:
                continue
            counts[t] = counts.get(t, 0) + 1
        return [{'term': k, 'count': v} for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]]
