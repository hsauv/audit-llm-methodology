# 📄 Rapport d'audit IA — [Nom du système]

> **Préparé pour** : [Client]
> **Préparé par** : Hanen Mizouni — IA au féminin
> **Date de livraison** : _____________
> **Version** : 1.0
> **Statut** : ✅ Final

---

# 1. Résumé exécutif

## 1.1 Vue d'ensemble

> Synthèse en 3-4 paragraphes du système audité, du contexte et des résultats principaux.

## 1.2 Score global

```
┌─────────────────────────────────────────────┐
│                                             │
│   SCORE GLOBAL : __ / 100                   │
│                                             │
│   Grade : __                                │
│                                             │
│   Statut : 🟢/🟡/🟠/🔴 [Statut textuel]    │
│                                             │
└─────────────────────────────────────────────┘
```

## 1.3 Top 3 risques majeurs identifiés

1. 🔴 **[Risque 1]** — Sévérité critique
   > Description courte (2-3 phrases)

2. 🟠 **[Risque 2]** — Sévérité élevée
   > Description courte

3. 🟡 **[Risque 3]** — Sévérité modérée
   > Description courte

## 1.4 Top 3 recommandations prioritaires

1. **R01** — [Titre] (effort : __ j-h, budget : ____ €)
2. **R02** — [Titre] (effort : __ j-h, budget : ____ €)
3. **R03** — [Titre] (effort : __ j-h, budget : ____ €)

---

# 2. Contexte et méthodologie

## 2.1 Description du système audité

[Description détaillée]

## 2.2 Périmètre de l'audit

[Inclus / exclus, comme défini dans le cahier des charges]

## 2.3 Méthodologie utilisée

L'audit suit la **Méthodologie d'audit LLM v1.0** en 7 étapes :

1. Cadrage et collecte
2. Analyse des données
3. Tests de fairness algorithmique
4. Red-teaming et tests adversariaux
5. Tests de robustesse
6. Synthèse et plan de remédiation
7. Documentation et livraison

Cette méthodologie est conforme aux référentiels :
- 🇪🇺 AI Act européen (Règlement 2024/1689)
- 🇺🇸 NIST AI Risk Management Framework
- 🌐 ISO/IEC 42001
- 🇫🇷 Recommandations CNIL sur l'IA

## 2.4 Limitations de l'audit

[Limitations méthodologiques et techniques de l'audit]

---

# 3. Analyse des données

## 3.1 Sources de données analysées

[Inventaire des sources]

## 3.2 Composition démographique

[Distributions par variable sensible avec graphiques]

## 3.3 Sous-représentations identifiées

[Tableau des sous-groupes en sous-représentation]

## 3.4 Probing du modèle de fondation

[Résultats des tests de probing pour LLMs opaques]

## 3.5 Synthèse de l'étape 2

> Score étape 2 : __ / 100

🚩 **Drapeaux rouges identifiés** :
- _____________
- _____________

---

# 4. Résultats de fairness

## 4.1 Métriques par sous-groupe

| Métrique | Femmes | Hommes | Écart | Statut |
|----------|--------|--------|-------|--------|
| Taux de sélection | | | | |
| TPR (Equal Opp.) | | | | |
| FPR | | | | |
| Accuracy | | | | |
| Disparate Impact | | | | |

## 4.2 Analyse intersectionnelle

[Résultats par croisement de variables]

## 4.3 Biais conversationnels (matched pairs)

[Mesures sur longueur, ton, suggestions, etc.]

## 4.4 Synthèse de l'étape 3

> Score fairness : __ / 100

🚩 **Drapeaux rouges identifiés** : ...

---

# 5. Red-teaming et vulnérabilités

## 5.1 Catalogue de tests utilisé

[___ tests répartis en ___ catégories]

## 5.2 Vulnérabilités détectées par catégorie

| Catégorie | Tests | Vulnérabilités | Taux |
|-----------|-------|----------------|------|
| Jailbreaks | | | |
| Prompt injection | | | |
| Extraction | | | |
| Toxicité | | | |
| Sectoriels | | | |

## 5.3 Top vulnérabilités critiques

[Liste détaillée avec sévérité et reproductibilité]

## 5.4 Synthèse de l'étape 4

> Score red-teaming : __ / 100

---

# 6. Robustesse et stabilité

## 6.1 Tests de perturbations

[Résultats]

## 6.2 Cohérence sémantique

[Variance des réponses sur 50 itérations]

## 6.3 Tests aux limites

[Comportement aux extrêmes]

## 6.4 Synthèse de l'étape 5

> Score robustesse : __ / 100

---

# 7. Plan de remédiation

[Voir document séparé `plan_remediation.md` pour le détail]

## 7.1 Synthèse des recommandations

| ID | Action | Priorité | Effort | Budget |
|----|--------|----------|--------|--------|
| R01 | | P0 | | |
| R02 | | P0 | | |
| R03 | | P0 | | |
| R04 | | P1 | | |
| R05 | | P1 | | |

## 7.2 Score attendu après remédiation

Score actuel : __ → Score cible : __

---

# 8. Conformité AI Act

## 8.1 Classification du système

[Niveau de risque + justification]

## 8.2 Obligations applicables

[Liste des obligations de l'AI Act applicables au système]

## 8.3 Statut de conformité actuel

| Obligation | Statut |
|------------|--------|
| Article 9 — Gestion des risques | ✅ / ⚠️ / ❌ |
| Article 10 — Gouvernance des données | |
| Article 11 — Documentation technique | |
| Article 13 — Transparence | |
| Article 14 — Supervision humaine | |
| Article 15 — Précision et robustesse | |

## 8.4 Fiche système IA (Annexe IV)

[Voir document séparé `fiche_systeme_ia.md`]

---

# 9. Annexes

## Annexe A — Détails méthodologiques

## Annexe B — Tableaux de métriques détaillés

## Annexe C — Catalogue de prompts adversariaux

## Annexe D — Notebooks Jupyter (sur demande)

## Annexe E — Bibliographie et références

---

## 📞 Contact pour suivi

**Hanen Mizouni**
Présidente fondatrice — IA au féminin
📧 contact@iaaufeminin.fr
📞 07 83 96 13 20
🌐 https://iaaufeminin.fr

---

*Rapport produit selon la Méthodologie d'audit LLM v1.0*
*Confidentialité : ce document est strictement confidentiel*
