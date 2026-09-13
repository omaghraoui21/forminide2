# La séquence expérimentale la plus courte vers une décision industrielle

**Question posée** : quelle est la séquence expérimentale la plus courte permettant de
déterminer **avec une forte confiance** si une capsule Budésonide/Formotérol **12/200 et 12/400**
peut être développée industriellement avec : APIs micronisés achetés, ML001 / SV003 / SV010,
Inversina ≈ 20 L, Russell 250 µm, Modu-C MS et le dispositif de type Aerolizer disponible ?

**Réponse courte** :

> **4 essais de mélange** suffisent à trancher la question technique, **6** pour couvrir les deux
> dosages et le scale-up industriel. Soit **≈ 8 à 10 semaines**, **≈ 30 g de formotérol** et
> **≈ 400 g de budésonide** au total.

La raison pour laquelle c'est si court : **la faisabilité du produit n'est pas la question.**
Elle est déjà démontrée par le marché (FORPACK 12/200 et 12/400 capsule 25,000 mg, lactose seul,
Turquie, autorisé depuis 2013) et par la littérature (équivalence pharmaceutique publiée d'une
capsule unique BUD/FOR, avec FPF FOR 56 %). La seule question ouverte est **l'architecture de
prémélange sur NOTRE procédé** — et une architecture se teste en trois lots, pas en trente.

---

## Phase 0 — Deux semaines, zéro lot

Ces trois actions conditionnent tout le reste et ne consomment pas de matière.

| Action | Pourquoi c'est bloquant | Propriétaire |
|---|---|---|
| **Récupérer les données du lot combiné 9 kg historique** (quel API a échoué ? assay ou RSD ? avant ou après tamisage ? combien de lots ?) | c'est l'information la moins chère et la plus discriminante du projet — elle peut à elle seule supprimer un lot | R&D / archives |
| **Obtenir le titre exact du formotérol** (fumarate dihydraté vs base) | sans lui, aucune pesée n'est valide | AQ / fournisseur |
| **Valider la méthode HPLC simultanée BUD + FOR sur une prise d'essai de 25 mg** et se procurer une sonde voleuse adaptée | si l'on ne sait pas mesurer à l'échelle de la dose, on ne saura pas si l'on a réussi. C'est le risque n°1 d'auto-illusion du projet | Labo |

> ⚠️ Si l'homogénéité historique a été jugée sur des prises de ~1 g, **tous les résultats
> historiques sont à relire** — un RSD à 1 g peut être excellent alors que l'uniformité de dose
> à 25 mg est mauvaise.

---

## Le chemin critique — 4 essais

Tous au dosage **12/400**, qui est le **pire cas pour le formotérol** (rapport de masse BUD:FOR =
33:1 au lieu de 16,7:1), sur **SV003**, avec la même matière première et le même opérateur.

### E1 — Prémix formotérol seul  *(144 g — une demi-journée)*

| | |
|---|---|
| **Question** | Sait-on rendre le formotérol homogène **tout seul**, à l'échelle de la dose ? |
| **Contenu** | FOR 1,44 g + SV003 142,6 g (prémix à 1,0 % m/m) ; sandwich → mélange 3 min → tamisage → Inversina 15 min |
| **Mesures** | assay FOR, RSD sur **10 × 25 mg**, bilan matière au tamisage, rinçage matériel |
| **GO** | RSD ≤ 5 %, teneur 95–105 %, bilan matière ≥ 99 % |
| **NO-GO** | RSD > 8 % → **arrêt immédiat du plan** : le problème est la qualité/l'état d'agglomération de l'API, pas l'architecture. Aucun lot combiné ne le corrigera. |
| **Ce que ça élimine** | l'hypothèse « API inadapté » et l'hypothèse « pertes au tamisage », en une demi-journée |

Ce n'est pas un mini-lot non représentatif : c'est **l'étape réelle du procédé**, à son échelle
réelle. C'est ce qui permet de la faire si tôt et si petit.

### E2 — Benchmark historique  *(3 kg — 1 jour)*

| | |
|---|---|
| **Question** | Le problème historique **se reproduit-il à 3 kg** ? |
| **Contenu** | Architecture A : co-sandwich BUD + FOR ensemble, répartition 3:3:3, SV003, procédé historique intégral |
| **Mesures** | Gate 1 (assay + RSD des 2 APIs sur 10 × 25 mg), Gate 2 (densités, Carr, ségrégation) |
| **Lecture** | **Si E2 échoue** → le problème est **chimique/architectural**, il est reproductible à petite échelle, et E3 doit le corriger.<br>**Si E2 réussit** → le problème historique était **mécanique / lié à l'échelle**. On saute alors directement à E4 (9 kg) : **on économise un lot.** |

C'est le lot que l'on est tenté de sauter. Il ne faut pas : **sans lui, on ne pourra jamais
prouver que l'on a résolu quelque chose**, et il porte à lui seul la bifurcation du plan.

### E3 — Architecture recommandée  *(3 kg — 1 jour)*

