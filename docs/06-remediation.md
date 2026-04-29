# 💡 Étape 6 — Synthèse et plan de remédiation

> **Durée estimée** : 0,5 jour (4 heures)
> **Livrable** : Plan de remédiation chiffré et priorisé
> **Prérequis** : Étapes 1-5 terminées

---

## 🎯 Pourquoi cette étape est cruciale

C'est **la valeur business** de votre audit. Vos clients ne paient pas pour
savoir qu'ils ont des biais — ils paient pour savoir **comment les corriger**.

C'est aussi votre **différenciation majeure** sur le marché : Giskard et
Credo AI font de l'audit, peu font de la remédiation actionnable.

### 📖 Ce qui distingue un bon plan de remédiation

❌ **Mauvais** : *"Améliorez la diversité de vos données d'entraînement."*
→ Inactionnable, abstrait.

✅ **Bon** : *"Ajoutez 240 exemples de CV de femmes seniors (50+) au dataset de fine-tuning. Coût estimé : 2 jours-homme. Impact attendu : amélioration du selection_rate de cette population de 12 % à 28 %."*
→ Précis, chiffré, évaluable.

---

## 🗺️ Vue d'ensemble

```
6.1  Construction du score global multi-axes
6.2  Priorisation des problèmes (impact × effort)
6.3  Plan de remédiation par famille
6.4  Roadmap chiffrée
6.5  Document client final
```

---

## 6.1 Score global multi-axes

```
SCORE GLOBAL D'AUDIT IA = 
    30% × Score Fairness (étape 3)
  + 25% × Score Red-teaming (étape 4)
  + 20% × Score Données (étape 2)
  + 15% × Score Robustesse (étape 5)
  + 10% × Score Documentation/Conformité
```

Note finale traduite en **lettre A à E** (à la NutriScore).

| Note | Score | Statut | Recommandation |
|------|-------|--------|----------------|
| 🟢 A | 85-100 | Exemplaire | Communicable publiquement |
| 🟢 B | 70-84 | Bon | Améliorations recommandées |
| 🟡 C | 55-69 | Moyen | Remédiation avant prod grand public |
| 🟠 D | 40-54 | Préoccupant | Déploiement déconseillé en l'état |
| 🔴 E | 0-39 | Critique | Refactoring profond requis |

---

## 6.2 Priorisation impact × effort

Pour chaque problème détecté, vous évaluez :

**Impact** (1-5) :
- Sévérité du risque (légal, image, opérationnel)
- Nombre d'utilisateurs concernés
- Réversibilité

**Effort** (1-5) :
- Temps de mise en œuvre (jours-homme)
- Complexité technique
- Risque de régression

**Matrice de priorisation** :

```
        EFFORT FAIBLE       EFFORT ÉLEVÉ
       ┌──────────────────┬──────────────────┐
IMPACT │  🟢 QUICK WINS   │  🟠 PROJETS      │
ÉLEVÉ  │  À faire d'abord │  À planifier     │
       ├──────────────────┼──────────────────┤
IMPACT │  🟡 BONUS        │  ⚪ À ÉVITER     │
FAIBLE │  Si temps        │  Pas prioritaire │
       └──────────────────┴──────────────────┘
```

---

## 6.3 Les 4 familles de remédiation

### Famille 1 — Pré-traitement des données

- **Reweighing** : pondérer les échantillons sous-représentés
- **Oversampling** : dupliquer ou synthétiser les minorités
- **Suppression de proxies** : retirer les variables qui leakent les variables sensibles

**Outils** : `aif360.algorithms.preprocessing`

### Famille 2 — Post-traitement

- **Calibration par sous-groupe** : ajuster les seuils par population
- **Reject option classifier** : zone d'incertitude où on délègue à l'humain
- **Filtres en sortie** : détection de biais en temps réel

**Outils** : `aif360.algorithms.postprocessing`, `Guardrails AI`

### Famille 3 — Re-entraînement

- **Adversarial debiasing** : entraîner contre un classifieur de biais
- **Fine-tuning ciblé** : sur datasets équilibrés
- **RLHF orienté équité** : pour LLMs, retour humain ciblé

### Famille 4 — Garde-fous architecturaux

- **Prompt engineering** : prompts système anti-biais
- **Validation humaine** : sur les cas à haut risque
- **Multi-modèles** : ensemble de modèles avec voting

---

## 6.4 Roadmap chiffrée

Pour chaque recommandation, vous fournissez :

```markdown
## RECOMMANDATION #1 — Quick win

### Diagnostic
Sous-représentation des femmes seniors (1.2 % vs 25 % attendus)
→ Impact direct sur Disparate Impact (0.43)

### Solution proposée
Ajout de 240 exemples synthétiques de CV de femmes 50+ ans
au dataset de fine-tuning, via génération assistée par GPT-4
puis validation manuelle.

### Effort estimé
- 1 jour-homme génération
- 1 jour-homme validation manuelle
- 2 heures de fine-tuning
- Coût total : ~1 200 €

### Impact attendu
- Selection rate F50+ : 4 % → 22 %
- Disparate Impact : 0.43 → 0.78
- Score fairness : +12 points

### Indicateur de succès
Re-test fairness après remédiation : DI > 0.80
```

### Synthèse en tableau

```
ID  | Recommandation              | Effort   | Impact | Priorité
────┼─────────────────────────────┼──────────┼────────┼─────────
R01 | Rééquilibrage femmes 50+    | 2 j-h    | 9/10   | 🔴 P0
R02 | Patch jailbreak DAN         | 1 j-h    | 8/10   | 🔴 P0
R03 | Filtre prompt injection     | 3 j-h    | 9/10   | 🔴 P0
R04 | Documentation AI Act        | 5 j-h    | 6/10   | 🟠 P1
R05 | Calibration par groupe      | 8 j-h    | 7/10   | 🟠 P1
R06 | Monitoring continu          | 15 j-h   | 5/10   | 🟡 P2
```

---

## 6.5 Document client final

Le **plan de remédiation** est un document autonome, livrable séparément
du rapport d'audit. Il contient :

- Synthèse exécutive (1 page)
- Top 5 recommandations détaillées
- Roadmap visuelle sur 6-12 mois
- Estimation budgétaire globale
- Plan de re-test post-remédiation

📁 **Template** : [`templates/plan_remediation.md`](../templates/plan_remediation.md)

---

## ✅ Checklist de fin d'étape

- [ ] Score global multi-axes calculé (A-E)
- [ ] Priorisation impact × effort effectuée
- [ ] Recommandations chiffrées (effort + impact)
- [ ] Roadmap visuelle produite
- [ ] Plan de remédiation rédigé

---

## ➡️ Prochaine étape

➡️ **[Étape 7 — Documentation et livraison](07-rapport.md)**
