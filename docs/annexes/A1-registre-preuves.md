# Registre de preuves

Format imposé par `CLAUDE.md` :
**SOURCE → DONNÉE → NIVEAU DE CONFIANCE → INTERPRÉTATION → CONSÉQUENCE POUR NOTRE ESSAI**

Consulté en septembre 2026. Les URL sont données pour vérification ; **une fiche produit ou un
brevet doit toujours être re-téléchargé avant usage réglementaire**.

---

## P1 — Notice réglementaire turque FORPACK 12/200 capsair (KÜB)

- **SOURCE** : Kısa Ürün Bilgisi, FORPACK 12/200 mcg capsair, Neutec İnhaler İlaç,
  AMM 250/43, 1re autorisation 06/05/2013.
  `https://nuvomedilac.com/pdf/forpack-12-200-mcg-Capsair-inhaler-Kapsul-Kub.pdf`
- **DONNÉE** : §2 — formotérol fumarate dihydraté 12 mcg ; budésonide 200 mcg ;
  **« Laktoz 24,7880 mg »**. §6.1 — liste des excipients : **« Laktoz »** (seul).
  §6.3 — 24 mois. §6.4 — < 25 °C, au sec. §6.5 — blister Alu/Alu, 60 ou 120 gélules.
  §3 — gélule, coiffe violet clair transparent, corps naturel, poudre blanche.
  §4.2 — gélule en **gélatine** ; dispositif mono-dose à **bouton de perforation**.
- **CONFIANCE** : **FAIT CONFIRMÉ** (document réglementaire primaire).
- **INTERPRÉTATION** : masse totale = 24,7880 + 0,200 + 0,012 = **25,0000 mg**. Un produit
  strictement identique à notre cible est autorisé depuis 2013, **avec le lactose pour seul
  excipient**.
- **CONSÉQUENCE** : (a) figer la masse à 25,0 mg ; (b) **ne pas ajouter d'excipient** sans
  nécessité démontrée ; (c) utiliser ce produit comme référence de faisabilité dans toute
  discussion interne ; (d) viser 24 mois de péremption avec conservation au sec.

### P1 bis — FORPACK **12/400** mcg capsair (KÜB) — *question Q12 fermée*

- **SOURCE** : `https://neutecinhaler.com/pdf/forpack-12-400-mcg-capsair-inhaler-Kapsul-Kub.pdf`
  AMM **250/44**, 1re autorisation **06/05/2013**, KÜB révisé 07/01/2015.
- **DONNÉE** : §2 — formotérol fumarate dihydraté 12 mcg ; budésonide 400 mcg ;
  **« Laktoz 24,588 mg »**. §6.1 — **« Laktoz »** (seul excipient). §3 — coiffe **violet foncé**
  transparent, corps naturel (le 12/200 a une coiffe violet **clair**). §6.3–6.5 — 24 mois,
  < 25 °C au sec, Alu/Alu 60 ou 120 gélules.
- **CONFIANCE** : **FAIT CONFIRMÉ**.
- **INTERPRÉTATION** : masse totale = 24,588 + 0,400 + 0,012 = **25,0000 mg**, exactement comme
  pour le 12/200. **Le même fabricant utilise donc le même bulk à 25,000 mg pour les deux
  dosages**, la seule différence étant l'échange budésonide ↔ lactose (200 → 400 µg de BUD,
  24,788 → 24,588 mg de lactose). C'était une inférence dans la version précédente du dossier ;
  c'est désormais un fait.
- **CONSÉQUENCE** : **valide directement notre stratégie « un seul bulk, deux dosages »** : les
  deux présentations partagent la masse, l'excipient unique, le device et la gélule. Notre lot
  L7 (12/200) n'a donc à démontrer qu'une chose — que la charge de budésonide plus faible
  (0,800 % au lieu de 1,600 %) reste homogène — et non une nouvelle architecture.

## P2 — Notice réglementaire turque FORPACK 12/400 discair (KÜB)

- **SOURCE** : `https://neutecinhaler.com/pdf/forpack-12-400-mcg-Discair-inh-icin-Toz-Kub.pdf`
- **DONNÉE** : §2 — FOR 12 mcg + BUD 400 mcg + **« Laktoz 12,5880 mg »** par dose ; §6.1 lactose seul.
- **CONFIANCE** : **FAIT CONFIRMÉ**.
- **INTERPRÉTATION** : masse totale **13,0000 mg** par dose pour la version **multidose**, contre
  25,0 mg pour la version gélule du même fabricant.
