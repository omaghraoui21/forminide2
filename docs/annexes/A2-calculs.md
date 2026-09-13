# Annexe A2 — Calculs de référence

Tous ces calculs sont reproductibles par `python3 scripts/calculs_cles.py`.
Ils sont marqués `calcul interne` partout où ils sont cités.

## 1. Charges massiques

Base : 25,0 mg de poudre par gélule.

| Dosage | Budésonide | Formotérol (fumarate dihydraté) | Lactose | Ratio BUD:FOR |
|---|---|---|---|---|
| 12 / 200 | 200 µg = **0,800 % m/m** | 12 µg = **0,0480 % m/m** | 24,788 mg | **16,7 : 1** |
| 12 / 400 | 400 µg = **1,600 % m/m** | 12 µg = **0,0480 % m/m** | 24,588 mg | **33,3 : 1** |

> Vérification externe : le KÜB de FORPACK 12/200 déclare **24,7880 mg de lactose**, soit
> exactement la valeur calculée. `FAIT CONFIRMÉ`

## 2. Masse d'un agglomérat en fonction de son diamètre

Hypothèse : agglomérat sphérique, masse volumique **effective** (poudre micronisée peu tassée)
comprise entre **0,4 et 0,6 g/cm³**. `m = (π/6)·d³·ρ_eff`

| d (µm) | masse à ρ=0,4 | masse à ρ=0,6 | **% d'une dose de FOR (12 µg)** |
|---|---|---|---|
| 355 | 9,37 µg | 14,06 µg | 78 – 117 % |
| **250 (maille Russell)** | **3,27 µg** | **4,91 µg** | **27 – 41 %** |
| 212 | 2,00 µg | 3,00 µg | 17 – 25 % |
| 150 | 0,71 µg | 1,06 µg | 6 – 9 % |
| 100 | 0,21 µg | 0,31 µg | 2 – 3 % |
| 56 | 0,04 µg | 0,06 µg | < 1 % |

**Conséquence** : un unique agglomérat de formotérol passant le tamis de 250 µm suffit à faire
sortir une gélule des spécifications. Réduire la maille du **prémix** à 212 µm divise le pire cas
par ~1,6 ; à 150 µm, par ~4,6.

## 3. Limite statistique du mélange — le formotérol est-il « dosable » ?

Modèle : mélange aléatoire binaire, `RSD_min = 1/√N` où N est le nombre d'entités indépendantes
d'actif dans la prise d'essai. ρ_vraie ≈ 1,3 g/cm³.

| d des particules primaires de FOR | Masse par particule | N par dose de 12 µg | **RSD statistique minimal** |
|---|---|---|---|
| 1,5 µm | 2,30 × 10⁻⁶ µg | 5,22 × 10⁶ | **0,044 %** |
| 2,5 µm | 1,06 × 10⁻⁵ µg | 1,13 × 10⁶ | **0,094 %** |
| 4,0 µm | 4,36 × 10⁻⁵ µg | 2,76 × 10⁵ | **0,191 %** |

> **Résultat central du dossier** : même pour un formotérol grossièrement micronisé, le RSD
> statistique minimal est **inférieur à 0,2 %**. **Tout RSD mesuré au-dessus de ~1 % est donc
> intégralement dû à des agglomérats ou à de la ségrégation, jamais à la « faible dose » en
> elle-même.** L'argument « 12 µg, c'est trop peu pour être homogène » est faux.

## 4. Inversion du raisonnement : à quel diamètre correspond un RSD mesuré ?

| RSD observé (prise de 25 mg) | Entités indépendantes par dose | Masse par entité | **Diamètre effectif** |
|---|---|---|---|
| 2 % | 2 500 | 0,005 µg | **19 µm** |
| 5 % | 400 | 0,030 µg | **35 µm** |
| **10 %** | 100 | 0,120 µg | **56 µm** |
| 15 % | 44 | 0,270 µg | **73 µm** |

