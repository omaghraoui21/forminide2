# RAPPORT — Développer un bulk DPI combiné Budésonide / Formotérol en capsule unique

**Livrable A → R** · Équipe virtuelle (voir `AGENTS.md`) · Niveaux de confiance selon `CLAUDE.md`
Sources détaillées : `docs/annexes/A1-registre-preuves.md` · Calculs : `docs/annexes/A2-calculs.md`

---

## Résumé en une page

**Le problème n'est pas le couple BUD/FOR.** Un produit en capsule unique 12/400 existe,
est commercialisé et a été publié comme équivalent à deux capsules séparées, avec un
**formotérol non pénalisé** (FPF FOR 56 % vs FPF BUD 45 %). `FAIT CONFIRMÉ`

**Le problème n'est pas non plus le procédé historique.** Le procédé maison (sandwich
lactose/API/lactose, dilution séquentielle en trois fractions, tamisage, tumbler 15 min par
étape) est exactement la plateforme décrite et chiffrée dans EP3175842A1, qui l'utilise avec
succès sur un principe actif à 0,41 % m/m. `FAIT CONFIRMÉ`

**Le problème est la rencontre de deux poudres cohésives dans le même sandwich, au moment
où la dernière dilution se fait dans les pires conditions de mélange.** Deux mécanismes se
cumulent :

1. **Co-agglomération API–API.** Dans le sandwich commun, le budésonide représente 17 à 33 fois
   la masse du formotérol. Le formotérol se retrouve piégé dans des agglomérats riches en
   budésonide. Sa distribution cesse d'être gouvernée par le lactose et devient gouvernée par
   celle des agglomérats de budésonide. `INFÉRENCE HAUTE CONFIANCE`
   → Un agglomérat survivant de 250 µm porte **3,3 à 4,9 µg**, soit **27 à 41 % d'une dose de
   formotérol**. Le Russell 250 µm ne peut donc pas protéger le formotérol. `calcul interne`
   → Inversement, un RSD FOR de 10 % correspond à des entités effectives de **≈ 56 µm** :
   **le tamis ne les verra jamais**, seule la désagglomération peut les supprimer. `calcul interne`

2. **La dernière dilution est faite au pire taux de remplissage.** À 9 kg, l'Inversina 20 L est
   remplie à **65–72 %** (79 % avec un mélange riche en ML001), alors que les étapes à 3 et 6 kg
   sont à 22–24 % et 43–48 %. Le procédé demande donc à **l'étape la moins efficace** de faire
   **le travail le plus difficile** : distribuer un API à 0,048 % dans l'ensemble du lot.
   L'ancienne route « 3 × sous-lots de 3 kg » ne le faisait jamais : la dernière étape n'y était
   qu'une combinaison de trois mélanges déjà homogènes. `INFÉRENCE HAUTE CONFIANCE`

**La modification minimale recommandée** (aucun achat, aucun équipement, même nombre d'étapes) :

> **(i)** un **prémix formotérol dédié** à ≈ 1 % m/m, tamisé, avant tout contact avec le
> budésonide ; **(ii)** une répartition du lactose en **7 : 2 : 1** au lieu de 3 : 3 : 3 ;
> **(iii)** on ne termine jamais le procédé par un tamisage.

Le 7 : 2 : 1 règle deux problèmes d'un coup : c'est la meilleure répartition publiée pour
l'uniformité d'un actif à faible dose, **et** elle réduit à 10 % de la masse le travail confié
à l'étape à fort taux de remplissage.

**Décision industrielle possible en 4 essais de mélange** (1 prémix + 3 lots) — voir
`docs/07-sequence-minimale.md`.

---

## A. Diagnostic historique — pourquoi le combiné 9 kg a probablement échoué

### A.1 Pourquoi le procédé historique marche sur les mono-produits

Le procédé maison réalise, sans le nommer, quatre opérations physiques distinctes :

| Opération | Étape du procédé | Ce qu'elle accomplit |
|---|---|---|
| **Confinement** | sandwich lactose / API / lactose | l'API n'est jamais libre : il est capturé entre deux lits de lactose, ce qui limite les pertes, l'électrostatique et la projection |
| **Désagglomération calibrée** | tamisage 250 µm | transforme les mottes d'API micronisé en **agglomérats de taille bornée**, puis le mélange les érode |
| **Distribution** | Inversina 15 min | transport convectif + diffusif à l'échelle du lot |
| **Dilution progressive** | 3 fractions successives | chaque ajout ne perturbe qu'une fraction d'un mélange déjà bon |

`FAIT CONFIRMÉ` — Ce n'est pas une pratique isolée : **EP3175842A1** (Alfred E. Tiefenbacher,
priorité 03/12/2015) revendique exactement cette séquence — première portion de lactose, totalité
de l'actif, deuxième portion par-dessus, mélange, tamisage optionnel, puis troisième portion,
mélange, tamisage optionnel — avec **Turbula 22 rpm, 15 min par étape**.

`FAIT CONFIRMÉ` — **US9616024** (Norton Healthcare, priorité 2003) chiffre le mécanisme du
tamisage sur budésonide et formotérol, en mélangeur **bas cisaillement** (Turbula T2C, gear 3,
10 min) :

| Formulation | RSD | Récupération |
|---|---|---|
| Budésonide 9,6 % m/m, **sans** tamisage | 14,3 % | 79,6 % |
| Budésonide 9,6 % m/m, **tamisé 250 µm** | 4,6 % | 88,5 % |
| Budésonide, tamisé + tamisage final 355 µm | **1,5 %** | 82,0 % |
| Formotérol 0,265 % m/m, **sans** tamisage | 1,2 % | 91,4 % |
| Formotérol 0,265 % m/m, **tamisé 250 µm** | **0,9 %** | **99,6 %** |

**Conséquence pour nous** : le tamisage à 250 µm n'est pas un détail du procédé, c'est **le**
mécanisme qui rend le mélange bas cisaillement suffisant. Il faut le conserver — et comprendre
pourquoi il ne suffit plus à deux APIs.

### A.2 Ce qui change quand on passe à deux APIs

**(a) La charge d'API de la première fraction est multipliée.**
`calcul interne` — Dans la première fraction (1/3 du lot), la concentration locale est 3× la
finale :

| Cas | API dans la 1re fraction | Concentration locale |
|---|---|---|
| FOR seul | 0,048 % × 3 | **0,14 %** |
| BUD 400 seul | 1,600 % × 3 | 4,8 % |
| **BUD 400 + FOR ensemble** | (1,600 + 0,048) × 3 | **4,94 %** dont FOR 0,14 % |

Le sandwich combiné doit donc désagglomérer **près de 5 % m/m de poudre micronisée cohésive**
en une seule séquence tamisage + 15 min, contre 0,14 % dans le cas du formotérol seul. C'est un
changement de régime, pas un changement de degré.

**(b) Les deux APIs s'agglomèrent entre eux avant d'atteindre le lactose.**
`FAIT CONFIRMÉ` — Des travaux sur un couple corticoïde/β2 (salbutamol base + dipropionate de
béclométasone, mélange physique sur carrier lactose commun) montrent par microscopie Raman une
**co-agglomération SB–BDP** et des profils de dépôt par étage significativement différents entre
les deux actifs : dans un mélange physique, les deux APIs s'influencent mutuellement.
`INFÉRENCE HAUTE CONFIANCE` — Le même phénomène appliqué à BUD/FOR, avec un rapport de masse de
17 à 33 pour 1, signifie que **le formotérol est le passager, le budésonide est le véhicule**.

**(c) L'arithmétique des agglomérats condamne le formotérol.**
`calcul interne` (détail dans `docs/annexes/A2-calculs.md`) :

| Diamètre d'agglomérat survivant | Masse (ρ_eff 0,4–0,6) | En % d'une dose FOR de 12 µg |
|---|---|---|
| 250 µm (= maille Russell) | 3,3 – 4,9 µg | **27 – 41 %** |
| 212 µm | 2,0 – 3,0 µg | 17 – 25 % |
| 150 µm | 0,7 – 1,1 µg | 6 – 9 % |
| 100 µm | 0,21 – 0,31 µg | 2 – 3 % |

Et dans l'autre sens :

| RSD FOR observé à 25 mg | Nb d'entités FOR indépendantes par dose | Diamètre effectif |
|---|---|---|
| 2 % | 2 500 | 19 µm |
| 5 % | 400 | 35 µm |
| **10 %** | **100** | **56 µm** |
| 15 % | 44 | 73 µm |

À titre de comparaison, si le formotérol était parfaitement dispersé en particules primaires de
2,5 µm, le RSD statistique minimal serait de **0,09 %** (≈ 1,1 million de particules par dose).
**Donc : tout RSD mesuré au-dessus de 1 % est intégralement d'origine agglomérat/ségrégation,
jamais d'origine statistique.** C'est une information de diagnostic très forte — et elle dit que
le problème se joue entre 20 et 80 µm, très en dessous de la maille de 250 µm.