- **CONSÉQUENCE** : le système carrier est accordé au device. **Ne jamais transposer une
  composition multidose (y compris Symbicort) dans une gélule.**

## P3 — Étude d'équivalence pharmaceutique brésilienne (gélule unique BUD/FOR) — **texte intégral**

- **SOURCE** : Andrade-Lima M, Pereira LFF, Fernandes ALG. *Pharmaceutical equivalence of the
  combination formulation of budesonide and formoterol in a single capsule with a dry powder
  inhaler.* J Bras Pneumol. 2012;38(6):748-756. DOI 10.1590/S1806-37132012000600010.
  Texte intégral : `https://www.jbp.org.br/export-pdf/1765/2012_38_6_10_english.pdf`
  Essais réalisés au laboratoire accrédité T&E Analítica (Campinas), **sous supervision directe
  de deux techniciens de l'ANVISA**.
- **MÉTHODES (§ Methods)** : dosage HPLC-UV ; uniformité de dose délivrée par **DUSA-DPI**
  (Westech Scientific Instruments) ; APSD par **impacteur en cascade d'Andersen (ACI, modèle
  8301-60, Copley)** ; teneur en eau par **Karl Fischer** ; contrôles microbiologiques.
  Débit de référence cité par les auteurs : **90 L/min**.
  **Définitions explicites du texte** : *fine particle dose* = masse des particules < 5 µm dans
  la dose délivrée ; **« fine particle fraction = fine particle dose divisée par la dose
  délivrée totale »**. → l'ambiguïté sur le dénominateur, signalée dans la version précédente
  du dossier, **est levée**.
- **DONNÉES — Tableau 1 complet** :

| Variable | **Test** : gélule **unique** BUD/FOR 400/12, Aerocaps® | **Référence** : BUD seul, gélule séparée, Aerolizer® | **Référence** : FOR seul, gélule séparée, Aerolizer® |
|---|---|---|---|
| **Masse de la gélule**, mg (n = 20) | **25,56 ± 0,79** [25,3 (24,2–27,1)] | 25,35 ± 1,08 [25,5 (23,0–27,3)] | 25,19 ± 0,70 [25,3 (23,8–26,3)] |
| *RSD de masse* `calcul interne` | **3,09 %** | 4,26 % | 2,78 % |
| Teneur en principe actif, % | BUD 111,41 · FOR 103,80 | BUD 110,59 | FOR 104,51 |
| **Uniformité de dose délivrée**, µg (n = 30) | BUD **293,24 ± 12,91** · FOR **10,23 ± 0,47** | BUD 353,04 ± 11,48 | FOR 11,07 ± 0,60 |
| *RSD de dose délivrée* `calcul interne` | BUD **4,40 %** · FOR **4,59 %** | BUD 3,25 % | FOR 5,42 % |
| Dose délivrée / dose étiquetée (texte) | BUD **73 %** · FOR **85 %** | BUD 88 % | FOR 92 % |
| Plage de dose délivrée, % | BUD 92,69–109,25 · FOR 89,63–108,01 | BUD 91,31–107,14 | FOR 91,32–111,83 |
| **Uniformité de teneur**, % (n = 10) | BUD **103,68 ± 1,68** · FOR **97,93 ± 1,98** | BUD 107,20 ± 5,83 | FOR 100,00 ± 3,23 |
| ***RSD d'uniformité de teneur*** `calcul interne` | **BUD 1,62 % · FOR 2,02 %** | **BUD 5,44 %** | **FOR 3,23 %** |
| **Dose de particules fines**, µg (% de la dose délivrée) | BUD **140,67 (44,71 %)** · FOR **6,18 (56,13 %)** | BUD 181,53 (53,56 %) | FOR 5,46 (52,05 %) |
| *FPD en % de la dose étiquetée* `calcul interne` | BUD **35,2 %** · FOR **51,5 %** | BUD 45,4 % | FOR 45,5 % |

