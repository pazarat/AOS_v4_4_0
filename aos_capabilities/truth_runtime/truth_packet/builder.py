from __future__ import annotations

from typing import Any, Dict, List
from aos_capabilities.truth_runtime.models import TruthPacket
from aos_capabilities.truth_runtime.incomplete_truth.reasoner import IncompleteTruthReasoner
from aos_capabilities.truth_runtime.truth_value.artifact_semantics import ArtifactTruthSemantics
from aos_capabilities.truth_runtime.truth_value.story_packet import TruthStoryPacketBuilder
from aos_capabilities.truth_runtime.identity_sync.philosophy_sync import PhilosophySyncAdvisor


class TruthPacketBuilder:
    """Builds value/provenance-aware truth packets from artifact evidence."""

    HIGH_VALUE_MARKERS = [
        'canon','standard','contract','identity','layer_identity','manifest','constitution','decision','truth','readme','api','schema','governance','policy'
    ]

    def build(self, requirement: Dict[str, Any], artifact_matrix: Dict[str, Any] | None = None, truth_store: Dict[str, Any] | None = None, cockpit: Dict[str, Any] | None = None) -> Dict[str, Any]:
        matrix = artifact_matrix or {}
        records = matrix.get('records') or []
        semantics = ArtifactTruthSemantics().analyze(matrix)
        evidence = self._evidence_from_matrix(requirement, matrix)
        high_value = self._high_value_sources(records, semantics=semantics)
        relationship = self._relationship_evidence(matrix, cockpit, semantics=semantics)
        incomplete = IncompleteTruthReasoner().detect(requirement, matrix, truth_store, semantics=semantics)
        truth_story = TruthStoryPacketBuilder().build(requirement, matrix, semantics, incomplete)
        packet = TruthPacket(
            requirement=requirement,
            evidence=evidence,
            high_value_sources=high_value,
            relationship_evidence=relationship,
            incomplete_truth=incomplete,
            source_truth_store=truth_store or {},
        )
        data = packet.to_dict()
        data['truth_value_semantics'] = semantics
        data['truth_story'] = truth_story
        data['identity_sync'] = PhilosophySyncAdvisor().advise(data)
        return data

    def _evidence_from_matrix(self, requirement: Dict[str, Any], matrix: Dict[str, Any]) -> List[Dict[str, Any]]:
        evidence: List[Dict[str, Any]] = []
        search = matrix.get('search') or {}
        for item in (search.get('results') or [])[:30]:
            evidence.append({
                'grade': 'derived',
                'source': item.get('path'),
                'reason': 'matched_request_query',
                'score': item.get('score'),
                'surface': item.get('surface'),
                'role': item.get('role'),
            })
        known = matrix.get('content_knownness_map') or {}
        for concept, info in (known.get('concept_status') or {}).items():
            if info.get('evidence_count',0) > 0:
                evidence.append({
                    'grade': 'verified',
                    'source': info.get('evidence_files', [])[:5],
                    'reason': f'concept_documented:{concept}',
                    'score': info.get('score',0),
                })
        return evidence

    def _high_value_sources(self, records: List[Dict[str, Any]], semantics: Dict[str, Any] | None = None) -> List[Dict[str, Any]]:
        out=[]
        semantic_scores = {x.get('path'): x for x in (semantics or {}).get('high_value_sources', [])}
        for r in records:
            path=(r.get('path') or '').lower()
            role=(r.get('role') or '').lower()
            sample=(r.get('sample') or '').lower()
            marker_score = sum(1 for m in self.HIGH_VALUE_MARKERS if m in path or m in role)
            marker_score += 1 if any(x in sample[:1200] for x in ['must','forbidden','law','قاعدة','ممنوع','يجب','حقيقة','حوكمة']) else 0
            if r.get('path') in semantic_scores:
                marker_score += int(semantic_scores[r.get('path')].get('score') or 0)
            if marker_score:
                out.append({
                    'path': r.get('path'),
                    'role': r.get('role'),
                    'surface': r.get('surface'),
                    'size_bytes': r.get('size_bytes'),
                    'value_score': marker_score,
                    'reason': 'high_value_marker_not_file_size',
                })
        return sorted(out, key=lambda x: (-x['value_score'], x['path'] or ''))[:50]

    def _relationship_evidence(self, matrix: Dict[str, Any], cockpit: Dict[str, Any] | None, semantics: Dict[str, Any] | None = None) -> Dict[str, Any]:
        api = matrix.get('api_intelligence') or {}
        db = matrix.get('database_intelligence') or {}
        impact = matrix.get('impact_map') or {}
        return {
            'symbol_count': (matrix.get('symbol_graph') or {}).get('symbol_count', 0),
            'call_edges': len((matrix.get('call_graph') or {}).get('edges', []) or []),
            'import_edges': len((matrix.get('import_graph') or {}).get('edges', []) or []),
            'api_routes': len((api.get('routes') or {}).get('routes', []) if isinstance(api.get('routes'), dict) else api.get('routes') or []),
            'database_relation_count': len((db.get('relations') or {}).get('relations', []) if isinstance(db.get('relations'), dict) else []),
            'impact_items': len(impact.get('items', []) if isinstance(impact, dict) else []),
            'cockpit_views': len((cockpit or {}).get('views', []) if isinstance(cockpit, dict) else []),
            'declared_edges': len((semantics or {}).get('declared_edges', []) if isinstance(semantics, dict) else []),
            'empty_declared_targets': int((semantics or {}).get('empty_declared_target_count') or 0) if isinstance(semantics, dict) else 0,
            'declared_missing_artifacts': int((semantics or {}).get('declared_missing_artifact_count') or 0) if isinstance(semantics, dict) else 0,
        }
