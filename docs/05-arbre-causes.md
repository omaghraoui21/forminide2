# Arbre de causes de l'échec historique du combiné 9 kg

Classement : **TRÈS PLAUSIBLE** · **PLAUSIBLE** · **PEU PROBABLE** · **DONNÉES INSUFFISANTES**
Pour chaque cause : le **test expérimental le moins cher** permettant de la confirmer ou de l'éliminer.

```
ÉCHEC DU BULK COMBINÉ BUD/FOR À 9 KG
│
├── 1. DISTRIBUTION DU FORMOTÉROL
│   ├── 1.1 Co-agglomération BUD–FOR dans le sandwich commun ......... TRÈS PLAUSIBLE
│   ├── 1.2 Mauvais prémix (pas de prémix du tout) ................... TRÈS PLAUSIBLE
│   ├── 1.3 Agglomérats de FOR survivant au tamis 250 µm ............. TRÈS PLAUSIBLE
│   └── 1.4 Statistique de mélange (trop peu de particules) .......... PEU PROBABLE
│
├── 2. INTERACTIONS API / API / CARRIER
│   ├── 2.1 Compétition de sites actifs BUD vs FOR ................... PLAUSIBLE
│   ├── 2.2 Déplacement d'un API par l'autre en cours de mélange ..... DONNÉES INSUFFISANTES
│   └── 2.3 Adhésion préférentielle (CAB) défavorable au BUD ......... PLAUSIBLE
│
├── 3. PROCÉDÉ / MÉCANIQUE
│   ├── 3.1 Taux de remplissage 71–79 % à l'étape finale ............. ⛔ ÉLIMINÉE (2026-09-13)
│   ├── 3.2 Sous-mélange à l'étape 3 ................................. PEU PROBABLE
│   ├── 3.3 Sur-mélange cumulé (3 × 15 min = press-on) ............... PLAUSIBLE
│   ├── 3.4 Répartition 3:3:3 non optimale ........................... PLAUSIBLE
│   └── 3.5 Tamisage destructeur / reclassement granulométrique ...... PLAUSIBLE
│
├── 4. PERTES ET ENVIRONNEMENT
│   ├── 4.1 Pertes de FOR au tamisage / sur les parois ............... PLAUSIBLE
│   ├── 4.2 Électrostatique (FOR micronisé, 4,3 g) ................... PLAUSIBLE
│   ├── 4.3 Variation d'humidité entre lots .......................... DONNÉES INSUFFISANTES
│   └── 4.4 Ségrégation au transfert / au stockage du bulk ........... PLAUSIBLE
│
├── 5. CARRIER
│   ├── 5.1 Ratio fines/grossier inadapté au dual-API ................ PLAUSIBLE
│   ├── 5.2 Grade de lactose inadapté au dual-API .................... PEU PROBABLE
│   └── 5.3 Carrier du combiné hérité du budésonide : le formotérol
│           passe de 100 % à ~50 % de ML001 ...................... ★ TRÈS PLAUSIBLE
│
└── 6. MESURE
    └── 6.1 Prise d'essai trop grosse (~1 g au lieu de 25 mg) ........ DONNÉES INSUFFISANTES
             (si confirmée, elle invalide aussi les "succès" mono-produits)
```

---

## ⛔ Causes éliminées par les données de production (2026-09-13)

`FAIT INTERNE CONFIRMÉ` — Les **deux mono-produits sont fabriqués en routine à 9 kg**, masse de
remplissage **25 mg**, sur les mêmes équipements. Le formotérol mono est sur **ML001 seul**
(densité versée 570 g/L → **78,9 % de remplissage**), le budésonide mono sur **SV003/ML001 50:50**
(598 g/L → **75,2 %**).

Un actif à **0,048 % m/m** est donc distribué de façon homogène dans **9 kg**, à **79 % de
remplissage**, en routine. Cela élimine d'un coup :

| Cause | Pourquoi elle tombe |
|---|---|
| **3.1 — taux de remplissage** | 79 % est la condition de fabrication **normale** du formotérol mono, et elle fonctionne. L'argument tiré de la guidance générique du constructeur ne résiste pas aux données du site |
| **1.4 — statistique du mélange** | déjà écartée par le calcul, et confirmée par la pratique |
| **3.2 — sous-mélange** · **3.3 — sur-mélange** | mêmes temps, mêmes révolutions, mêmes trois tamisages sur les mono-produits qui réussissent → rétrogradées en PEU PROBABLE |
| **taille de lot de 9 kg** | c'est l'échelle de production courante des deux mono-produits |
| **écoulement d'un carrier riche en ML001 au dosator** | le formotérol mono est rempli à 25 mg sur **ML001pur** — l'objection « ML001 ne coule pas assez » est empiriquement fausse |