**(d) La dernière dilution est faite au pire moment mécanique.**
`calcul interne` à partir des densités versées DFE `FAIT CONFIRMÉ` :

| Étape du procédé 9 kg | Masse | Volume (SV003, 630 g/L) | Remplissage de 20 L |
|---|---|---|---|
| 1re fraction | 3 kg | 4,8 L | **24 %** |
| après 2e ajout | 6 kg | 9,5 L | 48 % |
| **après 3e ajout** | **9 kg** | **14,3 L** | **71 %** |

Avec ML001 (densité versée 570 g/L), 9 kg occupent **15,8 L → 79 %**. Avec SV010 (690 g/L),
13,0 L → 65 %.

`INFÉRENCE HAUTE CONFIANCE` — Dans un mélangeur à retournement, l'efficacité du mélange chute
quand le taux de remplissage augmente : la couche cascadante libre se réduit, la mobilité des
particules à travers le plan de symétrie diminue, le temps de mélange augmente. Le procédé 9 kg
demande donc le travail le plus difficile (répartir 4,32 g de formotérol dans 9 kg) à l'étape la
moins capable.

**C'est le point qui explique le contraste observé** : la route « trois sous-lots de 3 kg »
faisait toujours le travail difficile à 24 % de remplissage et ne réservait à la haute charge
qu'une simple combinaison de mélanges déjà homogènes. La route 9 kg directe a inversé cet ordre.

### A.3 Diagnostic consolidé

> Le combiné 9 kg a probablement échoué par **cumul** de trois effets, aucun n'étant suffisant
> seul :
> 1. **co-agglomération BUD–FOR** dans le sandwich commun (le formotérol devient un passager) ;
> 2. **inefficacité du tamis 250 µm sur ce mécanisme** (les entités critiques font 20–80 µm) ;
> 3. **la dilution finale exécutée à 65–79 % de remplissage**, là où le mélangeur est le moins
>    efficace.
>
> S'y ajoute, non démontrée mais probable, une **quatrième cause de mesure** : si l'homogénéité
> historique a été jugée sur des prises d'essai de l'ordre du gramme et non de 25 mg, le RSD
> rapporté n'a aucun rapport avec l'uniformité de dose réelle. Voir `memory/questions-ouvertes.md` Q4.

**Ce que ce diagnostic implique** : la correction ne passe **ni** par un nouveau lactose,
**ni** par un nouvel équipement, **ni** par un excipient supplémentaire. Elle passe par
**l'ordre d'incorporation et la répartition du lactose**.

---

## B. Reverse engineering mondial — produits commercialisés

Détail complet, marché par marché : `docs/02-produits-commercialises.md`.

| Produit | Marché | Titulaire | Forme | Dosages | Masse poudre | Excipients | Device |
|---|---|---|---|---|---|---|---|
| **FORPACK capsair** | Turquie | Neutec İnhaler | capsule gélatine | **12/200**, 12/400 µg | **25,000 mg** (lactose **24,7880 mg**) | **lactose seul** | Capsair (mono-dose à perforation) |
| **FORPACK discair** | Turquie | Neutec İnhaler | poudre multidose | 12/400 µg | **13,000 mg** (lactose **12,5880 mg**) | lactose seul | Discair |
| **ALENIA** | Brésil | Biosintética (Aché) | capsule | 6/100, 6/200, **12/400** µg | non déclarée | lactose monohydraté | Aerocaps® |
| **FORACORT Rotacaps** | Inde | Cipla | capsule | 6/100, 6/200, 6/400 µg | non déclarée | lactose | Rotahaler |
| **FORMONIDE** | Inde | Lupin | capsule | 6/100, 6/200, 6/400 µg | non déclarée | lactose | Rotahaler |
| **Symbicort Turbuhaler** | Monde | AstraZeneca | multidose sans carrier | 100/6 → 400/12 | 0,49–0,81 mg lactose/dose | lactose | Turbuhaler |
| **BF Spiromax** | Europe | Teva/Pharmachemie | multidose | 80/4,5 → 320/9 | non déclarée | lactose (PSD brevetée) | Spiromax |

### Les trois enseignements décisifs

1. **`FAIT CONFIRMÉ` — Notre cible existe déjà, à l'unité près.** Le KÜB turc de FORPACK
   12/200 capsair déclare : formotérol fumarate dihydraté 12 mcg + budésonide 200 mcg +
   **laktoz 24,7880 mg**. Somme = **25,0000 mg exactement**. La rubrique 6.1 ne liste qu'un seul
   excipient : **le lactose**. Notre cahier des charges (25 mg, capsule, lactose seul, 12/200 et
   12/400) est donc **la copie d'un produit autorisé depuis le 06/05/2013**, avec 24 mois de
   péremption, conservation < 25 °C au sec, blister Alu/Alu.
   → **Conséquence** : aucune justification à ajouter un excipient, ni à changer la masse cible.

2. **`FAIT CONFIRMÉ` — La performance cible est publiée.** L'étude d'équivalence pharmaceutique
   brésilienne (J Bras Pneumol 2012) compare la **capsule unique** (Aerocaps®) aux **deux capsules
   séparées** (Aerolizer®) :

   | | Capsule unique | Deux capsules séparées |
   |---|---|---|
   | Teneur BUD / FOR | 111,0 % / 103,8 % | 110,5 % / 104,5 % |
   | Dose délivrée BUD / FOR | 293,2 µg / 10,2 µg | 353,0 µg / 11,1 µg |
   | FPF < 5 µm BUD / FOR | **45 % / 56 %** | 54 % / 52 % |

   → La capsule unique **perd un peu sur le budésonide** (45 vs 54 %) et **gagne sur le
   formotérol** (56 vs 52 %). `INFÉRENCE HAUTE CONFIANCE` : la combinaison, correctement
   formulée, **améliore** le détachement du formotérol — cohérent avec l'idée que le budésonide,
   17 à 33 fois plus abondant, **sature les sites de haute énergie** du lactose et laisse au
   formotérol des sites plus faibles. La compétition BUD/FOR n'est donc pas seulement un risque,
   c'est aussi un **levier**, à condition qu'elle se produise sur le carrier et non dans un
   agglomérat.
   → **Conséquence pour nos essais** : viser FPF ≥ 30 % en screening, 45–56 % en cible ; dose
   délivrée ≥ 70 % (le marché est à 73 % pour BUD et 85 % pour FOR).

3. **`FAIT CONFIRMÉ` — Le même industriel utilise deux masses différentes selon le device**
   (25 mg en capsule, 13 mg en multidose). `INFÉRENCE HAUTE CONFIANCE` : le système carrier est
   accordé au device et à la plateforme de remplissage. → Ne jamais transposer une composition
   multidose dans une capsule.

---

## C. OSINT « formulation fingerprint »

Méthode et preuves : `docs/02-produits-commercialises.md`. Synthèse pour **FORPACK 12/200 capsair**,
le produit le plus proche de notre cible :

| Élément | Statut | Contenu |
|---|---|---|
| Masse totale par capsule | **FAIT CONFIRMÉ** | 25,0000 mg (24,7880 + 0,200 + 0,012) |
| Excipient unique | **FAIT CONFIRMÉ** | lactose (mention « contient de faibles quantités de protéines de lait ») |
| Enveloppe | **FAIT CONFIRMÉ** | gélatine ; coiffe violet clair transparent, corps naturel |
| Conditionnement / conservation | **FAIT CONFIRMÉ** | blister Alu/Alu, < 25 °C au sec, 24 mois |
| Device | **FAIT CONFIRMÉ** | inhalateur mono-dose à bouton de perforation (architecture type Aerolizer) |
| Taille de capsule | **INFÉRENCE HAUTE CONFIANCE** | taille 3 (standard des DPI capsule à 25 mg ; les brevets Zambon utilisent la taille 3 HPMC avec RS01) |
| Type de mélange | **INFÉRENCE HAUTE CONFIANCE** | mélange ordonné carrier-based classique (lactose = 99,15 % de la masse) |
| Présence de fines de lactose | **INFÉRENCE FAIBLE CONFIANCE** | probable (intrinsèques et/ou extrinsèques) — aucune notice ne déclare une répartition granulométrique |
| Grade de lactose exact | **INCONNU** | aucune source publique |
| Architecture de prémélange | **INCONNU** | aucune source publique |
| Rapport dose délivrée / dose mesurée | **INFÉRENCE HAUTE CONFIANCE** | 73–85 % (mesuré sur le produit brésilien équivalent) |

> **Règle appliquée** : rien de ce qui figure en « inférence » ne doit être cité en interne
> comme une caractéristique du produit concurrent.

---

## D. Brevets — les exemples réellement reproductibles

Extraction complète des exemples : `docs/03-brevets.md`.

### D.1 Directement applicables (mêmes équipements, mêmes APIs ou équivalents)

