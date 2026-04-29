# 📋 Questionnaire client — Préparation de l'audit IA

> **Usage** : à envoyer au client avant le kick-off de l'audit
> **Durée de remplissage** : 30-45 minutes
> **Format** : à compléter par écrit ou à utiliser comme guide d'entretien

---

## 🎯 Objectif de ce questionnaire

Ce questionnaire nous permet de **comprendre votre système IA en profondeur**
avant de démarrer l'audit. Plus vos réponses sont précises, plus l'audit
sera ciblé et utile.

**Toutes vos réponses sont confidentielles** et couvertes par notre accord
de confidentialité.

---

## SECTION 1 — Le système IA en quelques mots

**Q1. En 3 phrases maximum, décrivez ce que fait votre système IA.**
> Réponse libre :
>
> ___________________________________________________________
> ___________________________________________________________
> ___________________________________________________________

**Q2. Pouvez-vous donner 2-3 exemples concrets d'interactions typiques
       avec votre système ?**
> Exemple 1 (input → output attendu) :
>
> ___________________________________________________________
>
> Exemple 2 :
>
> ___________________________________________________________
>
> Exemple 3 (cas plus complexe) :
>
> ___________________________________________________________

**Q3. Depuis quand le système est-il en production ?**
> ☐ Pas encore en prod (en développement)
> ☐ Beta privée
> ☐ Beta publique
> ☐ Production depuis moins de 6 mois
> ☐ Production depuis 6-18 mois
> ☐ Production depuis plus de 18 mois

---

## SECTION 2 — Architecture technique

**Q4. Quel modèle de fondation utilisez-vous ?**
> ☐ GPT-4 / GPT-4 Turbo / GPT-4o (OpenAI)
> ☐ Claude (Anthropic) — précisez la version : __________
> ☐ Mistral / Mixtral
> ☐ Llama 3 (Meta)
> ☐ Modèle propriétaire entraîné en interne
> ☐ Autre : __________

**Q5. Comment utilisez-vous le modèle ?**
> ☐ Zero-shot (juste des prompts)
> ☐ Few-shot (exemples dans le prompt)
> ☐ RAG (Retrieval Augmented Generation, base de connaissances)
> ☐ Fine-tuning sur vos données
> ☐ Architecture multi-agents
> ☐ Autre : __________

**Q6. Quel est le volume de requêtes mensuelles ?**
> ☐ < 1 000
> ☐ 1 000 — 10 000
> ☐ 10 000 — 100 000
> ☐ 100 000 — 1 million
> ☐ > 1 million

**Q7. Quelle est la latence cible ?**
> ☐ Temps réel (< 1s)
> ☐ Quasi temps réel (1-5s)
> ☐ Asynchrone acceptable

---

## SECTION 3 — Données

**Q8. Si vous faites du fine-tuning ou du RAG, quelles sont les sources
       de vos données ?**
> ___________________________________________________________
> ___________________________________________________________

**Q9. Avez-vous documenté la composition démographique de vos données
       (genre, âge, origine...) ?**
> ☐ Oui, complètement
> ☐ Oui, partiellement
> ☐ Non, mais nous avons les données brutes
> ☐ Non, données anonymisées et non labellisées

**Q10. Vos données contiennent-elles des informations personnelles
        (RGPD-sensibles) ?**
> ☐ Aucune donnée personnelle
> ☐ Données pseudonymisées
> ☐ Données personnelles (nom, contact...) avec consentement
> ☐ Données sensibles (santé, religion, opinion...) avec consentement
> ☐ Je ne sais pas

---

## SECTION 4 — Utilisateurs et usage

