# 📋 Étape 1 — Cadrage et collecte

> **Durée estimée** : 0,5 jour (4 heures)
> **Livrable** : Une fiche système IA complétée + un cahier des charges d'audit
> **Prérequis** : Aucun (c'est ici que tout commence)

---

## 🎯 Pourquoi cette étape est cruciale

Avant de toucher au modèle, **avant même d'écrire une ligne de code**, vous
devez comprendre **dans quel contexte le modèle existe**. C'est l'étape que
80 % des audits techniques sautent — et c'est précisément ce qui distingue
un vrai audit professionnel d'un script Python jeté en l'air.

Pourquoi ? Parce qu'un même résultat technique peut être :
- **Acceptable** dans un contexte (chatbot ludique pour adultes)
- **Catastrophique** dans un autre (chatbot santé pour adolescents)

Sans cadrage, vous mesurerez peut-être très bien... mais vous mesurerez peut-être
**la mauvaise chose**.

### 📖 Une histoire pour comprendre

Imaginez deux audits du même modèle GPT-4 :

**Audit A** — Le client est une scale-up EdTech qui utilise GPT-4 pour répondre
aux questions de mathématiques d'élèves de collège. Vous découvrez que le
modèle hallucine 3 % du temps sur des questions complexes.

**Audit B** — Le client est une healthtech qui utilise GPT-4 pour répondre à
des questions de santé mentale d'adolescents. Vous découvrez exactement le
même taux d'hallucination de 3 %.

**Le même résultat technique. Deux conclusions opposées.**

Dans le cas A, 3 % d'hallucinations sur des maths est gérable (un prof peut
corriger). Dans le cas B, 3 % d'hallucinations sur des conseils de santé
mentale aux ados, c'est un risque vital.

C'est pour ça qu'on commence toujours par le cadrage.

---

## 🗺️ Vue d'ensemble de l'étape

```
┌─────────────────────────────────────────────────────────┐
│  ÉTAPE 1 — CADRAGE ET COLLECTE                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1.1  Comprendre l'usage métier                         │
│       └─ Questionnaire client (45 min)                  │
│                                                         │
│  1.2  Documenter le système IA                          │
│       └─ Fiche système IA (30 min)                      │
│                                                         │
│  1.3  Classifier le niveau de risque AI Act             │
│       └─ Grille de classification (30 min)              │
│                                                         │
│  1.4  Identifier les variables sensibles                │
│       └─ Cartographie des biais possibles (45 min)      │
│                                                         │
│  1.5  Définir le périmètre et les objectifs de l'audit  │
│       └─ Cahier des charges audit (1h)                  │
│                                                         │
│  1.6  Collecter les accès et les données               │
│       └─ Liste des éléments à recevoir (30 min)         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 1.1 Comprendre l'usage métier

### Pourquoi

Un LLM en lui-même n'est ni « bon » ni « biaisé ». Ce sont **les usages**
qu'on en fait qui créent les risques. Vous devez comprendre :

- **Qui** utilise le modèle (les utilisateurs finaux)
- **Pourquoi** ils l'utilisent (le besoin réel)
- **Quand** et **comment** ils l'utilisent (le contexte d'usage)
- **Qu'est-ce qui se passe** si le modèle se trompe (les conséquences)

### Comment

Vous menez un **entretien structuré** avec votre client (typiquement 45 minutes
en visio), guidé par le questionnaire ci-dessous.

📁 **Template** : [`templates/questionnaire_client.md`](../templates/questionnaire_client.md)

### Les 10 questions essentielles

```
1. Pouvez-vous me décrire en 3 phrases ce que fait votre modèle IA ?

2. Qui sont vos utilisateurs finaux ? (démographie, attentes, niveau tech)

3. Quel est le bénéfice principal pour eux ?

4. Combien de requêtes par jour traite votre modèle aujourd'hui ?

5. Que se passe-t-il si le modèle donne une réponse incorrecte ou
   biaisée ? (Conséquences : économiques, juridiques, humaines)

6. Avez-vous déjà eu des incidents, plaintes ou retours négatifs liés
   au modèle ?

7. Le modèle est-il déployé en autonomie totale, ou y a-t-il une
   supervision humaine ?

8. Quels sont les sujets sensibles ou interdits que le modèle ne doit
   PAS aborder ?

9. Quelles populations spécifiques (vulnérables, mineurs, personnes
   âgées...) interagissent avec le modèle ?

10. Quel est l'horizon réglementaire qui vous préoccupe ? (AI Act,
    RGPD, secteur spécifique...)
