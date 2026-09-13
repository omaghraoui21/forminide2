# Architectures de bulk et protocoles de lots

## Partie 1 — Comparaison des architectures (P0 → P5 / A → G)

| Architecture | Mécanisme | Avantages | Risques | Scale-up | Compatibilité Inversina / Russell |
|---|---|---|---|---|---|
| **A = P0 — Co-sandwich** (benchmark historique)<br>BUD + FOR ensemble dans la 1re fraction | une seule séquence de désagglomération pour les deux APIs | le plus simple, le moins de manipulations, procédé connu | **les deux poudres micronisées se rencontrent à l'état pur** → co-agglomération ; le FOR devient passager des agglomérats de BUD ; charge d'API locale ≈ 4,9 % m/m | mauvais : la difficulté croît avec la masse | totale |
| **B = P1 — Prémix formotérol** ⭐<br>prémix FOR ≈ 1 % → incorporé → BUD déposé **après**, en couche séparée | la désagglomération du FOR est faite **seule**, concentrée et tamisée ; la distribution est faite ensuite en douceur | aucun achat, aucun équipement, **même nombre d'étapes Inversina** ; architecture des brevets Nycomed ; point de contrôle possible sur le prémix | une manipulation de plus ; bilan matière du prémix à surveiller | **excellent** : concentration du prémix et répartition sans dimension | totale |
| **C = P2 — Prémix budésonide**<br>BUD/carrier d'abord, **prémix FOR ajouté en dernier** | le BUD sature les sites de haute énergie ; le FOR se pose ensuite sur des sites faibles → détachement facilité | peut maximiser la **FPD du formotérol** | le FOR arrive tard : moins de temps de mélange pour se distribuer → risque d'uniformité | bon | totale |
| **D = P3 — Double prémix**<br>prémix FOR **et** prémix BUD, combinés en fin | séparation totale des deux APIs ; chaque prémix contrôlable à l'assay avant combinaison | **la plus robuste** ; deux points de contrôle qualité gratuits | deux manipulations de plus ; le prémix BUD concentré est très cohésif ; temps opérateur | bon | totale |
| **E = P4 — Carriers distincts**<br>un grade par API, combinaison finale | chaque API son support optimal | **deux populations de PSD/densité** dans un même bulk → percolation et ségrégation au transfert et au dosator | mauvais | totale mais déconseillé |
| **F = P5 — Carrier pré-conditionné**<br>SV003 + 5–10 % ML001 mélangés et tamisés **avant** les APIs | les fines saturent les sites forts et s'intercalent entre les particules d'API ; favorise les co-agglomérats BUD–fines co-déposés | corrige la FPD ; ordre « fines + carrier d'abord » documenté comme favorable à faible concentration d'actif | chute de densité versée → **remplissage mélangeur**, écoulement dosator, fines libres ségrégeantes | bon | totale |
| **G — Architecture publiée supérieure** | recherchée dans brevets/littérature/produits | — | — | — | — |

> **Résultat de la recherche pour G** : aucune architecture publiée supérieure n'a été trouvée
> qui soit compatible avec nos équipements. Les seules architectures publiques nettement plus
> performantes (Zambon FPF > 60 %, AstraZeneca Turbuhaler) reposent sur du **spray drying** ou de
> la **sphéronisation**. **L'architecture la mieux documentée qui nous soit accessible est
> B, éventuellement combinée à F** (= exactement Nycomed ex. 3 + Tiefenbacher 7:2:1 + Zambon
> carrier + fines).

**Recommandation d'équipe : B, avec F comme première optimisation et D comme repli de robustesse.**

---

## Partie 2 — Protocoles de lots

### Conventions communes à tous les lots

- **Dosage de screening : 12/400** (pire cas pour le formotérol, ratio de masse BUD:FOR = 33:1).
- **Échelle de screening : 3 kg.** Masses : lactose 2 950,6 g · BUD 48,00 g · **FOR 1,44 g**
  (à corriger du titre). `calcul interne`
- **Carrier de screening : SV003** (sauf L5).
- Chaque étape de dilution : ajout → **mélange court 3 min** → **Russell 250 µm** →
  **Inversina 15 min**.
