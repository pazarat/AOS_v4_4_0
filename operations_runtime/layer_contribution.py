from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List


@dataclass
class LayerContribution:
    layer: str
    mode: str
    value: str
    evidence: List[Dict[str, Any]] = field(default_factory=list)
    risks: List[Dict[str, Any]] = field(default_factory=list)
    next_needs: List[str] = field(default_factory=list)
    ignored_noise: List[str] = field(default_factory=list)
    confidence: str = "derived"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
