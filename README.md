# Eterna Underwriting Brain (Phase 2 MVP)

Decision-support prototype for underwriting recommendation based on manual intake.

## What it does
- Loads normalized carrier/product data and condition/rule data.
- Scores products for fit (age, goal, condition tolerance, path/speed, budget/coverage).
- Returns primary + backup recommendations, avoid flags, knockout flags, and follow-up questions.
- Logs submission outcomes into local JSON for feedback-loop learning.

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install streamlit
streamlit run app.py
```

## Data files
- `data/normalized_carrier_products.json`: product catalog + underwriting metadata.
- `data/condition_library.json`: supported condition slugs.
- `data/underwriting_rules.json`: global rules and GI triggers.
- `data/scoring_rules.json`: transparent configurable weights.
- `data/sample_client_profiles.json`: demo testing profiles only.
- `data/submission_outcomes.json`: local outcome log store.

## Add/modify rules
1. Add products in `normalized_carrier_products.json`.
2. Update knockouts/tolerances and approval path.
3. Tune weights in `scoring_rules.json`.
4. Extend GI trigger conditions in `underwriting_rules.json`.

## Outcome logging
Use the Streamlit Outcome section or call `src/outcome_logger.py` function `log_outcome`.

## Limitations
- Rules are heuristic and prototype-grade.
- Some entries are marked `DATA_GAP` and need ongoing guideline validation.
- No external data/API sync yet.

## Compliance
Decision support only. Verify current carrier guidelines before submitting. No guarantee of approval.