**EP3175842A1 — « Dry powder mixing process » (Alfred E. Tiefenbacher / Naonopharm, prio. 2015-12-03)**
`FAIT CONFIRMÉ` — C'est **notre procédé, publié**. Revendique : 1re portion de lactose → totalité
de l'actif → 2e portion de lactose → mélange (Turbula 22 rpm, 15 min) → tamisage optionnel →
3e portion de lactose → mélange → tamisage optionnel. Les exemples (bromure de tiotropium
monohydraté à **0,41 % m/m**, donc un actif à faible dose) font varier **la répartition des trois
portions** :

| Exemple | Répartition 1re:2e:3e | Assay | RSD | AV |
|---|---|---|---|---|
| 3 | **7 : 2 : 1** | 100,4 % | **2,9 %** | **7,1** |
| 2 | 5 : 2 : 3 | 99,9 % | 3,3 % | 7,8 |
| 5 | 4 : 1 : 5 | 101,0 % | 3,2 % | 7,7 |
| 6 | 2 : 1 : 7 | 101,5 % | 4,1 % | 10,0 |
| 4 | 5 : 1 : 4 | 102,2 % | 4,8 % | 12,5 |

**Interprétation** `INFÉRENCE HAUTE CONFIANCE` : les deux meilleures valeurs d'AV correspondent
aux répartitions dont la **deuxième portion vaut 2** et dont la **première portion est grande** ;
les deux plus mauvaises reportent l'essentiel du lactose sur la fin. Notre répartition historique
(3:3:3, soit 3,33:3,33:3,33) n'est pas testée dans le brevet et se situe au milieu.
**Conséquence** : la répartition du lactose est un **facteur de procédé à part entière**, gratuit
à modifier, et dont l'effet publié sur un actif à 0,41 % est du même ordre que l'effet attendu de
tout le reste de nos leviers. → **Passer en 7:2:1.**
⚠️ **FTO** : brevet postérieur possible à notre usage interne — à faire vérifier par le conseil PI
(antériorité d'exploitation) avant toute revendication. Voir `memory/questions-ouvertes.md` Q8.

**US9616024 / US9345664 / US9987229 — « Process for preparing a medicament » (Norton Healthcare, prio. 2003-09-02)**
`FAIT CONFIRMÉ` — Cœur du brevet : **tamiser l'actif (50–3000 µm, exemples à 250 µm) pour former
des agglomérats lâches calibrés**, puis mélanger en **bas cisaillement** jusqu'à ce que ≥ 90 % de
l'actif soit sous 50 µm. Exemples sur **budésonide** et **formotérol** (tableau en §A.1).
Points exploitables immédiatement :
- mélange en tumbler **Turbula 15 min = optimum** ; au-delà, la FPF diminue (exemple salbutamol) ;
- les agglomérats **< 355 µm donnent une FPF significativement supérieure** aux agglomérats
  < 250 µm (43,6–42,2 % vs 38,5–31,2 %) — donnée contre-intuitive à garder en tête si notre FPD
  est faible malgré une bonne CU ;
- critère d'homogénéité retenu par le brevet : **RSD ≤ 5 %**.
Priorité 2003 → **protection très probablement expirée** `INFÉRENCE HAUTE CONFIANCE`.

### D.2 Adaptables (mécanisme transposable, chimie ou device différents)

**US7879833 / US8258124 — « Combination medicament » (Nycomed → Covis, prio. 2002-12-12)**
`FAIT CONFIRMÉ` — Association corticoïde (ciclésonide) + **formotérol**, en capsule 25 mg et en
multidose. **L'architecture est exactement celle que nous recommandons** :
- Exemple 3 : **60 mg de formotérol fumarate dihydraté micronisé prémélangés avec 7,27 g de
  lactose** (soit un prémix à **0,82 % m/m**), tamisage 0,5 mm, Turbula ; le corticoïde
  (2,67 g) et les 90 g de lactose restants sont ajoutés **ensuite** ;
- Exemple 2 : formotérol 300 mg prémélangé avec 97,2 g de lactose, corticoïde prémélangé
  séparément avec 250 g, puis 650 g de lactose de dilution — **double prémix** ;
- Exemple 1 (capsule) : mélange en **deux portions**, tamisage 0,71 mm, **25 mg en capsule taille 3**.
**Conséquence directe** : notre prémix formotérol cible **≈ 1 % m/m** n'est pas une invention,
c'est la valeur d'un exemple de brevet sur le même API. Priorité 2002 → expiré
`INFÉRENCE HAUTE CONFIANCE`.

**US10449147 / US10226421 / ES2837040 — Zambon (prio. 2013–2014)**
`FAIT CONFIRMÉ` — Le **système carrier** y est décrit avec précision : lactose grossier
**Respitose® SV003 (85–96 %)** + lactose fin **Lacto-Sphere® MM3 (4–15 %)**, l'optimum cité étant
**91 : 9**. Capsules **taille 3 HPMC**, inhalateur **RS01 (Plastiape, type Aerolizer)**, MSLI,
FPF > 60 %, fraction délivrée > 80 %.
⚠️ **Les actifs y sont obtenus par spray drying avec leucine** → **incompatible avec nos moyens**.
Mais **le couple carrier grossier + 4–15 % de fines est, lui, directement transposable**.
**Conséquence** : si nous devons ajouter des fines, la fenêtre utile publiée est **4–15 %, optimum
≈ 9 %**, sur base SV003.

**US11642475 / BR112016011996 — Pharmachemie/Teva, BF Spiromax (prio. 2013-12-09)**
`FAIT CONFIRMÉ` — Revendique pour un DPI budésonide/formotérol un carrier lactose de
**d10 20–65 µm, d50 80–120 µm, d90 130–180 µm, fines < 10 µm : moins de 10 %**.
`INFÉRENCE HAUTE CONFIANCE` — Cette fenêtre se situe **entre SV003 et SV010** : ni l'un ni
l'autre seul n'y tombe, mais un mélange SV003/SV010 peut y tomber. Utile comme **cible
granulométrique de référence** pour un couple BUD/FOR.
⚠️ FTO : revendications liées au device Spiromax — à faire vérifier.

### D.3 Intéressants pour le mécanisme seulement

- **HU228622B1 (AstraZeneca, prio. 1997)** — formulation BUD/FOR de densité versée
  **0,30–0,36 g/mL**, obtenue par re-micronisation puis **sphéronisation** en agglomérats
  100–2000 µm (technologie Turbuhaler, sans carrier). Donne une **référence de densité** pour une
  poudre BUD/FOR, mais le procédé est hors de portée.
- Littérature « CAB » (cohesive–adhesive balance, AFM) : le budésonide micronisé est un actif
  **plutôt cohésif** (valeur CAB publiée 0,62 pour un lot d90 = 4,40 µm) → il a tendance à
  s'auto-agglomérer plutôt qu'à tapisser le lactose. Cohérent avec notre diagnostic.

### D.4 Incompatibles avec nos équipements

| Brevet / technologie | Pourquoi incompatible |
|---|---|
| Zambon (leucine + spray drying) | pas de spray dryer interne |
| AstraZeneca HU228622 / Turbuhaler | re-micronisation, sphéronisation, pas de carrier |
| Toute voie « co-micronisation » ou « particules ingéniérées » | exclue par le hand-off |

---

## E. ML001 / SV003 / SV010 — analyse comparative

`FAIT CONFIRMÉ` — Valeurs typiques, brochure DFE Pharma *Your Inhalation Grade Lactose* (#004,
mai 2020), PSD Sympatec :

| Grade | Procédé | Forme | D10 (µm) | D50 (µm) | D90 (µm) | Densité tassée (g/L) | Densité versée (g/L) | Indice de Carr |
|---|---|---|---|---|---|---|---|---|
| **Respitose® ML001** | broyé | irrégulière | **3 – 7** | 37 – 61 | 124 – 194 | 880 | **570** | **> 25 %** |
| **Respitose® SV003** | tamisé | tomahawk | 19 – 43 | 53 – 66 | 75 – 106 | 780 | 630 | **19 %** |
| **Respitose® SV010** | tamisé | tomahawk | 35 – 65 | 95 – 125 | 160 – 190 | 830 | **690** | **17 %** |
| *(repères)* ML003 | broyé | irrégulière | 1 – 6 | 20 – 50 | 65 – 140 | 850 | 560 | > 25 % |
| *(repères)* SV001 | tamisé | tomahawk | 120 – 160 | 210 – 250 | 290 – 350 | 810 | 700 | 14 % |

**Lecture** :
- **SV003** est le grade de référence mondial pour les DPI capsule (DFE : « les clients
  privilégient particulièrement SV003 »), et c'est **le carrier grossier des exemples Zambon
  budésonide/formotérol**. PSD étroite (D90/D10 ≈ 3), écoulement correct (Carr 19 %).
- **SV010** est le plus **coulant** (Carr 17 %) et le plus **dense** (690 g/L) : c'est lui qui
  donne **le meilleur taux de remplissage à 9 kg (65 %)** et la meilleure sécurité au dosator
  Modu-C. Mais D50 ≈ 110 µm et surface spécifique moindre = **moins de sites** pour un API à
  0,048 % → risque d'uniformité et de ségrégation.
- **ML001 n'est pas un carrier de remplissage** : Carr > 25 % (cohésif), densité versée la plus
  faible (570 g/L → **79 % de remplissage à 9 kg**, le pire cas). En revanche **D10 = 3–7 µm** :
  c'est le seul des trois qui apporte une **population réellement submicronique-à-fine interne**.
  → C'est notre **donneur de fines gratuit**, en minorité.

### Matrice de rôles

| Grade | Rôle possible | Avantage BUD | Avantage FOR | Risque | Utilisation proposée |
|---|---|---|---|---|---|
| **ML001** | donneur de fines / modulateur de surface | ++ (co-agglomérats BUD–fines favorables à la FPF) | + (saturation des sites de haute énergie) | écoulement dosator, chute de densité → remplissage mélangeur 79 % à 9 kg, ségrégation des fines libres | **5–10 % m/m**, pré-mélangé au carrier **avant** les APIs |
| **SV003** | carrier principal | référence publiée BUD/FOR | surface suffisante, PSD étroite | fines < 10 µm quasi absentes | **base par défaut du bulk** |
| **SV010** | carrier d'écoulement / diluant final | neutre | – (moins de sites) | uniformité FOR, ségrégation | **fraction de dilution finale** et/ou correctif d'écoulement si le Modu-C peine |

### Comparaison des combinaisons

| Système | Verdict | Motif |
|---|---|---|
| **ML001 seul** | **non** | Carr > 25 %, 79 % de remplissage à 9 kg, incompatible dosator 25 mg |
| **SV003 seul** | **oui — référence de départ** | seul grade avec précédent publié BUD/FOR ; compromis flux/surface |
| **SV010 seul** | oui, en secours | meilleur écoulement et meilleur remplissage mélangeur ; mais le plus pauvre en sites |
| **ML001 / SV003** | **oui — 1re optimisation** | apporte des fines sans achat ; densité quasi inchangée (≈ 625 g/L à 8 %) |
| **ML001 / SV010** | oui — alternative | compense la faible densité de ML001 par la plus haute (690) ; bon si le flux devient critique |
| **SV003 / SV010** | oui, mais autre finalité | élargit la PSD **sans ajouter de fines** ; permet de viser la fenêtre d10 20–65 / d50 80–120 / d90 130–180 du brevet Spiromax |
| **Ternaire ML001+SV003+SV010** | **seulement en phase 2** | justifié uniquement si l'on a besoin simultanément de fines (ML001), de sites (SV003) et d'écoulement (SV010). Ex. conceptuel : 20 SV003 / 72 SV010 / 8 ML001 |

---

## F. TOP « secret sauces », classées par niveau de preuve

### F.1 Fortement documentées (preuve directe et chiffrée)

| # | Levier | Preuve | Applicable chez nous |
|---|---|---|---|
| **S1** | **Tamiser pour fabriquer des agglomérats calibrés, puis mélanger en bas cisaillement** | US9616024 : BUD RSD 14,3 → 4,6 % ; FOR récupération 91,4 → 99,6 % | **déjà fait** — à conserver absolument |
| **S2** | **Dilution séquentielle en 3 fractions + sandwich, 15 min/étape** ; la **répartition** des fractions est un facteur | EP3175842A1 : AV de 7,1 à 12,5 selon la répartition, à actif constant | **gratuit** — passer de 3:3:3 à **7:2:1** |
| **S3** | **Prémix dédié du β2-agoniste (≈ 0,8–1 % m/m) avant toute rencontre avec le corticoïde** | US7879833/US8258124, ex. 2 et 3 (formotérol) | **cœur de la recommandation** |
| **S4** | **Carrier grossier + 4–15 % de fines (optimum ≈ 9 %)** | Zambon US10449147 : SV003 + MM3 91:9 | oui, via **ML001** d'abord (sans achat) |
| **S5** | **Les fines extrinsèques améliorent la FPF d'un budésonide cohésif** par formation d'agglomérats médicament–fines co-déposés | Kinnunen *et al.*, Int J Pharm 2015;478:53-59 (NGI, Cyclohaler 90 L/min) | oui — explique pourquoi les fines aident **BUD** |
| **S6** | **15 min en tumbler est un optimum, pas un minimum** ; au-delà la FPF baisse | US9616024 ex. 6 ; PLOS One 2013 (Turbula 90 rpm, 0,5–780 min) | **ne pas allonger** ; mesurer |

### F.2 Prometteuses (mécanisme solide, preuve indirecte sur notre couple)

| # | Levier | Base | Statut |
|---|---|---|---|
| **S7** | **Ne jamais laisser les deux APIs micronisés se toucher à l'état pur** | co-agglomération observée sur un couple corticoïde/β2 analogue (Raman) | à tester — **L2 vs L1** |
| **S8** | **Ordre d'ajout du ternaire** : fines + carrier d'abord, actif ensuite, à faible concentration d'actif | littérature ordre de mélange (30 min : FPF supérieure avec fines+carrier d'abord) | à tester — **L4** |
| **S9** | **Piloter le taux de remplissage du mélangeur plutôt que la masse** au scale-up | mécanique des tumblers, densités versées mesurées | à appliquer — voir §O |
| **S10** | **Contrôle de l'humidité relative** de la salle de mélange (fenêtre resserrée) | le lactose est décrit comme « capteur d'eau libre » protégeant le formotérol (brevets Zambon) ; FOR sensible à l'humidité | à instrumenter, pas à optimiser tout de suite |

