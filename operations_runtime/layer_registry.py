from __future__ import annotations

import importlib
from pathlib import Path
from typing import Any, Dict


class OperationsLayerRegistry:
    """Authoritative runtime registry for layer gateways.

    v4.4 behavior: registration is manifest-declared and gateway loading is lazy.
    The kernel no longer imports heavy capability layers during ordinary startup;
    a layer is instantiated only when the execution graph actually calls it.
    """

    def __init__(self, root: Path, paths: Any):
        self.root = Path(root)
        self.paths = paths
        self.layers: Dict[str, Any] = {}
        self.definitions: Dict[str, Dict[str, Any]] = {}
        self.metadata: Dict[str, Dict[str, Any]] = {}
        self._register_defaults()

    def _register_defaults(self) -> None:
        self.register('intent_cognition', 'aos_core.intent.main', create_kwargs={})
        self.register('project_truth', 'operations_runtime.project_truth_reader', create_kwargs={})
        self.register('truth_runtime', 'aos_capabilities.truth_runtime.main', create_kwargs={'paths': self.paths})
        self.register('artifact_matrix', 'aos_capabilities.file_intelligence.main', create_kwargs={})
        self.register('goal_runtime', 'aos_capabilities.goal_runtime.main', create_kwargs={'paths': self.paths})

    def register(self, name: str, module: str, *, create_kwargs: Dict[str, Any] | None = None) -> None:
        manifest_path = self._manifest_path_from_module(module)
        self.definitions[name] = {'module': module, 'create_kwargs': create_kwargs or {}, 'manifest_path': manifest_path}
        self.metadata[name] = {
            'module': module,
            'facade': 'main.py',
            'gateway': True,
            'lazy_loaded': True,
            'direct_model_entry': 'forbidden',
            'descriptor': {'layer_id': name, 'role': 'declared_layer_gateway_loaded_on_first_use'},
            'health': {'status': 'not_loaded', 'reason': 'lazy_gateway_not_called_in_this_operation'},
            'contract': {'passed': True, 'mode': 'manifest_declared_lazy_gateway_contract'},
            'manifest': {'path': manifest_path.as_posix() if manifest_path else None, 'exists': bool(manifest_path and manifest_path.exists())},
        }

    def _manifest_path_from_module(self, module: str) -> Path | None:
        parts = module.split('.')
        if parts[-1].endswith('.py'):
            parts[-1] = parts[-1][:-3]
        path = self.root.joinpath(*parts)
        if path.name in {'main', 'project_truth_reader'}:
            return path.parent / 'layer_manifest.yaml'
        return path.parent / 'layer_manifest.yaml'

    def _load(self, name: str) -> Any:
        if name in self.layers:
            return self.layers[name]
        if name not in self.definitions:
            raise KeyError(f'Layer is not registered behind Operations Runtime: {name}')
        definition = self.definitions[name]
        module = definition['module']
        mod = importlib.import_module(module)
        obj = mod.create(**definition.get('create_kwargs', {}))
        self._validate_gateway(name, module, obj)
        self.layers[name] = obj
        descriptor = obj.describe() if hasattr(obj, 'describe') else {}
        health = obj.healthcheck() if hasattr(obj, 'healthcheck') else {'status': 'unknown'}
        contract = obj.validate_contract() if hasattr(obj, 'validate_contract') else {'passed': False, 'issues': ['missing_validate_contract']}
        self.metadata[name].update({
            'lazy_loaded': False,
            'descriptor': descriptor,
            'health': health,
            'contract': contract,
        })
        return obj

    def _validate_gateway(self, name: str, module: str, obj: Any) -> None:
        missing = [m for m in ['describe', 'healthcheck', 'validate_contract', 'execute'] if not hasattr(obj, m)]
        if missing:
            raise TypeError(f'Layer gateway {name} from {module} is missing required methods: {missing}')

    def get(self, name: str) -> Any:
        return self._load(name)

    def describe(self) -> Dict[str, Any]:
        return {
            'registry_id': 'operations_runtime_layer_registry_v44_lazy',
            'owner': 'operations_runtime',
            'registered_layers': self.metadata,
            'loaded_layers': sorted(self.layers.keys()),
            'law': 'layers are manifest-declared and lazily loaded through registered gateways, operation contracts, scoped contexts, and layer command/result contracts',
        }
