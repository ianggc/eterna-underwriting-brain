from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ClientProfile:
    age: int
    gender: str
    state: str
    height: str
    weight: float
    tobacco: bool
    nicotine_vape: bool
    marijuana_cannabis: bool
    product_goal: str
    budget_monthly: float
    desired_coverage: int
    conditions: List[Dict[str, Any]] = field(default_factory=list)
    medications: List[str] = field(default_factory=list)
    hospitalizations: List[str] = field(default_factory=list)
    surgeries: List[str] = field(default_factory=list)
    dui_mvr_history: Optional[Dict[str, Any]] = None
    criminal_history: Optional[Dict[str, Any]] = None
    current_coverage: Optional[Dict[str, Any]] = None
    primary_objective: str = ""
    speed_priority: str = "balanced"


@dataclass
class ProductScore:
    carrier: str
    product: str
    score: int
    approval_path: str
    speed: str
    reasoning: List[str]
    avoid_reasons: List[str] = field(default_factory=list)
    knockout_flags: List[str] = field(default_factory=list)