### F.3 Spéculatives (à ne tester qu'en dernier)

| # | Levier | Pourquoi en dernier |
|---|---|---|
| S11 | **Deux carriers distincts, un par API** | crée deux populations de PSD/densité → moteur de ségrégation (désaccord D5) |
| S12 | **Stéarate de magnésium** | change la stabilité, le mouillage et le dossier ; l'ordre d'ajout est critique (fines puis MgSt : FPF 46,6 % ; MgSt puis fines : 33,9 %) |
| S13 | **Période de relaxation** avant remplissage | plausible (décharge électrostatique), aucune donnée chiffrée sur BUD/FOR |
| S14 | **Leucine** | **inapplicable** sans spray drying |

---

## G. TOP 3 architectures de bulk

Comparaison complète des 7 architectures (A → G) : `docs/06-protocole-lots.md`.

### 🥇 Architecture B — « Prémix formotérol + 7:2:1 » (recommandée)

```
Étape 0  Prémix FOR :  FOR (4,32 g pour 9 kg) + ~1 % de lactose (≈ 430 g)
         → sandwich lactose/FOR/lactose → mélange → TAMISAGE → mélange court
Étape 1  1re fraction = 70 % du lactose (6,3 kg, dont le prémix)
         → prémix FOR incorporé, puis BUD déposé en couche SÉPARÉE, recouvert de lactose
         → mélange 5 min → Russell 250 µm → Inversina 15 min
Étape 2  + 20 % du lactose (1,8 kg) → mélange → Russell 250 µm → Inversina 15 min
Étape 3  + 10 % du lactose (0,9 kg) → mélange → Russell 250 µm → Inversina 15 min
```
- **Mécanisme** : la désagglomération du formotérol est faite **seule**, concentrée et tamisée,
  avant que le budésonide (17–33× sa masse) ne puisse le capturer ; la distribution est ensuite
  faite en douceur sur un grand lit.
- **Avantages** : aucun achat, aucun équipement, **même nombre d'étapes Inversina** ; l'étape la
  plus mal placée mécaniquement (71 % de remplissage) n'a plus que 10 % de la masse à incorporer.
- **Risques** : une manipulation supplémentaire (le prémix) ; pesée de 4,32 g de FOR à contrôler ;
  bilan matière du prémix à surveiller.
- **Scale-up** : excellent, la logique 7:2:1 est identique à 3, 6 et 9 kg.
- **Compatibilité Inversina/Russell** : totale.

### 🥈 Architecture D — « Double prémix »

Prémix FOR (≈ 1 %) **et** prémix BUD (≈ 10–20 %) préparés séparément, puis combinés dans le
lactose de dilution.
- **Avantages** : sépare totalement les deux APIs ; chaque prémix peut être contrôlé à l'assay
  avant combinaison (un point de contrôle qualité gratuit, très précieux en cas de litige).
- **Risques** : deux manipulations supplémentaires ; le prémix BUD concentré est très cohésif ;
  temps opérateur.
- **Verdict** : **la meilleure architecture si l'on veut de la robustesse plutôt que de la
  simplicité**. À retenir si B est insuffisante, ou d'emblée si l'atelier accepte la charge.

### 🥉 Architecture F+B — « Carrier pré-conditionné puis prémix FOR »

