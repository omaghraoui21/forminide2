# GOAL — Bulk DPI combiné Budésonide / Formotérol

*Version 1.0 — rédigée par l'équipe virtuelle (voir `AGENTS.md`), à valider par le chef de projet.*

## 1. Énoncé de l'objectif (north star)

> Obtenir **un seul bulk** DPI, homogène, reproductible et aérosolisable, permettant de remplir
> à **25,0 mg/capsule taille 3** les deux dosages **Formotérol 12 µg / Budésonide 200 µg** et
> **Formotérol 12 µg / Budésonide 400 µg**, avec **les APIs micronisés achetés**, **les lactoses
> ML001 / SV003 / SV010**, **l'Inversina ≈ 20 L**, **le Russell 250 µm**, **le Modu-C MS** et
> **le dispositif de type Aerolizer déjà disponible** — sans jet milling, sans co-micronisation,
> sans spray drying, sans mélangeur à haut cisaillement.

Ce n'est pas un objectif de recherche : la faisabilité est **démontrée par le marché**
(FORPACK 12/200 et 12/400 capsule, Turquie ; ALENIA 12/400 capsule, Brésil — voir
`docs/02-produits-commercialises.md`). L'objectif est de retrouver **l'architecture de
prémélange** qui rend le procédé maison compatible avec deux APIs.

## 2. Ce qui définit la réussite de la phase (critères de sortie)

La phase est terminée quand les huit livrables suivants existent **et sont documentés** :

| # | Livrable | Critère quantitatif d'acceptation |
|---|---|---|
| G1 | Architecture de prémélange arrêtée | 1 architecture retenue, justifiée contre ≥ 2 alternatives testées |
| G2 | Système carrier arrêté | grade(s) + % fines figés, avec justification des données |
| G3 | Ordre d'incorporation figé | décrit étape par étape, reproductible par un opérateur |
| G4 | Décision tamisage | par étape (lactose / prémix FOR / prémix BUD / intermédiaire / bulk) |
| G5 | Temps & énergie de mélange rationnels | issus d'une cinétique mesurée, pas d'une habitude |
| G6 | Taille de lot R&D justifiée | représentativité démontrée (taux de remplissage, pas seulement la masse) |
| G7 | Bulk homogène | **RSD ≤ 5 %** sur 10 points à l'échelle de la dose unitaire (25 mg), **pour les DEUX APIs**, teneur 95–105 % |
| G8 | Performance aérodynamique prometteuse | **FPF ≥ 30 %** et **fraction délivrée ≥ 70 %** pour les deux APIs à l'échelle bulk→capsule (cible de référence marché : FPF 45–56 %, DD 73–85 % — voir §4) |

## 3. Ce qui n'est PAS l'objectif de cette phase

- Optimiser le blister, le conditionnement secondaire, le device final.
- Atteindre la bioéquivalence. On vise « crédible et prometteur », pas « équivalent ».
- Trouver l'optimum. On cherche **l'architecture**, l'optimisation vient après.
- Explorer 20 formulations. Le budget est de 4 à 6 essais en phase 1.

## 4. Références de performance visées (benchmark public, produit équivalent)

`FAIT CONFIRMÉ` — Andrade-Lima, Pereira & Fernandes, *J Bras Pneumol* 2012;38(6), équivalence
pharmaceutique d'une association fixe BUD/FOR **en capsule unique** (Aerocaps®) vs deux capsules
séparées (Aerolizer®) :

| Paramètre | Capsule unique (test) | Deux capsules (référence) |
|---|---|---|
| Teneur BUD / FOR | 111,0 % / 103,8 % | 110,5 % / 104,5 % |
| Dose délivrée BUD / FOR | 293,2 µg / 10,2 µg | 353,0 µg / 11,1 µg |
| FPF < 5 µm BUD / FOR | 45 % / 56 % | 54 % / 52 % |

**Lecture directrice** : dans un produit commercial en capsule unique, le **formotérol n'est pas
pénalisé par la présence du budésonide** (FPF FOR 56 % > FPF BUD 45 %). L'échec historique maison
n'est donc **pas** une fatalité physico-chimique du couple BUD/FOR.

## 5. Critères d'arrêt (kill criteria) — à quel moment on renonce

| Situation | Décision |
|---|---|
| Le prémix FOR seul (essai L0) ne descend pas sous RSD 5 % à 25 mg | **STOP formulation** — le problème est amont : qualité/PSD/état d'agglomération de l'API. Réunion fournisseur avant tout autre lot. |
| Toutes les architectures testées donnent RSD FOR > 8 % à 3 kg | **STOP architecture** — passer en branche « fines / excipient » (ML001 puis achat fines), pas en branche « nouveaux lots d'architecture ». |
| Bulk homogène à 3 kg mais jamais à 9 kg, après correction du taux de remplissage | **Réduire la taille de lot industrielle à 6 kg** plutôt que de dégrader la formule. |
| FPD FOR < 10 % de la dose alors que la CU est bonne | Problème carrier/fines ou interface device — **pas** un problème de mélange. |

## 6. Horizon

| Phase | Contenu | Essais |
|---|---|---|
| 0 | Données manquantes + méthode analytique + prémix FOR seul | 1 prémix |
| 1 | Screening d'architecture à 3 kg | 3–4 lots |
| 2 | Optimisation (fines, temps de mélange) | 2–4 lots |
| 3 | Confirmation indépendante | 1 lot |
| 4 | Scale-up 6 puis 9 kg | 2 lots |

Voir `docs/07-sequence-minimale.md` pour le chemin critique le plus court.
