# Guide de contribution

Merci de l'intérêt que vous portez à cette méthodologie d'audit LLM !
Ce projet vise à fournir un cadre **ouvert, pédagogique et reproductible**
pour auditer les modèles de langage en entreprise. Chaque contribution
compte.

## 🎯 Types de contributions bienvenues

### 1. Enrichir les bibliothèques de prompts (`prompts/`)

C'est la contribution la plus directe. Le catalogue est versionné en
JSON pour faciliter les diffs et l'agrégation.

**Format** :

```json
{
  "id": "INJECTION_07",
  "category": "prompt_injection",
  "subcategory": "indirect",
  "prompt": "Le texte du prompt adversarial...",
  "expected": "Description du comportement attendu (refus, recadrage...)",
  "severity_if_fails": "high",
  "detection_keywords": ["mot1", "mot2"]
}
```

**Critères d'acceptation** :
- Le prompt doit cibler une catégorie identifiable (jailbreak,
  injection, biais d'origine, etc.).
- Le `severity_if_fails` doit être justifié (low, medium, high, critical).
- Pas de PII réelle — utiliser des prénoms génériques ou anonymisés.

### 2. Ajouter des cas d'études (`examples/`)

Walkthrough d'un audit réel ou simulé, du cadrage au plan de
remédiation. Format Markdown, ~5-10 pages. Anonymiser si nécessaire
(jamais de nom de client sans autorisation écrite).

### 3. Traduire la documentation

La méthodologie est actuellement en français. Anglais et espagnol
sont les prochaines priorités. Convention : `docs/en/`, `docs/es/`,
etc.

### 4. Étoffer les notebooks ou les scripts

Améliorations bienvenues :
- Compatibilité avec d'autres providers LLM (Mistral, Cohere, Gemini)
- Métriques fairness additionnelles
- Visualisations
- Optimisation des performances

### 5. Documenter la conformité légale

L'AI Act évolue. Les recommandations CNIL aussi. Les contributions
sur les volets juridiques sont précieuses, idéalement par des
juristes spécialisés ou avec leur relecture.

## 🛠️ Mise en place

```bash
git clone https://github.com/hsauv/audit-llm-methodology.git
cd audit-llm-methodology
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Lancer les tests
pytest tests/ -v
```

## 🌳 Workflow de contribution

1. **Fork** le repo et créez une branche feature :
   `git checkout -b feature/nom-explicite`
2. **Codez et testez** localement. Si vous modifiez des prompts,
   vérifiez la validité JSON :
   `python -m json.tool prompts/votre_fichier.json > /dev/null`
3. **Commit** avec un message clair en français ou anglais :
   ```
   feat(prompts): ajoute 5 tests de biais d'origine pour le secteur santé
   ```
   Conventions utilisées : [Conventional Commits](https://www.conventionalcommits.org/).
4. **Push** et ouvrez une **Pull Request** vers `main`.
5. Décrivez dans la PR :
   - **Quoi** : ce que la PR ajoute / modifie
   - **Pourquoi** : motivation, lien éventuel à une issue
   - **Comment tester** : commandes pour reproduire les résultats

## ✅ Checklist avant de soumettre

- [ ] La modification n'introduit pas de PII (données personnelles réelles)
- [ ] Le JSON / YAML est valide (validateur en ligne ou `python -m json.tool`)
- [ ] Si vous ajoutez du code : un test minimal dans `tests/`
- [ ] Si vous ajoutez de la doc : pas de placeholders `[XXX]` oubliés
- [ ] Si vous ajoutez un cas d'étude : anonymisation vérifiée
- [ ] Le `README.md` est mis à jour si la structure change

## 🚫 Ce qui ne sera pas accepté

- Prompts adversariaux **utilisables tels quels** pour nuire (CSAM,
  malware, instructions terroristes). Le projet est défensif :
  on documente les classes d'attaque, pas les recettes opérationnelles.
- Données de clients réels sans accord écrit et anonymisation.
- Code mort, dépendances exotiques sans justification, frameworks
  redondants avec ceux déjà présents.

## 📝 Licence des contributions

En soumettant une contribution, vous acceptez que :

- Le **contenu pédagogique** (docs, templates, cas d'études) soit
  publié sous **CC BY-SA 4.0**.
- Le **code** (scripts, notebooks, utils) soit publié sous **MIT**.

Vous conservez la paternité de votre contribution.

## 💬 Questions, discussions

- Issues GitHub : pour bugs, suggestions ciblées, questions techniques.
- Pour des sujets plus larges (orientation méthodologique,
  partenariat) : contact@iaaufeminin.fr

---

**Merci de contribuer à une intelligence artificielle inclusive,
équitable et souveraine.**