Le carrier est d'abord préparé seul : SV003 + 5–10 % ML001, mélangé et tamisé, **avant** tout API.
Puis architecture B.
- **Mécanisme** : les fines saturent les sites de haute énergie et s'intercalent entre les
  particules d'API, ce qui limite les contacts API–API ; elles favorisent en outre les
  co-agglomérats BUD–fines qui améliorent la FPF du budésonide (S5).
- **Risques** : chute de densité versée (→ remplissage mélangeur), écoulement dosator, fines
  libres ségrégeantes.
- **Verdict** : **la première optimisation à faire si B donne une bonne CU mais une FPD faible.**

---

## G-bis. Focus Formotérol 12 µg (0,0480 % m/m)

`calcul interne` — 12 µg dans 25,0 mg = **0,0480 % m/m** de formotérol fumarate dihydraté
(à corriger du titre réel). Par lot : **1,44 g** à 3 kg, **2,88 g** à 6 kg, **4,32 g** à 9 kg.

| Stratégie | Homogénéité probable | Risque de pertes | Scale-up | Ségrégation | Compatibilité procédé |
|---|---|---|---|---|---|
| **Addition directe** (pas de prémix) | mauvaise dès qu'un 2e API est présent | élevé (pesée de 1,4 g, électrostatique) | mauvais | élevée | oui mais déconseillé |
| **Prémix ≈ 1 % m/m** (Nycomed ex. 3 : 0,82 %) | **bonne** | **faible** (le FOR est confiné dans le lactose immédiatement) | **excellent** (concentration constante à toute échelle) | faible | **oui — recommandé** |
| **Dilution géométrique** (doublements successifs) | bonne | moyen (multiplie les transferts) | lourd | faible | oui mais 5–6 manipulations |
| **Dilution sérielle** (prémix du prémix) | bonne | moyen | bon | faible | réservé si le prémix 1 % échoue |
| Prémix sur **ML001** | meilleure désagglomération (fines + surface) | moyen (cohésif, colle aux parois) | moyen | fines libres | **oui pour le prémix uniquement** |
| Prémix sur **SV003** | bonne | faible | bon | faible | **option par défaut** |
| Prémix sur **SV010** | la moins bonne (peu de sites) | faible | bon | moyenne | non recommandé pour le prémix |
| Prémix **enrichi en fines** (SV003 + 10 % ML001) | la meilleure attendue | moyen | bon | moyenne | **option de phase 2** |
| **Double prémix** | la meilleure | moyen | bon | faible | architecture D |

**Recommandation** : **prémix formotérol à 1,0 % m/m sur SV003**, sandwiché, tamisé, ré-homogénéisé.
Pour un lot de 9 kg : 4,32 g de FOR + 427,7 g de SV003 = 432,0 g de prémix (soit 4,8 % du lot).
Pour 3 kg : 1,44 g + 142,6 g = 144,0 g.

**Protections spécifiques au formotérol, à écrire dans le dossier de lot :**
1. **Pesée** : pesée par différence, contenant en verre ou inox mis à la terre ; ne jamais
   transvaser le FOR pur dans un sac plastique.
2. **Électrostatique** : ioniseur ou barre antistatique au poste de pesée ; HR de salle
   documentée à chaque lot (voir Q6).
3. **Bilan matière obligatoire** à chaque tamisage (pesée entrée/sortie, ±0,5 %) — c'est le
   test le moins cher pour détecter une perte préférentielle.
4. **Échantillonnage à l'échelle de la dose** : 25 mg (ou 1 à 3 doses), **jamais 1 g**.
5. **Rinçage analytique du matériel** du prémix sur le premier lot, pour quantifier l'adsorption.

---

## G-ter. Compétition Budésonide / Formotérol — réponses

**1. BUD et FOR peuvent-ils se concurrencer ?**
`INFÉRENCE HAUTE CONFIANCE` — **Oui, et c'est même mécaniquement inévitable.** La saturation des
sites de haute énergie du carrier est le mécanisme d'action reconnu des composants ternaires ;
un deuxième API se comporte comme un composant ternaire massif. Avec un rapport de masse de
16,7:1 (dosage 200) à 33,3:1 (dosage 400), **le budésonide gagne la compétition de sites par
simple effet de masse**.
Mais l'observation publique va dans un sens favorable : sur le produit brésilien en capsule
unique, la **FPF du formotérol (56 %) dépasse celle du budésonide (45 %)** et dépasse celle du
formotérol en capsule séparée (52 %) `FAIT CONFIRMÉ`. Autrement dit, quand la compétition a lieu
**sur le carrier**, elle **profite** au formotérol (il occupe des sites plus faibles, donc il se
détache mieux).
**Le danger n'est donc pas la compétition de sites : c'est la compétition qui a lieu ailleurs
que sur le carrier**, c'est-à-dire l'agglomération mutuelle des deux poudres micronisées.

**2. Peut-on réduire cette compétition avec deux prémix ?**
Non — on ne la **réduit** pas, on la **réordonne**, ce qui est mieux. Les deux prémix
garantissent que chaque API rencontre d'abord le **lactose** et non l'autre API. La compétition
de sites a ensuite lieu, mais entre deux populations déjà désagglomérées et déjà fixées.
→ **C'est l'objectif recherché.**

**3. Peut-on utiliser deux populations de lactose différentes ?**
Techniquement oui, mais `INFÉRENCE FAIBLE CONFIANCE` sur le bénéfice, et risque avéré :
deux populations de PSD/densité différentes dans un même bulk percolent et ségrégent au
transfert et au dosator. **Repoussé en phase 2** (désaccord D5 dans `AGENTS.md`), et seulement
avec des grades granulométriquement proches (SV003/SV010 et non ML001/SV010).

**4. Faut-il combiner les APIs tardivement ?**
**Oui.** C'est la conclusion la plus solide de toute l'analyse : plus la rencontre BUD/FOR est
tardive, moins il y a d'étapes de mélange partagées, moins il y a de *press-on forces* cumulées
et moins il y a d'occasions de co-agglomération. Les deux brevets qui traitent explicitement
d'une association corticoïde + formotérol en poudre sèche (Nycomed ex. 2 et 3) font
**exactement cela**.

---

## H. Premier lot à fabriquer — recommandation

> **L0 — Qualification du prémix formotérol seul.** À faire **avant** tout lot combiné.

