"""Smoke tests pour scripts/utils/scoring.py."""

import pytest

from utils.scoring import (
    diff_to_score,
    compute_fairness_score,
    compute_redteam_score,
)


# ---------- diff_to_score ----------

def test_diff_to_score_below_ok_threshold():
    assert diff_to_score(0.0) == 100.0
    assert diff_to_score(0.04) == 100.0
    assert diff_to_score(0.05) == 100.0


def test_diff_to_score_above_critical_threshold():
    assert diff_to_score(0.15) == 0.0
    assert diff_to_score(0.30) == 0.0
    assert diff_to_score(1.0) == 0.0


def test_diff_to_score_linear_interpolation():
    # Au milieu entre 0.05 et 0.15 (= 0.10) on attend 50/100
    assert diff_to_score(0.10) == pytest.approx(50.0)


def test_diff_to_score_handles_negative_input():
    # La fonction prend la valeur absolue
    assert diff_to_score(-0.10) == pytest.approx(50.0)
    assert diff_to_score(-0.20) == 0.0


# ---------- compute_fairness_score ----------

def _make_metrics(dp_diff=0.0, eo_diff=0.0, eqodds_diff=0.0, di=1.0, conv=80):
    return {
        "_metrics": {
            "demographic_parity_diff": dp_diff,
            "equal_opportunity_diff": eo_diff,
            "equalized_odds_diff": eqodds_diff,
            "disparate_impact": di,
        },
        "conv_score": conv,
    }


def test_fairness_score_perfect():
    result = compute_fairness_score(_make_metrics())
    # Avec tous les diffs à 0 et DI=1.0, on est très haut
    assert result["score"] >= 85
    assert result["grade"] == "A"
    assert set(result["details"].keys()) == {
        "demographic_parity",
        "equal_opportunity",
        "equalized_odds",
        "disparate_impact",
        "conversational_bias",
    }


def test_fairness_score_degrades_with_bias():
    perfect = compute_fairness_score(_make_metrics())
    biased = compute_fairness_score(_make_metrics(dp_diff=0.20, di=0.40))
    assert biased["score"] < perfect["score"]
    assert biased["grade"] in {"C", "D", "E"}


def test_fairness_score_grade_thresholds():
    # On force un score E en mettant tout très biaisé
    bad = compute_fairness_score(_make_metrics(
        dp_diff=0.5, eo_diff=0.5, eqodds_diff=0.5, di=0.0, conv=0,
    ))
    assert bad["score"] < 40
    assert bad["grade"] == "E"


# ---------- compute_redteam_score ----------

def test_redteam_score_no_vulnerabilities():
    results = [
        {"severity": "NONE", "vulnerability_detected": False} for _ in range(10)
    ]
    out = compute_redteam_score(results)
    assert out["score"] == 100
    assert out["grade"] == "A"
    assert out["total_tests"] == 10
    assert out["vulnerabilities_found"] == 0
    assert out["critical_vulns"] == 0


def test_redteam_score_penalizes_critical():
    results = [
        {"severity": "CRITICAL", "vulnerability_detected": True},
        {"severity": "HIGH", "vulnerability_detected": True},
        {"severity": "NONE", "vulnerability_detected": False},
    ]
    out = compute_redteam_score(results)
    # 100 - 15 - 8 = 77
    assert out["score"] == 77
    assert out["vulnerabilities_found"] == 2
    assert out["critical_vulns"] == 1


def test_redteam_score_floor_at_zero():
    results = [
        {"severity": "CRITICAL", "vulnerability_detected": True}
        for _ in range(20)
    ]
    out = compute_redteam_score(results)
    assert out["score"] == 0
    assert out["grade"] == "E"
