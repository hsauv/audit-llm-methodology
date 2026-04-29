# 📄 Étape 7 — Documentation et rapport final

> **Durée estimée** : 0,5 jour (4 heures)
> **Livrable** : Rapport d'audit professionnel + Documentation AI Act
> **Prérequis** : Étapes 1-6 terminées

---

## 🎯 Pourquoi cette étape est cruciale

Le rapport d'audit est **ce que votre client achète vraiment**. Il doit :

1. **Être lisible** par un dirigeant non-tech
2. **Être défendable** devant un régulateur
3. **Être actionnable** pour les équipes techniques
4. **Servir de référence** pendant 12-24 mois

C'est aussi votre **vitrine professionnelle** : votre rapport circule en
interne chez le client. Il sera vu par des dizaines de personnes. Faites-en
un objet de fierté.

---

## 🗺️ Vue d'ensemble

```
7.1  Structure du rapport client (25-30 pages)
7.2  Fiche système IA conforme AI Act Annexe IV
7.3  Model Card publiable
7.4  Annexes techniques
7.5  Restitution orale
```

---

## 7.1 Structure du rapport client

Format recommandé : **PDF de 25-30 pages**, généré automatiquement à partir
des notebooks et templates.

```
┌────────────────────────────────────────────────────┐
│  RAPPORT D'AUDIT IA — [Nom du système]            │
│  Préparé pour : [Client]                          │
│  Par : Hanen Mizouni, IA au féminin               │
│  Date : [date]                                     │
├────────────────────────────────────────────────────┤
│                                                    │
│  1. RÉSUMÉ EXÉCUTIF (1 page)                      │
│     • Score global et lettre (A-E)                │
│     • 3 risques majeurs                            │
│     • 3 recommandations prioritaires               │
│                                                    │
│  2. CONTEXTE ET MÉTHODOLOGIE (2 pages)            │
│     • Description du système audité                │
│     • Méthodologie utilisée                        │
│     • Limitations de l'audit                       │
│                                                    │
│  3. ANALYSE DES DONNÉES (3-4 pages)               │
│     • Composition démographique                    │
│     • Sous-représentations                         │
│     • Probing et inférence des biais               │
│                                                    │
│  4. RÉSULTATS DE FAIRNESS (4-5 pages)             │
│     • Métriques par sous-groupe                    │
│     • Analyse intersectionnelle                    │
│     • Biais conversationnels (LLMs)                │
│                                                    │
│  5. RED-TEAMING (4-5 pages)                       │
│     • Vulnérabilités par catégorie                 │
│     • Cas concrets reproductibles                  │
│     • Sévérité et exposition                       │
│                                                    │
│  6. ROBUSTESSE (2 pages)                          │
│                                                    │
│  7. PLAN DE REMÉDIATION (4-5 pages)               │
│     • Top recommandations                          │
│     • Roadmap chiffrée                             │
│                                                    │
│  8. CONFORMITÉ AI ACT (3-4 pages)                 │
│     • Classification de risque                     │
│     • Annexe IV pré-remplie                        │
│                                                    │
│  9. ANNEXES TECHNIQUES (5-10 pages)               │
│                                                    │
└────────────────────────────────────────────────────┘
```

📁 **Template LaTeX** : [`templates/rapport_audit.tex`](../templates/rapport_audit.tex)
📁 **Template Markdown** : [`templates/rapport_audit.md`](../templates/rapport_audit.md)

---

## 7.2 Fiche système IA conforme AI Act

Récupérée et complétée depuis l'étape 1, mise à jour avec les findings de l'audit.

📁 **Template** : [`templates/fiche_systeme_ia.md`](../templates/fiche_systeme_ia.md)

---

## 7.3 Model Card publiable

Format inspiré des **HuggingFace Model Cards**, adapté pour la transparence
publique :

```markdown
# Model Card — [Nom du système]

## Vue d'ensemble
- Type : [Chatbot RH / Scoring crédit / etc.]
- Architecture : [GPT-4 + RAG / Modèle propriétaire fine-tuné]
- Date d'évaluation : [date]
- Score d'audit : [Note A-E]

## Performance
- Accuracy globale : XX %
- Précision : XX %
- Rappel : XX %

## Équité
- Demographic Parity Diff : 0.XX
- Disparate Impact : 0.XX
- Statut : ✅ / ⚠️ / 🚨

## Limites connues
- Sous-représentations identifiées : ...
- Domaines de moindre fiabilité : ...
- Cas d'usage déconseillés : ...

## Recommandations d'usage
- Public cible : ...
- Supervision humaine recommandée : ...
- Mises à jour prévues : ...
```

---

## 7.4 Annexes techniques

Documentent **tout** ce qui rend l'audit reproductible :

- Notebooks Jupyter complets (notebooks 1-6)
- Logs des tests adversariaux
- Datasets de test utilisés
- Code de remédiation suggéré
- Bibliographie technique

---

## 7.5 Restitution orale

Format recommandé : **présentation de 1h30** en visio ou présentiel.

**Trame standard** :

```
1. Contexte et objectifs       — 5 min
2. Synthèse exécutive          — 10 min
3. Top 3 risques détaillés     — 20 min
4. Plan de remédiation         — 30 min
5. Questions-réponses          — 25 min
```

**Conseil pratique** : préparez **3 versions** de la présentation :
- 15 min (pour un comité de direction)
- 45 min (pour l'équipe produit)
- 1h30 (pour les équipes techniques)

---

## ✅ Checklist de fin d'étape

- [ ] Rapport PDF de 25-30 pages produit
- [ ] Fiche système IA finalisée (AI Act Annexe IV)
- [ ] Model Card rédigée
- [ ] Annexes techniques zippées
- [ ] Présentation orale préparée (3 versions)
- [ ] Restitution programmée

---

## 🎯 Vous y êtes !

Vous avez complété un **audit IA professionnel de bout en bout**.

Votre client repart avec :
- Une compréhension claire des risques
- Un plan d'action chiffré
- La documentation conforme à ses obligations légales
- Un partenaire de confiance pour la suite

**Et vous repartez avec** :
- Une mission facturée
- Une référence client
- De la matière pour vos prochains posts LinkedIn
- Une amélioration continue de votre méthodologie

---

## 📚 Pour aller plus loin

- 📖 [Model Cards for Model Reporting (Mitchell et al., 2019)](https://arxiv.org/abs/1810.03993)
- 📖 [Datasheets for Datasets (Gebru et al., 2018)](https://arxiv.org/abs/1803.09010)
- 📖 [AI Act — Annexe IV (documentation technique)](https://artificialintelligenceact.eu/annex/4/)

---

## 🌱 Et après ?

Votre méthodologie est faite pour **évoluer** :

- Enrichissez le catalogue de prompts adversariaux après chaque audit
- Mettez à jour les seuils légaux selon la jurisprudence
- Ajoutez des modules sectoriels au fur et à mesure
- Partagez vos améliorations avec la communauté open source

**Vers une intelligence artificielle inclusive, équitable et souveraine. 🌍**

---

*Méthodologie d'audit LLM v1.0 — par Hanen Mizouni, Présidente fondatrice
de l'association IA au féminin. Licence CC BY-SA 4.0.*
