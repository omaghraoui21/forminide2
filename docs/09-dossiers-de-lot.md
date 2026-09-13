# Dossiers de lot exécutables — L0, L1, L2

> Documents de travail R&D, **non GMP**. À transposer dans le format documentaire du site avant
> exécution. Les cases `☐` sont à cocher par l'opérateur ; les champs `______` à renseigner.
> Toutes les masses sont issues de `scripts/calculs_cles.py` (`calcul interne`).

## Préalables communs à tous les lots

| Vérification avant de commencer | Réf. | Fait |
|---|---|---|
| **Titre exact du formotérol** obtenu (fumarate dihydraté ou base) et facteur de correction appliqué | Q2 | ☐ |
| Méthode HPLC simultanée BUD + FOR validée **sur prise d'essai de 25 mg** | Q11 | ☐ |
| Statut des épimères 22R/22S du budésonide tranché dans la méthode | Q11 | ☐ |
| **Sonde voleuse** adaptée à des prises de 25–75 mg disponible | achat n°1 | ☐ |
| Enregistreur **HR / température** en place dans la salle | Q6 | ☐ |
| Barre/soufflette **antistatique** au poste de pesée | achat n°3 | ☐ |
| Vitesse de l'Inversina relevée et notée (rpm) | Q5 | ☐ |
| Balance qualifiée pour peser **1,44 g** avec une incertitude ≤ 0,5 % | — | ☐ |

**Correction de titre** : masse à peser = masse théorique × (100 / titre %). À recalculer pour
chaque lot d'API et à consigner.

**Règle d'or de l'échantillonnage** : prises de **25 mg (1 dose)** ou 75 mg (3 doses).
**Jamais de prise de l'ordre du gramme** — voir `annexes/A3-plan-analytique.md`.

---

# L0 — Qualification du prémix formotérol

**Hypothèse** : un prémix FOR à 1,0 % m/m, sandwiché puis tamisé, atteint **RSD ≤ 5 %** à
l'échelle de 25 mg.
**Ce que L0 élimine** : qualité/état d'agglomération de l'API, pertes au tamisage, électrostatique.
**Décision qu'il conditionne** : si L0 échoue, **aucun lot combiné n'est lancé**.

## Formule (échelle prémix d'un lot 3 kg)

| Composant | Masse théorique | Masse corrigée du titre | Masse pesée | % m/m |
|---|---|---|---|---|
| Formotérol fumarate dihydraté micronisé | **1,44 g** | ______ | ______ | 1,00 |
| Respitose® SV003 | **142,56 g** | — | ______ | 99,00 |
| **Total** | **144,00 g** | | ______ | 100,00 |

*(Pour un lot de 9 kg : FOR 4,32 g + SV003 427,68 g = 432,00 g.)*

## Procédé

| # | Opération | Paramètre | Relevé | Fait |
|---|---|---|---|---|
| 1 | Relever HR et T° de salle | — | HR ____ % · T ____ °C | ☐ |
| 2 | Peser **71,3 g** de SV003 (moitié) et les déposer dans la cuve | — | ____ g | ☐ |
| 3 | Peser le FOR **par différence**, contenant verre/inox **mis à la terre** | 1,44 g corrigé | ____ g | ☐ |
| 4 | Déposer le FOR **au centre**, sans contact avec les parois | — | — | ☐ |
| 5 | Recouvrir avec les **71,3 g** restants de SV003 — **sandwich** | — | ____ g | ☐ |
| 6 | Mélange doux | **3 min** | ____ min | ☐ |
| 7 | **Pesée avant tamisage** (bilan matière) | — | ____ g | ☐ |
| 8 | **Tamisage** — scinder en 2 aliquotes : **A = 250 µm (Russell)**, **B = 212 µm (tamis manuel)** | — | A ____ g · B ____ g | ☐ |
| 9 | **Pesée après tamisage** de chaque aliquote | perte ≤ 1 % | A ____ g · B ____ g | ☐ |
| 10 | Inversina, chaque aliquote | **15 min**, ____ rpm | ____ min | ☐ |
| 11 | Rinçage analytique du matériel (cuve, tamis, spatule) | — | ☐ | ☐ |

**Variante embarquée (facultative, recommandée)** : répéter les étapes 2 à 6 **sans** ioniseur
puis **avec** ioniseur, et comparer bilan matière et RSD. Coût : une demi-journée, tranche la
cause 4.2.

## Plan de prélèvement — 10 positions × 25 mg

