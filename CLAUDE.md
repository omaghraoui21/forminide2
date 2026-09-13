# CLAUDE.md — Contrat de travail pour ce dépôt

Ce dépôt est un **dossier de développement formulation DPI**, pas un projet logiciel.
Le « code » est du raisonnement pharmaceutique traçable. Ces règles sont contraignantes.

## 1. Contexte permanent (à ne pas redécouvrir)

- **Produit** : bulk DPI unique → capsule taille 3, **25,0 mg de poudre**,
  **Formotérol fumarate dihydraté 12 µg** + **Budésonide 200 µg ou 400 µg**.
- **Charges massiques** : BUD 0,800 % (200 µg) ou 1,600 % (400 µg) ; **FOR 0,0480 %**.
  Ratio BUD:FOR = **16,7:1** ou **33,3:1**.
- **APIs** : achetés micronisés. Pas de jet milling, pas de co-micronisation, pas de spray drying.
- **Lactoses disponibles** : Respitose® **ML001**, **SV003**, **SV010** (DFE Pharma).
- **Carriers des mono-produits existants** (information interne, 2026-09-13) :
  **formotérol → ML001 seul** · **budésonide → mélange SV003 + ML001**.
  Conséquence : le prémix formotérol se fait **sur ML001** (ADR-015), et le **taux de ML001 du
  bulk combiné** est une variable d'essai de premier rang, pas un paramètre hérité du budésonide.
- **Équipements** : mélangeur **Inversina ≈ 20 L** (jusqu'à ~9 kg), tamiseur **Russell 250 µm**,
  remplisseuse **Harro Höfliger Modu-C MS**, dispositif **type Aerolizer** disponible.
- **Historique** : procédé mono-produit robuste à 3, 6 et 9 kg (dilution séquentielle en
  3 fractions, sandwich lactose/API/lactose, tamisage, Inversina 15 min par étape).
  Le **combiné BUD/FOR développé directement à 9 kg a échoué** ; l'équipe historique a
  séparé les deux formulations. Cause exacte non documentée → c'est la question centrale.
- **Diagnostic retenu** (voir `RAPPORT.md` §A) : co-agglomération API–API dans le sandwich
  commun + la dernière dilution (la plus difficile) exécutée au taux de remplissage le plus
  défavorable du mélangeur.

## 2. Règles de véracité — non négociables

1. **Ne jamais fabriquer une donnée.** Aucune valeur numérique sans source ou sans mention
   explicite `calcul interne`.
2. **Étiqueter chaque affirmation** avec l'un de :
   `FAIT CONFIRMÉ` (source primaire vérifiable : notice/KÜB/SmPC, brevet, article, fiche fournisseur)
   · `INFÉRENCE HAUTE CONFIANCE` · `INFÉRENCE FAIBLE CONFIANCE` · `INCONNU`.
3. **Format obligatoire pour toute information critique** :
   `SOURCE → DONNÉE → NIVEAU DE CONFIANCE → INTERPRÉTATION → CONSÉQUENCE POUR NOTRE ESSAI`.
   Le registre vit dans `docs/annexes/A1-registre-preuves.md`.
4. **Une inférence OSINT n'est jamais présentée comme une donnée officielle**, même plausible.
5. **Distinguer toujours** : faits · inférences · hypothèses · recommandations expérimentales.
6. Si une donnée manque, l'écrire dans `memory/questions-ouvertes.md` **et continuer** le
   travail qui n'en dépend pas. Ne pas bloquer l'ensemble sur une donnée manquante.

## 3. Règles de fond (garde-fous du projet)

- **Le procédé historique n'est pas mauvais** : il fonctionne sur les mono-produits et il
  correspond à une plateforme brevetée publiée (EP3175842A1). On cherche la **modification
  minimale** qui le rend compatible dual-API, pas un procédé neuf.
- **Ne jamais recommander un jet mill, un spray dryer ou un mélangeur haut cisaillement**
  pour simplifier le problème. Hors périmètre, hors budget, hors sujet.
- **Ne pas proposer 20 formulations.** Toute proposition doit éliminer une hypothèse.
- Toute nouvelle dépense (grade de lactose, excipient, équipement) doit nommer
  **la fonction absente** qu'elle apporte, sinon elle est refusée.
- Le **formotérol est le sujet** : à 0,048 % m/m, toute décision de procédé doit être
  évaluée d'abord par son effet sur le formotérol.

## 4. Conventions d'écriture

- **Langue : français.** Termes techniques anglais admis (fines, carrier, premix, FPF, FPD).
- Unités SI, virgule décimale française dans le texte, point dans les tableaux de calcul.
- « FOR » = formotérol fumarate dihydraté ; « BUD » = budésonide ; « CU » = content uniformity.
- Toujours préciser si un % est m/m, du dosé, du délivré ou du nominal.
- Les niveaux de dose sont exprimés **par capsule** (dose mesurée), pas par dose délivrée,
  sauf mention explicite.

## 5. Protocole de mémoire

| Fichier | Rôle | Quand l'écrire |
|---|---|---|
| `memory/decisions.md` | Décisions engageantes, format ADR (contexte / décision / raison / conséquence / réversibilité) | à chaque arbitrage |
| `memory/questions-ouvertes.md` | Données manquantes, avec propriétaire et impact | dès qu'une inconnue bloque une conclusion |
| `memory/journal.md` | Journal daté de ce qui a été fait et trouvé | fin de chaque session |
| `docs/annexes/A1-registre-preuves.md` | Toute donnée externe avec sa source | dès qu'une source est utilisée |

**Au démarrage d'une session** : lire `GOAL.md`, puis `memory/decisions.md`, puis
`memory/questions-ouvertes.md`. Ne pas relire tout `docs/` sauf besoin.

**En fin de session** : mettre à jour `memory/journal.md` et, si une décision a changé,
`memory/decisions.md`. Ne jamais réécrire l'historique d'une décision : on ajoute une
décision qui remplace la précédente, en la citant.

## 6. Sécurité

- **Aucune clé API, aucun secret, aucun identifiant ne doit être écrit dans ce dépôt**,
  même fourni par l'utilisateur en session. Utiliser des variables d'environnement.
- Les données de lots réels (résultats d'analyse) peuvent être confidentielles : vérifier
  avant tout partage externe ou publication d'artefact.

## 7. Ce qu'il ne faut pas refaire

- Ne pas relancer une recherche OSINT large : elle est faite, consolidée dans
  `docs/02-produits-commercialises.md` et `docs/03-brevets.md`. Compléter, pas recommencer.
- Ne pas recalculer les grandeurs de référence : `scripts/calculs_cles.py` les régénère.
