# Scale-up 3 → 6 → 9 kg : ce qu'il faut maintenir et ce qu'il faut recalculer

## 1. Le principe qui change tout

**La proportionnalité simple est ce qui a fait échouer le passage direct à 9 kg.**
Un mélangeur à retournement ne « fait pas la même chose en plus grand » : son efficacité dépend
du **taux de remplissage**, qui n'est pas conservé quand on multiplie la masse dans une cuve fixe.

`calcul interne` — Inversina 20 L, densités versées DFE :

| Masse | SV003 (630 g/L) | SV010 (690 g/L) | ML001 (570 g/L) | SV003 + 8 % ML001 (≈ 625 g/L) |
|---|---|---|---|---|
| 3 kg | 4,8 L → **24 %** | 4,3 L → 22 % | 5,3 L → 26 % | 4,8 L → 24 % |
| 4,5 kg | 7,1 L → 36 % | 6,5 L → 33 % | 7,9 L → 39 % | 7,2 L → 36 % |
| 6 kg | 9,5 L → **48 %** | 8,7 L → 43 % | 10,5 L → 53 % | 9,6 L → 48 % |
| 6,3 kg (1re fraction 7:2:1 à 9 kg) | 10,0 L → 50 % | 9,1 L → 46 % | 11,1 L → 55 % | 10,1 L → 50 % |
| 8,1 kg (après 2e fraction) | 12,9 L → 64 % | 11,7 L → 59 % | 14,2 L → 71 % | 13,0 L → 65 % |
| **9 kg** | 14,3 L → **71 %** | 13,0 L → **65 %** | 15,8 L → **79 %** | 14,4 L → **72 %** |

> ⚠️ Ces volumes sont calculés à partir des **densités versées du lactose seul**. La densité
> versée du **bulk réel** (après mélange, tamisage, avec les APIs) doit être **mesurée** au
> Gate 2 et les taux de remplissage recalculés. C'est une mesure à 10 minutes qui conditionne
> toute la stratégie de scale-up.

## 2. Les deux routes historiques, relues

| Route | Ce que fait la dernière étape à haute charge | Verdict |
|---|---|---|
| **« 3 sous-lots de 3 kg »** (ancien 6 et 9 kg) | **combiner trois mélanges déjà homogènes** — une opération de macro-mélange, facile | robuste, mais coûteuse (manipulations, tamisages, transferts, temps opérateur) |
| **« 9 kg direct, 3 × 3 kg de dilution »** | **distribuer 4,32 g de formotérol dans 9 kg** — l'opération la plus difficile du procédé, exécutée à **71 % de remplissage** | efficace en mono-produit, fragile en dual-API |

**Le passage de l'une à l'autre a donc inversé l'ordre de difficulté.** C'est une explication
mécanique simple, testable, et qui n'accuse ni la formule ni les APIs.

## 3. Paramètres : maintenir ou recalculer

| Paramètre | Statut au scale-up | Commentaire |
|---|---|---|
| **Répartition 7:2:1** | **MAINTENIR** | grandeur sans dimension |
| **Concentration du prémix FOR (1 % m/m)** | **MAINTENIR** | sans dimension — c'est l'intérêt majeur de l'architecture B |
| **Vitesse Inversina (rpm)** | **MAINTENIR** | à documenter (Q5) |
| **Nombre de révolutions (rpm × t)** | **RECALCULER** si le remplissage dépasse ~55–60 % | l'homogénéité en tumbler suit le **nombre de révolutions**, pas le temps ; mais à fort remplissage la relation se dégrade |
| **Temps par étape (15 min)** | **À CHALLENGER par la mesure** | cinétique embarquée dans L2 à 3 kg, **à refaire à 9 kg** si le 9 kg est marginal |
| **Taux de remplissage** | **PILOTER** | facteur critique n°1 ; c'est lui, et non la masse, qu'il faut chercher à reproduire |
| **Maille de tamisage (250 µm)** | **MAINTENIR** | vérifier le **débit** du Russell à 9 kg (Q7) : un tamisage plus long = plus de contact, plus de charge électrostatique |
| **Nombre d'étapes (3)** | **MAINTENIR** | ne pas ajouter d'étape au scale-up : chaque étape supplémentaire ajoute du press-on |
| **Échantillonnage** | **AUGMENTER** : 10 points à 3 et 6 kg, **15 points à 9 kg** | un lit plus profond exige plus de points, en particulier **au fond de cuve** |
| **Densité versée du bulk** | **MESURER à chaque échelle** | elle pilote le remplissage et le comportement au dosator |

## 4. Séquence recommandée

1. **3 kg** — screening d'architecture (L1 → L2, éventuellement L3/L4). *Variables : formulation.*
2. **6 kg** — confirmation à 48 % de remplissage, **zone favorable d'un tumbler**.
   *Variable : profondeur de lit.* C'est l'échelle la plus confortable et, si nécessaire, une
   **taille industrielle parfaitement acceptable**.
3. **9 kg** — **essai de robustesse mécanique**, pas essai de formulation.
   - Si 6 kg OK et 9 kg OK → GO industriel à 9 kg.
   - Si 6 kg OK et 9 kg marginal → deux parades, dans l'ordre :
     **(a)** augmenter le nombre de révolutions **de la seule étape 3** ;
     **(b)** **figer la taille industrielle à 6 kg**. La perte de productivité est très inférieure
     au coût récurrent d'un problème d'uniformité.
   - Si 6 kg KO → retour formulation (L4, fines), **pas** au scale-up.

## 5. Astuce de représentativité (à valider auprès du fabricant)

Si l'Inversina accepte des **cuves interchangeables**, faire le screening de 3 kg dans une cuve
de **6–8 L** donne **60–80 % de remplissage**, c'est-à-dire la **mécanique du lot de 9 kg**, pour
un tiers de la consommation d'API. C'est le moyen le moins cher de rendre un lot de 3 kg
réellement prédictif du 9 kg. → question **Q5**.

## 6. Le piège des fines au scale-up

`calcul interne` — ajouter 8 % de ML001 fait passer la densité versée d'environ 630 à 625 g/L
(effet faible), mais un bulk **dominé** par du ML001 tomberait à 570 g/L, soit **79 % de
remplissage à 9 kg**. Plus généralement : **toute modification de formule qui abaisse la densité
versée dégrade le mélange à 9 kg.** Toute décision d'ajouter des fines doit donc être validée sur
**deux** critères — la FPF **et** le taux de remplissage résultant.