| | |
|---|---|
| **Question** | La modification minimale (prémix FOR + répartition 7:2:1) résout-elle le problème ? |
| **Contenu** | Architecture B : prémix FOR de E1 → 1re fraction 70 % → BUD déposé **en couche séparée** → 2e fraction 20 % → 3e fraction 10 %. Tamisage et 15 min Inversina à chaque étape. |
| **Mesures** | Gate 1 + Gate 2 ; **cinétique de mélange embarquée** (prélèvements à 5/10/15/25 min à l'étape 3) ; **assay avant/après le tamisage final** (tranche le débat « tamisage destructeur ») ; puis **Gate 3** (remplissage Modu-C 25 mg) et **Gate 4** (NGI) |
| **GO** | RSD ≤ 5 % pour les deux APIs ; FPF ≥ 30 % pour les deux APIs ; dose délivrée ≥ 70 % |
| **Ce que ça élimine** | quatre hypothèses d'un coup : co-agglomération API–API, répartition des fractions, sur-mélange, tamisage destructeur |

E3 est **le lot le plus rentable du plan** : une seule fabrication, quatre hypothèses tranchées.

### E4 — Passage à l'échelle industrielle  *(6 kg puis 9 kg — 2 jours)*

| | |
|---|---|
| **Question** | L'architecture survit-elle au **taux de remplissage** industriel ? |
| **Contenu** | Architecture gagnante à **6 kg** (48 % de remplissage), puis à **9 kg** (71 %) |
| **Mesures** | Gate 1 sur **15 points**, Gate 2, Gate 3, Gate 4 |
| **Lecture** | 6 kg OK + 9 kg OK → **GO industriel**.<br>6 kg OK + 9 kg marginal → **figer la taille de lot à 6 kg** (décision économique, pas formulatoire).<br>6 kg KO → retour à E3 avec correction du carrier (fines ML001). |

---

## Les deux essais complémentaires (pour être complet, pas pour décider)

| Essai | Objet | Quand |
|---|---|---|
| **E5** | Même architecture au dosage **12/200** (3 ou 6 kg) | après E3 GO — la seule variable qui change est la charge de budésonide (0,8 % au lieu de 1,6 %) ; c'est le pire cas pour l'**uniformité du budésonide** |
| **E6** | Lot de **confirmation indépendant** (autre lot de lactose, autre opérateur, autre jour) | avant de déclarer la phase terminée — c'est ce lot qui distingue « ça a marché » de « c'est reproductible » |

---

## Vue d'ensemble

```
Phase 0 (2 sem., 0 lot)  ── données historiques + titre FOR + méthode 25 mg
        │
        ▼
   E1  prémix FOR seul ─── RSD > 8 % ──► STOP : problème API (réunion fournisseur)
        │ GO
        ▼
   E2  benchmark A 3 kg ── RÉUSSIT ──► le problème était mécanique ──┐
        │ ÉCHOUE (attendu)                                          │
        ▼                                                           │
   E3  architecture B 3 kg ─ ÉCHOUE ─► branche carrier/fines (L4)   │
        │ GO (Gates 1→4)                                            │
        ▼                                                           │
   E4  6 kg ──► 9 kg ◄────────────────────────────────────────────┘
        │
        ├─ 9 kg GO ─────────► GO INDUSTRIEL
        └─ 9 kg marginal ──► GO INDUSTRIEL à 6 kg
        │
        ▼
   E5 (12/200)  +  E6 (confirmation)  ──►  fin de phase, passage capsule/device
```

---

## Pourquoi cette séquence, et pas une autre

| Principe | Application |
|---|---|
| **Tester d'abord ce qui peut tout arrêter** | E1 (prémix FOR) coûte 1,4 g de formotérol et peut invalider le projet entier |
| **Conserver un témoin** | E2 est le seul moyen de démontrer un progrès ; il porte aussi la bifurcation « chimique vs mécanique » |
| **Une expérience, plusieurs hypothèses** | E3 tranche 4 hypothèses, dont la cinétique de mélange et le tamisage, sans lot supplémentaire |
| **Séparer formulation et mécanique** | E1–E3 à 3 kg (formulation) ; E4 à 6 et 9 kg (mécanique du mélangeur). Ne jamais les confondre dans un même essai |
| **Pire cas d'abord** | 12/400 pour le formotérol (ratio 33:1), 12/200 ensuite pour le budésonide (0,8 %) |
| **Ne pas gaspiller le NGI** | NGI seulement après un Gate 1 et un Gate 2 réussis |
| **Ne pas descendre arbitrairement en échelle** | seule exception : le prémix, qui **est** à sa taille réelle |

## Ce que cette séquence ne couvre PAS (et qui viendra après)

Stabilité 24 mois (le formotérol est sensible à l'humidité) · validation du procédé ·
robustesse inter-lots de lactose · optimisation de la FPF vers la cible marché de 45–56 % ·
blister, device final, dossier réglementaire.
