from __future__ import annotations

from typing import Any, Dict, List

import streamlit as st

from src.engine import recommend
from src.loaders import load_json
from src.outcome_logger import log_outcome

st.set_page_config(page_title="Eterna Underwriting Brain", layout="wide")

st.markdown(
    """
    <style>
      .stApp { background-color: #f8fbf8; color: #111111; }
      h1, h2, h3 { color: #0f5132 !important; }
      .eterna-box {
        border: 1px solid #cfe8d8;
        border-left: 5px solid #2e7d32;
        border-radius: 8px;
        background: #ffffff;
        padding: 0.8rem 1rem;
        margin-bottom: 0.75rem;
      }
      .stButton>button, .stFormSubmitButton>button {
        background-color: #2e7d32 !important;
        color: white !important;
        border: 1px solid #2e7d32 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Eterna Underwriting Brain — Phase 2 MVP")

condition_map = load_json("condition_library.json").get("conditions", {})
condition_options = sorted(condition_map.keys())

GOAL_LABEL_TO_VALUE = {
    "Final Expense / Whole Life": "final_expense",
    "IUL": "iul",
    "Term": "term",
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


with st.form("intake"):
    st.subheader("Client Intake")
    col1, col2, col3 = st.columns(3)
    age = col1.number_input("Age", 18, 90, 52)
    gender = col1.selectbox("Gender", ["male", "female", "other"])
    state = col1.text_input("State", "TX")
    height = col1.text_input("Height", "5'10")
    weight = col1.number_input("Weight", 80, 450, 230)

    tobacco = col2.checkbox("Tobacco")
    nicotine_vape = col2.checkbox("Nicotine/Vape")
    marijuana = col2.checkbox("Marijuana/Cannabis")
    goal_label = col2.selectbox("Product Goal", list(GOAL_LABEL_TO_VALUE.keys()), index=0)
    speed_priority = col2.selectbox("Speed Priority", ["balanced", "instant"])

    primary_objective = col3.text_input("Primary Objective", "cash value growth and living benefits")
    medications_raw = col3.text_area("Medications (comma separated)", "metformin")

    selected_conditions = st.multiselect(
        "Conditions",
        options=condition_options,
        default=["type_2_diabetes"] if "type_2_diabetes" in condition_options else [],
        help="Select known conditions. Additional follow-up questions are generated automatically.",
    )

    submitted = st.form_submit_button("Get Recommendation")

if submitted:
    product_goal = GOAL_LABEL_TO_VALUE[goal_label]
    # Safe internal defaults since budget and desired coverage were removed from UI.
    budget_default = 150 if product_goal == "final_expense" else 350
    coverage_default = 15000 if product_goal == "final_expense" else (250000 if product_goal == "term" else 150000)

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
        "budget_monthly": budget_default,
        "desired_coverage": coverage_default,
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
    st.markdown(f"<div class='eterna-box'><b>{primary.get('carrier', 'N/A')} — {primary.get('product', 'N/A')}</b><br/>Score: {primary.get('score', 0)} | Approval Path: {primary.get('approval_path', 'N/A')} | Speed: {primary.get('speed', 'N/A')}</div>", unsafe_allow_html=True)

    st.subheader("Confidence")
    st.markdown(f"<div class='eterna-box'><b>{result.get('confidence_level', 'low').upper()}</b> ({result.get('confidence_score', 0)}/100)</div>", unsafe_allow_html=True)
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
