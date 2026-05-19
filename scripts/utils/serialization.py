"""
Utilitaires de sérialisation pour les résultats d'audit.

Problème résolu : les types numpy (int64, float64, ndarray) ne sont pas
sérialisables directement en YAML/JSON. Plutôt qu'une conversion récursive
manuelle (fragile et incomplète), on utilise le pattern json.loads(json.dumps())
qui gère tous les cas via un encoder custom.
"""

import json
import yaml
from pathlib import Path
from typing import Any

import numpy as np


class _NumpyEncoder(json.JSONEncoder):
    """Encoder JSON qui gère les types numpy."""

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super().default(obj)


def safe_yaml_dump(data: Any, path: Path, **kwargs) -> None:
    """
    Sauvegarde des données en YAML en convertissant automatiquement
    les types numpy en types Python natifs.

    Utilise le pattern json.loads(json.dumps(data)) qui est plus robuste
    qu'une conversion récursive manuelle : il gère tous les types numpy
    via un encoder custom, y compris les cas imbriqués.

    Args:
        data: Données à sauvegarder (dict, list, etc.)
        path: Chemin du fichier YAML de sortie.
        **kwargs: Arguments supplémentaires passés à yaml.dump.
    """
    # Conversion via JSON round-trip (gère tous les types numpy)
    native_data = json.loads(json.dumps(data, cls=_NumpyEncoder))

    yaml_kwargs = {"allow_unicode": True, "default_flow_style": False}
    yaml_kwargs.update(kwargs)

    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(native_data, f, **yaml_kwargs)