| Position | Description | Masse prélevée (mg) | Assay FOR (%) |
|---|---|---|---|
| P1 | Haut — paroi | ____ | ____ |
| P2 | Haut — centre | ____ | ____ |
| P3 | Milieu — paroi (0°) | ____ | ____ |
| P4 | Milieu — paroi (120°) | ____ | ____ |
| P5 | Milieu — paroi (240°) | ____ | ____ |
| P6 | Milieu — centre | ____ | ____ |
| P7 | Bas — paroi | ____ | ____ |
| P8 | Bas — centre | ____ | ____ |
| P9 | **Fond de cuve** | ____ | ____ |
| P10 | **Fond de cuve** (opposé) | ____ | ____ |

Chaque prise analysée **en triple**. Ajouter un **témoin de mélange parfait** (25 mg reconstitués
par pesée directe) passé comme un échantillon : s'il ne rend pas 100 ± 2 %, le problème est
analytique, pas formulatoire.

## Résultats et décision

| Réponse | Aliquote A (250 µm) | Aliquote B (212 µm) | Critère |
|---|---|---|---|
| Teneur moyenne FOR | ____ % | ____ % | **95 – 105 %** |
| **RSD FOR** | ____ % | ____ % | **≤ 5 %** |
| Valeur min / max | ____ / ____ | ____ / ____ | aucune hors 90–110 % |
| Bilan matière | ____ % | ____ % | **≥ 99 %** |
| FOR récupéré au rinçage | ____ mg | ____ mg | à documenter |
| Densité versée / tassée | ____ / ____ g/L | ____ / ____ | à documenter |