```

### Astuce pédagogique

Posez chaque question **et écoutez le silence après**. Souvent, les
informations les plus précieuses arrivent dans la deuxième moitié de la
réponse, après que le client a réfléchi. Ne coupez jamais.

### Drapeaux rouges à repérer 🚩

Pendant cet entretien, soyez attentive à ces signaux :

- 🚩 *« On n'a jamais vraiment regardé ce que ça donne sur des profils différents »*
- 🚩 *« On a eu des retours bizarres de quelques utilisateurs mais bon... »*
- 🚩 *« Notre dataset, c'est ce qu'on a trouvé en open source »*
- 🚩 *« On a juste pris GPT-4 et on a mis nos prompts par-dessus »*
- 🚩 *« On n'a pas encore réfléchi à l'AI Act »*

Chaque drapeau = une zone à creuser en profondeur dans l'audit.

---

## 1.2 Documenter le système IA

### Pourquoi

L'AI Act (Annexe IV) impose la production d'une **fiche descriptive du
système IA**. C'est aussi un livrable que votre client gardera bien après
votre audit. Profitez de l'audit pour la produire.

### Comment

À partir de l'entretien, remplissez la **Fiche Système IA** standardisée.

📁 **Template** : [`templates/fiche_systeme_ia.md`](../templates/fiche_systeme_ia.md)

### Structure de la fiche

```markdown
## Fiche descriptive du système IA

### 1. Identification
- Nom du système : ___
- Version : ___
- Éditeur/exploitant : ___
- Date de mise en production : ___

### 2. Finalité
- Objectif principal : ___
- Cas d'usage couverts : ___
- Cas d'usage explicitement exclus : ___

### 3. Architecture technique
- Type de modèle : (LLM propriétaire / Fine-tuné / API tierce)
- Modèle de base : (GPT-4 / Claude / Mistral / Llama / autre)
- Méthode d'utilisation : (zero-shot / few-shot / RAG / fine-tuning)
- Composants associés : (vector DB, retrieval, agents...)

### 4. Données
- Sources des données d'entraînement : ___
- Sources des données de fine-tuning si applicable : ___
- Sources des données de RAG si applicable : ___
- Données utilisateurs collectées : ___

### 5. Utilisation
- Volume mensuel : ___ requêtes
- Type d'interaction : (chat / one-shot / pipeline)
- Niveau d'autonomie : (totale / supervisée / co-pilotée)

### 6. Population concernée
- Utilisateurs directs : ___
- Personnes concernées par les décisions : ___
- Populations vulnérables impliquées : ___

### 7. Risques identifiés (à compléter au fil de l'audit)
- Risques de biais : ___
- Risques de sécurité : ___
- Risques d'usage détourné : ___
- Risques RGPD : ___
```

---

## 1.3 Classifier le niveau de risque AI Act

### Pourquoi

L'AI Act classe les systèmes IA en **4 niveaux de risque**, avec des
obligations très différentes pour chacun. Vous **devez** savoir dans quelle
catégorie tombe le système audité, parce que :

- Les obligations légales en dépendent
- L'étendue de votre audit en dépend
- Le pricing de votre audit en dépend (un système haut risque = plus de travail)

### Comment

Vous appliquez la grille de décision officielle. Voici une version simplifiée :

```
┌──────────────────────────────────────────────────────────────┐
│  GRILLE DE CLASSIFICATION DES RISQUES AI ACT                 │
└──────────────────────────────────────────────────────────────┘

QUESTION 1 : Le système est-il utilisé pour...
   • Manipuler subliminalement le comportement ?
   • Exploiter des vulnérabilités (âge, handicap...) ?
   • Pratiquer de la notation sociale ?
   • Reconnaître les émotions au travail ou à l'école ?
   • Identifier biométriquement à distance dans l'espace public ?

   ┌─ OUI ─→ 🔴 RISQUE INACCEPTABLE (interdit)
   │
   └─ NON ─→ Question 2

QUESTION 2 : Le système est-il utilisé dans l'un de ces domaines ?
   • Recrutement, RH, évaluation de performance
   • Évaluation pour l'éducation ou la formation
   • Accès à des services essentiels (santé, crédit, assurance,
     services publics, prestations sociales)
   • Application de la loi
   • Migration, asile, contrôle aux frontières
   • Justice et démocratie

   ┌─ OUI ─→ 🟠 HAUT RISQUE (obligations strictes)
   │
   └─ NON ─→ Question 3

QUESTION 3 : Le système est-il un système IA générative ou un chatbot
              qui interagit avec des humains ?

   ┌─ OUI ─→ 🟡 RISQUE LIMITÉ (obligations de transparence)
   │
   └─ NON ─→ 🟢 RISQUE MINIMAL (recommandations facultatives)
