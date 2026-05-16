import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.engine import recommend
from src.loaders import load_json


def _product_key(rec: dict) -> str:
    return f"{rec.get('carrier','')}::{rec.get('product','')}"


def _contains_all_keywords(haystack: str, keywords: list[str]) -> bool:
    keys = [k for k in keywords if k.strip()]
    return all(k.lower() in haystack.lower() for k in keys)


def main() -> None:
    profiles = load_json("sample_client_profiles.json")["profiles"]
    audits = {a["profile_name"]: a for a in load_json("../tests/audit_expected_outputs.json").get("audits", [])}

    total = 0
    passed = 0

    for p in profiles:
        result = recommend(p)
        profile_name = p["name"]
        audit = audits.get(profile_name)

        print("=" * 100)
        print(profile_name)
        pr = result["primary_recommendation"]
        primary_key = _product_key(pr)
        print(f"Top: {pr['carrier']} - {pr['product']} ({pr['score']})")
        print("Decision Category:", result["decision_category"])
        print("Manual Review Required:", result["manual_review_required"])
        print("Missing Questions:", result["missing_questions"])

        if not audit:
            print("AUDIT: FAIL (missing audit config)")
            total += 1
            continue

        checks: list[tuple[str, bool, str]] = []

        acceptable = set(audit.get("acceptable_primary_products", []))
        unacceptable = set(audit.get("unacceptable_primary_products", []))

        checks.append((
            "primary acceptable",
            (not acceptable) or (primary_key in acceptable),
            f"primary={primary_key}, acceptable={sorted(acceptable)}",
        ))
        checks.append((
            "primary not unacceptable",
            primary_key not in unacceptable,
            f"primary={primary_key}, unacceptable={sorted(unacceptable)}",
        ))

        expected_category = audit.get("expected_decision_category")
        checks.append((
            "decision_category",
            result.get("decision_category") == expected_category,
            f"got={result.get('decision_category')} expected={expected_category}",
        ))

        expected_mr = audit.get("expected_manual_review_required")
        checks.append((
            "manual_review_required",
            result.get("manual_review_required") == expected_mr,
            f"got={result.get('manual_review_required')} expected={expected_mr}",
        ))

        warning_blob = " ".join(pr.get("reasoning", {}).get("risk_warnings", [])) if isinstance(pr.get("reasoning"), dict) else str(pr.get("reasoning", ""))
        checks.append((
            "required warning keywords",
            _contains_all_keywords(warning_blob, audit.get("required_warning_keywords", [])),
            f"warnings={warning_blob}",
        ))

        missing_blob = " ".join(result.get("missing_questions", []))
        checks.append((
            "required missing-question keywords",
            _contains_all_keywords(missing_blob, audit.get("required_missing_question_keywords", [])),
            f"missing={missing_blob}",
        ))

        all_pass = True
        for name, ok, detail in checks:
            status = "PASS" if ok else "FAIL"
            if not ok:
                all_pass = False
            print(f"  - {name}: {status} ({detail})")

        total += 1
        if all_pass:
            passed += 1
            print("AUDIT: PASS")
        else:
            print("AUDIT: FAIL")

    print("=" * 100)
    print(f"Audit Summary: {passed}/{total} profiles passed")
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
