# Catalogues de prompts adversariaux

Ce dossier contient les **bibliotheques de prompts** utilisees dans l'etape 4 (Red-teaming) de la methodologie d'audit.

## Catalogues disponibles

| Fichier | Description | Nb prompts |
|---------|-------------|------------|
| `biais_genre.json` | Tests de biais de genre | 15 |
| `biais_origine.json` | Tests de biais d'origine et d'ethnicite | 16 |
| `catalogue_adversarial.json` | Tests adversariaux multi-categories (jailbreaks, injections, extraction, toxicite, hallucination, sycophancy, multi-tour) | 56 |
| `tests_sectoriels/rh.json` | Tests specifiques RH et recrutement | 16 |
| `tests_sectoriels/sante.json` | Tests specifiques sante | 15 |
| `tests_sectoriels/education.json` | Tests specifiques education et orientation | 15 |
| `tests_sectoriels/finance.json` | Tests specifiques finance et credit | 15 |

**Total : 148 prompts** couvrant 12 categories de risques.

## Categories du catalogue adversarial

| Categorie | Nb prompts | Description |
|-----------|------------|-------------|
| `jailbreak` | 12 | Contournement des garde-fous (DAN, roleplay, encodage, escalade) |
| `prompt_injection` | 12 | Injection directe, indirecte, encodee, JSON, markdown, conditionnelle |
| `extraction` | 8 | Fuite de prompt systeme, donnees d'entrainement, PII, RAG |
| `toxicity` | 8 | Discours haineux, validisme, ageisme, discrimination religieuse, mineurs |
| `sectoral_rh` | 5 | Discrimination a l'embauche, grossesse, handicap, syndicat |
| `hallucination` | 5 | Citations inventees, fausses statistiques, URLs fabriquees, desinformation medicale |
| `sycophancy` | 4 | Accord factice, changement d'opinion, flatterie, deference a l'autorite |
| `multi_turn` | 4 | Escalade progressive, derive de persona, empoisonnement du contexte, manipulation de memoire |

## Comment utiliser ces catalogues

```python
import json

# Chargement d'un catalogue
with open("prompts/biais_genre.json") as f:
    catalogue = json.load(f)

# Iteration sur les prompts
for prompt_data in catalogue["prompts"]:
    print(f"Test {prompt_data['id']} : {prompt_data['objectif']}")
    # ... appel API du LLM avec prompt_data["prompt"]
```

## Format standard d'un prompt

```json
{
  "id": "categorie_001",
  "type": "type_de_test",
  "prompt": "Le prompt a envoyer au LLM",
  "vs_prompt": "Prompt de comparaison (matched pairs)",
  "objectif": "Ce qu'on cherche a mesurer",
  "metric": "Comment evaluer la reponse",
  "seuil_alerte": "Quand declencher un drapeau rouge",
  "comportement_attendu": "Reponse ideale du modele",
  "severite_si_echec": "CRITICAL / HIGH / MEDIUM / LOW"
}
```

## Contribuer un nouveau prompt

Pour enrichir les catalogues :

1. Identifiez un type de test manquant
2. Redigez le prompt en suivant le format standard
3. Documentez l'objectif et les metriques
4. Testez sur 2-3 modeles differents
5. Soumettez via Pull Request

## Licence

Ces catalogues sont publies sous **Creative Commons BY-SA 4.0**.

Vous pouvez les utiliser librement, y compris commercialement, a condition de :
- Citer l'auteur (Hanen Mizouni / IA au feminin)
- Partager vos ameliorations sous la meme licence

## Vision

L'objectif est de constituer la **plus grande bibliotheque francophone open source** de prompts d'audit pour LLMs, avec des contributions de la communaute tech et associative francaise.

---

*Catalogue maintenu par Hanen Mizouni — Methodologie d'audit LLM v1.0*
