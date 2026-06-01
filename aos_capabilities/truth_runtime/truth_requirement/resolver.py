from __future__ import annotations

from typing import Any, Dict
from aos_capabilities.truth_runtime.models import TruthRequirement


class TruthRequirementResolver:
    """Converts intent/surface/risk into required truth depth.

    This resolver intentionally avoids file-size or filename-only truth. It
    estimates what truth depth is required by the operation, then downstream
    layers collect evidence.
    """

    WRITE_WORDS = {'write','create','edit','modify','build','implement','generate','fix','refactor','delete','move','rename','execute','apply','انشئ','اكتب','عدل','نفذ','ابن','اصلح','احذف','غير'}
    ARCH_WORDS = {'architecture','stack','runtime','governance','canon','standard','layer','system','surface','truth','معمارية','طبقة','حوكمة','معايير','حقيقة','سطح','نظام'}
    LOGIC_WORDS = {'logic','workflow','scenario','process','business','endpoint','api','database','state','event','permissions','shipping','payment','tax','customs','user','store','منطق','سيناريو','رحلة','حالات','احداث','صلاحيات','شحن','ضرائب','جمارك','مستخدم','متجر'}
    FILE_WORDS = {'file','path','folder','where','name','exists','ملف','مسار','مجلد','اسم'}

    def resolve(self, request_text: str, intent: Dict[str, Any] | None = None, surface: str | None = None) -> Dict[str, Any]:
        intent = intent or {}
        text = (request_text or '').lower()
        surface = surface or intent.get('surface') or intent.get('scope') or 'active_project_payload'
        intent_type = intent.get('intent_type') or intent.get('type') or 'unknown'
        risk = intent.get('risk_level') or ('write' if intent.get('may_modify_files') else 'read_only')
        words = set(text.replace('/', ' ').replace('_', ' ').split())
        execution_sensitive = bool(intent.get('may_modify_files')) or any(w in text for w in self.WRITE_WORDS)
        has_arch = any(w in text for w in self.ARCH_WORDS)
        has_logic = any(w in text for w in self.LOGIC_WORDS)
        has_file = any(w in text for w in self.FILE_WORDS)

        if execution_sensitive:
            depth, label = 5, 'executable'
            reason = 'Write/execute/fix intent requires executable truth.'
        elif has_arch:
            depth, label = 4, 'architecture_or_canon'
            reason = 'Architecture/canon/system intent requires higher-truth and cross-layer evidence.'
        elif has_logic:
            depth, label = 3, 'relational_logic'
            reason = 'Business/code/workflow logic intent requires relational truth across related artifacts.'
        elif has_file:
            depth, label = 2, 'structural'
            reason = 'File/path question requires literal and structural evidence.'
        else:
            depth, label = 2, 'structural'
            reason = 'Default requires literal and structural truth; expand if evidence indicates cross-domain dependency.'

        layers = ['literal_truth', 'structural_truth']
        relations = []
        scopes = [surface]
        if depth >= 3:
            layers += ['relational_truth', 'intent_truth']
            relations += ['dependencies', 'neighboring_domains', 'apis', 'tests', 'states_events']
        if depth >= 4:
            layers += ['project_truth', 'canon_truth', 'incomplete_truth']
            scopes += ['workshop_general_truth_as_silent_lens', 'aos_identity_as_silent_runtime_lens']
        if depth >= 5:
            layers += ['executable_truth']
            relations += ['impact', 'write_gate', 'verification', 'rollback']
        req = TruthRequirement(
            request_text=request_text,
            surface=surface,
            intent_type=intent_type,
            risk_level=risk,
            truth_depth=depth,
            depth_label=label,
            required_layers=list(dict.fromkeys(layers)),
            required_scopes=list(dict.fromkeys(scopes)),
            required_relations=list(dict.fromkeys(relations)),
            execution_sensitive=execution_sensitive,
            reason=reason,
        )
        return req.to_dict()
