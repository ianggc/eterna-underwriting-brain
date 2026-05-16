from __future__ import annotations

import json
from typing import Any, Dict, List

import streamlit as st

from src.engine import recommend
from src.loaders import load_json
from src.outcome_logger import log_outcome

st.set_page_config(page_title="Eterna Underwriting Brain", layout="wide")
st.title("Eterna Underwriting Brain — Phase 2 MVP")

condition_map = load_json("condition_library.json").get("conditions", {})
condition_options = sorted(condition_map.keys())
sample_profiles = load_json("sample_client_profiles.json").get("profiles", [])
sample_names = [p.get("name", f"Sample {i + 1}") for i, p in enumerate(sample_profiles)]


def _profile_to_form_defaults(profile: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "age": int(profile.get("age", 52)),
        "gender": profile.get("gender", "male"),
        "state": profile.get("state", "TX"),
        "height": profile.get("height", "5'10"),
        "weight": int(profile.get("weight", 230)),
        "tobacco": bool(profile.get("tobacco", False)),
        "nicotine_vape": bool(profile.get("nicotine_vape", False)),
        "marijuana_cannabis": bool(profile.get("marijuana_cannabis", False)),
        "product_goal": str(profile.get("product_goal", "final_expense")).lower(),
        "speed_priority": profile.get("speed_priority", "balanced"),
        "budget_monthly": int(profile.get("budget_monthly", 300)),
        "desired_coverage": int(profile.get("desired_coverage", 150000)),
        "primary_objective": profile.get("primary_objective", ""),
        "conditions": [c.get("condition") for c in profile.get("conditions", []) if isinstance(c, dict) and c.get("condition")],
        "medications": profile.get("medications", []),
        "dui_recent": bool((profile.get("dui_mvr_history") or {}).get("recent_dui", False)),
    }


def _agent_notes(profile: Dict[str, Any], result: Dict[str, Any]) -> str:
    primary = result.get("primary_recommendation", {})
    backups = result.get("backup_recommendations", [])
    reasons = primary.get("reasoning", {}) if isinstance(primary.get("reasoning"), dict) else {}
    why = reasons.get("product_fit_reasons", []) + reasons.get("underwriting_reasons", [])
    warnings = reasons.get("risk_warnings", [])
    lines = [
        f"Client goal: {profile.get('product_goal')}",
        f"Primary recommendation: {primary.get('carrier')} {primary.get('product')} (score: {primary.get('score')})",
        f"Confidence: {result.get('confidence_level')} ({result.get('confidence_score')}/100)",
        f"Decision category: {result.get('decision_category')}",
        "Why this fit:",
    ]
    lines.extend([f"- {w}" for w in why[:4]] or ["- Needs manual review due to limited clean fit."])
    if warnings:
        lines.append("Risk warnings:")
        lines.extend([f"- {w}" for w in warnings[:4]])
    if backups:
        lines.append("Backup options:")
        lines.extend([f"- {b.get('carrier')} {b.get('product')}" for b in backups[:3]])
    if result.get("missing_questions"):
        lines.append("Questions to ask next:")
        lines.extend([f"- {q}" for q in result.get("missing_questions", [])[:5]])
    return "\n".join(lines)


st.subheader("Quick Sample Preset")
selected_sample_name = st.selectbox("Load a sample profile", ["None"] + sample_names, index=0)
if selected_sample_name != "None":
    selected_profile = sample_profiles[sample_names.index(selected_sample_name)]
    defaults = _profile_to_form_defaults(selected_profile)
else:
    defaults = _profile_to_form_defaults({})

with st.form("intake"):
    col1, col2, col3 = st.columns(3)
    age = col1.number_input("Age", 18, 90, defaults["age"])
    gender = col1.selectbox("Gender", ["male", "female", "other"], index=["male", "female", "other"].index(defaults["gender"]) if defaults["gender"] in ["male", "female", "other"] else 0)
    state = col1.text_input("State", defaults["state"])
    height = col1.text_input("Height", defaults["height"])
    weight = col1.number_input("Weight", 80, 450, defaults["weight"])

    tobacco = col2.checkbox("Tobacco", value=defaults["tobacco"])
    nicotine_vape = col2.checkbox("Nicotine/Vape", value=defaults["nicotine_vape"])
    marijuana = col2.checkbox("Marijuana/Cannabis", value=defaults["marijuana_cannabis"])
    goal_options = ["final_expense", "iul", "term"]
    product_goal = col2.selectbox("Product Goal", goal_options, index=goal_options.index(defaults["product_goal"]) if defaults["product_goal"] in goal_options else 0)
    speed_priority = col2.selectbox("Speed Priority", ["balanced", "instant"], index=["balanced", "instant"].index(defaults["speed_priority"]) if defaults["speed_priority"] in ["balanced", "instant"] else 0)

    budget = col3.number_input("Budget Monthly", 20, 2000, defaults["budget_monthly"])
    desired_coverage = col3.number_input("Desired Coverage", 5000, 5000000, defaults["desired_coverage"])
    primary_objective = col3.text_input("Primary Objective", defaults["primary_objective"] or "cash value growth and living benefits")

    selected_conditions = st.multiselect(
        "Conditions",
        options=condition_options,
        default=[c for c in defaults["conditions"] if c in condition_options],
        help="Select known conditions. Additional follow-up questions are generated automatically.",
    )
    medications_raw = st.text_area("Medications (comma separated)", ", ".join(defaults["medications"]) if defaults["medications"] else "")

    submitted = st.form_submit_button("Get Recommendation")

