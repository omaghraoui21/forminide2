# Marche à suivre — étape par étape

> Ce document dit **quoi faire, dans quel ordre, et à quelle condition passer à la suite**.
> Le détail opératoire est dans `09-dossiers-de-lot.md`, le raisonnement dans `RAPPORT.md`.
> Saisie des résultats : plateforme `platform/cahier-essais.html`.

---

## Les 5 règles non négociables

Elles conditionnent la validité de tout ce qui suit. Une seule oubliée, et les résultats ne
veulent rien dire.

1. **Prises d'essai de 25 mg** (1 dose), jamais de l'ordre du gramme. Une prise d'1 g masque
   mathématiquement l'hétérogénéité que l'on cherche à mesurer.
2. **Doser BUD et FOR sur la MÊME prise d'essai.** C'est le seul moyen de calculer la corrélation
   entre les deux — le test le plus direct de l'hypothèse de co-agglomération.
3. **Pesée entrée / sortie à chaque tamisage** (±0,5 %). C'est le test le moins cher des pertes
   de formotérol.
4. **Ne jamais terminer un lot par un tamisage.** Toujours une ré-homogénéisation après.
5. **Relever HR et température à chaque étape**, et noter toute observation qualitative
   (collage, motte, poudre qui « saute »). Ces notes diagnostiquent souvent mieux que les chiffres.

---

## SEMAINE 0 — avant de toucher à une poudre

Aucune matière consommée. **Deux de ces actions bloquent le premier lot.**

| # | Action | Qui | Bloquant ? |
|---|---|---|---|
| 0.1 | **Titre exact du formotérol** : fumarate dihydraté ou base ? Facteur de correction ? | AQ / fournisseur | **OUI — bloque L0** |
| 0.2 | **Méthode HPLC simultanée BUD + FOR validée sur une prise de 25 mg**, et statut des épimères 22R/22S du budésonide tranché | Labo | **OUI — bloque L0** |
| 0.3 | **Sortir les archives du lot combiné 9 kg historique** : quel API a échoué, assay ou RSD, avant ou après tamisage, combien de lots, quelles valeurs | R&D | non, mais **c'est l'action au meilleur rapport information/coût du projet** |
| 0.4 | **Retrouver la masse de prise d'essai utilisée historiquement.** Si c'était ~1 g, les « succès » mono-produits sont à relire | Labo / archives | non |
| 0.5 | **Sonde voleuse** adaptée à des prises de 25–75 mg · tamis manuels **150 et 212 µm** · barre antistatique au poste de pesée · thermohygromètre enregistreur | Achats | **OUI en pratique** — sans la sonde, la porte 1 n'est pas mesurable |
| 0.6 | **Fiche technique Inversina** : vitesse réelle en rpm, cuves interchangeables disponibles, taux de remplissage recommandé | Production | non |
| 0.7 | **Identifier la version du dispositif RS01** (4 kPa à ≈ 100 L/min ou à 65 L/min) et mesurer sa résistance | R&D / device | non, mais **avant la porte 4** |
| 0.8 | **Relever les paramètres actuels du Modu-C MS** pour 25 mg : diamètre de dosator, chambre de dosage, hauteur de lit, pré-compression, vitesse | Production | non, mais **avant la porte 3** |
| 0.9 | Demander des **échantillons gratuits de Lactohale LH230** (délai fournisseur, à anticiper) | Achats | non |

> Ne pas attendre 0.3 à 0.9 pour lancer L0 : seuls 0.1, 0.2 et 0.5 sont bloquants.

---

## JOUR 1 — L0, prémix formotérol seul

**Une demi-journée · 1,44 g de formotérol · 144 g au total.**
C'est l'expérience qui élimine le plus d'hypothèses par gramme d'API consommé.

1. Relever HR et T° de salle.
2. Peser **71,3 g de SV003**, les déposer dans la cuve de prémix.
3. Peser le formotérol **par différence**, dans un contenant verre ou inox **mis à la terre** —
   1,44 g corrigé du titre. Ioniseur en marche.
4. Déposer le FOR **au centre**, sans contact avec les parois.
5. Recouvrir des **71,3 g** restants — **sandwich**.
6. Mélange doux **3 min**.
7. **Peser** l'ensemble (bilan matière).
8. **Scinder en deux aliquotes** : A tamisée au **Russell 250 µm**, B tamisée au **tamis manuel
   212 µm**.
