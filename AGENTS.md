# Agent Instructions for Eterna Underwriting Brain

## Scope
Applies to entire repository.

## Project intent
Build and maintain a lean, local MVP underwriting recommendation engine.

## Rules
- Keep architecture simple (JSON + Python + Streamlit).
- Prioritize final expense logic before broader product expansion.
- Do not add call listening, telephony, or CRM integrations in this phase.
- Use fake/demo data only; avoid storing sensitive PII.
- If carrier data is missing/conflicting, annotate with `DATA_GAP`.
- Preserve `compliance_note` in recommendation outputs.

## Development checks
- Run `python tests/run_sample_profiles.py` before commit.
- Keep scoring weights configurable in `data/scoring_rules.json`.
