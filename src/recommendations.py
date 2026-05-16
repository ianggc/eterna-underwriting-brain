from __future__ import annotations

from typing import Any, Dict, List


def as_output(
    scored: List[Dict[str, Any]],
    avoid: List[Dict[str, Any]],
    knockout_flags: List[str],
    missing_questions: List[str],
    original_goal_viability: str,
    manual_review_required: bool,
    alternative_strategy: Dict[str, Any] | None = None,
    confidence_score: int = 0,
    confidence_level: str = "low",
    confidence_reasons: List[str] | None = None,
    decision_category: str = "needs_more_info",
) -> Dict[str, Any]:
    primary = scored[0] if scored else {
        "carrier": "needs_more_info",
        "product": "manual_review",
        "score": 0,
        "approval_path": "needs_more_info",
        "speed": "needs_more_info",
        "reasoning": {
            "eligibility_reasons": [],
            "underwriting_reasons": [],
            "product_fit_reasons": [],
            "risk_warnings": ["No viable matching-goal products after rule checks."],
            "missing_info": missing_questions,
        },
    }
    backups = scored[1:4] if len(scored) > 1 else []
    return {
        "primary_recommendation": primary,
        "backup_recommendations": backups,
        "avoid": avoid,
        "knockout_flags": knockout_flags,
        "missing_questions": missing_questions,
        "original_goal_viability": original_goal_viability,
        "manual_review_required": manual_review_required,
        "alternative_strategy": alternative_strategy or {},
        "confidence_score": confidence_score,
        "confidence_level": confidence_level,
        "confidence_reasons": confidence_reasons or [],
        "decision_category": decision_category,
        "agent_positioning": "Set expectations: recommendation optimizes suitability and likely approval path before speed.",
        "compliance_note": "Decision support only. Verify current carrier guidelines before submitting.",
    }