- **CONFIANCE** : **FAIT CONFIRMÉ** (article peer-reviewed, essais supervisés par l'autorité).
- **INTERPRÉTATIONS** — trois résultats, par ordre d'importance pour notre projet :
  1. **La gélule combinée est PLUS uniforme que les deux gélules séparées qu'elle remplace.**
     RSD d'uniformité de teneur : **formotérol 2,02 % en combiné contre 3,23 % en mono-produit**,
     et **budésonide 1,62 % contre 5,44 %**. C'est l'inverse exact de l'intuition qui a conduit
     notre site à séparer les deux formulations.
  2. **Le formotérol gagne aussi en masse fine absolue** : **FPD 6,18 µg en combiné contre
     5,46 µg en gélule séparée**, malgré une dose délivrée inférieure (10,23 contre 11,07 µg).
     La combinaison **améliore** l'aérosolisation du formotérol.
  3. **La masse de 25 mg est la norme de la classe**, y compris pour un **mono-produit
     formotérol 12 µg** (gélule de référence à **25,19 mg**) — c'est-à-dire pour une formulation
     à 0,048 % m/m analogue à la nôtre.
- **CONSÉQUENCES POUR NOS ESSAIS** :
  (a) **Cibles chiffrées, issues du marché et non d'une convention** : RSD de masse ≈ 3 % ;
  RSD d'uniformité de teneur ≤ 2 % atteignable, notre critère de 5 % est donc prudent ;
  RSD de dose délivrée ≈ 4,5 % ; FPF 45 % (BUD) et 56 % (FOR) ; dose délivrée 73–85 %.
  (b) **L'argument qui clôt le débat interne** : la séparation historique des deux formulations
  n'a même pas amélioré l'uniformité — mesurée sur produits commerciaux, elle la dégrade.
  (c) L'APSD de référence de la classe est mesurée à l'**ACI à 90 L/min** : notre plan NGI doit
  documenter son débit (ΔP = 4 kPa) pour rester comparable — voir Q10.

## P4 — Fiches DFE Pharma des lactoses d'inhalation

- **SOURCE** : DFE Pharma, *Your Inhalation Grade Lactose*, brochure #004, mai 2020.
  `https://dfepharma.com/media/2ianc2oo/dpi-corporate-brochure.pdf`
- **DONNÉE** : valeurs typiques Sympatec — **ML001** : D10 3–7 / D50 37–61 / D90 124–194 µm,
  tassée 880 g/L, **versée 570 g/L**, Carr > 25 % · **SV003** : 19–43 / 53–66 / 75–106 µm,
  780 / **630** g/L, Carr 19 % · **SV010** : 35–65 / 95–125 / 160–190 µm, 830 / **690** g/L,
  Carr 17 %. Également ML003, SV001, et la gamme Lactohale (LH230 : D50 < 10 µm ; LH300 : D50 < 5 µm).
  SV = tamisé (tomahawk, surface lisse) ; ML = broyé (irrégulier).
- **CONFIANCE** : **FAIT CONFIRMÉ** (documentation fournisseur) — valeurs **typiques**,
  non spécifications de lot.
- **INTERPRÉTATION** : seul ML001 possède une population fine (D10 3–7 µm) ; SV010 est le plus
  dense et le plus coulant ; aucun des trois n'apporte de vraies fines respirables (< 5 µm).
- **CONSÉQUENCE** : (a) SV003 = carrier par défaut ; (b) ML001 = donneur de fines **en minorité** ;
  (c) **les densités versées permettent de calculer les taux de remplissage de l'Inversina** — voir
  A2 ; (d) si des fines respirables deviennent nécessaires, LH230/LH300 est le seul chemin.

## P5 — EP3175842A1, procédé de mélange à sec (Tiefenbacher)

- **SOURCE** : `https://patents.google.com/patent/EP3175842A1/en`, priorité 2015-12-03.
- **DONNÉE** : procédé = 1re portion de lactose / totalité de l'actif / 2e portion (**sandwich**),
  mélange, tamisage optionnel, puis 3e portion, mélange, tamisage optionnel ;
  **Turbula 22 rpm, 15 min par étape**. Exemples sur tiotropium à **0,41 % m/m** :
  7:2:1 → RSD 2,9 %, AV 7,1 · 5:2:3 → 3,3 %, 7,8 · 4:1:5 → 3,2 %, 7,7 · 2:1:7 → 4,1 %, 10,0 ·
  5:1:4 → 4,8 %, 12,5.
- **CONFIANCE** : **FAIT CONFIRMÉ** pour les données ; **INFÉRENCE HAUTE CONFIANCE** pour la
  transposition au formotérol.
- **INTERPRÉTATION** : notre procédé historique est une plateforme publiée ; la **répartition**
  des trois fractions modifie l'AV d'un facteur ~1,8 à formule constante.
- **CONSÉQUENCE** : **passer de 3:3:3 à 7:2:1**. Et instruire la **liberté d'exploitation** (Q8).

## P6 — US9616024 / US9345664 / US9987229 (Norton Healthcare)

- **SOURCE** : `https://patents.google.com/patent/US9616024B2/en`, priorité 2003-09-02.
- **DONNÉE** : budésonide 9,6 % m/m, Turbula T2C gear 3, 10 min — **non tamisé : RSD 14,3 %,
  récupération 79,6 % ; tamisé 250 µm : RSD 4,6 %, 88,5 % ; + tamisage final 355 µm : RSD 1,5 %**.
  Formotérol 0,265 % m/m — **non tamisé : RSD 1,2 %, 91,4 % ; tamisé 250 µm : RSD 0,9 %, 99,6 %**.
  Salbutamol : **Turbula optimum à 15 min** ; agglomérats **< 355 µm → FPF 43,6–42,2 %** contre
  **< 250 µm → 38,5–31,2 %** ; l'allongement du mélange **diminue** la FPF. Critère du brevet :
  **RSD ≤ 5 %**. Le brevet énonce que le budésonide était réputé exiger un mélangeur à **haut
  cisaillement**, et démontre que le tamisage préalable rend le **bas cisaillement** suffisant.
- **CONFIANCE** : **FAIT CONFIRMÉ**.
- **INTERPRÉTATION** : le tamisage n'est pas un accessoire, c'est le mécanisme qui rend
  l'Inversina suffisante, y compris pour le budésonide.
- **CONSÉQUENCE** : (a) **conserver les tamisages** ; (b) **refuser tout achat de mélangeur haut
  cisaillement** ; (c) **ne pas allonger** les 15 min ; (d) retenir la piste « maille plus
  grossière » (355 µm) **uniquement** si la FPD est faible malgré une bonne CU ; (e) adopter
  RSD ≤ 5 % comme critère de Gate 1.

## P7 — US7879833 / US8258124 (Nycomed → Covis), association corticoïde + formotérol

- **SOURCE** : `https://patents.google.com/patent/US7879833B2/en`, priorité 2002-12-12.
- **DONNÉE** : ex. 3 — **formotérol fumarate dihydraté 60 mg + 7,27 g de lactose (prémix
  ≈ 0,82 % m/m)**, tamisage 0,5 mm, Turbula, prémix re-tamisé ; le corticoïde (2,67 g) et 90 g de
  lactose sont ajoutés **ensuite**. Ex. 2 — **double prémix** (FOR + 97,2 g ; corticoïde + 250 g ;
  puis 650 g de dilution), lactose désaggloméré au broyeur à tamis. Ex. 1 — gélule, mélange en
  **deux portions**, tamisage 0,71 mm, **25 mg en gélule taille 3**.
- **CONFIANCE** : **FAIT CONFIRMÉ** (le corticoïde est le ciclésonide, pas le budésonide).
- **INTERPRÉTATION** : le seul déposant ayant publié des exemples chiffrés d'une association
  corticoïde + formotérol en mélange à sec fait **systématiquement un prémix formotérol dédié**.
- **CONSÉQUENCE** : **notre prémix FOR à ≈ 1 % m/m est une transposition directe**, pas une
  invention ; la gélule 25 mg taille 3 y est également exemplifiée.

## P8 — US10449147 / US10226421 / ES2837040 (Zambon), budésonide + formotérol

- **SOURCE** : `https://patents.google.com/patent/US10449147B2/en`, priorité 2014-10-08.
- **DONNÉE** : mélange de lactose = **Respitose® SV003 (grossier, X50 35–75 µm) 85–96 %** +
  **Lacto-Sphere® MM3 (fin, X50 1,5–10 µm) 4–15 %**, **optimum cité 91:9** ; gélules **taille 3
  HPMC**, inhalateur **RS01 modèle 7 (type Aerolizer)**, MSLI, FPF > 60 %, fraction délivrée > 80 % ;
  actifs **spray-dried avec leucine**, dépôt des poudres actives **entre deux couches de lactose**.
- **CONFIANCE** : **FAIT CONFIRMÉ** pour le système carrier ; voie active **incompatible** avec
  nos équipements.
- **INTERPRÉTATION** : la fenêtre utile de fines sur base SV003 est **4–15 %**, optimum ≈ 9 %,
  retenue notamment parce qu'elle **conserve l'homogénéité dans le temps**.
- **CONSÉQUENCE** : si le Gate 4 impose des fines, viser **≈ 8–10 %** — d'abord avec **ML001**
  (sans achat), puis LH230 si insuffisant.

## P9 — US11642475 / BR112016011996B1 (Pharmachemie/Teva, BF Spiromax)

- **SOURCE** : `https://patents.google.com/patent/US11642475B2/en`, priorité 2013-12-09.
- **DONNÉE** : carrier lactose revendiqué **d10 20–65 · d50 80–120 · d90 130–180 µm**,
  **fines < 10 µm : moins de 10 %** ; BUD 50–500 µg, FOR 1–20 µg ; uniformité ± 15 %.
- **CONFIANCE** : **FAIT CONFIRMÉ**.
- **INTERPRÉTATION** : fenêtre située **entre SV003 et SV010** `INFÉRENCE HAUTE CONFIANCE`.
- **CONSÉQUENCE** : un mélange SV003/SV010 permet de viser une granulométrie de carrier
  documentée pour un couple BUD/FOR. FTO à instruire (device Spiromax).

## P10 — Fines extrinsèques et budésonide (Kinnunen et al.)

- **SOURCE** : Kinnunen H, Hebbink G, Peters H, Huck D, Makein L, Price R.
  *Extrinsic lactose fines improve dry powder inhaler formulation performance of a cohesive batch
  of budesonide via agglomerate formation and consequential co-deposition.*
  Int J Pharm 2015;478(1):53-59.
- **DONNÉE** : l'augmentation de la teneur en **fines de lactose < 4,5 µm** augmente **à la fois**
  la FPF **et** le MMAD du budésonide ; analyse Raman de l'étage 2 du NGI : plus il y a de fines,
  plus des **agglomérats budésonide–lactose** sont délivrés (NGI, Cyclohaler, 90 L/min).
- **CONFIANCE** : **FAIT CONFIRMÉ**.
- **INTERPRÉTATION** : les fines n'agissent pas seulement par saturation de sites : elles font
  **co-déposer** le budésonide sous forme d'agglomérats médicament–fines.
- **CONSÉQUENCE** : si la **FPD du budésonide** est faible, la première correction à essayer est
  **l'ajout de fines** (L4), pas un changement d'architecture.

## P11 — Cinétique de mélange en tumbler

- **SOURCE** : *Mixing Time Effects on the Dispersion Performance of Adhesive Mixtures for
  Inhalation.* PLOS ONE 2013;8(7):e69263.
- **DONNÉE** : salmétérol et fluticasone sur lactose fin (63–90 µm) ou grossier (250–315 µm),
  **Turbula 90 rpm, de 0,5 à 780 min**. Trois processus superposés : **désagglomération
  (0–10 min)**, **compression / press-on (0–60 min)**, **ré-agglomération (> 60 min)** ;
  « l'effet du temps de mélange est le plus marqué dans les **120 premières minutes** ».
  Comportements opposés selon l'actif et le débit.
- **CONFIANCE** : **FAIT CONFIRMÉ** (actifs différents des nôtres).
- **INTERPRÉTATION** : il n'existe pas de durée universelle ; 3 × 15 min = 45 min nous place dans
  le régime des press-on forces.
- **CONSÉQUENCE** : **mesurer** notre cinétique (embarquée dans L2 : 5/10/15/25 min) plutôt que
  de copier une durée ; ne pas allonger.

## P12 — Ordre d'ajout des composants ternaires

- **SOURCE** : *The relationship between drug concentration, mixing time, blending order and
  ternary dry powder inhalation performance.* Int J Pharm 2010 (PMID 20211715). Et
  *Selected addition of ternary component at specific mixing order…* J Pharm Investig 2024.
- **DONNÉE** : à **15 min**, ni la concentration d'actif ni l'ordre n'ont d'effet sur la FPF ;
  à **30 min**, **fines + carrier d'abord** donne une FPF supérieure aux faibles concentrations
  d'actif ; à 60 min, l'inverse à 0,5 % de salbutamol. — Ternaires multiples : **fines 5 % puis
  MgSt 0,5 % → FPF 46,55 %** ; **MgSt puis fines → 33,86 %**.
- **CONFIANCE** : **FAIT CONFIRMÉ** (actifs différents).
- **INTERPRÉTATION** : l'ordre d'ajout est un facteur réel mais **couplé au temps de mélange** ;
  à faible concentration d'actif, pré-conditionner le carrier avec les fines est favorable.
- **CONSÉQUENCE** : justifie l'architecture F (**carrier pré-conditionné**, lot L4) ; et impose de
  **fixer le temps de mélange avant** de conclure quoi que ce soit sur l'ordre.

## P13 — Co-agglomération de deux actifs sur un carrier commun

- **SOURCE** : *Preparation and Evaluation of Single and Co-Engineered Combination Inhalation
  Carrier Formulations for the Treatment of Asthma* (salbutamol base + dipropionate de
  béclométasone, mélange physique et co-spray-dried, NGI + microscopie Raman haut débit).
- **DONNÉE** : les deux actifs présentent des profils de dépôt par étage **significativement
  différents** ; une **co-agglomération SB–BDP est observée dans le mélange physique**.
- **CONFIANCE** : **FAIT CONFIRMÉ** (couple d'actifs différent du nôtre).
- **INTERPRÉTATION** : dans un mélange physique de deux actifs sur un carrier commun,
  les actifs **s'associent entre eux** et s'influencent mutuellement.
- **CONSÉQUENCE** : **preuve de mécanisme** la plus proche de notre hypothèse principale ; justifie
  de ne jamais mettre BUD et FOR en contact à l'état pur → architecture B.

## P14 — Précédent réglementaire du stéarate de magnésium en gélule DPI

- **SOURCE** : SmPC Seebri® Breezhaler et Ultibro® Breezhaler (emc / EMA).
- **DONNÉE** : chaque gélule contient **lactose monohydraté ~23,5–23,6 mg** et **stéarate de
  magnésium**.
- **CONFIANCE** : **FAIT CONFIRMÉ**.
- **INTERPRÉTATION** : le MgSt est accepté dans une gélule DPI à ~25 mg dans un produit autorisé
  en Europe.
- **CONSÉQUENCE** : la branche de secours « MgSt » est **réglementairement praticable**, mais
  reste une dette (stabilité, ordre d'ajout critique) — à n'ouvrir qu'après échec des leviers
  lactose.

## P15 — Symbicort Turbuhaler (contraste)

- **SOURCE** : SmPC Symbicort Turbohaler 100/6, 200/6, 400/12.
- **DONNÉE** : lactose monohydraté **0,81 mg (100/6)**, **0,73 mg (200/6)**, **0,49 mg (400/12)**
  par dose délivrée.
- **CONFIANCE** : **FAIT CONFIRMÉ**.
- **INTERPRÉTATION** : architecture **sans carrier grossier** (agglomérats sphéronisés,
  cf. HU228622B1, densité versée cible 0,30–0,36 g/mL).
- **CONSÉQUENCE** : **ne jamais comparer nos 25 mg à Symbicort** : ce n'est pas la même classe de
  formulation. Le comparateur pertinent est FORPACK / ALENIA / Foracort.

## P16 — Taux de remplissage recommandé par le fabricant de l'Inversina

- **SOURCE** : documentation Bioengineering AG relayée par les fiches distributeurs
  (LabWrench, DirectIndustry) — *la fiche technique primaire n'a pas pu être téléchargée
  (403) ; elle est disponible en interne puisque le site possède la machine* → **Q5**.
- **DONNÉE** : remplir à **environ 2/3 du volume total pour une poudre sèche légère** et à
  **environ 50 % du volume total pour une poudre sèche lourde**. Vitesse recommandée pour le
  modèle **20 L : 20–30 rpm**. La vitesse absolue de brassage reste comparable d'une taille à
  l'autre (20 L à 30 rpm ≈ 2 L à 60 rpm).
- **CONFIANCE** : **INFÉRENCE HAUTE CONFIANCE** (guidance fabricant relayée, source primaire non
  téléchargée) — **à confirmer sur la fiche technique interne avant toute décision engageante**.
- **INTERPRÉTATION** : le lactose d'inhalation (densité versée 570–690 g/L) est une **poudre
  sèche lourde** → la recommandation applicable est **≈ 50 %**. Or `calcul interne` :
  **3 kg = 24 %** · **6 kg = 43–53 %** · **9 kg = 65–79 %**.
- **CONSÉQUENCE — c'est la confirmation la plus directe du diagnostic** : le lot de **9 kg
  travaille nettement au-dessus de la plage recommandée par le fabricant**, tandis que le lot de
  **6 kg tombe exactement dessus**. L'hypothèse 3.1 de l'arbre de causes (« la dernière dilution
  est exécutée au pire taux de remplissage ») n'est plus seulement un raisonnement mécanique :
  elle est adossée à la guidance du constructeur. Cela **renforce** la recommandation de
  répartition 7:2:1 (l'étape à fort remplissage n'a plus que 10 % de la masse à incorporer) et
  la position de repli « figer la taille industrielle à 6 kg ».
  Note complémentaire : **20–30 rpm** est cohérent avec les 22 rpm du Turbula d'EP3175842A1 →
  à 25 rpm, nos 15 min font ≈ **375 révolutions**, contre ≈ 330 pour le brevet. Les deux
  procédés sont donc énergétiquement comparables.

## P17 — Résistance du dispositif RS01 / Aerolizer (débit de test NGI)

- **SOURCE** : documentation Plastiape/Berry CPI et littérature DPI sur le RS01.
- **DONNÉE** : en version standard, le **RS01 est un dispositif à faible résistance atteignant
  une perte de charge de 4 kPa à environ 100 L/min** ; il existe une **version haute résistance
  (4 kPa à 65 L/min)**.
- **CONFIANCE** : **INFÉRENCE HAUTE CONFIANCE** (documentation fabricant relayée).
- **INTERPRÉTATION** : le débit de test Ph. Eur. 2.9.18 (ΔP = 4 kPa) dépend donc de **la version
  exacte** du dispositif dont nous disposons — l'écart est considérable (65 contre 100 L/min) et
  change complètement la FPF mesurée.
- **CONSÉQUENCE** : **identifier la version du dispositif avant le premier NGI** (Q10), et
  **mesurer la résistance** plutôt que la supposer. Repère de comparabilité : l'étude
  d'équivalence de référence de la classe (P3) travaille à l'**ACI, 90 L/min**.

## P18 — Remplissage par dosator à faible masse (Faulhammer et al.)

- **SOURCE** : Faulhammer E, Fink M, Llusá M, Lawrence S, Biserni S, Calzolari V, Khinast J.
  *Low-dose capsule filling of inhalation products: critical material attributes and process
  parameters.* Int J Pharm 2014 (PMID 25087508). · Faulhammer E *et al.* *The effects of material
  attributes on capsule fill weight and weight variability in dosator nozzle machines.*
  Int J Pharm 2014;471(1-2):332-338. · Faulhammer E *et al.* *Development of a design space and
  predictive statistical model for capsule filling of low-fill-weight inhalation products.*
  Drug Dev Ind Pharm 2015.
- **DONNÉES** : six poudres remplies en **gélules taille 3**, trois volumes de chambre de dosage,
  deux vitesses. Corrélation nette entre la **masse de remplissage** et la **taille de particule**,
  la **perméabilité à l'air** et la **compressibilité**. **Plus la masse de remplissage diminue,
  plus le nombre de facteurs influents augmente** : angle de friction à la paroi, densité tassée
  et forme des particules deviennent importants. **Aucune corrélation n'a été trouvée entre les
  attributs du matériau et la variabilité de masse** : celle-ci est dominée par les **paramètres
  procédé**. Un **design space a été établi pour les lactoses d'inhalation** sur des masses de
  **1 à 45 mg**, avec des modèles prédictifs (R² 0,94–0,96), et transposé d'une machine de
  laboratoire à une machine industrielle.
- **CONFIANCE** : **FAIT CONFIRMÉ** (articles peer-reviewed, travaux conduits avec MG2 et GSK).
- **INTERPRÉTATION** : à 25 mg en gélule taille 3, **la masse moyenne** dépend du carrier (PSD,
  perméabilité, compressibilité, densité tassée) mais **la variabilité de masse dépend d'abord
  des réglages machine** (taille de chambre de dosage, hauteur du lit de poudre, pré-compression,
  vitesse).
- **CONSÉQUENCE POUR NOS ESSAIS** : au **Gate 3**, un RSD de masse insuffisant au Modu-C **ne
  justifie pas de changer de carrier en premier**. L'ordre correct est : (1) régler les paramètres
  machine ; (2) seulement ensuite envisager SV010 ou SV001. Cela **corrige** la consigne initiale
  du Gate 3, qui renvoyait directement au carrier. À l'inverse, si la **masse moyenne** visée de
  25 mg n'est pas atteignable, c'est bien un sujet de carrier (densité tassée, perméabilité).
