# 📂 Catalogues de prompts adversariaux

Ce dossier contient les **bibliothèques de prompts** utilisées dans l'étape 4 (Red-teaming) de la méthodologie d'audit.

## 📦 Catalogues disponibles

| Fichier | Description | Nb prompts |
|---------|-------------|------------|
| `biais_genre.json` | Tests de biais de genre | 15+ |
| `biais_origine.json` | Tests de biais d'origine (à enrichir) | TODO |
| `jailbreaks.json` | Tests de contournement des garde-fous (à enrichir) | TODO |
| `tests_sectoriels/` | Tests spécifiques par secteur | TODO |

## 🎯 Comment utiliser ces catalogues

```python
import json

# Chargement d'un catalogue
with open("prompts/biais_genre.json") as f:
    catalogue = json.load(f)

# Itération sur les prompts
for prompt_data in catalogue["prompts"]:
    print(f"Test {prompt_data['id']} : {prompt_data['objectif']}")
    # ... appel API du LLM avec prompt_data["prompt"]
```

## 📝 Format standard d'un prompt

```json
{
  "id": "categorie_001",
  "type": "type_de_test",
  "prompt": "Le prompt à envoyer au LLM",
  "vs_prompt": "Prompt de comparaison (matched pairs)",
  "objectif": "Ce qu'on cherche à mesurer",
  "metric": "Comment évaluer la réponse",
  "seuil_alerte": "Quand déclencher un drapeau rouge",
  "comportement_attendu": "Réponse idéale du modèle",
  "severite_si_echec": "CRITICAL / HIGH / MEDIUM / LOW"
}
```

## 🤝 Contribuer un nouveau prompt

Pour enrichir les catalogues :

1. Identifiez un type de test manquant
2. Rédigez le prompt en suivant le format standard
3. Documentez l'objectif et les métriques
4. Testez sur 2-3 modèles différents
5. Soumettez via Pull Request

## ⚖️ Licence

Ces catalogues sont publiés sous **Creative Commons BY-SA 4.0**.

Vous pouvez les utiliser librement, y compris commercialement, à condition de :
- Citer l'auteur (Hanen Mizouni / IA au féminin)
- Partager vos améliorations sous la même licence

## 🌱 Vision

L'objectif est de constituer la **plus grande bibliothèque francophone open source** de prompts d'audit pour LLMs, avec des contributions de la communauté tech et associative française.

---

*Catalogue maintenu par Hanen Mizouni — Méthodologie d'audit LLM v1.0*
