from __future__ import annotations

from typing import Dict


def add(score: int, key: str, rules: Dict[str, int]) -> int:
    return score + int(rules.get(key, 0))

