# 📋 Fiche descriptive du système IA

> **Conforme à l'Annexe IV de l'AI Act européen (Règlement 2024/1689)**
> **Document de référence à tenir à jour tout au long du cycle de vie du système**

---

## 1. Identification du système

| Champ | Valeur |
|-------|--------|
| **Nom du système IA** | _____________________________________ |
| **Version** | _____________________________________ |
| **Date de mise en production** | _____________________________________ |
| **Éditeur / Exploitant** | _____________________________________ |
| **Représentant légal** | _____________________________________ |
| **Référent technique** | _____________________________________ |
| **Référent conformité (DPO)** | _____________________________________ |

---

## 2. Finalité et cas d'usage

### 2.1 Description générale

> _____________________________________________________________________
> _____________________________________________________________________
> _____________________________________________________________________

### 2.2 Objectif principal du système

> _____________________________________________________________________

### 2.3 Cas d'usage couverts

- [ ] Cas d'usage 1 : __________________________________
- [ ] Cas d'usage 2 : __________________________________
- [ ] Cas d'usage 3 : __________________________________

### 2.4 Cas d'usage explicitement exclus

> _____________________________________________________________________

### 2.5 Bénéfices attendus pour les utilisateurs

> _____________________________________________________________________

---

## 3. Classification AI Act

### 3.1 Niveau de risque