```

### Cas concrets

| Système | Classification | Obligations principales |
|---------|---------------|------------------------|
| Chatbot service client e-commerce | 🟡 Limité | Informer l'utilisateur qu'il parle à une IA |
| Outil de tri de CV | 🟠 Haut risque | Documentation complète, audit, supervision humaine |
| Chatbot santé mentale | 🟠 Haut risque | Idem + obligations sectorielles HAS |
| Assistant de rédaction d'emails | 🟢 Minimal | Bonnes pratiques recommandées |
| Système de scoring crédit | 🟠 Haut risque | Obligations strictes + ACPR |
| IA de recommandation produit | 🟡 Limité | Transparence sur l'usage IA |

### Astuce

Pour 90 % des LLMs grand public que vous auditez, vous serez en **Risque
Limité** ou **Haut Risque**. Le Haut Risque est votre **prix premium** : ces
audits prennent 2-3x plus de temps mais peuvent se facturer 3-5x plus.

---

## 1.4 Identifier les variables sensibles

### Pourquoi

Avant d'auditer les biais, vous devez savoir **sur quelles dimensions** les
chercher. C'est plus subtil qu'il n'y paraît.

### Les 8 axes de variables sensibles à considérer

```
1. 👤 GENRE
   - Femmes / hommes / non-binaires
   - Variations cis/trans

2. 🎂 ÂGE
   - Mineurs (< 18 ans, encore plus sensible)
   - Jeunes adultes (18-30 ans)
   - Adultes (30-60 ans)
   - Seniors (> 60 ans)

3. 🌍 ORIGINE / ETHNICITÉ
   - Inférable via prénom, nom, accent, dialecte
   - Variations géographiques
   - Statut migratoire

4. 💰 STATUT SOCIO-ÉCONOMIQUE
   - Niveau d'éducation
   - Catégorie professionnelle
   - Revenus / pouvoir d'achat
   - Niveau de littératie numérique

5. 🌐 LANGUE
   - Français vs autres langues
   - Niveau de français (natif, intermédiaire, débutant)
   - Dialectes et registres (jeunes, banlieues, régions)

6. ⚕️ SANTÉ ET HANDICAP
   - Personnes en situation de handicap
   - Maladies chroniques
   - Santé mentale

7. 🏠 SITUATION FAMILIALE
   - Marital status
   - Parents isolés
   - Aidants familiaux

8. 🏛️ APPARTENANCE PHILOSOPHIQUE / RELIGIEUSE
   - À tester avec précaution éthique
```

### Pour chaque axe, posez-vous 3 questions

1. **Cette variable est-elle pertinente** pour le cas d'usage ?
2. **Le modèle peut-il l'inférer** des inputs (même sans qu'on la lui donne) ?
3. **Y a-t-il une raison historique de soupçonner un biais** sur cette variable
   dans le domaine concerné ?

Si oui à au moins 2 des 3, **incluez l'axe dans votre audit**.

### Cas pratique : audit d'un chatbot RH

Pour un chatbot qui répond aux questions de candidat·es, vous incluriez :
- ✅ **Genre** : biais documentés massifs en RH
- ✅ **Âge** : seniors souvent désavantagé·es
- ✅ **Origine** : prénom = signal d'origine fort
- ✅ **Niveau d'éducation** : vocabulaire utilisé biaise les réponses
- ⚠️ **Handicap** : à inclure si le chatbot peut être interrogé sur ce sujet
- ❌ **Religion** : moins pertinent ici, à exclure (risque de violation RGPD)

---

## 1.5 Définir le périmètre et les objectifs de l'audit

### Pourquoi

Sans périmètre clair, votre audit dérive. Vous passez 3 jours sur un sujet
secondaire, et vous bâclez le sujet principal. Le périmètre, c'est votre
boussole.

### Comment

Vous co-rédigez avec votre client un **cahier des charges d'audit** d'une
page, qui définit :

- 🎯 **Les 3 objectifs prioritaires** de l'audit
- 🚪 **Le périmètre inclus** (modules, populations, langues...)
- 🚫 **Le périmètre exclus** (ce qui n'est pas dans cet audit)
- 📅 **Le calendrier**
- 📦 **Les livrables attendus**
- 🔐 **Les conditions d'accès** (données, API, environnements)

📁 **Template** : [`templates/cahier_des_charges_audit.md`](../templates/cahier_des_charges_audit.md)

### Exemple de cahier des charges (chatbot RH)

```markdown
# Cahier des charges — Audit du chatbot "Talia"

## Contexte
Talia est un chatbot IA basé sur GPT-4 qui répond aux questions
des candidat·es pendant le processus de recrutement chez [Client].

## Objectifs prioritaires
1. Détecter les biais de genre, d'origine et d'âge dans les réponses
2. Identifier les vulnérabilités de prompt injection
3. Évaluer la conformité AI Act (système haut risque RH)

## Périmètre inclus
- Le chatbot Talia version 2.3 (production actuelle)
- Réponses en français (langue principale)
- Tous les modules : FAQ, planification d'entretien, conseils CV