9. **Repeser** chaque aliquote.
10. Inversina **15 min** sur chaque aliquote.
11. **Prélever 10 positions × 25 mg** par aliquote (haut/milieu/bas × paroi/centre + 2 au fond de
    cuve), analyser **en triple**.
12. Passer un **témoin de mélange parfait** (25 mg reconstitués par pesée directe) comme un
    échantillon. S'il ne rend pas 100 ± 2 %, le problème est analytique, pas formulatoire.
13. **Rincer et doser** cuve, tamis et spatule (adsorption du formotérol).

**Décision**

| Résultat | Suite |
|---|---|
| **RSD ≤ 5 %**, teneur 95–105 %, bilan matière ≥ 99 % | ✅ **GO** — lancer L1 et L2 |
| 5 % < RSD ≤ 8 % | ⚠️ refaire avec la maille la plus fine et une dilution sérielle avant de décider |
| **RSD > 8 %** | ⛔ **ARRÊT DU PLAN.** Le problème est amont (PSD, état d'agglomération de l'API). Réunion fournisseur **avant** tout lot combiné — aucun lot combiné ne le corrigera |

**Lecture complémentaire** : si l'aliquote B (212 µm) est nettement meilleure que A (250 µm), la
taille des agglomérats est bien le facteur limitant → appliquer la maille fine à tous les prémix.

---

## JOURS 2–3 — L1 et L2, le même jour

**Même opérateur, même lot de lactose, même journée.** 3 kg chacun, dosage **12/400**
(pire cas pour le formotérol : rapport de masse 33:1).

### L1 — benchmark historique *(le lot qu'on est tenté de sauter)*

Procédé historique intégral, **sans aucune modification** : BUD 48,00 g et FOR 1,44 g déposés
**ensemble** dans le sandwich, répartition **3 : 3 : 3** (983,5 g par fraction), tamisage 250 µm et
Inversina 15 min à chaque étape.

> Sans ce témoin, **aucun progrès ne sera démontrable**. Et c'est lui qui porte la bifurcation du
> plan : si L1 réussit, le problème historique était mécanique, pas architectural.

### L2 — architecture recommandée

Répartition **7 : 2 : 1** → fractions de **2 065,4 / 590,1 / 295,1 g**.

**Étape 1 — première fraction (70 %)**
1. Déposer ≈ **960 g** de SV003.
2. Étaler **la totalité du prémix FOR (144,0 g)**.
3. Recouvrir de ≈ **330 g** de SV003 — **COUCHE BARRIÈRE**.
   *Le budésonide ne doit jamais toucher le prémix formotérol. C'est le geste central du lot.*
4. Étaler **BUD 48,00 g**.
5. Recouvrir du reste, ≈ **631 g**.
6. Mélange **5 min** → pesée → **Russell 250 µm** → pesée → **Inversina 15 min**.

**Étape 2 — deuxième fraction (590,1 g)**
7. Ajouter → mélange **3 min** → pesée → tamis → pesée → **Inversina 15 min**.

**Étape 3 — troisième fraction (295,1 g) — étape instrumentée**
8. Ajouter → mélange **3 min**.
9. **Prélever 10 positions AVANT le tamisage.**
10. Pesée → **Russell 250 µm** → pesée.
11. **Prélever 10 positions APRÈS le tamisage.**
12. Inversina, avec **prélèvements à 5, 10, 15 et 25 min**.

> Ces prélèvements embarqués tranchent quatre hypothèses sans lot supplémentaire :
> co-agglomération, répartition des fractions, sous- ou sur-mélange, tamisage destructeur.

---

## JOURS 4–5 — analyses et lecture

1. **Porte 1** — assay BUD et FOR sur chaque prise, RSD par API, cartographie spatiale.
2. **Calculer la corrélation BUD ↔ FOR** prise par prise.
   - `r ≥ 0,6` → **signature de la co-agglomération**, hypothèse principale confirmée.
   - `r ≈ 0` → ségrégation ou défaut de mélange, pas de co-agglomération.
3. **Saisir les relevés dans la plateforme** — RSD, corrélation, diamètre effectif et verdicts se
   calculent seuls, avec le repère marché en regard.
4. **Porte 2** — densités versée et tassée (et **recalculer le taux de remplissage réel**),
   Carr, Hausner, écoulement, test de ségrégation.
