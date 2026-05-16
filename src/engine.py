from __future__ import annotations

from typing import Any, Dict, List

from src.loaders import load_json
from src.recommendations import as_output
from src.scoring import add

IMPAIRED_IUL_CONDITIONS = {
    "type_1_diabetes", "type_2_diabetes", "copd", "chf", "stroke", "bipolar_disorder", "hepatitis_b", "hepatitis_c", "high_bmi"
}


def _condition_map() -> Dict[str, Dict[str, Any]]:
    return load_json("condition_library.json").get("conditions", {})


def _extract_conditions(profile: Dict[str, Any]) -> List[str]:
    library = _condition_map()
    alias_index = {alias: key for key, meta in library.items() for alias in meta.get("aliases", [])}
    names: List[str] = []
    for c in profile.get("conditions", []):
        raw = c.get("condition", "") if isinstance(c, dict) else str(c)
        normalized = raw.strip().lower().replace(" ", "_")
        names.append(alias_index.get(normalized, normalized))
    if profile.get("tobacco"):
        names.append("tobacco")
    if profile.get("nicotine_vape"):
        names.append("vaping_nicotine")
    if profile.get("marijuana_cannabis"):
        names.append("marijuana_cannabis")
    if (profile.get("dui_mvr_history") or {}).get("recent_dui"):
        names.append("dui")
    return sorted(list(set(names)))


def _is_clean_accumulation_iul(profile: Dict[str, Any], conds: List[str]) -> bool:
    obj = profile.get("primary_objective", "").lower()
    high_budget = profile.get("budget_monthly", 0) >= 350
    accumulation_obj = any(k in obj for k in ["max-funded", "accumulation", "retirement", "cash value"])
    impaired = any(c in IMPAIRED_IUL_CONDITIONS for c in conds)
    return profile.get("product_goal", "").lower() == "iul" and high_budget and accumulation_obj and not impaired


def _reason_pack() -> Dict[str, List[str]]:
    return {
        "eligibility_reasons": [],
        "underwriting_reasons": [],
        "product_fit_reasons": [],
        "risk_warnings": [],
        "missing_info": [],
    }


def _confidence(primary: Dict[str, Any], missing_questions: List[str], original_goal_viability: str, manual_review_required: bool) -> tuple[int, str, List[str]]:
    score = 75
    reasons: List[str] = []
    if not primary.get("goal_match", False):
        score -= 30
        reasons.append("Primary recommendation is fallback outside requested goal.")
    if manual_review_required:
        score -= 35
        reasons.append("Manual underwriting review is required.")
    if original_goal_viability in {"risky", "unlikely"}:
        score -= 20
        reasons.append(f"Original goal viability is {original_goal_viability}.")
    if len(missing_questions) >= 6:
        score -= 15
        reasons.append("Multiple unresolved follow-up questions remain.")
    if primary.get("knocked_out"):
        score -= 40
        reasons.append("Primary option has knockout conflicts.")
    if score >= 80:
        level = "high"
        reasons.append("Strong goal/eligibility/product-fit alignment.")
    elif score >= 55:
        level = "medium"
        reasons.append("Usable fit with manageable uncertainty.")
    else:
        level = "low"
        reasons.append("Significant uncertainty or fallback/manual-review conditions.")
    return max(0, min(100, score)), level, reasons


