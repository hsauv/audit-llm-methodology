# 🔍 Audit LLM — Méthodologie complète

> Une méthodologie open source, pédagogique et reproductible pour auditer les
> grands modèles de langage (LLMs) déployés en entreprise : détection des biais,
> red-teaming, robustesse, et plan de remédiation.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python%203.10+-blue.svg)](https://www.python.org/)
[![AI Act](https://img.shields.io/badge/AI%20Act-aligned-green.svg)](https://artificialintelligenceact.eu/)

---

## 🎯 Pourquoi ce projet

L'AI Act européen entre progressivement en application en 2026-2027. Les
entreprises qui déploient des LLMs (chatbots service client, assistants RH,
outils de tri de CV, agents santé...) ont besoin d'**auditer leurs systèmes**
pour identifier les biais, vulnérabilités et risques de non-conformité.

Or, les méthodes existantes sont soit :
- **Trop académiques** : papiers de recherche peu actionnables
- **Trop opaques** : produits SaaS commerciaux fermés
- **Trop fragmentées** : un outil pour les biais, un autre pour le red-teaming...

Cette méthodologie propose un **cycle complet d'audit en 7 étapes**, documenté
de façon pédagogique, avec des notebooks Jupyter exécutables et des templates
réutilisables.

## 👤 Pour qui ?

- **Data scientists et ML engineers** qui doivent prouver l'équité de leurs modèles
- **Responsables conformité (DPO, CISO)** qui doivent se mettre en conformité AI Act
- **Auditeurs externes** qui cherchent un cadre méthodologique
- **Chercheurs et étudiants** en éthique de l'IA
- **Citoyens et associations** qui veulent comprendre comment auditer une IA

## 📚 La méthodologie en 7 étapes

| Étape | Nom | Durée | Objectif |
|-------|-----|-------|----------|
| 1 | **Cadrage et collecte** | 0,5 jour | Comprendre le système et son contexte |
| 2 | **Analyse des données** | 1 jour | Identifier les biais à la source |
| 3 | **Tests de fairness** | 1 jour | Mesurer l'équité algorithmique |
| 4 | **Red-teaming** | 1 jour | Stresser le modèle avec des prompts adversariaux |
| 5 | **Robustesse** | 0,5 jour | Vérifier la stabilité des sorties |
| 6 | **Synthèse et remédiation** | 0,5 jour | Construire le plan d'action |
| 7 | **Documentation et livraison** | 0,5 jour | Rapport conforme AI Act |

**Total : 5 jours** pour un audit complet sur un LLM.

## 🗂️ Structure du repo

```
audit-llm-methodology/
│
├── README.md                       # Vous êtes ici
├── docs/                           # Documentation pédagogique par étape
│   ├── 01-cadrage.md
│   ├── 02-donnees.md
│   ├── 03-fairness.md
│   ├── 04-redteaming.md
│   ├── 05-robustesse.md
│   ├── 06-remediation.md
│   └── 07-rapport.md
│
├── notebooks/                      # Notebooks Jupyter exécutables
│   ├── 01_cadrage_systeme.ipynb
│   ├── 02_analyse_donnees.ipynb
│   ├── 03_fairness_metrics.ipynb
│   ├── 04_redteaming_llm.ipynb
│   ├── 05_robustesse_tests.ipynb
│   └── 06_synthese_remediation.ipynb
│
├── templates/                      # Templates réutilisables
│   ├── questionnaire_client.md
│   ├── fiche_systeme_ia.md
│   ├── rapport_audit.tex
│   └── model_card.md
│
├── prompts/                        # Bibliothèques de prompts adversariaux
│   ├── biais_genre.json
│   ├── biais_origine.json
│   ├── jailbreaks.json
│   └── tests_sectoriels/
│
├── scripts/                        # Scripts Python utilitaires
│   ├── run_full_audit.py
│   ├── generate_report.py
│   └── utils/
│
└── examples/                       # Cas d'études complets
    └── case_study_chatbot_rh.md
```

## 🚀 Démarrage rapide

### Prérequis

- Python 3.10+
- Une clé API OpenAI ou Anthropic (pour tester sur des LLMs commerciaux)
- 8 Go de RAM minimum (16 Go recommandés si vous testez des modèles locaux)

### Installation

```bash
git clone https://github.com/[votre-username]/audit-llm-methodology.git
cd audit-llm-methodology
pip install -r requirements.txt
```

### Premier audit

1. Ouvrez `notebooks/01_cadrage_systeme.ipynb`
2. Suivez les instructions étape par étape
3. Enchaînez avec les notebooks 02 à 06
4. Générez votre rapport final avec `python scripts/generate_report.py`

## 📖 Documentation pédagogique

Chaque étape a sa propre documentation détaillée dans `docs/`. Commencez par :

➡️ **[Étape 1 — Cadrage et collecte](docs/01-cadrage.md)**

## ⚖️ Cadre légal et normatif

Cette méthodologie s'appuie sur :

- 🇪🇺 **AI Act européen** (Règlement 2024/1689) — annexes IV et XI
- 🇺🇸 **NIST AI Risk Management Framework** (NIST AI 100-1)
- 🌐 **ISO/IEC 42001** — Système de management de l'IA
- 📜 **OECD AI Principles**
- 🇫🇷 **Recommandations CNIL** sur l'IA

## 🧰 Stack technique

- **Fairness** : [`fairlearn`](https://github.com/fairlearn/fairlearn) (Microsoft), [`aif360`](https://github.com/Trusted-AI/AIF360) (IBM)
- **Red-teaming LLM** : [`garak`](https://github.com/leondz/garak) (NVIDIA), [`promptfoo`](https://github.com/promptfoo/promptfoo)
- **Robustesse** : [`giskard`](https://github.com/Giskard-AI/giskard), [`textattack`](https://github.com/QData/TextAttack)
- **Reporting** : `reportlab`, `weasyprint`, `jinja2`

## 🤝 Contribuer

Ce projet est ouvert aux contributions :

- 🐛 [Signaler un bug ou suggérer une amélioration](https://github.com/[votre-username]/audit-llm-methodology/issues)
- 🌍 Traduire la documentation
- 📝 Ajouter des cas d'études dans `examples/`
- 🎯 Enrichir les bibliothèques de prompts dans `prompts/`

## 📄 Licence

Cette méthodologie est publiée sous licence **Creative Commons BY-SA 4.0**.

Vous pouvez :
- ✅ La partager et la modifier
- ✅ L'utiliser à des fins commerciales (audits payants)
- ⚠️ À condition de citer l'auteur et de partager sous la même licence

Le code (notebooks, scripts) est sous licence **MIT**.

## 👤 À propos

Cette méthodologie est portée par **[Hanen Mizouni](https://www.linkedin.com/in/[votre-profil])**,
Architecte Cloud et Présidente fondatrice de l'association
[**IA au féminin**](https://iaaufeminin.fr), qui œuvre à la sensibilisation
sur les biais de l'IA et à l'inclusion numérique.

📧 contact@iaaufeminin.fr

## ⭐ Citations recommandées

Si vous utilisez cette méthodologie dans un travail académique ou professionnel :

```bibtex
@misc{mizouni2026auditllm,
  author = {Mizouni, Hanen},
  title = {Audit LLM — Méthodologie complète},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/[votre-username]/audit-llm-methodology}
}
```

---

**🌱 Pour une intelligence artificielle inclusive, équitable et souveraine.**
