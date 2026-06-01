from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Any

from aos_core.config import load_json, write_json, AOSPaths
from aos_core.contracts import Fact


class TruthManager:
    """Layered truth store.

    Facts, assumptions, questions, decisions and conflicts are separated to prevent
    accidental promotion of guesses into verified truth.
    """

    DEFAULT_INDEX = {'facts': [], 'assumptions': [], 'questions': [], 'decisions': [], 'conflicts': []}

    def __init__(self, paths: AOSPaths):
        self.paths = paths
        self.truth_index_path = paths.project_truth / 'truth_index.json'
        if not self.truth_index_path.exists():
            write_json(self.truth_index_path, self.DEFAULT_INDEX)

    def load(self) -> Dict[str, Any]:
        data = load_json(self.truth_index_path, self.DEFAULT_INDEX)
        for key in self.DEFAULT_INDEX:
            data.setdefault(key, [])
        return data

    def save(self, data: Dict[str, Any]) -> None:
        write_json(self.truth_index_path, data)

    def add_fact(self, fact: Fact) -> None:
        data = self.load()
        data['facts'].append(asdict(fact))
        self.save(data)

    def add_assumption(self, statement: str, source: str, confidence: float = 0.5) -> None:
        data = self.load()
        data['assumptions'].append({'statement': statement, 'source': source, 'confidence': confidence, 'status': 'unverified'})
        self.save(data)

    def add_question(self, question: str, reason: str) -> None:
        data = self.load()
        data['questions'].append({'question': question, 'reason': reason, 'status': 'open'})
        self.save(data)

    def snapshot(self) -> Dict[str, Any]:
        return self.load()