- **Le procédé ne se termine jamais par un tamisage.**
- **Bilan matière obligatoire** (pesée entrée/sortie, ±0,5 %) à **chaque** tamisage.
- **HR et température de salle enregistrées** à chaque étape.
- **Échantillonnage : 10 positions × 25 mg** (haut/milieu/bas × paroi/centre + fond de cuve).
  **Jamais de prise de l'ordre du gramme.**

---

### L0 — Qualification du prémix formotérol *(144 g)*

**Hypothèse** : un prémix FOR à 1,0 % m/m, sandwiché et tamisé, atteint RSD ≤ 5 % à 25 mg.

| | |
|---|---|
| Composition | FOR 1,44 g + SV003 142,6 g |
| Procédé | SV003 (moitié) → **FOR au centre** → SV003 (moitié) → mélange 3 min → tamisage → Inversina 15 min |
| Variante embarquée | aliquote tamisée à **212 µm** (tamis manuel) en parallèle du 250 µm |
| Variante embarquée 2 | une répétition **avec** et **sans** ioniseur au poste de pesée |
| Réponses | assay FOR ; **RSD 10 × 25 mg** ; bilan matière ; rinçage analytique du matériel ; densités versée/tassée |
| **GO** | RSD ≤ 5 % · teneur 95–105 % · bilan matière ≥ 99 % |
| **NO-GO** | RSD > 8 % → **arrêt du plan**, réunion fournisseur API (PSD, état d'agglomération) |

---

### L1 — Benchmark historique *(3 kg, architecture A)*

**Hypothèse** : le problème historique se reproduit à 3 kg.

| | |
|---|---|
| Composition | SV003 2 950,6 g · BUD 48,00 g · FOR 1,44 g |
| Répartition | **3 : 3 : 3** (983,5 g × 3) |
| Procédé | 1re fraction → **BUD + FOR déposés ENSEMBLE** en sandwich → 5 min → tamis → 15 min ; puis 2 dilutions identiques |
| Réponses | Gate 1 (assay + RSD des 2 APIs) ; Gate 2 (densités, Carr, Hausner, ségrégation) |
| **Lecture** | **Échec attendu** → le problème est architectural, reproductible à 3 kg.<br>**Succès** → le problème historique était **mécanique / d'échelle** : on saute L3–L5 et on va directement au 9 kg. |

⚠️ **Ne pas sauter ce lot.** C'est le seul témoin, et il porte la bifurcation du plan entier.

---

### L2 — Architecture B recommandée *(3 kg)*

**Hypothèse** : prémix FOR + répartition 7:2:1 résolvent le problème.

| Étape | Opération |
|---|---|
| 0 | **Prémix FOR** (celui de L0, ou refait) : 1,44 g FOR + 143,0 g SV003 |
| 1 | 1re fraction = **70 %** du lactose (2 065,4 g au total, prémix inclus) :<br>≈ 960 g SV003 → **prémix FOR étalé** → ≈ 330 g SV003 (**couche barrière**) → **BUD 48,00 g étalé** → ≈ 630 g SV003<br>→ mélange 5 min → **Russell 250 µm** → **Inversina 15 min** |
| 2 | + **20 %** (590,1 g) → mélange 3 min → tamis → Inversina 15 min |
| 3 | + **10 %** (295,1 g) → mélange 3 min → tamis → **cinétique embarquée** |

**Mesures embarquées dans L2 :**
1. **Cinétique de mélange** à l'étape 3 : prélèvements à **5 / 10 / 15 / 25 min**, 10 positions
   à chaque temps ; **NGI uniquement à 15 et 25 min**.
2. **Tamisage destructeur ?** assay + RSD **avant** et **après** le tamisage de l'étape 3.
3. Gates 1 → 2 → 3 (remplissage Modu-C 25 mg) → 4 (NGI).

**GO** : RSD ≤ 5 % pour les deux APIs · FPF ≥ 30 % pour les deux APIs · dose délivrée ≥ 70 %.

---

### L3 — Architecture C : ordre inversé *(3 kg, conditionnel)*

**Hypothèse testée** : le désaccord D2 — quel API doit toucher le carrier en premier ?

Identique à L2, mais **le budésonide est mélangé au carrier en premier** (1re fraction complète,
tamis, 15 min) et **le prémix FOR est ajouté en dernier**, avec la 3e fraction.

**Lancé si** : L2 n'atteint pas RSD FOR ≤ 5 %, **ou** si la FPD FOR de L2 est décevante.
**Lecture** : L3 > L2 sur la FPD FOR → la saturation préalable des sites par le budésonide est
bénéfique ; L3 < L2 sur la CU FOR → le formotérol a besoin de temps de mélange, ne pas l'ajouter
en dernier.

---

### L4 — Architecture F+B : carrier pré-conditionné *(3 kg, conditionnel)*

**Hypothèse** : les fines corrigent la FPD (et/ou la CU).

| | |
|---|---|
| Carrier | SV003 **92 %** + **ML001 8 %**, mélangés **et tamisés ensemble avant tout API** (Inversina 15 min + tamis) |
| Suite | architecture B identique à L2 |
| Contrôle supplémentaire | **densité versée du carrier pré-conditionné** → recalculer le taux de remplissage à 9 kg (`calcul interne` : ≈ 625 g/L → 72 %) |
| **Lancé si** | Gate 1 OK mais **Gate 4 faible** (FPD insuffisante pour l'un ou l'autre API) |
| **Lecture** | si la FPD BUD s'améliore nettement → mécanisme des co-agglomérats médicament–fines confirmé → envisager LH230 pour aller plus loin |

---

### L5 — Effet carrier *(3 kg, conditionnel)*

Architecture gagnante (L2 ou L3) sur **SV010** ou **SV003/SV010 50:50**.

**Lancé si** : problème d'écoulement / de remplissage au Gate 3, **ou** pour disposer d'un plan B
industriel documenté. **Bénéfice attendu au scale-up** : SV010 fait passer le remplissage 9 kg de
71 % à **65 %** `calcul interne`.

---

### L6 — Scale-up *(6 kg puis 9 kg)*

Architecture gagnante, répartition **7:2:1**, prémix FOR à concentration inchangée (1 %).

| Échelle | Lactose | BUD (400) | FOR | Prémix FOR | Fractions 7:2:1 | Remplissage (SV003) |
|---|---|---|---|---|---|---|
| 3 kg | 2 950,6 g | 48,00 g | 1,44 g | 144,0 g | 2 065 / 590 / 295 g | 24 % |
| 6 kg | 5 901,1 g | 96,00 g | 2,88 g | 288,0 g | 4 131 / 1 180 / 590 g | 48 % |
| 9 kg | 8 851,7 g | 144,00 g | 4,32 g | 432,0 g | 6 196 / 1 770 / 885 g | **71 %** |

Échantillonnage porté à **15 positions** à 9 kg. Gates 1 → 4 complets.

---

### L7 (= E5) — Dosage 12/200 *(3 ou 6 kg)*

Même architecture, **BUD 0,800 % au lieu de 1,600 %** (24,00 g à 3 kg, 72,00 g à 9 kg).
C'est le **pire cas pour l'uniformité du budésonide** (concentration la plus faible).

---

## Partie 3 — Récapitulatif « une expérience = des hypothèses éliminées »

| Lot | Hypothèses éliminées ou confirmées |
|---|---|
| **L0** | 1.2 (absence de prémix), 1.3 (taille d'agglomérat), 4.1 (pertes), 4.2 (électrostatique) |
| **L1** | 6.1 partiellement ; établit si la cause est chimique ou mécanique |
| **L2** | 1.1 (co-agglomération), 3.4 (répartition), 3.2/3.3 (sous/sur-mélange, par la cinétique), 3.5 (tamisage) |
| **L3** | 2.1 (compétition de sites), désaccord D2 |
| **L4** | 5.1 (ratio fines/grossier) |
| **L5** | 5.2 (grade de carrier) |
| **L6** | 3.1 (taux de remplissage) |