| | |
|---|---|
| **Hypothèse testée** | « Un prémix FOR à 1 % m/m, sandwiché puis tamisé à 250 µm, atteint RSD ≤ 5 % à l'échelle de 25 mg. » |
| **Pourquoi en premier** | Si le prémix seul n'est pas homogène, **aucune architecture combinée ne le sera**. C'est l'expérience qui élimine le plus d'hypothèses par gramme d'API consommé. Ce n'est pas un « mini-lot » non représentatif : c'est **l'étape réelle du procédé**, à son échelle réelle. |
| **Taille** | 432 g (échelle prémix d'un lot 9 kg) ou 144 g (échelle 3 kg) |
| **Composition** | FOR 4,32 g + SV003 428 g (ou 1,44 g + 143 g) |
| **Procédé** | sandwich SV003 / FOR / SV003 → mélange 3–5 min → tamisage (250 µm ; **et en parallèle un tamis manuel 212 µm sur une aliquote**) → Inversina 15 min |
| **Réponses** | assay FOR, **RSD sur 10 prises de 25 mg**, bilan matière avant/après tamisage, rinçage du matériel, densités versée/tassée |
| **GO** | RSD ≤ 5 %, teneur 95–105 %, bilan matière ≥ 99 % |
| **NO-GO** | RSD > 8 % → **arrêt** : problème amont (PSD/état d'agglomération de l'API) → réunion fournisseur avant tout lot combiné (critère d'arrêt n°1 de `GOAL.md`) |
| **Coût** | ≈ 4 g de formotérol, une demi-journée |

> **L1 et L2 sont ensuite lancés en parallèle** (même journée, même opérateur, même lot de lactose) :
> **L1 = benchmark historique** (architecture A, co-sandwich, 3:3:3) et **L2 = architecture B**
> (prémix FOR + 7:2:1). Sans L1, on ne pourra pas prouver que l'on a résolu quoi que ce soit.

Les deux sont faits à **3 kg** et au dosage **12/400**, qui est le **pire cas** pour le formotérol
(c'est là que le rapport de masse BUD:FOR est maximal, 33:1).

---

## I. Lots 2 à 6 — plan conditionnel

Protocoles détaillés : `docs/06-protocole-lots.md`.

| Lot | Architecture | Hypothèse testée | Lancé si… |
|---|---|---|---|
| **L1** | A — co-sandwich, 3:3:3, SV003 | « Le problème se reproduit-il à 3 kg ? » | toujours (benchmark) |
| **L2** | B — prémix FOR, 7:2:1, SV003 | « Séparer les APIs + recharger la 1re fraction suffit » | toujours |
| **L3** | C — BUD/carrier d'abord, **prémix FOR ajouté en dernier**, 7:2:1 | tranche le désaccord D2 : quel API doit toucher le carrier en premier | si L2 ne donne pas RSD FOR ≤ 5 % **ou** si la FPD FOR de L2 est faible |
| **L4** | F+B — carrier pré-conditionné SV003 + 8 % ML001, puis B | « Les fines corrigent la FPD (et/ou la CU) » | si CU bonne mais **FPD faible** (l'un ou l'autre API) |
| **L5** | B sur **SV010** ou SV003/SV010 50:50 | « Le carrier est-il un facteur, et le flux dosator est-il tenable ? » | si écoulement/remplissage problématique, ou si L2 est bon et qu'on veut un plan B industriel |
| **L6** | Meilleure architecture, **6 kg puis 9 kg** | « L'architecture survit-elle au taux de remplissage industriel ? » | dès qu'un lot 3 kg passe les gates 1 et 2 |

**Étude cinétique de mélange : embarquée dans L2, pas de lot dédié.** Prélèvements à **5, 10,
15 et 25 min** à l'étape finale (10 positions à chaque temps). Coût marginal : des analyses, pas
un lot.

---

## J. Taille de lot — 3 kg, 6 kg ou 9 kg ?

`calcul interne` (densités versées DFE) :

| Masse | SV003 (630 g/L) | SV010 (690 g/L) | ML001 (570 g/L) |
|---|---|---|---|
| 3 kg | 4,8 L → **24 %** | 4,3 L → 22 % | 5,3 L → 26 % |
| 6 kg | 9,5 L → **48 %** | 8,7 L → 43 % | 10,5 L → 53 % |
| 9 kg | 14,3 L → **71 %** | 13,0 L → 65 % | 15,8 L → **79 %** |

**Conclusion en trois points :**

1. **3 kg est la bonne échelle de screening d'architecture** — procédé connu, consommation d'API
   faible (1,44 g FOR + 48 g BUD par lot), et surtout **les variables testées (ordre, prémix,
   carrier) sont indépendantes de l'échelle**.
2. **3 kg n'est PAS représentatif de la mécanique de mélange à 9 kg** (24 % contre 71 % de
   remplissage). Il ne faut donc **jamais** conclure « ça marche » à partir de 3 kg seuls, ni
   conclure « ça ne marche pas » à 9 kg sans avoir regardé le remplissage.
3. **6 kg est la taille la plus intéressante industriellement** (43–48 % de remplissage, la zone
   favorable d'un tumbler). `RECOMMANDATION` : si le 9 kg reste marginal après correction de la
   répartition, **figer la taille industrielle à 6 kg** plutôt que de dégrader la formule — la
   perte de productivité est très inférieure au coût d'un problème d'uniformité récurrent.

⚠️ **Ne pas descendre sous 3 kg** pour un lot d'architecture. En revanche, le **prémix** (L0)
est fait à sa taille réelle (144–432 g) : ce n'est pas une réduction d'échelle, c'est l'étape
elle-même.

**Astuce de représentativité** `RECOMMANDATION` : si l'Inversina accepte des **cuves
interchangeables**, faire le screening 3 kg dans une cuve de **6–8 L** (→ 60–80 % de remplissage)
reproduit la mécanique du 9 kg pour un sixième de l'API. À vérifier auprès du fournisseur
(question Q5).

---

## K. Procédé proposé — étape par étape (architecture B, lot 9 kg, dosage 12/400)

Quantités `calcul interne` : lactose total 8 851,7 g · BUD 144,0 g · FOR 4,32 g (à corriger du titre).

**Étape 0 — Prémix formotérol (432 g)**
1. Peser 427,7 g de SV003 ; en déposer **la moitié** dans la cuve de prémix.
2. Déposer les **4,32 g de FOR** au centre, sans contact avec les parois.
3. Recouvrir avec l’autre moitié du SV003 (**sandwich**).
4. Mélange doux 3 min.
5. **Tamisage** (Russell 250 µm ; tamis manuel plus fin si disponible sur cette petite masse).
6. Inversina **15 min**. → *Contrôle : assay FOR + RSD sur 10 × 25 mg. GO si RSD ≤ 5 %.*

**Étape 1 — Première fraction : 70 % du lactose (6 196 g au total avec le prémix)**
7. Déposer ≈ 2 900 g de SV003 dans la cuve principale.
8. Étaler **la totalité du prémix FOR** (432 g) en couche régulière.
9. Recouvrir de ≈ 1 000 g de SV003 — **couche barrière** : le budésonide ne doit jamais toucher
   le prémix formotérol à l'état non dilué.
10. Étaler la **totalité du BUD** (144,0 g) en couche régulière.
11. Recouvrir avec le reste de la première fraction (≈ 1 868 g).
12. Mélange initial 5 min (Inversina).
13. **Russell 250 µm.**
14. **Inversina 15 min.**

**Étape 2 — Deuxième fraction : 20 % du lactose (1 770 g)**
15. Ajouter la fraction. 16. Mélange 3 min. 17. **Russell 250 µm.** 18. **Inversina 15 min.**

**Étape 3 — Troisième fraction : 10 % du lactose (885 g)**
19. Ajouter la fraction. 20. Mélange 3 min. 21. **Russell 250 µm.** 22. **Inversina 15 min.**
→ **Le procédé ne se termine jamais par un tamisage.**

**Contrôles en cours** : bilan matière à chaque tamisage ; HR et température de salle à chaque
étape ; prélèvements de l'étude cinétique à l'étape 3 sur le lot L2.

**Transposition 3 kg** : prémix 144,0 g (FOR 1,44 g + SV003 142,6 g) ; fractions 2 065 / 590 / 295 g.
**Transposition 12/200** : BUD 72,0 g, lactose total 8 923,7 g, tout le reste inchangé.

---

## L. Tamisage — décision étape par étape

| Étape | Bénéfice | Risque | Pertes | Effet sur l'ordered mixture | **Décision** |
|---|---|---|---|---|---|
| **Lactose seul (avant APIs)** | dé-mottage, casse les agglomérats de fines si ML001 est présent | quasi nul | négligeables | neutre | **OUI**, systématique si ML001 ou fines sont utilisés ; optionnel sinon |
| **API pur (BUD ou FOR seul)** | calibre les agglomérats (US9616024) | **exposition opérateur, électrostatique, pertes élevées** sur 4,3 g de FOR | fortes | — | **NON au Russell.** Tamiser l'API **dans son sandwich de lactose**, jamais seul |
| **Prémix FOR** | **critique** — c'est là que se joue la taille des entités FOR | faible | à mesurer (bilan matière) | favorable | **OUI, impératif** ; utiliser la maille la plus fine disponible sur cette petite masse (212 µm si possible) |
| **Prémix BUD** (architecture D) | casse les agglomérats cohésifs de BUD | faible | faibles | favorable | **OUI** |
| **Mélange intermédiaire** (après fractions 1 et 2) | désagglomération continue, c'est le mécanisme S1 | faible | faibles | favorable | **OUI** — c'est l'acquis du procédé historique, à conserver |
| **Bulk final** | gain d'homogénéité documenté (RSD 4,6 → 1,5 % avec tamisage final) | un tamis **classe** : il peut retenir des fines et défaire l'ordered mixture ; il re-génère de la ségrégation par taille à la sortie | faibles mais réelles | **défavorable si c'est la dernière opération** | **OUI mais jamais en dernier** : tamiser puis **ré-homogénéiser 15 min** |

**Test le moins cher pour trancher le débat « le tamisage est-il destructeur ? »** (désaccord D3) :
sur le lot L2, prélever **avant** et **après** le tamisage de l'étape 3 → assay des deux APIs +
RSD + bilan matière. Deux analyses supplémentaires répondent définitivement.

---

## M. Stratégie de temps de mélange

**État de l'art** `FAIT CONFIRMÉ` :
- plateforme publiée : **15 min par étape** en tumbler (Turbula 22 rpm) ;
- optimum mesuré en tumbler : **15 min** ; au-delà, la FPF **diminue** (US9616024, salbutamol) ;
- trois processus se superposent : **désagglomération (0–10 min)**, **compression de l'API sur le
  carrier / press-on (0–60 min)**, **ré-agglomération (> 60 min)** ; l'essentiel de l'évolution
  se joue dans les **120 premières minutes** (PLOS One 2013).

**Notre situation** : 3 × 15 min = **45 min cumulées** — dans le régime des press-on forces, mais
loin du régime destructeur. **Il n'y a pas lieu d'allonger. La question est de savoir si l'on peut
raccourcir.**

**Mini-étude, embarquée dans L2, étape 3 :**

| Temps | Prélèvements | Ce qu'on lit |
|---|---|---|
| **5 min** (précoce) | 10 positions | la désagglomération est-elle déjà faite ? |
| **10 min** | 10 positions | pente de la courbe d'homogénéisation |
| **15 min** (référence) | 10 positions | valeur du procédé actuel |
| **25 min** (tardif) | 10 positions | signe d'un sur-mélange (RSD stable mais FPD qui baisse) |

Analyses : assay BUD + FOR à chaque temps ; **NGI uniquement à 15 et 25 min**, pour détecter la
perte de FPD par press-on sans exploser le budget analytique.

**Lecture** : si RSD(10 min) ≈ RSD(15 min) et FPD(25) < FPD(15) → **raccourcir à 10 min par étape**,
ce qui retire 15 min de temps de contact par lot et réduit le risque de press-on. Aucune durée
n'est proposée en dehors de ce qui est mesuré.

---

## N. Analyses — les quatre portes GO / NO-GO

**Principe** : ne jamais envoyer un mauvais mélange en NGI. Le NGI est la ressource rare.

| Gate | Analyses | Critères GO | Si NO-GO |
|---|---|---|---|
| **Gate 1 — Homogénéité** | assay BUD et FOR ; **10 positions × 25 mg** (haut/milieu/bas × paroi/centre + fond de cuve) ; RSD par API ; cartographie spatiale | teneur **95–105 %** ; **RSD ≤ 5 %** pour les deux APIs ; aucun point hors 90–110 % | ne pas poursuivre le lot ; voir arbre de décision |
| **Gate 2 — Aptitude poudre** | densité versée/tassée, **Carr**, **Hausner**, écoulement ; **test de ségrégation** (vibration contrôlée ou tamisage-fractionnement, assay FOR par fraction) | Carr ≤ 25 % ; pas de dérive d'assay FOR > 10 % entre fractions | corriger le carrier (L5) avant tout essai de remplissage |
| **Gate 3 — Remplissage** | essai Modu-C MS, **25 mg**, capsule taille 3 ; masse de remplissage (RSD), **dose délivrée** (UDD, Ph. Eur. 2.9.18) sur le dispositif type Aerolizer | RSD masse ≤ 3 % ; dose délivrée ≥ **70 %** de la dose mesurée ; UDD conforme | revenir au carrier/flux (SV010), pas à l'architecture |
| **Gate 4 — Aérodynamique** | **NGI**, débit fixé pour ΔP = 4 kPa (Ph. Eur. 2.9.18) ; FPD et FPF **par API** ; MMAD ; GSD | **FPF ≥ 30 %** pour les deux APIs en screening (cible marché 45–56 %) ; MMAD 2–4 µm | voir arbre de décision §N.2 |

**Méthode analytique** : dosage simultané BUD + FOR par HPLC-UV. `calcul interne` — 12 µg de FOR
dans 25 mg extraits dans 5 mL donnent **2,4 µg/mL**, parfaitement dosable ; **la contrainte n'est
pas la sensibilité, c'est la taille de la prise d'essai**. Voir `docs/annexes/A3-plan-analytique.md`.

### N.2 — Arbre de décision

```
Gate 1 : RSD ?
├─ FOR NON homogène (RSD > 5 %)
│   ├─ et BUD homogène  ──────────► problème SPÉCIFIQUE bas dosage
│   │                               → renforcer le prémix FOR : dilution sérielle,
│   │                                 tamis plus fin, prémix enrichi en fines (ML001)
│   │                                 [L3 puis L4]
│   └─ et BUD aussi NON homogène ─► problème de MÉLANGE, pas de formulation
│                                   → taux de remplissage, nb de révolutions, répartition
│                                     des fractions  [§O]
├─ BUD NON homogène, FOR homogène ► agglomérats de budésonide
│                                   → prémix BUD dédié (architecture D) + tamisage amont
└─ Les deux homogènes ────────────► Gate 2 puis 3 puis 4

Gate 4 : FPD ?
├─ CU bonne mais FPD FOR faible ──► carrier / fines : ajouter 5–10 % ML001 [L4]
│                                   (les fines saturent les sites forts et libèrent le FOR)
├─ FPD FOR bonne mais FPD BUD faible ► compétition / agglomérats de BUD
│                                   → fines extrinsèques (S5) + prémix BUD séparé
├─ Les DEUX FPD faibles ──────────► architecture de carrier ou interface device
│                                   → vérifier d'abord la capsule/le device et le débit,
│                                     puis passer à un couple carrier+fines [L4, L5]
└─ Les deux FPD bonnes ───────────► scale-up [§O]

Scale-up :
├─ 3 kg bon, 9 kg mauvais ────────► mécanique de mélange : taux de remplissage (71–79 %),
│                                   nb de révolutions, répartition 7:2:1
│                                   → si non résolu : figer la taille industrielle à 6 kg
└─ avant tamisage bon / après tamisage mauvais ► tamisage destructeur
                                    → réduire le nombre de passages, ne jamais finir
                                      sur un tamisage, vérifier le bilan matière
```

---

## O. Plan de scale-up 3 → 6 → 9 kg

**Principe directeur : ne pas raisonner en masse, raisonner en taux de remplissage et en nombre
de révolutions.** La proportionnalité simple est ce qui a fait échouer le passage direct à 9 kg.

| Paramètre | 3 kg | 6 kg | 9 kg | À maintenir ou recalculer |
|---|---|---|---|---|
| **Taux de remplissage** (SV003) | 24 % | 48 % | **71 %** | **facteur critique n°1** — à mesurer réellement sur le bulk (densité versée du mélange, pas du lactose seul) |
| **Répartition des fractions** | 7:2:1 | 7:2:1 | 7:2:1 | **maintenu** (sans dimension) |
| **Concentration du prémix FOR** | 1 % | 1 % | 1 % | **maintenue** (sans dimension) |
| **Vitesse Inversina (rpm)** | X | X | X | **maintenue** (donnée Q5 à récupérer) |
| **Nombre de révolutions** (rpm × t) | N | N | **≥ N, à confirmer** | à **recalculer** si le remplissage dépasse ~55–60 % |
| **Temps par étape** | 15 min | 15 min | **15 min, à challenger** | issu de la cinétique L2 et, si besoin, d'une cinétique refaite à 9 kg |
| **Temps de séjour / transferts** | 3 étapes | 3 étapes | 3 étapes | **maintenu** |
| **Tamisage** | 3 passages | 3 passages | 3 passages | **maintenu** ; débit Russell à vérifier à 9 kg (Q7) |
| **Échantillonnage** | 10 pts × 25 mg | 10 pts × 25 mg | **15 pts × 25 mg** | **augmenté** : un lit plus profond exige plus de points, surtout au fond de cuve |

**Séquence recommandée :**
1. Architecture figée à **3 kg** (L1 → L2/L3, éventuellement L4).
2. **6 kg** : confirmation dans la zone favorable de remplissage (48 %). C'est ici que l'on vérifie
   que l'architecture tient à un lit deux fois plus profond, sans encore affronter la haute charge.
3. **9 kg** : c'est un **essai de robustesse mécanique**, pas un essai de formulation. Si le 9 kg
   échoue alors que le 6 kg passe, la conclusion est **mécanique** (remplissage, révolutions) et
   non formulatoire. Deux parades, dans l'ordre :
   a. augmenter le nombre de révolutions **de la seule étape 3** (celle à 71 %) ;
   b. si insuffisant : **figer la taille industrielle à 6 kg**.
4. **Piège identifié** `calcul interne` : si l'on ajoute 8–10 % de ML001 (densité versée 570 g/L),
   le volume du lot 9 kg augmente et le remplissage passe de 71 % à ~72–74 % (et à 79 % pour un
   bulk ML001-dominant). **Toute décision d'ajouter des fines doit être re-vérifiée sur le taux de
   remplissage, pas seulement sur la FPF.**

**Échantillonnage au scale-up** : sonde voleuse, 10 (3 kg) à 15 (9 kg) positions couvrant
haut/milieu/bas × paroi/centre **et le fond de cuve**, prises de **25 mg (1 dose)** ou 75 mg
(3 doses) — jamais des prises de l'ordre du gramme, qui masquent mathématiquement l'hétérogénéité
que l'on cherche à mesurer.

---

## P. Achats — maintenant / plus tard / inutile

### Maintenant (faible coût, fort effet de levier)

| Article | Pourquoi | Priorité |
|---|---|---|
| **Sonde voleuse (thief) adaptée à des prises de 25–75 mg** | sans elle, le Gate 1 n'est pas mesurable ; c'est probablement l'angle mort historique | **1** |
| **Tamis manuels 150 et 212 µm** (usage prémix uniquement) | un agglomérat de 250 µm porte 27–41 % d'une dose de FOR ; à 150 µm il n'en porte plus que 6–9 % | **2** |
| **Barre/soufflette antistatique au poste de pesée** | 4,3 g de FOR micronisé, pesée et transfert | **3** |
| **Thermohygromètre enregistreur en salle de mélange** | rend la variabilité inter-lots interprétable au lieu d'être subie | **3** |
| **Échantillons gratuits de fines DFE** (LH230 et/ou LH300) | pas un achat : un échantillonnage fournisseur, à demander dès maintenant pour ne pas attendre 8 semaines le jour où on en aura besoin | **2** |

### Plus tard (seulement si une porte le déclenche)

| Grade | Fabricant | PSD | Morphologie | Fonction apportée | Problème qu'il résout | Priorité |
|---|---|---|---|---|---|---|
| **Lactohale® LH230** | DFE Pharma | D10 1–3 / D50 < 10 / D90 < 30 µm | fine, micronisée | **vraies fines respirables** — absentes des trois grades disponibles (ML001 ne descend qu'à D10 3–7 µm) | FPD faible malgré une CU correcte (co-agglomérats médicament–fines, S5) | **1** |
| **Lactohale® LH210 ou LH220** | DFE Pharma | D50 14–19 / 11–15 µm | fine | **fines « non respirables »** : saturent les sites actifs **sans** contribuer à la FPD ni modifier le MMAD | uniformité/ségrégation du FOR sans perturber l'APSD | 2 |
| **Respitose® SV001** | DFE Pharma | D50 210–250 µm, Carr 14 % | tomahawk grossier | **squelette très coulant** | uniquement si le dosator Modu-C n'arrive pas à un RSD de masse acceptable à 25 mg | 3 |

> Règle : **aucun de ces grades ne doit être commandé avant qu'une porte GO/NO-GO ne l'ait
> explicitement déclenché.** L'espace ML001/SV003/SV010 doit être épuisé d'abord.

### Excipients supplémentaires — branche de secours uniquement

| Excipient | Mécanisme | Bénéfice | Risque | Stabilité | Réglementaire | Preuve sur BUD/FOR | Classement |
|---|---|---|---|---|---|---|---|
| **Stéarate de magnésium** | agent de contrôle des forces, revêtement partiel du carrier | ↑ FPF, ↓ adhésion | l'**ordre d'ajout est critique** (fines puis MgSt : FPF 46,6 % ; MgSt puis fines : 33,9 %) ; sur-mélange délétère | modifie le mouillage ; à surveiller sur 24 mois | **précédent solide** : Seebri®/Ultibro® Breezhaler = lactose ~23,5–23,6 mg + MgSt en capsule `FAIT CONFIRMÉ` | **rescue option** |
| **Leucine** | modificateur de surface | ↑ dispersibilité | — | — | — | utilisée **uniquement en spray drying** dans les brevets BUD/FOR (Zambon) | **non applicable** (pas de spray dryer) |
| Autres (phospholipides, acides aminés) | — | — | — | — | dossier lourd | aucune | **non nécessaire** |

### Inutile (à refuser explicitement)

Jet mill · broyeur à jet d'air · co-micronisation · spray dryer · **mélangeur à haut cisaillement**
(US9616024 démontre précisément qu'il est **inutile** pour le budésonide dès lors que l'on tamise
pour former des agglomérats calibrés) · nouveau mélangeur.

---

## Q. Données manquantes — ce qui bloque quoi

Liste vivante et propriétaires : `memory/questions-ouvertes.md`.

| # | Donnée manquante | Bloque | Criticité |
|---|---|---|---|
| **Q1** | **PSD des deux APIs (D10/D50/D90)** + surface spécifique | le calibrage de l'agglomération, le choix des fines, la prédiction de la FPD | **haute** (mais n'empêche pas L0/L1/L2) |
| **Q2** | **Titre exact du formotérol** (fumarate dihydraté vs base ; facteur de correction) | la pesée de 4,32 g et tous les assays | **haute** — à obtenir avant L0 |
| **Q3** | **Que s'est-il exactement passé en 2009-20xx sur le combiné 9 kg ?** assay ? RSD ? quel API ? avant ou après tamisage ? combien de lots ? | tout le diagnostic — c'est la donnée la moins chère et la plus informative du projet | **très haute** |
| **Q4** | **Quelle était la masse de prise d'essai historique** pour l'homogénéité ? | si c'était ~1 g, le « bon » résultat des mono-produits est peut-être un artefact | **très haute** |
| **Q5** | **Fiche Inversina** : vitesse(s), cuves interchangeables disponibles, taux de remplissage recommandé par le fabricant | tout le §O ; et la possibilité de screener à 3 kg dans une petite cuve | **haute** |
| **Q6** | **HR et température** de la salle de mélange (historique et actuelles) | l'interprétation de la variabilité inter-lots ; sensibilité du FOR à l'eau | moyenne |
| **Q7** | **Configuration exacte du Russell** (type d'agitateur, débit, matériau), pertes typiques | le §L et le bilan matière | moyenne |
| **Q8** | **Analyse de liberté d'exploitation** sur EP3175842A1 et US11642475 (antériorité d'usage interne ?) | une éventuelle revendication ; **pas** le développement | moyenne |
| **Q9** | **Teneur en eau** des trois grades de lactose et conditions de stockage | stabilité 24 mois, cohésion | basse |
| **Q10** | **Référence exacte du dispositif** « Aerosolizer » disponible (RS01 modèle ?), sa résistance | le débit de test NGI (ΔP = 4 kPa) | moyenne — avant Gate 4 |

**Règle appliquée** : aucune de ces questions n'empêche de lancer **L0, L1 et L2**, sauf **Q2**
(titre du formotérol), indispensable avant toute pesée.

---

## R. Conclusion

### La question posée

> *Quelle modification minimale de notre procédé historique et de notre architecture
> lactose/prémix offre la meilleure probabilité de réussir un bulk Budésonide/Formotérol combiné,
> sans jet milling ni équipement lourd supplémentaire ?*

### La réponse

**Trois modifications, aucune ne coûte un euro d'investissement, aucune n'ajoute une étape
d'Inversina.**

**1. Ne plus jamais mettre les deux APIs dans le même sandwich.**
Fabriquer d'abord un **prémix formotérol à ≈ 1 % m/m** (4,32 g de FOR dans 427,7 g de lactose pour
un lot de 9 kg), sandwiché, **tamisé**, ré-homogénéisé. Ce prémix est ensuite incorporé au lactose,
et le budésonide n'est déposé qu'**après**, séparé du prémix par une couche de lactose.
*Pourquoi* : le budésonide représente 17 à 33 fois la masse du formotérol ; dans un sandwich
commun, le formotérol cesse d'être distribué par le lactose et devient un passager des agglomérats
de budésonide. C'est l'architecture exacte des seuls brevets qui traitent d'une association
corticoïde + formotérol en poudre sèche (Nycomed/Covis, exemples 2 et 3 — prémix formotérol à
0,82 % m/m).

**2. Répartir le lactose en 7 : 2 : 1 au lieu de 3 : 3 : 3.**
*Pourquoi* : c'est la seule variable de procédé pour laquelle il existe une **donnée publique
chiffrée sur un actif à faible dose** (EP3175842A1, 0,41 % m/m : AV 7,1 en 7:2:1 contre 12,5 en
5:1:4), **et** c'est la modification qui réduit de 33 % à 10 % la masse que doit incorporer
l'étape finale — celle qui travaille à **71 % de remplissage du mélangeur**, donc dans les plus
mauvaises conditions mécaniques du procédé. Une seule modification corrige deux causes racines.

**3. Ne jamais terminer le procédé par un tamisage.**
Conserver les trois tamisages à 250 µm (ils sont le mécanisme qui rend le mélange bas cisaillement
suffisant : RSD budésonide 14,3 % → 4,6 %, récupération formotérol 91,4 % → 99,6 %), mais toujours
les faire suivre d'une ré-homogénéisation — un tamis est aussi un classificateur granulométrique.

### Ce qui reste inchangé

Le sandwich, les trois fractions, le Russell 250 µm, l'Inversina, les 15 minutes par étape,
SV003 comme carrier, le lactose comme unique excipient, 25 mg par capsule. **Le procédé
historique n'était pas mauvais : il était mono-API.**

### Ce que l'on saura, et quand

- Après **L0** (un prémix, ~4 g de formotérol, une demi-journée) : si le problème est amont ou non.
- Après **L1 + L2** (deux lots de 3 kg, une semaine) : si l'architecture résout le problème, et si
  le problème existait seulement à 9 kg.
- Après **L6** (6 puis 9 kg) : si le produit est industrialisable tel quel ou s'il faut figer la
  taille de lot à 6 kg.

**Séquence complète et la plus courte : 4 essais de mélange pour la décision technique,
6 pour couvrir les deux dosages et le scale-up** — voir `docs/07-sequence-minimale.md`.

### L'argument qui doit clore le débat interne

Un produit **12/200 et 12/400 en capsule unique, à 25,000 mg, avec le lactose pour seul
excipient**, est autorisé et commercialisé depuis 2013 (FORPACK, Turquie) `FAIT CONFIRMÉ` ;
un produit équivalent au Brésil a été publiquement mesuré comme équivalent à deux capsules
séparées, **avec un formotérol mieux aérosolisé en capsule unique qu'en capsule séparée**
(FPF 56 % contre 52 %) `FAIT CONFIRMÉ`.

La séparation des deux formulations décidée historiquement n'était pas une limite de la physique.
C'était une limite de l'architecture de prémélange.
