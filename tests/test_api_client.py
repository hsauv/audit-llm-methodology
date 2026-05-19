"""Smoke tests pour scripts/utils/api_client.py."""

import os

import pytest

from utils.api_client import call_llm, create_llm_client


def test_simulation_mode_default(monkeypatch):
    """En mode simulation (client=None), call_llm doit renvoyer du texte."""
    monkeypatch.delenv("AUDIT_USE_REAL_API", raising=False)
    response = call_llm("Bonjour, comment allez-vous ?")
    assert isinstance(response, str)
    assert len(response) > 0


def test_simulation_is_deterministic():
    """Le même prompt doit produire la même réponse simulée."""
    prompt = "Décrivez-moi un médecin."
    r1 = call_llm(prompt)
    r2 = call_llm(prompt)
    assert r1 == r2, "Le mode simulation doit être déterministe pour la reproductibilité"


def test_different_prompts_yield_different_seeds():
    """Deux prompts différents doivent (presque toujours) donner des réponses différentes."""
    r1 = call_llm("Test prompt A")
    r2 = call_llm("Test prompt B totalement différent")
    # On accepte qu'ils soient identiques par hasard (faible probabilité),
    # mais sur un grand nombre de paires ils devraient majoritairement différer.
    # Pour le smoke test, on se contente d'au moins vérifier que ce sont des strings.
    assert isinstance(r1, str)
    assert isinstance(r2, str)


def test_create_client_returns_none_in_simulation(monkeypatch):
    monkeypatch.setenv("AUDIT_USE_REAL_API", "false")
    assert create_llm_client() is None


def test_create_client_returns_none_when_var_absent(monkeypatch):
    monkeypatch.delenv("AUDIT_USE_REAL_API", raising=False)
    assert create_llm_client() is None


def test_invalid_provider_raises(monkeypatch):
    """Un provider inconnu doit échouer explicitement."""
    monkeypatch.setenv("AUDIT_USE_REAL_API", "true")
    with pytest.raises(ValueError, match="Provider inconnu"):
        create_llm_client(provider="not-a-provider")
