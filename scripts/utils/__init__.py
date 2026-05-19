"""
Utilitaires partagés pour la méthodologie d'audit LLM.

Modules :
- api_client : wrapper unifié OpenAI/Anthropic avec retry et rate-limiting
- serialization : sérialisation YAML sûre (types numpy, etc.)
- scoring : fonctions de scoring avec seuils justifiés
"""

from .api_client import create_llm_client, call_llm
from .serialization import safe_yaml_dump
from .scoring import diff_to_score, compute_fairness_score, compute_redteam_score
