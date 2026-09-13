# Annexe A3 — Plan analytique et protocole d'échantillonnage

> **Le risque n°1 du projet n'est pas de rater le mélange : c'est de croire qu'on l'a réussi.**
> Un RSD mesuré sur des prises d'essai de 1 g peut être excellent alors que l'uniformité de dose
> à 25 mg est inacceptable. Tout ce plan découle de ce principe.

## 1. Règle d'échantillonnage

| Paramètre | Valeur | Justification |
|---|---|---|
| **Masse de prise d'essai** | **25 mg (1 dose)**, ou 75 mg (3 doses) si la précision de pesée l'exige | c'est l'échelle à laquelle le patient reçoit le produit ; toute autre échelle mesure autre chose |
| **Nombre de positions** | **10** à 3 et 6 kg · **15** à 9 kg | un lit plus profond exige plus de points |
| **Cartographie** | haut / milieu / bas × paroi / centre, **+ fond de cuve** | le fond de cuve est le point le plus souvent hors spécification dans un tumbler |
| **Outil** | sonde voleuse adaptée aux petites prises | à acquérir (achat prioritaire n°1) |
| **Réplicats** | analyse en triple sur chaque prise | sépare la variabilité analytique de la variabilité du mélange |

**Contrôle de la méthode d'échantillonnage** : sur le premier lot, préparer un **témoin de
mélange parfait** (25 mg de bulk reconstitué par pesée directe des trois composants) et le passer
comme un échantillon. Si le témoin ne donne pas 100 ± 2 %, le problème est analytique, pas
formulatoire.

## 2. Méthode de dosage

- **HPLC-UV, dosage simultané budésonide + formotérol**, gamme couvrant 50–150 % des
  concentrations attendues (FOR ≈ 2,4 µg/mL et BUD ≈ 40–80 µg/mL pour 25 mg dans 5 mL).
- **Le budésonide est un mélange d'épimères 22R/22S** : la méthode doit statuer explicitement
  (somme des deux pics ou pic unique non résolu) — point à figer avant le premier lot.
- **Récupération** : valider l'extraction sur un mélange lactose/API reconstitué ; viser ≥ 98 %.
- **Blancs de rinçage** : sur L0, rincer et doser le matériel du prémix pour quantifier
  l'adsorption du formotérol.

## 3. Les quatre portes

### Gate 1 — Homogénéité du bulk *(obligatoire sur tous les lots)*

| Analyse | Critère GO |
|---|---|
| Teneur moyenne BUD et FOR | **95 – 105 %** de la valeur théorique |
| **RSD BUD** (10–15 × 25 mg) | **≤ 5 %** |
| **RSD FOR** (10–15 × 25 mg) | **≤ 5 %** |
| Valeurs individuelles | aucune hors **90 – 110 %** |
| Cartographie spatiale | pas de gradient systématique haut/bas ou paroi/centre |
| Bilan matière du lot | ≥ 98 % |

*Critère de RSD ≤ 5 % : c'est celui retenu par US9616024 pour une homogénéité acceptable.*

### Gate 2 — Aptitude de la poudre *(obligatoire avant tout essai de remplissage)*

| Analyse | Critère GO |
|---|---|
| Densité versée et tassée | mesurées et **reportées dans le calcul de taux de remplissage** |
| **Indice de Carr** | ≤ 25 % (viser ≤ 20 %) |
| **Rapport de Hausner** | ≤ 1,34 |
| Écoulement | mesuré (débit à l'orifice ou angle de repos) |
| **Test de ségrégation** | après sollicitation (vibration contrôlée ou transfert répété), **pas de dérive de l'assay FOR > 10 %** entre le haut et le bas du lit |

### Gate 3 — Remplissage *(seulement si Gates 1 et 2 GO)*

| Analyse | Critère GO |
|---|---|
| Essai Modu-C MS, **25 mg**, gélule taille 3 | **RSD de masse ≤ 3 %** |
| Teneur en gélule (n ≥ 20) | 95 – 105 %, RSD ≤ 5 % |
| **Dose délivrée** (Ph. Eur. 2.9.18) sur le dispositif type Aerolizer | **≥ 70 %** de la dose mesurée (référence marché : 73 % BUD, 85 % FOR) |
| Uniformité de la dose délivrée | conforme Ph. Eur. |

### Gate 4 — Performance aérodynamique *(la ressource rare — jamais sur un mauvais mélange)*

| Analyse | Critère GO |
|---|---|
| **NGI**, débit réglé pour **ΔP = 4 kPa** (Ph. Eur. 2.9.18) | débit à déterminer selon la résistance du dispositif (à documenter — Q10 ; la littérature sur dispositifs de type Aerolizer/Cyclohaler travaille entre 60 et 100 L/min) |
| **FPD et FPF (< 5 µm) pour CHAQUE API séparément** | **FPF ≥ 30 %** en screening ; cible marché **45–56 %** |
| **MMAD** et GSD par API | MMAD 2 – 4 µm |
| Dépôt dans l'induction / la gélule / le dispositif | documenté (les pertes dans le dispositif renseignent sur l'adhésion) |

> **Règle d'économie** : NGI uniquement sur les lots ayant passé Gates 1 et 2, et — pour l'étude
> cinétique — uniquement aux temps 15 et 25 min.

## 4. Analyses spécifiques embarquées

| Sur quel lot | Analyse | Ce qu'elle tranche |
|---|---|---|
| **L0** | assay + RSD du prémix seul ; rinçage du matériel | qualité de l'API, pertes, électrostatique |
| **L0** | comparaison tamis 250 µm vs 212 µm | effet de la maille sur les entités de formotérol |
| **L2** | assay + RSD **avant et après** le tamisage final | le tamisage est-il destructeur ? (désaccord D3) |
| **L2** | cinétique 5 / 10 / 15 / 25 min | sous-mélange vs sur-mélange (désaccord D4) |
| **Tous** | bilan matière à chaque tamisage (±0,5 %) | pertes préférentielles de formotérol |
| **Tous** | HR et T° de salle à chaque étape | variabilité inter-lots |

## 5. Ce qu'il ne faut pas faire

- Ne pas juger l'homogénéité sur des prises de 1 g.
- Ne pas lancer un NGI pour « voir », sur un mélange dont la CU n'est pas connue.
- Ne pas comparer un RSD obtenu sur 10 points à un RSD obtenu sur 3 points.
- Ne pas analyser un seul API : **le formotérol et le budésonide doivent toujours être dosés sur
  la même prise d'essai** — c'est le seul moyen de voir si les deux varient ensemble
  (co-agglomération) ou indépendamment (ségrégation).

> **Signature diagnostique à rechercher** : si, prise par prise, les teneurs en BUD et en FOR sont
> **corrélées positivement**, c'est la signature de la **co-agglomération BUD–FOR**. Si elles
> varient indépendamment, c'est de la ségrégation ou un défaut de mélange. Cette corrélation est
> gratuite à calculer et c'est le test le plus direct de notre hypothèse principale.