**Décision** : ☐ **GO** (RSD ≤ 5 %) → lancer L1 et L2 · ☐ **NO-GO** (RSD > 8 %) → **arrêt du
plan**, réunion fournisseur API (PSD, état d'agglomération) · ☐ **zone grise** (5 < RSD ≤ 8 %) →
refaire L0 avec la maille la plus fine et une dilution sérielle avant de décider.

**Lecture complémentaire** : si B (212 µm) est nettement meilleure que A (250 µm), la taille des
agglomérats est bien le facteur limitant → appliquer la maille fine au prémix de tous les lots.

---

# L1 — Benchmark historique (architecture A, co-sandwich)

**Hypothèse** : le problème historique se reproduit à 3 kg.
**Pourquoi ce lot est indispensable** : sans témoin, aucun progrès n'est démontrable. Il porte
aussi la bifurcation du plan (cause chimique vs mécanique).

## Formule — 3 kg, dosage 12/400

| Composant | Masse théorique | Masse pesée | % m/m |
|---|---|---|---|
| Budésonide micronisé | **48,00 g** | ______ | 1,600 |
| Formotérol fumarate dihydraté micronisé | **1,44 g** (corrigé : ______) | ______ | 0,048 |
| Respitose® SV003 | **2 950,56 g** | ______ | 98,352 |
| **Total** | **3 000,00 g** | ______ | 100,000 |

**Répartition du lactose : 3 : 3 : 3** → **983,52 g** par fraction.

## Procédé (procédé historique intégral, sans modification)

| # | Opération | Paramètre | Relevé | Fait |
|---|---|---|---|---|
| 1 | HR / T° de salle | — | HR ____ % · T ____ °C | ☐ |
| 2 | Déposer ≈ **490 g** de SV003 (moitié de la 1re fraction) | — | ____ g | ☐ |
| 3 | Étaler **BUD 48,00 g ET FOR 1,44 g ENSEMBLE** | co-sandwich | ____ / ____ g | ☐ |
| 4 | Recouvrir avec ≈ **493 g** de SV003 | — | ____ g | ☐ |
| 5 | Mélange initial | **5 min** | ____ min | ☐ |
| 6 | Pesée / **Russell 250 µm** / pesée | perte ≤ 1 % | ____ → ____ g | ☐ |
| 7 | Inversina | **15 min**, ____ rpm | ____ min | ☐ |
| 8 | Ajouter la **2e fraction 983,52 g** | — | ____ g | ☐ |
| 9 | Mélange | **3 min** | ____ min | ☐ |
| 10 | Pesée / **Russell 250 µm** / pesée | perte ≤ 1 % | ____ → ____ g | ☐ |
| 11 | Inversina | **15 min** | ____ min | ☐ |
| 12 | Ajouter la **3e fraction 983,52 g** | — | ____ g | ☐ |
| 13 | Mélange | **3 min** | ____ min | ☐ |
| 14 | Pesée / **Russell 250 µm** / pesée | perte ≤ 1 % | ____ → ____ g | ☐ |
| 15 | Inversina | **15 min** | ____ min | ☐ |

**Taux de remplissage attendu** `calcul interne` : 3 kg / 630 g/L = **4,8 L, soit 24 % de 20 L**.
Mesurer la **densité versée du bulk réel** et recalculer.

## Prélèvements et analyses

Même plan à 10 positions que L0, mais **assay BUD ET FOR sur la MÊME prise d'essai**.

| Position | Masse (mg) | Assay BUD (%) | Assay FOR (%) |
|---|---|---|---|
| P1 … P10 | ____ | ____ | ____ |

**Analyse obligatoire** : calculer le **coefficient de corrélation entre teneur BUD et teneur FOR**
prise par prise.
- Corrélation **positive marquée** (r > 0,6) → **signature de la co-agglomération BUD–FOR**,
  hypothèse principale confirmée.
- Corrélation nulle → défaut de mélange ou ségrégation, pas de co-agglomération.

**Gate 2** : densité versée / tassée, Carr, Hausner, écoulement, test de ségrégation.

## Décision

| Résultat | Interprétation | Suite |
|---|---|---|
| **RSD FOR > 5 %** (échec attendu) | le problème est **architectural** et reproductible à 3 kg | poursuivre L2, le témoin est acquis |
| **RSD FOR ≤ 5 %** (succès) | le problème historique était **mécanique / d'échelle** | **sauter L3–L5**, aller directement au 9 kg avec l'architecture B |

---

# L2 — Architecture B recommandée (prémix FOR + 7 : 2 : 1)

**Hypothèse** : séparer les deux APIs et recharger la première fraction résout le problème.
**Ce lot tranche à lui seul 4 hypothèses** : co-agglomération, répartition des fractions,
sous-/sur-mélange, tamisage destructeur.

## Formule — 3 kg, dosage 12/400

| Composant | Masse | % m/m |
|---|---|---|
| Budésonide micronisé | **48,00 g** | 1,600 |
| Formotérol fumarate dihydraté (dans le prémix) | **1,44 g** (corrigé : ____) | 0,048 |
| Respitose® SV003 | **2 950,56 g** | 98,352 |
| **Total** | **3 000,00 g** | 100,000 |

**Répartition du lactose 7 : 2 : 1**

| Fraction | % | Masse | Dont |
|---|---|---|---|
| **F1** | 70 % | **2 065,39 g** | dont **142,56 g** engagés dans le prémix FOR |
| **F2** | 20 % | **590,11 g** | — |
| **F3** | 10 % | **295,06 g** | — |

## Procédé

### Étape 0 — Prémix formotérol (144,00 g)
Reprendre **intégralement le protocole L0** (étapes 2 à 10, maille retenue à l'issue de L0).
☐ Prémix conforme (assay et RSD de L0 disponibles) — **ne pas engager un prémix non qualifié**.

### Étape 1 — Première fraction (70 %)

| # | Opération | Paramètre | Relevé | Fait |
|---|---|---|---|---|
| 1 | HR / T° de salle | — | HR ____ % · T ____ °C | ☐ |
| 2 | Déposer ≈ **960 g** de SV003 | lit de base | ____ g | ☐ |
| 3 | Étaler **la totalité du prémix FOR (144,00 g)** en couche régulière | — | ____ g | ☐ |
| 4 | Recouvrir de ≈ **330 g** de SV003 — **COUCHE BARRIÈRE** | *le BUD ne doit jamais toucher le prémix FOR* | ____ g | ☐ |
| 5 | Étaler **BUD 48,00 g** en couche régulière | — | ____ g | ☐ |
| 6 | Recouvrir avec le reste de F1, ≈ **631 g** | — | ____ g | ☐ |
| 7 | Mélange initial | **5 min** | ____ min | ☐ |
| 8 | Pesée / **Russell 250 µm** / pesée | perte ≤ 1 % | ____ → ____ g | ☐ |
| 9 | Inversina | **15 min**, ____ rpm | ____ min | ☐ |

### Étape 2 — Deuxième fraction (20 %, 590,11 g)
| 10 | Ajouter F2 | — | ____ g | ☐ |
| 11 | Mélange | **3 min** | ____ min | ☐ |
| 12 | Pesée / Russell 250 µm / pesée | perte ≤ 1 % | ____ → ____ g | ☐ |
| 13 | Inversina | **15 min** | ____ min | ☐ |

### Étape 3 — Troisième fraction (10 %, 295,06 g) — **étape instrumentée**
| 14 | Ajouter F3 | — | ____ g | ☐ |
| 15 | Mélange | **3 min** | ____ min | ☐ |
| 16 | **PRÉLÈVEMENT « avant tamisage »** — 10 positions | *test du tamisage destructeur* | ☐ | ☐ |
| 17 | Pesée / Russell 250 µm / pesée | perte ≤ 1 % | ____ → ____ g | ☐ |
| 18 | **PRÉLÈVEMENT « après tamisage, t = 0 »** — 10 positions | | ☐ | ☐ |
| 19 | Inversina — **prélèvements à 5, 10, 15 et 25 min** | *cinétique de mélange* | ☐ | ☐ |

> **Le lot se termine sur un mélange, jamais sur un tamisage.**

## Mesures embarquées — ce que chacune tranche

| Mesure | Prélèvements | Hypothèse tranchée |
|---|---|---|
| **Cinétique** : assay BUD + FOR à 5 / 10 / 15 / 25 min | 4 × 10 | sous-mélange (3.2) vs sur-mélange (3.3) ; désaccord **D4** |
| **NGI à 15 min et à 25 min uniquement** | 2 séries | perte de FPD par press-on |
| **Avant / après tamisage** (étapes 16 et 18) | 2 × 10 | tamisage destructeur (3.5) ; désaccord **D3** |
| **Corrélation BUD–FOR** prise par prise | toutes | co-agglomération (1.1) |
| **Bilan matière** à chaque tamisage | 3 | pertes de FOR (4.1) |

## Tableau de résultats

| Temps de mélange (étape 3) | Teneur BUD (%) | RSD BUD (%) | Teneur FOR (%) | RSD FOR (%) | r (BUD, FOR) |
|---|---|---|---|---|---|
| avant tamisage | ____ | ____ | ____ | ____ | ____ |
| après tamisage, t = 0 | ____ | ____ | ____ | ____ | ____ |
| 5 min | ____ | ____ | ____ | ____ | ____ |
| 10 min | ____ | ____ | ____ | ____ | ____ |
| **15 min (référence)** | ____ | ____ | ____ | ____ | ____ |
| 25 min | ____ | ____ | ____ | ____ | ____ |

| Gate | Réponse | Résultat | Critère | Repère marché |
|---|---|---|---|---|
| 1 | RSD BUD / FOR | ____ / ____ % | ≤ 5 % | 1,62 % / 2,02 % |
| 2 | Carr / Hausner | ____ % / ____ | ≤ 25 % / ≤ 1,34 | — |
| 2 | Densité versée du bulk | ____ g/L | à reporter au calcul de remplissage | — |
| 3 | RSD de masse (Modu-C, 25 mg) | ____ % | ≤ 3 % | 3,09 % |
| 3 | Dose délivrée BUD / FOR | ____ / ____ % | ≥ 70 % | 73 % / 85 % |
| 4 | FPF BUD / FOR | ____ / ____ % | ≥ 30 % | 44,7 % / 56,1 % |
| 4 | FPD BUD / FOR | ____ / ____ µg | — | 140,7 / 6,18 µg |
| 4 | MMAD BUD / FOR | ____ / ____ µm | 2 – 4 µm | — |

## Décision

☐ **GO** — Gates 1 à 4 conformes → passer à **L6 (6 kg puis 9 kg)**
☐ **CU bonne, FPD faible** → **L4** (carrier pré-conditionné SV003 + 8 % ML001)
☐ **RSD FOR > 5 %** → **L3** (ordre inversé : BUD d'abord, prémix FOR en dernier)
☐ **Écoulement / remplissage insuffisant** → **L5** (SV010 ou SV003/SV010) — mais **régler
d'abord les paramètres machine** : la littérature montre que la variabilité de masse dépend
davantage des paramètres procédé que des attributs du matériau.

---

## Annexe — feuille de relevé environnement (à joindre à chaque lot)

| Étape | Heure | HR (%) | T (°C) | Opérateur | Observations |
|---|---|---|---|---|---|
| Pesée | ____ | ____ | ____ | ____ | ____ |
| Sandwich | ____ | ____ | ____ | ____ | ____ |
| Tamisage 1 | ____ | ____ | ____ | ____ | ____ |
| Mélange 1 | ____ | ____ | ____ | ____ | ____ |
| Tamisage 2 | ____ | ____ | ____ | ____ | ____ |
| Mélange 2 | ____ | ____ | ____ | ____ | ____ |
| Tamisage 3 | ____ | ____ | ____ | ____ | ____ |
| Mélange 3 | ____ | ____ | ____ | ____ | ____ |

**À noter systématiquement** : tout collage aux parois, toute motte visible, tout comportement
électrostatique (poudre qui « saute »), toute difficulté au tamisage. Ces observations
qualitatives sont souvent plus informatives que les chiffres pour diagnostiquer un lot raté.