5. **Porte 3** — seulement si 1 et 2 sont franchies : remplissage Modu-C à 25 mg, gélule taille 3,
   RSD de masse, dose délivrée sur le dispositif.
6. **Porte 4** — seulement si 1 à 3 sont franchies : **NGI sur L2 uniquement**, aux temps de
   mélange 15 et 25 min. FPD et FPF **par API**.

> Le NGI est la ressource rare : jamais sur un mélange dont l'uniformité n'est pas connue.

**Comparaison des deux lots** — c'est elle qui décide :

| L1 (benchmark) | L2 (architecture B) | Conclusion |
|---|---|---|
| échoue | réussit | ✅ **L'architecture est la cause et la solution.** Passer au scale-up |
| échoue | échoue | la cause est ailleurs → branche **L3** (ordre inversé) ou **L4** (fines) |
| réussit | réussit | le problème historique était **mécanique** → sauter directement au **9 kg** |

---

## SEMAINE 3 — selon le résultat, une seule branche

| Situation | Lot | Ce qu'on change |
|---|---|---|
| RSD FOR > 5 % en L2, ou FPD FOR faible | **L3** | architecture C : BUD/carrier d'abord, prémix FOR **en dernier** |
| Uniformité correcte mais **FPD faible** | **L4** | carrier pré-conditionné : SV003 + **8 % ML001**, mélangés et tamisés **avant** les APIs |
| Porte 3 en échec **après** réglage machine | **L5** | SV010, ou SV003/SV010 50:50 |
| Tout est conforme | **L6** | scale-up |

> Au Gate 3 : si la **masse moyenne** de 25 mg est inatteignable, c'est un sujet **carrier**.
> Si la masse est bonne mais le **RSD** élevé, ce sont les **réglages machine** — chambre de
> dosage, hauteur de lit, pré-compression, vitesse. Ne pas changer le carrier avant de les avoir
> épuisés.

---

## SEMAINE 4 — L6, le scale-up

1. **6 kg d'abord** — 48 % de remplissage, exactement la plage recommandée par le constructeur.
   Portes 1 à 4 complètes. *Variable testée : la profondeur de lit.*
2. **9 kg ensuite** — 71 % de remplissage. **C'est un essai de robustesse mécanique, pas de
   formulation.** Échantillonnage porté à **15 positions**.

| Résultat | Décision |
|---|---|
| 6 kg ✅ et 9 kg ✅ | **GO industriel à 9 kg** |
| 6 kg ✅ et 9 kg marginal | augmenter les révolutions de **la seule étape 3** ; si insuffisant, **figer la taille industrielle à 6 kg**. Décision économique, pas formulatoire |
| 6 kg ❌ | retour formulation (L4, fines) — **pas** au scale-up |

---

## SEMAINES 5–6 — clôture de la phase

1. **L7** — même architecture au dosage **12/200** (BUD 0,800 % au lieu de 1,600 %).
   C'est le pire cas pour l'uniformité du **budésonide**.
2. **Lot de confirmation indépendant** — autre lot de lactose, autre opérateur, autre jour.
   C'est ce lot qui distingue « ça a marché » de « c'est reproductible ».

**La phase est terminée quand les huit critères de `GOAL.md` sont satisfaits** : architecture de
prémix, système carrier, ordre d'incorporation, décision de tamisage, temps de mélange rationnel,
taille de lot, bulk homogène, performances aérodynamiques prometteuses.

---

## Récapitulatif de la consommation

| Essai | Lactose | Budésonide | Formotérol | Durée |
|---|---|---|---|---|
| L0 | 143 g | — | 1,44 g | ½ journée |
| L1 | 2,95 kg | 48 g | 1,44 g | 1 jour |
| L2 | 2,95 kg | 48 g | 1,44 g | 1 jour |
| L6 (6 + 9 kg) | 14,75 kg | 240 g | 7,20 g | 2 jours |
| L7 (12/200) | 5,95 kg | 48 g | 2,88 g | 1 jour |
| Confirmation | 2,95 kg | 48 g | 1,44 g | 1 jour |
| **Total** | **≈ 29,7 kg** | **≈ 432 g** | **≈ 15,8 g** | **≈ 7 jours de fabrication** |

Soit **6 à 8 semaines** en comptant les analyses, pour une décision industrielle documentée.