- [ ] 🔴 **Risque inacceptable** (système interdit — ne pas déployer)
- [ ] 🟠 **Haut risque** (Annexe III de l'AI Act)
- [ ] 🟡 **Risque limité** (obligations de transparence)
- [ ] 🟢 **Risque minimal** (recommandations facultatives)

### 3.2 Justification de la classification

> _____________________________________________________________________
> _____________________________________________________________________

### 3.3 Domaine d'application (si Haut Risque)

- [ ] Éducation et formation
- [ ] Emploi et gestion des travailleurs (incluant recrutement)
- [ ] Accès aux services privés essentiels
- [ ] Accès aux services publics et prestations
- [ ] Application de la loi
- [ ] Migration, asile, contrôle aux frontières
- [ ] Justice et démocratie
- [ ] Identification biométrique
- [ ] Infrastructure critique

---

## 4. Architecture technique

### 4.1 Type de système

- [ ] LLM propriétaire entraîné en interne
- [ ] LLM open source self-hosted
- [ ] API d'un fournisseur tiers (OpenAI, Anthropic...)
- [ ] LLM fine-tuné sur des données propriétaires
- [ ] Système hybride (préciser) : __________

### 4.2 Modèle de fondation utilisé

| Champ | Valeur |
|-------|--------|
| **Nom du modèle** | __________ |
| **Fournisseur** | __________ |
| **Version exacte** | __________ |
| **Licence** | __________ |

### 4.3 Méthode d'utilisation

- [ ] Zero-shot (prompts uniquement)
- [ ] Few-shot (exemples dans le prompt)
- [ ] Retrieval Augmented Generation (RAG)
- [ ] Fine-tuning sur données propriétaires
- [ ] Architecture multi-agents
- [ ] Autre : __________

### 4.4 Composants associés

> Décrire les autres briques techniques (vector DB, retrieval, agents,
> outils externes appelés...) :
>
> _____________________________________________________________________
> _____________________________________________________________________

### 4.5 Diagramme d'architecture

> [À insérer ou à joindre en annexe]

---

## 5. Données

### 5.1 Données d'entraînement

| Source | Volume | Période | Méthode d'acquisition |
|--------|--------|---------|----------------------|
| | | | |
| | | | |

### 5.2 Données de fine-tuning (si applicable)

| Source | Volume | Période | Consentement |
|--------|--------|---------|--------------|
| | | | |

### 5.3 Données de RAG (si applicable)

| Source | Mise à jour | Format | Sensibilité |
|--------|-------------|--------|-------------|
| | | | |

### 5.4 Données utilisateurs collectées en production

- [ ] Logs de conversations
- [ ] Métriques d'usage
- [ ] Feedback utilisateurs
- [ ] Données de profil (lesquelles ?) : __________
- [ ] Aucune donnée utilisateur conservée

### 5.5 Composition démographique des données

> Si connue, décrire la répartition selon les variables sensibles
> (genre, âge, origine, langue...) :
>
> _____________________________________________________________________

### 5.6 Sous-représentations identifiées

> _____________________________________________________________________

---

## 6. Population concernée

### 6.1 Utilisateurs directs

| Caractéristique | Description |
|-----------------|-------------|
| Âge moyen | __________ |
| Répartition genre | __________ |
| Niveau de littératie numérique | __________ |
| Langues principales | __________ |
| Volume mensuel d'utilisateurs uniques | __________ |

### 6.2 Personnes affectées par les décisions du système

> _____________________________________________________________________

### 6.3 Populations vulnérables impliquées

- [ ] Mineurs
- [ ] Personnes âgées
- [ ] Personnes en situation de handicap
- [ ] Personnes vulnérables économiquement
- [ ] Personnes éloignées du numérique
- [ ] Aucune population vulnérable
- [ ] Autre : __________

### 6.4 Mesures spécifiques pour les populations vulnérables

> _____________________________________________________________________

---

## 7. Performance et limites du système

### 7.1 Métriques de performance

| Métrique | Valeur cible | Valeur mesurée | Date mesure |
|----------|--------------|----------------|-------------|
| Précision | __________ | __________ | __________ |
| Rappel | __________ | __________ | __________ |
| F1-score | __________ | __________ | __________ |
| Taux d'hallucination | __________ | __________ | __________ |
| Latence moyenne | __________ | __________ | __________ |

### 7.2 Limites connues du système

> _____________________________________________________________________
> _____________________________________________________________________

### 7.3 Conditions d'utilisation requises

> Le système est conçu pour fonctionner dans les conditions suivantes :
>
> _____________________________________________________________________

### 7.4 Conditions d'utilisation déconseillées

> Le système ne doit PAS être utilisé pour :
>
> _____________________________________________________________________

---

## 8. Risques identifiés

### 8.1 Risques de biais

| Type de biais | Niveau | Mesure de mitigation |
|---------------|--------|----------------------|
| Biais de genre | __________ | __________ |
| Biais d'âge | __________ | __________ |
| Biais d'origine | __________ | __________ |
| Biais socio-économique | __________ | __________ |
| Autre | __________ | __________ |

### 8.2 Risques de sécurité

- [ ] Prompt injection
- [ ] Data leakage
- [ ] Jailbreaking
- [ ] Détournement d'usage
- [ ] Autre : __________

### 8.3 Risques RGPD

> _____________________________________________________________________

### 8.4 Risques d'usage détourné

> _____________________________________________________________________

---

## 9. Supervision humaine

### 9.1 Niveau d'autonomie

- [ ] Autonomie totale (le modèle décide seul, pas de supervision)
- [ ] Co-pilote (le modèle propose, un humain valide avant action)
- [ ] Assistance (le modèle aide, l'humain décide)
- [ ] Supervision continue (modérateur humain en permanence)

### 9.2 Mécanismes d'override humain

> Comment un humain peut-il contredire ou corriger le modèle ?
>
> _____________________________________________________________________

### 9.3 Procédure de remontée d'alerte

> _____________________________________________________________________

---

## 10. Cycle de vie et maintenance

### 10.1 Date de dernière mise à jour majeure

> __________

### 10.2 Fréquence de mise à jour prévue

> __________

### 10.3 Procédure de gestion des changements

> _____________________________________________________________________

### 10.4 Plan de retrait du service

> Que se passe-t-il quand le système est retiré ?
>
> _____________________________________________________________________

---

## 11. Documentation associée

- [ ] Politique de confidentialité utilisateur
- [ ] CGU mentionnant l'usage de l'IA
- [ ] Mention de l'IA dans l'interface (transparence)
- [ ] Documentation technique pour développeurs
- [ ] Guide utilisateur
- [ ] Précédents rapports d'audit
- [ ] Contrat avec le fournisseur du modèle

---

## 12. Historique des audits et évaluations

| Date | Type d'audit | Auditeur | Résultats principaux |
|------|--------------|----------|----------------------|
| | | | |
| | | | |

---

## 13. Validation et signatures

| Rôle | Nom | Date | Signature |
|------|-----|------|-----------|
| Référent technique | | | |
| DPO / Conformité | | | |
| Représentant légal | | | |

---

## 📚 Références normatives

- **AI Act européen** (Règlement UE 2024/1689) — Annexe IV
- **NIST AI Risk Management Framework** (NIST AI 100-1)
- **ISO/IEC 42001:2023** — Système de management de l'IA
- **CNIL** — Recommandations sur l'IA

---

*Fiche établie selon la méthodologie d'audit LLM v1.0 — avril 2026.*
*© Hanen Mizouni / Association IA au féminin — Licence CC BY-SA 4.0*
