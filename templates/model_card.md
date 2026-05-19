# Model Card — [Nom du systeme IA]

> Template HuggingFace-style pour documenter un modele IA audite.
> Reference : Mitchell et al. (2019), "Model Cards for Model Reporting"
> A remplir par l'auditeur a la fin de l'audit (etape 7).

---

## Informations generales

| Champ | Valeur |
|-------|--------|
| **Nom du modele** | [ex: Talia v2.3] |
| **Type** | [LLM proprietaire / Fine-tune / RAG / Agent] |
| **Modele de base** | [ex: GPT-4 / Claude 3.5 / Mistral 7B] |
| **Developpeur** | [Nom de l'entreprise] |
| **Date de mise en production** | [JJ/MM/AAAA] |
| **Date de l'audit** | [JJ/MM/AAAA] |
| **Auditeur** | [Nom et organisation] |
| **Version du modele** | [ex: 2.3.1] |
| **Licence du modele** | [ex: proprietaire / Apache 2.0 / MIT] |

---

## Finalite et usage prevu

### Description
[2-3 phrases decrivant ce que fait le systeme IA]

### Cas d'usage prevus
- [Cas 1 : ex. reponse aux questions des candidats pendant le recrutement]
- [Cas 2 : ex. planification d'entretiens]
- [Cas 3 : ex. conseils pour la preparation de CV]

### Cas d'usage hors perimetre
- [Ex: prise de decision automatisee sur les candidatures]
- [Ex: evaluation de performance des employes]

### Utilisateurs cibles
- [Ex: candidats au recrutement (18-65 ans, tous profils)]
- [Ex: equipe RH interne (utilisateurs avances)]

---

## Donnees

### Sources d'entrainement
| Source | Type | Volume | Periode |
|--------|------|--------|---------|
| [Ex: conversations RH anonymisees] | [Fine-tuning] | [10K exemples] | [2023-2024] |
| [Ex: base documentaire entreprise] | [RAG] | [500 docs] | [2020-2024] |

### Composition demographique des donnees
| Variable | Distribution observee | Distribution attendue | Statut |
|----------|----------------------|----------------------|--------|
| Genre | [F: 32%, M: 65%, NB: 3%] | [F: 50%, M: 50%] | [PREOCCUPANT] |
| Age | [<30: 45%, 30-50: 40%, 50+: 15%] | [repartition egale] | [PREOCCUPANT] |
| Origine | [details] | [population nationale] | [A EVALUER] |

### Pre-traitement
[Description des traitements appliques aux donnees]

---

## Performance

### Metriques globales
| Metrique | Valeur | Seuil acceptable |
|----------|--------|------------------|
| Accuracy | [%] | > 85% |
| Taux de refus adequat | [%] | > 95% |
| Taux d'hallucination | [%] | < 5% |
| Latence moyenne | [ms] | < 2000ms |

### Metriques de fairness (resultats d'audit)
| Metrique | Valeur | Statut |
|----------|--------|--------|
| Demographic Parity Diff | [0.XXX] | [OK/PREOCCUPANT/CRITIQUE] |
| Equal Opportunity Diff | [0.XXX] | [OK/PREOCCUPANT/CRITIQUE] |
| Equalized Odds Diff | [0.XXX] | [OK/PREOCCUPANT/CRITIQUE] |
| Disparate Impact Ratio | [0.XX] | [OK/PREOCCUPANT/CRITIQUE] |
| Score fairness global | [XX/100] | Grade [A-E] |

### Score global d'audit
| Dimension | Score | Grade |
|-----------|-------|-------|
| Fairness | [XX/100] | [A-E] |
| Red-teaming | [XX/100] | [A-E] |
| Robustesse | [XX/100] | [A-E] |
| Donnees | [XX/100] | [A-E] |
| **Global** | **[XX/100]** | **[A-E]** |

---

## Limites et risques

### Limites connues
- [Ex: performances degradees pour les dialectes regionaux]
- [Ex: hallucinations sur les questions juridiques specifiques]
- [Ex: biais de genre detecte sur les conseils de carriere]

### Risques identifies
| Risque | Severite | Mitigation |
|--------|----------|------------|
| [Biais de genre dans les conseils] | [ELEVEE] | [Prompt engineering + monitoring] |
| [Prompt injection indirect] | [CRITIQUE] | [Filtre de sortie + validation] |
| [Hallucination medicale] | [ELEVEE] | [Redirection vers professionnel] |

### Populations vulnerables
[Description des protections en place pour les populations vulnerables]

---

## Conformite reglementaire

### Classification AI Act
- **Niveau de risque** : [Inacceptable / Haut risque / Risque limite / Minimal]
- **Justification** : [reference aux articles applicables]
- **Domaine** : [si haut risque : Annexe III reference]

### Obligations applicables
- [ ] Documentation technique (Annexe IV)
- [ ] Systeme de gestion des risques (Art. 9)
- [ ] Gouvernance des donnees (Art. 10)
- [ ] Journalisation (Art. 12)
- [ ] Transparence (Art. 13)
- [ ] Supervision humaine (Art. 14)
- [ ] Exactitude et robustesse (Art. 15)

---

## Recommandations post-audit

### Priorite haute (P0)
1. [Recommandation 1]
2. [Recommandation 2]

### Priorite moyenne (P1)
1. [Recommandation 3]

### Suivi
- **Date du prochain re-test** : [JJ/MM/AAAA]
- **Frequence de monitoring** : [mensuel / trimestriel]

---

## Citation

```
Audit realise par [Auditeur], [Organisation].
Methodologie : Audit LLM v1.0 — Hanen Mizouni / IA au feminin
Date : [JJ/MM/AAAA]
```

---

*Template de Model Card — Methodologie d'audit LLM v1.0*
*Licence : CC BY-SA 4.0*