## Périmètre exclus
- Les autres outils IA du client (matching CV, scoring)
- Les versions multilingues (audit séparé prévu)
- L'audit de sécurité infrastructure (hors scope)

## Calendrier
- Lancement : lundi 15/05/2026
- Livraison rapport : vendredi 19/05/2026
- Restitution orale : mardi 23/05/2026

## Livrables
- Rapport PDF de 25-30 pages
- Annexes techniques (logs, métriques détaillées)
- Présentation de restitution (15 slides)
- Plan de remédiation chiffré

## Accès et conditions
- Accès API au chatbot avec quota dédié (~10 000 requêtes)
- Accès au prompt système (en read-only)
- 2 contacts client : [tech] et [DPO]
```

---

## 1.6 Collecter les accès et les données

### Pourquoi

Un audit qui démarre **sans tous les accès** = un audit qui prend 2x plus de
temps. La collecte se fait AVANT le jour 1 du sprint d'audit.

### La checklist d'accès

```
☐ Accès au modèle audité
   ☐ Clé API OU
   ☐ Endpoint déployé OU
   ☐ Modèle téléchargeable

☐ Documentation technique
   ☐ Architecture du système
   ☐ Prompt système (si applicable)
   ☐ Liste des modules/fonctionnalités

☐ Données
   ☐ Données d'entraînement (si propriétaire)
   ☐ Données de test/évaluation
   ☐ Logs d'usage (anonymisés) sur 30 jours
   ☐ Échantillon de conversations réelles (anonymisées)

☐ Environnement de test
   ☐ Quota API dédié à l'audit
   ☐ Environnement de pre-prod ou sandbox
   ☐ Permissions techniques nécessaires

☐ Documents existants
   ☐ Précédents audits ou évaluations
   ☐ Politique de confidentialité utilisateur
   ☐ Contrats avec sous-traitants IA (OpenAI, Anthropic...)
   ☐ Mentions légales et CGU

☐ Contacts
   ☐ Référent technique (1 personne)
   ☐ Référent métier/produit (1 personne)
   ☐ Référent conformité (DPO ou équivalent)
```

### Astuce critique

Insistez pour obtenir **un échantillon de conversations réelles anonymisées**.
C'est ce qui vous permet de découvrir des cas d'usage que personne n'avait
anticipés. Souvent, le client résiste — c'est normal. Expliquez que sans cela,
vous ne pouvez pas auditer le **comportement réel** du modèle.

---

## ✅ Checklist de fin d'étape

À la fin de l'étape 1, vous devez avoir :

- [ ] Un entretien client de 45 min réalisé et documenté
- [ ] Une **fiche système IA** complétée
- [ ] Une classification de risque AI Act
- [ ] Une cartographie des variables sensibles à auditer
- [ ] Un **cahier des charges d'audit** signé par le client
- [ ] Tous les accès techniques fonctionnels
- [ ] Les données et documents collectés

Si une seule case n'est pas cochée, **ne passez pas à l'étape 2**. Demandez
les éléments manquants. Sinon, vous payez en jour 4 ou 5 avec des allers-retours
qui font exploser votre planning.

---

## 🧠 Approfondissement : les pièges classiques

### Piège 1 — Le client minimise

> *« Notre IA est juste un petit chatbot, pas besoin d'audit poussé. »*

Beaucoup de clients sous-estiment leur exposition. Votre rôle est de leur
montrer concrètement (avec un cas réel ou un benchmark) ce qui peut mal tourner.

### Piège 2 — Le client cache les incidents

> *« Non, pas de problème particulier... »*

S'il y a eu des plaintes utilisateurs, des bug reports, des controverses
internes — vous devez les connaître. Sinon, vous risquez de découvrir les mêmes
problèmes en repartant de zéro.

**Astuce** : posez la question 3 fois sous 3 formes différentes. Vous gagnez
souvent une info au 3ème tour.

### Piège 3 — Le périmètre qui s'élargit en cours

Un client paye 4 500 € pour auditer 1 module, et vous demande au jour 3
*« tu peux jeter un œil à notre autre IA aussi ? »*. Refusez gentiment et
proposez un avenant. Le scope creep tue les audits.

---

## 📚 Pour aller plus loin

- 📖 [AI Act — Texte intégral](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- 📖 [Annexe IV de l'AI Act — Documentation technique](https://artificialintelligenceact.eu/annex/4/)
- 📖 [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- 📖 [CNIL — Plan d'action sur l'IA](https://www.cnil.fr/fr/intelligence-artificielle)
- 📖 [The Mom Test (Rob Fitzpatrick)](https://www.momtestbook.com/) — méthode d'entretien client

---

## ➡️ Prochaine étape

Une fois le cadrage terminé, on passe à l'analyse des données.

➡️ **[Étape 2 — Analyse des données](02-donnees.md)**
