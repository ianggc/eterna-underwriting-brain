from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

from src.loaders import load_json, save_json


def log_outcome(entry: Dict[str, Any]) -> None:
    data = load_json("submission_outcomes.json")
    entry = {"date": datetime.utcnow().strftime("%Y-%m-%d"), **entry}
    data.setdefault("outcomes", []).append(entry)
    save_json("submission_outcomes.json", data)