def recommend(profile: Dict[str, Any]) -> Dict[str, Any]:
    products = load_json("normalized_carrier_products.json")["products"]
    rules = load_json("underwriting_rules.json")
    scoring = load_json("scoring_rules.json")["weights"]

    conds = _extract_conditions(profile)
    severe_conditions = set(rules.get("global", {}).get("gi_trigger_conditions", []))
    severe_hit = any(c in severe_conditions for c in conds)
    goal = profile["product_goal"].lower()

    scored_goal_match: List[Dict[str, Any]] = []
    scored_alternatives: List[Dict[str, Any]] = []
    avoid: List[Dict[str, Any]] = []
    knockout_flags: List[str] = []

    clean_iul = _is_clean_accumulation_iul(profile, conds)

    for p in products:
        if not (p["age_min"] <= profile["age"] <= p["age_max"]):
            avoid.append({"carrier": p["carrier"], "product": p["product"], "reason": f"age {profile['age']} outside {p['age_min']}-{p['age_max']}"})
            continue

        pgoal_match = goal in [g.lower() for g in p["goal_fit"]]
        key = f"{p['carrier']}::{p['product']}"
        prule = rules.get("product_rules", {}).get(key, {})
        reasons = _reason_pack()
        avoid_reasons: List[str] = []
        score = add(0, "age_eligible", scoring)
        reasons["eligibility_reasons"].append(f"Age {profile['age']} fits issue range {p['age_min']}-{p['age_max']}.")

        if pgoal_match:
            score = add(score, "goal_match", scoring)
            reasons["product_fit_reasons"].append(f"Product category supports {goal} goal.")
        else:
            score -= 35
            reasons["risk_warnings"].append("Outside requested product goal; fallback-only candidate.")

        if p["face_min"] <= profile["desired_coverage"] <= p["face_max"]:
            score = add(score, "coverage_fit", scoring)
            reasons["eligibility_reasons"].append("Coverage target fits product face range.")
        else:
            score -= 15
            reasons["risk_warnings"].append("Coverage target outside product face range.")

        if profile.get("speed_priority") == "instant" and p["speed"] == "fast":
            score = add(score, "instant_issue_speed", scoring)
            reasons["product_fit_reasons"].append("Fast issue path matches instant speed preference.")
        elif profile.get("speed_priority") == "instant" and p["approval_path"] == "full_underwriting":
            score = add(score, "full_uw_penalty_when_instant", scoring)
            reasons["risk_warnings"].append("Full underwriting penalized for instant speed request.")

        tolerated = set(p.get("condition_tolerances", []))
        knockouts = set(p.get("knockout_conditions", [])) | set(prule.get("decline_conditions", []))

        if severe_hit and p["approval_path"] != "guaranteed_issue":
            score = add(score, "severe_impairment_penalty", scoring)
            reasons["risk_warnings"].append("Severe impairment present; non-GI path penalized.")

        for c in conds:
            if c in knockouts:
                score = add(score, "knockout_condition", scoring)
                flag = f"{c} conflicts with {p['carrier']} {p['product']}"
                knockout_flags.append(flag)
                avoid_reasons.append(flag)
                reasons["risk_warnings"].append(flag)
            elif c in tolerated:
                score = add(score, "condition_favorable", scoring)
                reasons["underwriting_reasons"].append(f"{c} is tolerated for this underwriting path.")
            else:
                score = add(score, "condition_risk", scoring)
                reasons["underwriting_reasons"].append(f"{c} adds underwriting risk.")

        if goal == "iul":
            if clean_iul and p["product"] in {"FlexLife IUL", "QoL Max Accumulator+"}:
                score += 30
                reasons["product_fit_reasons"].append("Healthy max-funded accumulation profile prioritizes accumulation-first IUL designs.")
            if clean_iul and p["carrier"] == "F&G":
                score -= 20
                reasons["risk_warnings"].append("F&G de-prioritized for clean accumulation profile.")
            if any(c in IMPAIRED_IUL_CONDITIONS for c in conds) and p["product"] == "Pathsetter IUL":
                score += 35
                reasons["underwriting_reasons"].append("Impaired-risk profile favors F&G Pathsetter.")

        if p["approval_path"] == "guaranteed_issue" and not severe_hit:
            score -= 25
            reasons["risk_warnings"].append("GI de-prioritized because severe GI-trigger conditions not present.")

        score = score - 10 if p["budget_tier"] == "premium" and profile["budget_monthly"] < 200 else add(score, "budget_fit", scoring)

        row = {
            "carrier": p["carrier"], "product": p["product"], "score": int(score), "approval_path": p["approval_path"], "speed": p["speed"],
            "reasoning": reasons, "goal_match": pgoal_match, "knocked_out": bool(avoid_reasons)
        }
        if avoid_reasons:
            avoid.append({"carrier": p["carrier"], "product": p["product"], "reason": "; ".join(avoid_reasons)})
        (scored_goal_match if pgoal_match else scored_alternatives).append(row)

    scored_goal_match.sort(key=lambda x: x["score"], reverse=True)
    scored_alternatives.sort(key=lambda x: x["score"], reverse=True)

    manual_review_required = False
    alternative_strategy: Dict[str, Any] = {}
    viable_goal_products = [r for r in scored_goal_match if r["score"] > -40 and not r.get("knocked_out")]

    if viable_goal_products:
        final_scored = viable_goal_products + [r for r in scored_goal_match if r not in viable_goal_products][:2]
        final_scored += scored_alternatives[:2]
    else:
        manual_review_required = True
        final_scored = []

    if goal == "term" and not viable_goal_products:
        manual_review_required = True
        alternative_strategy = {
            "message": "No clean term fit found. Use full underwriting term review; only use final expense if client is open to permanent fallback.",
            "required_questions": ["DUI date", "number of DUI incidents", "license status", "probation/court status", "current driving record"],
        }

    viability = "unlikely" if not viable_goal_products else ("risky" if any(r["score"] < 20 for r in viable_goal_products[:2]) else ("needs_more_info" if len(_missing_questions(profile, conds)) > 4 else "viable"))

    decision_category = "manual_review" if manual_review_required else "clean_match"
    if manual_review_required and not final_scored:
        decision_category = "manual_review"
    elif final_scored and not final_scored[0]["goal_match"]:
        decision_category = "goal_mismatch_fallback"
    elif final_scored and final_scored[0]["approval_path"] == "guaranteed_issue":
        decision_category = "guaranteed_issue_fallback" if severe_hit else "needs_more_info"
    elif any(c in IMPAIRED_IUL_CONDITIONS for c in conds) and goal == "iul":
        decision_category = "impaired_risk_match"
    elif viability == "needs_more_info":
        decision_category = "needs_more_info"

    missing_qs = _missing_questions(profile, conds)
    primary = final_scored[0] if final_scored else {"goal_match": False, "knocked_out": False}
    conf_score, conf_level, conf_reasons = _confidence(primary, missing_qs, viability, manual_review_required)

    if final_scored:
        final_scored[0]["reasoning"]["missing_info"] = missing_qs

    return as_output(final_scored, avoid, sorted(set(knockout_flags)), missing_qs, viability, manual_review_required, alternative_strategy, conf_score, conf_level, conf_reasons, decision_category)


def _missing_questions(profile: Dict[str, Any], conds: List[str]) -> List[str]:
    questions: List[str] = []
    library = _condition_map()
    for c in conds:
        questions.extend(library.get(c, {}).get("follow_up_questions", []))
    if not profile.get("hospitalizations"):
        questions.append("Any hospitalizations or surgeries in the last 24 months?")
    if "dui" in conds:
        questions.extend(["DUI date?", "How many DUI incidents total?", "License status currently active?", "Any probation/court requirements still open?", "Any additional MVR violations currently?", "Current driving record status?"])
    return sorted(list(dict.fromkeys(questions)))[:10]