**Ce qui reste après élimination — deux causes, et elles se testent en trois lots :**

| # | Cause restante | Différence avec le mono-produit qui marche |
|---|---|---|
| **1.1** | **Co-agglomération BUD–FOR** | 144 g de budésonide arrivent dans le même sandwich, soit **33 × la masse du formotérol** |
| **5.3** | **Perte de l'environnement de fines** | le carrier passe de **100 % à ≈ 50 % de ML001** si le combiné hérite du système du budésonide |

```
E-A  co-sandwich   · carrier BUD  (50 % ML001)   ← reproduit la tentative historique
E-B  double prémix · carrier BUD  (50 % ML001)   ← E-A vs E-B = effet ARCHITECTURE
E-C  double prémix · carrier FOR (100 % ML001)   ← E-B vs E-C = effet CARRIER
```

---

## Tableau détaillé

| # | Cause | Classement | Argument | **Test le moins cher** | Coût |
|---|---|---|---|---|---|
| **1.1** | **Co-agglomération BUD–FOR** : les deux poudres micronisées se rencontrent à l'état pur dans le même sandwich ; le BUD est 17 à 33× plus abondant et le FOR devient un passager de ses agglomérats | **TRÈS PLAUSIBLE** | co-agglomération démontrée par Raman sur un couple corticoïde/β2 analogue ; budésonide décrit comme cohésif (CAB 0,62) | **E2 vs E3** : un lot co-sandwich contre un lot prémix FOR, tout le reste identique | 2 lots de 3 kg |
| **1.2** | **Absence de prémix formotérol** | **TRÈS PLAUSIBLE** | les deux brevets traitant corticoïde+formotérol en poudre sèche font systématiquement un prémix FOR (0,82 % m/m) | **E1** : qualifier le prémix seul | 1,4 g de FOR |
| **1.3** | **Agglomérats de FOR > la taille utile** : un agglomérat de 250 µm porte 27–41 % d'une dose ; un RSD de 10 % correspond à des entités de ~56 µm, invisibles pour le tamis | **TRÈS PLAUSIBLE** | `calcul interne`, voir `annexes/A2-calculs.md` | **E1 avec double tamisage** : une aliquote à 250 µm, une à 212 µm, comparer les RSD | 1 tamis manuel |
| **1.4** | Limite statistique du mélange | **PEU PROBABLE** | `calcul interne` : ~1,1 million de particules de FOR par dose → RSD théorique 0,09 % | aucun test nécessaire — éliminé par le calcul | 0 |
| **2.1** | **Compétition de sites actifs** : le BUD sature les sites de haute énergie par effet de masse | **PLAUSIBLE** (et **favorable** au FOR si elle a lieu sur le carrier) | mécanisme reconnu des composants ternaires ; sur le produit brésilien, FPF FOR (56 %) > FPF FOR en capsule séparée (52 %) | **E3 vs L3** : inverser l'ordre d'arrivée des APIs sur le carrier | 1 lot |
| **2.2** | Déplacement d'un API par l'autre pendant le mélange prolongé | **DONNÉES INSUFFISANTES** | aucune donnée publique sur BUD/FOR | **cinétique embarquée dans E3** : si l'assay d'un API dérive entre 5 et 25 min alors que l'autre est stable | 4 × 10 analyses |
| **2.3** | Adhésion préférentielle défavorable (le BUD préfère le BUD au lactose) | **PLAUSIBLE** | CAB budésonide 0,62, actif plutôt cohésif | **E3 Gate 4** : si FPD BUD faible avec MMAD élevé → dépôt en agglomérats | NGI déjà prévu |
| **3.1** | ~~Taux de remplissage à l'étape la plus difficile~~ | **⛔ ÉLIMINÉE** | les deux mono-produits sont fabriqués en routine à 9 kg, à **75–79 % de remplissage**, avec succès. Le formotérol mono, à 0,048 % m/m sur ML001 pur, est le contre-exemple direct | aucun essai nécessaire — la production courante fait foi | 0 |
| **3.2** | Sous-mélange à l'étape 3 | **PLAUSIBLE** | conséquence directe de 3.1 | **cinétique embarquée** à l'étape 3 : si le RSD s'améliore encore entre 15 et 25 min, il y avait sous-mélange | 10 analyses |
| **3.3** | Sur-mélange cumulé (press-on forces) | **PLAUSIBLE** | l'essentiel de l'évolution se joue dans les 120 premières min ; press-on dominant sur 0–60 min ; 15 min = optimum publié en tumbler | **même cinétique** : NGI à 15 et 25 min ; si FPD(25) < FPD(15) à RSD constant → sur-mélange | 2 NGI |
| **3.4** | Répartition 3:3:3 non optimale | **PLAUSIBLE** | EP3175842A1 : AV de 7,1 (7:2:1) à 12,5 (5:1:4) à actif constant | **E2 (3:3:3) vs E3 (7:2:1)** — déjà dans le plan | 0 (inclus) |
| **3.5** | Tamisage destructeur / reclassement | **PLAUSIBLE** | un tamis est un classificateur ; mais US9616024 montre qu'un tamisage final **améliore** le RSD (4,6 → 1,5 %) | **assay + RSD avant/après le tamisage final de E3** | 2 × 10 analyses |
| **4.1** | Pertes de FOR au tamisage / parois | **PLAUSIBLE** | 4,32 g répartis dans 9 kg ; toute rétention préférentielle se voit sur l'assay | **bilan matière systématique** (pesée entrée/sortie ± 0,5 %) + rinçage analytique du matériel sur E1 | ~0 |
| **4.2** | Électrostatique | **PLAUSIBLE** | poudres micronisées + inox ; charge triboélectrique documentée en DPI | **E1 en double** : une fois avec ioniseur, une fois sans ; comparer bilan matière et RSD | 1 demi-lot de prémix |
| **4.3** | Variation d'humidité | **DONNÉES INSUFFISANTES** | aucun enregistrement historique | **enregistreur HR/T** en salle, dès maintenant, sur tous les lots | coût d'un capteur |
| **4.4** | Ségrégation au transfert/stockage | **PLAUSIBLE** | mélange ordonné = résistant, sauf fines libres | **Gate 2** : test de ségrégation par vibration + assay FOR par fraction granulométrique | inclus |
| **5.1** | Ratio fines/grossier inadapté | **PLAUSIBLE** | SV003 et SV010 n'ont presque pas de fines < 10 µm ; la fenêtre publiée utile est 4–15 % | **L4** : SV003 + 8 % ML001, uniquement si CU bonne et FPD faible | 1 lot conditionnel |
| **5.3 ★** | **Le carrier du combiné a été hérité du budésonide.** Le mono-produit formotérol utilise **ML001 seul** ; le mono-produit budésonide utilise **SV003 + ML001**. Si le combiné a été fait sur le carrier du BUD, le formotérol a perdu l'environnement de fines dont dépend son propre mono-produit | **TRÈS PLAUSIBLE** | information interne (2026-09-13) ; ML001 est le seul des trois grades à posséder une vraie population fine (D10 3–7 µm) | **E-B vs E-C** à 1 kg : même architecture, taux de ML001 différent (≈ 14 % contre ≈ 33 %) | 2 lots de 1 kg, 0,96 g de FOR |
| **5.2** | Grade de lactose inadapté au dual-API | **PEU PROBABLE** | SV003 est le carrier grossier des exemples BUD/FOR publiés ; le même grade fonctionne en mono-produit chez nous | **L5**, en dernier | 1 lot conditionnel |
| **6.1** | **Prise d'essai historique trop grosse** | **DONNÉES INSUFFISANTES — priorité d'investigation n°1** | un RSD mesuré sur 1 g masque mathématiquement l'hétérogénéité à 25 mg | **question Q4** : consulter les protocoles d'analyse historiques. **Coût : zéro, délai : une journée** | 0 |

---

## Hiérarchie d'action

1. **Q3 + Q4** (archives historiques) — coût nul, effet maximal.
2. **E1** — élimine 1.2, 1.3, 4.1, 4.2 pour 1,4 g de formotérol.
3. **E2 vs E3** — élimine 1.1, 3.4 et, via la cinétique embarquée, 2.2, 3.2, 3.3, 3.5.
4. **E4** — élimine ou confirme 3.1.
5. **L4 / L5** (conditionnels) — 5.1 puis 5.2.

**Révision du 2026-09-13** : la cause **5.3** entre directement au premier étage d'essais
(lots E-B et E-C à 1 kg, voir `11-petites-echelles.md`), avant même les lots de 3 kg. Elle est
moins chère à tester que toutes les autres et elle découle d'une pratique interne établie.
La question **Q18** (taille de lot et cuve des mono-produits) peut par ailleurs départager
les causes 3.1 et 5.3 **sans consommer un gramme d'API**.

Les causes 1.4 et 5.2 ne justifient **aucun essai dédié**.