**Q11. Qui sont vos utilisateurs finaux ? (cochez tout ce qui s'applique)**
> ☐ Grand public adulte
> ☐ Mineurs (sous quelle forme ?) : __________
> ☐ Professionnels (B2B)
> ☐ Salariés en interne
> ☐ Personnes en situation de vulnérabilité (préciser) : __________

**Q12. Quelles populations spécifiques utilisent activement votre système ?**
> Décrivez la démographie connue ou estimée :
>
> ___________________________________________________________
> ___________________________________________________________

**Q13. Le système est-il utilisé en autonomie totale ou avec supervision
        humaine ?**
> ☐ Autonomie totale (le modèle décide seul)
> ☐ Co-pilote (le modèle propose, l'humain valide)
> ☐ Assistance (le modèle aide, l'humain décide)
> ☐ Supervision continue par modérateur

**Q14. Que se passe-t-il si le modèle donne une réponse incorrecte ?**
> ___________________________________________________________
> ___________________________________________________________

---

## SECTION 5 — Risques et incidents

**Q15. Avez-vous déjà eu des incidents ou retours négatifs concernant le
        comportement du modèle ?**
> ☐ Non, jamais
> ☐ Oui, retours mineurs (préciser) : __________
> ☐ Oui, incidents notables (préciser) : __________
> ☐ Oui, plaintes formelles (préciser) : __________

**Q16. Quels types d'erreurs vous inquiètent le plus ?**
> Classez de 1 (le plus critique) à 5 :
>
> ☐ Hallucinations / informations factuellement fausses
> ☐ Biais discriminatoires (genre, origine, âge...)
> ☐ Réponses inappropriées ou offensantes
> ☐ Fuites de données ou prompts sensibles
> ☐ Détournement par injection de prompts

**Q17. Y a-t-il des sujets que le modèle ne doit absolument PAS aborder ?**
> ___________________________________________________________
> ___________________________________________________________

---

## SECTION 6 — Conformité

**Q18. Avez-vous identifié les obligations AI Act qui vous concernent ?**
> ☐ Oui, et nous sommes en conformité
> ☐ Oui, et nous travaillons à la conformité
> ☐ Oui, mais nous n'avons pas commencé
> ☐ Non, nous n'avons pas encore regardé
> ☐ Non, nous ne pensons pas être concernés

**Q19. Êtes-vous soumis à des réglementations sectorielles ?**
> ☐ RGPD général
> ☐ ACPR (banque, assurance)
> ☐ HAS / ANSM (santé)
> ☐ CNIL spécifique IA
> ☐ Code du travail (RH, recrutement)
> ☐ Loi pour une République numérique (services publics)
> ☐ Autre : __________

**Q20. Avez-vous une personne dédiée à la conformité IA ?**
> ☐ Oui, en interne (qui ?) : __________
> ☐ Oui, externalisée (cabinet ?) : __________
> ☐ Non, c'est diffus
> ☐ Non, c'est mon rôle (CEO / CTO / CPO)

---

## SECTION 7 — Vos attentes vis-à-vis de l'audit

**Q21. Quelles sont vos 3 attentes principales pour cet audit ?**
> 1. ___________________________________________________________
> 2. ___________________________________________________________
> 3. ___________________________________________________________

**Q22. Avez-vous des contraintes calendaires ?**
> ☐ Pas de contrainte particulière
> ☐ Audit à terminer avant : __________ (date)
> ☐ Audit à présenter au board le : __________ (date)
> ☐ Demande client urgente

**Q23. Comment souhaitez-vous recevoir le livrable final ?**
> ☐ Rapport PDF + restitution orale (recommandé)
> ☐ Rapport PDF uniquement
> ☐ Présentation interactive uniquement
> ☐ Autre format : __________

---

## SECTION 8 — Logistique

**Q24. Qui sera mon point de contact technique principal pendant l'audit ?**
> Nom : __________
> Fonction : __________
> Email : __________
> Téléphone : __________

**Q25. Qui sera mon point de contact côté conformité ou DPO ?**
> Nom : __________
> Fonction : __________
> Email : __________

**Q26. Pouvez-vous fournir un accès API dédié pour l'audit ?**
> ☐ Oui, avec quota défini : __________ requêtes
> ☐ Oui, sans quota
> ☐ À voir avec l'équipe technique
> ☐ Non, accès via interface utilisateur uniquement

**Q27. Pouvez-vous fournir un échantillon anonymisé de conversations
        réelles ?**
> ☐ Oui, sans problème
> ☐ Oui, avec NDA renforcé
> ☐ Non, contraintes RGPD/confidentialité

---

## ✍️ Signature et engagement

Je certifie avoir répondu de bonne foi et de manière exhaustive à ce
questionnaire, et m'engage à fournir les accès et documents nécessaires
au bon déroulement de l'audit.

> Nom : __________
> Fonction : __________
> Date : __________
> Signature : __________

---

## 📞 Questions ?

Pour toute question concernant ce questionnaire, contactez :

**Hanen Mizouni**
contact@iaaufeminin.fr · 07 83 96 13 20

---

*Document préparé par Hanen Mizouni, Présidente fondatrice de l'association
IA au féminin. Méthodologie d'audit LLM v1.0 — avril 2026.*
