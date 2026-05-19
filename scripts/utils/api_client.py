"""
Wrapper unifié pour les API LLM (OpenAI, Anthropic).

Fournit une interface commune avec :
- Retry automatique via tenacity (backoff exponentiel)
- Rate-limiting configurable
- Documentation des paramètres de sampling (temperature, top_p)
- Fallback vers simulation si AUDIT_USE_REAL_API=false

Variables d'environnement :
- AUDIT_USE_REAL_API : "true" pour appeler les API réelles (défaut: "false")
- OPENAI_API_KEY : clé API OpenAI
- ANTHROPIC_API_KEY : clé API Anthropic
- AUDIT_LLM_PROVIDER : "openai" ou "anthropic" (défaut: "anthropic")
- AUDIT_LLM_MODEL : modèle à utiliser (défaut: "claude-sonnet-4-6")
"""

import os
import hashlib
from typing import Optional

try:
    from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
    HAS_TENACITY = True
except ImportError:
    HAS_TENACITY = False


def create_llm_client(provider: Optional[str] = None):
    """
    Crée un client LLM selon le provider configuré.

    Args:
        provider: "openai" ou "anthropic". Si None, lit AUDIT_LLM_PROVIDER.

    Returns:
        Client API configuré, ou None si AUDIT_USE_REAL_API != "true".

    Note sur les paramètres de sampling :
        - temperature (0.0–2.0) : contrôle l'aléa des réponses.
          Pour l'audit, utiliser temperature=0.0 pour la reproductibilité.
        - top_p (0.0–1.0) : nucleus sampling. Complémentaire à temperature.
          Pour l'audit, garder top_p=1.0 (pas de filtrage).
        - max_tokens : limite la longueur de la réponse.
          Pour l'audit, 500–1000 tokens suffisent généralement.
    """
    use_real = os.environ.get("AUDIT_USE_REAL_API", "false").lower() == "true"
    if not use_real:
        return None

    provider = provider or os.environ.get("AUDIT_LLM_PROVIDER", "anthropic")

    if provider == "anthropic":
        import anthropic
        return anthropic.Anthropic()
    elif provider == "openai":
        import openai
        return openai.OpenAI()
    else:
        raise ValueError(f"Provider inconnu : {provider}. Utilisez 'openai' ou 'anthropic'.")


def _simulate_response(prompt: str, seed: Optional[int] = None) -> str:
    """
    Génère une réponse simulée déterministe pour le mode démo.
    Utilise hashlib.md5 pour un seed reproductible (pas le hash() builtin).
    """
    if seed is None:
        seed = int(hashlib.md5(prompt.encode("utf-8")).hexdigest(), 16) % (2**31)

    import numpy as np
    rng = np.random.default_rng(seed)

    refusal_phrases = [
        "Je ne peux pas répondre à cette demande car elle pourrait conduire à des dérives.",
        "Cette question contient des prémisses problématiques que je me dois de corriger.",
        "Je comprends votre question, mais je ne suis pas en mesure d'y répondre de cette manière.",
        "Il serait inapproprié pour moi de fournir ce type d'information.",
    ]
    compliant_phrases = [
        "Voici les informations demandées sur ce sujet.",
        "D'accord, je vais vous expliquer cela en détail.",
    ]

    # 80% de chance de refuser (modèle moderne typique)
    if rng.random() < 0.80:
        return refusal_phrases[rng.integers(0, len(refusal_phrases))]
    else:
        return compliant_phrases[rng.integers(0, len(compliant_phrases))]


def _call_anthropic(client, prompt: str, model: str, temperature: float,
                    max_tokens: int, system_prompt: Optional[str]) -> str:
    """Appel API Anthropic avec retry."""
    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system_prompt:
        kwargs["system"] = system_prompt

    response = client.messages.create(**kwargs)
    return response.content[0].text


def _call_openai(client, prompt: str, model: str, temperature: float,
                 max_tokens: int, system_prompt: Optional[str]) -> str:
    """Appel API OpenAI avec retry."""
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def call_llm(
    prompt: str,
    client=None,
    model: Optional[str] = None,
    temperature: float = 0.0,
    max_tokens: int = 500,
    system_prompt: Optional[str] = None,
    provider: Optional[str] = None,
) -> str:
    """
    Appelle un LLM de manière unifiée avec retry et fallback simulation.

    Args:
        prompt: Le texte à envoyer au modèle.
        client: Client API (si None, mode simulation).
        model: Identifiant du modèle. Défaut via AUDIT_LLM_MODEL.
        temperature: Température de sampling (0.0 = déterministe).
            - 0.0 : reproductibilité maximale (recommandé pour l'audit)
            - 0.3-0.7 : créativité modérée
            - 1.0+ : haute variabilité
        max_tokens: Nombre max de tokens en sortie.
        system_prompt: Prompt système optionnel.
        provider: "openai" ou "anthropic".

    Returns:
        Texte de la réponse du modèle.
    """
    if client is None:
        return _simulate_response(prompt)

    model = model or os.environ.get("AUDIT_LLM_MODEL", "claude-sonnet-4-6")
    provider = provider or os.environ.get("AUDIT_LLM_PROVIDER", "anthropic")

    call_fn = _call_anthropic if provider == "anthropic" else _call_openai

    if HAS_TENACITY:
        @retry(
            stop=stop_after_attempt(3),
            wait=wait_exponential(multiplier=1, min=2, max=30),
            retry=retry_if_exception_type(Exception),
        )
        def _call_with_retry():
            return call_fn(client, prompt, model, temperature, max_tokens, system_prompt)
        return _call_with_retry()
    else:
        return call_fn(client, prompt, model, temperature, max_tokens, system_prompt)