if submitted:
    profile = {
        "age": age,
        "gender": gender,
        "state": state,
        "height": height,
        "weight": weight,
        "tobacco": tobacco,
        "nicotine_vape": nicotine_vape,
        "marijuana_cannabis": marijuana,
        "product_goal": product_goal,
        "budget_monthly": budget,
        "desired_coverage": desired_coverage,
        "conditions": [{"condition": c} for c in selected_conditions],
        "medications": [m.strip() for m in medications_raw.split(",") if m.strip()],
        "hospitalizations": [],
        "surgeries": [],
        "dui_mvr_history": {"recent_dui": "dui" in selected_conditions},
        "criminal_history": None,
        "current_coverage": None,
        "primary_objective": primary_objective,
        "speed_priority": speed_priority,
    }
    result = recommend(profile)
    primary = result.get("primary_recommendation", {})
    reasoning = primary.get("reasoning", {}) if isinstance(primary.get("reasoning"), dict) else {}

    st.subheader("Primary Recommendation")
    st.markdown(f"**{primary.get('carrier', 'N/A')} — {primary.get('product', 'N/A')}**")
    st.caption(f"Score: {primary.get('score', 0)} | Approval Path: {primary.get('approval_path', 'N/A')} | Speed: {primary.get('speed', 'N/A')}")

    st.subheader("Confidence")
    st.write(f"**{result.get('confidence_level', 'low').upper()}** ({result.get('confidence_score', 0)}/100)")
    for r in result.get("confidence_reasons", []):
        st.write(f"- {r}")

    st.subheader("Why This Fit")
    for r in reasoning.get("product_fit_reasons", []):
        st.write(f"- {r}")
    for r in reasoning.get("underwriting_reasons", []):
        st.write(f"- {r}")

    st.subheader("Risk Warnings")
    if reasoning.get("risk_warnings"):
        for r in reasoning.get("risk_warnings", []):
            st.warning(r)
    else:
        st.write("No major risk warnings flagged.")

    st.subheader("Missing Questions")
    for q in result.get("missing_questions", []):
        st.write(f"- {q}")

    st.subheader("Backup Options")
    backups = result.get("backup_recommendations", [])
    if backups:
        for b in backups:
            st.write(f"- {b.get('carrier')} {b.get('product')} (score: {b.get('score')})")
    else:
        st.write("No backup options available.")

    st.subheader("Avoid List")
    if result.get("avoid"):
        for a in result.get("avoid", [])[:8]:
            st.write(f"- {a.get('carrier')} {a.get('product')}: {a.get('reason')}")
    else:
        st.write("No avoid flags for current input.")

    st.subheader("Alternative Strategy")
    if result.get("alternative_strategy"):
        st.write(result.get("alternative_strategy"))
    else:
        st.write("No alternative strategy required.")

    st.subheader("Compliance Note")
    st.info(result.get("compliance_note", "Decision support only. Verify current carrier guidelines before submitting."))

    st.subheader("Copy Agent Notes")
    st.text_area("Plain-English recommendation summary", _agent_notes(profile, result), height=240)

    with st.expander("Raw JSON Output"):
        st.json(result)

st.header("Log Submission Outcome")
with st.form("outcome"):
    agent = st.text_input("Agent", "Demo Agent")
    summary = st.text_input("Client Profile Summary")
    rec_carrier = st.text_input("Recommended Carrier")
    rec_product = st.text_input("Recommended Product")
    sub_carrier = st.text_input("Submitted Carrier")
    sub_product = st.text_input("Submitted Product")
    disposition = st.selectbox("Disposition", ["approved", "declined", "rated", "postponed"])
    instant = st.checkbox("Instant Approval")
    tta = st.text_input("Time to Approval")
    premium = st.number_input("Premium", 0.0, 10000.0, 0.0)
    issued = st.checkbox("Issued")
    paid = st.checkbox("Paid")
    placed = st.checkbox("Placed")
    not_taken = st.checkbox("Not Taken")
    chargeback = st.checkbox("Chargeback/Lapse")
    notes = st.text_area("Notes")
    log_btn = st.form_submit_button("Save Outcome")

if log_btn:
    log_outcome({
        "agent": agent,
        "client_profile_summary": summary,
        "recommended_carrier": rec_carrier,
        "recommended_product": rec_product,
        "submitted_carrier": sub_carrier,
        "submitted_product": sub_product,
        "disposition": disposition,
        "instant_approval": instant,
        "time_to_approval": tta,
        "premium": premium,
        "issued": issued,
        "paid": paid,
        "placed": placed,
        "not_taken": not_taken,
        "chargeback_lapse": chargeback,
        "notes": notes,
    })
    st.success("Outcome saved.")