> **Conséquence opérationnelle majeure** : les entités responsables d'une mauvaise uniformité du
> formotérol mesurent **20 à 80 µm**. Elles passent toutes le tamis de 250 µm sans être vues.
> **Aucune modification du tamisage ne corrigera une mauvaise CU** — seules la prévention de leur
> formation (prémix, séparation des APIs) et leur érosion par le mélange le peuvent.
> Le tamisage protège contre les **très gros** agglomérats (> 250 µm, qui donnent des valeurs
> aberrantes ponctuelles), pas contre le RSD.

## 5. Taux de remplissage de l'Inversina 20 L

`V = masse / densité versée` ; densités DFE `FAIT CONFIRMÉ`.

| Masse | ML001 (570 g/L) | SV003 (630 g/L) | SV010 (690 g/L) | SV003 + 8 % ML001 (≈ 625 g/L) |
|---|---|---|---|---|
| 3,0 kg | 5,3 L = 26 % | 4,8 L = **24 %** | 4,3 L = 22 % | 4,8 L = 24 % |
| 4,5 kg | 7,9 L = 39 % | 7,1 L = 36 % | 6,5 L = 33 % | 7,2 L = 36 % |
| 6,0 kg | 10,5 L = 53 % | 9,5 L = **48 %** | 8,7 L = 43 % | 9,6 L = 48 % |
| 6,3 kg | 11,1 L = 55 % | 10,0 L = 50 % | 9,1 L = 46 % | 10,1 L = 50 % |
| 7,2 kg | 12,6 L = 63 % | 11,4 L = 57 % | 10,4 L = 52 % | 11,5 L = 58 % |
| 8,1 kg | 14,2 L = 71 % | 12,9 L = 64 % | 11,7 L = 59 % | 13,0 L = 65 % |
| **9,0 kg** | **15,8 L = 79 %** | **14,3 L = 71 %** | **13,0 L = 65 %** | **14,4 L = 72 %** |

⚠️ Calculé sur la densité versée du **lactose seul**. La densité versée du **bulk réel** doit être
mesurée au Gate 2 et ces valeurs recalculées.

## 6. Quantités par lot (répartition 7 : 2 : 1)

| Lot | Dosage | BUD | FOR | Lactose total | Prémix FOR (1 %) | Fraction 1 (70 %) | Fraction 2 (20 %) | Fraction 3 (10 %) |
|---|---|---|---|---|---|---|---|---|
| 3 kg | 12/200 | 24,00 g | 1,44 g | 2 974,6 g | 144,0 g | 2 082,2 g | 594,9 g | 297,5 g |
| 3 kg | 12/400 | 48,00 g | 1,44 g | 2 950,6 g | 144,0 g | 2 065,4 g | 590,1 g | 295,1 g |
| 6 kg | 12/200 | 48,00 g | 2,88 g | 5 949,1 g | 288,0 g | 4 164,4 g | 1 189,8 g | 594,9 g |
| 6 kg | 12/400 | 96,00 g | 2,88 g | 5 901,1 g | 288,0 g | 4 130,8 g | 1 180,2 g | 590,1 g |
| 9 kg | 12/200 | 72,00 g | 4,32 g | 8 923,7 g | 432,0 g | 6 246,6 g | 1 784,7 g | 892,4 g |
| **9 kg** | **12/400** | **144,00 g** | **4,32 g** | **8 851,7 g** | **432,0 g** | **6 196,2 g** | **1 770,3 g** | **885,2 g** |

*(le prémix FOR est prélevé sur la fraction 1 ; sa masse de lactose est donc incluse dans les
70 %)*

## 7. Faisabilité analytique

| Volume d'extraction d'une prise de 25 mg | [FOR] | [BUD 200] | [BUD 400] |
|---|---|---|---|
| 2 mL | 6,00 µg/mL | 100,0 µg/mL | 200,0 µg/mL |
| **5 mL** | **2,40 µg/mL** | 40,0 µg/mL | 80,0 µg/mL |
| 10 mL | 1,20 µg/mL | 20,0 µg/mL | 40,0 µg/mL |

**Conclusion** : le dosage du formotérol à l'échelle de la dose unitaire est parfaitement
réalisable en HPLC-UV. **La contrainte du projet n'est pas la sensibilité analytique, c'est la
discipline d'échantillonnage** : accepter de prélever 25 mg et non 1 g.
