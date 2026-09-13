# OSINT — Produits Budésonide/Formotérol commercialisés et « formulation fingerprints »

Méthode : sources primaires d'abord (KÜB turcs, bulas brésiliennes, SmPC, brevets, articles
peer-reviewed), sources secondaires seulement comme piste. Chaque élément porte son niveau de
confiance. **Aucune inférence n'est présentée comme une donnée officielle.**

---

## 1. Turquie — FORPACK (Neutec İnhaler) — **le produit jumeau de notre cible**

### FORPACK 12/200 mcg capsair — poudre pour inhalation en gélule

| Élément | Valeur | Confiance |
|---|---|---|
| Formotérol fumarate dihydraté | **12 mcg** / gélule | **FAIT CONFIRMÉ** (KÜB §2) |
| Budésonide | **200 mcg** / gélule | **FAIT CONFIRMÉ** (KÜB §2) |
| **Lactose** | **24,7880 mg** / gélule | **FAIT CONFIRMÉ** (KÜB §2) |
| **Masse totale** | **25,0000 mg** | `calcul interne` : 24,7880 + 0,200 + 0,012 |
| Liste des excipients (§6.1) | **« Laktoz »** — un seul excipient | **FAIT CONFIRMÉ** |
| Forme | gélule, coiffe violet clair transparent, corps naturel, poudre blanche | **FAIT CONFIRMÉ** (KÜB §3) |
| Enveloppe | **gélatine** (KÜB §4.2 : « la gélule en gélatine peut se fragmenter ») | **FAIT CONFIRMÉ** |
| Device | inhalateur mono-dose dédié, **bouton de perforation** (« delme düğmesi »), capot à poussière, embout, chambre centrale | **FAIT CONFIRMÉ** |
| Conditionnement | blister **Alu/Alu**, 60 ou 120 gélules + inhalateur | **FAIT CONFIRMÉ** (§6.5) |
| Conservation / péremption | **< 25 °C, au sec** / **24 mois** | **FAIT CONFIRMÉ** (§6.3–6.4) |
| Titulaire / AMM | Neutec İnhaler İlaç, Sakarya — n° 250/43, **1re AMM 06/05/2013** | **FAIT CONFIRMÉ** (§7–9) |
| Incompatibilités (§6.2) | « non applicable » | **FAIT CONFIRMÉ** |
| Taille de gélule | taille 3 | **INFÉRENCE HAUTE CONFIANCE** (standard DPI 25 mg ; taille 3 HPMC utilisée dans les exemples Zambon avec RS01) |
| Architecture du mélange | mélange ordonné carrier-based (le lactose fait 99,15 % de la masse) | **INFÉRENCE HAUTE CONFIANCE** |
| Grade de lactose | — | **INCONNU** |
| Présence de fines extrinsèques | — | **INFÉRENCE FAIBLE CONFIANCE** (probable) |
| Procédé de prémélange | — | **INCONNU** |

### FORPACK 12/400 mcg discair — poudre pour inhalation multidose

| Élément | Valeur | Confiance |
|---|---|---|
| FOR / BUD | 12 mcg / 400 mcg par dose | **FAIT CONFIRMÉ** |
| **Lactose** | **12,5880 mg** par dose | **FAIT CONFIRMÉ** |
| **Masse totale** | **13,0000 mg** par dose | `calcul interne` |
| Conditionnement | Alu/Alu, 60 doses, dans le dispositif Discair | **FAIT CONFIRMÉ** |

> **Enseignement structurant** : **le même industriel, pour le même couple d'APIs, utilise
> 25,0 mg en gélule et 13,0 mg en multidose.** `INFÉRENCE HAUTE CONFIANCE` : le système carrier
> est accordé au device et à la plateforme de remplissage.
> **Conséquence pour nous** : notre masse de 25 mg est le bon choix pour une gélule, et aucune
> donnée multidose (y compris Symbicort) ne doit être transposée telle quelle.

### FORPACK 12/400 mcg capsair — gélule *(question Q12 fermée)*

| Élément | Valeur | Confiance |
|---|---|---|
| FOR / BUD | 12 mcg / 400 mcg par gélule | **FAIT CONFIRMÉ** (KÜB §2) |
| **Lactose** | **24,588 mg** / gélule | **FAIT CONFIRMÉ** |
| **Masse totale** | **25,0000 mg** | `calcul interne` : 24,588 + 0,400 + 0,012 |
| Excipients (§6.1) | **« Laktoz »** — un seul | **FAIT CONFIRMÉ** |
| Forme | coiffe **violet foncé** transparent, corps naturel (le 12/200 a une coiffe violet **clair**) | **FAIT CONFIRMÉ** |
| Conditionnement / conservation | Alu/Alu, 60 ou 120 gélules ; < 25 °C au sec ; 24 mois | **FAIT CONFIRMÉ** |
| AMM | **250/44**, 1re autorisation **06/05/2013**, KÜB révisé 07/01/2015 | **FAIT CONFIRMÉ** |

> **Le même fabricant utilise le même bulk à 25,000 mg pour les deux dosages**, la seule
> différence étant l'échange budésonide ↔ lactose (200 → 400 µg de BUD ; 24,788 → 24,588 mg de
> lactose). C'est exactement notre stratégie « un seul bulk, deux dosages » — **elle est validée
> par un produit autorisé**.

---

## 2. Brésil — ALENIA (Biosintética / Aché) — **la seule performance publiée**

| Élément | Valeur | Confiance |
|---|---|---|
| Dosages | 6/100, 6/200, **12/400** mcg, gélules pour inhalation | **FAIT CONFIRMÉ** (bula) |
| Excipient | **lactose monohydraté** (seul excipient du contenu) | **FAIT CONFIRMÉ** (bula, « Excipiente: lactose monoidratada ») |
| Device | **Aerocaps®** | **FAIT CONFIRMÉ** |
| Dose mesurée → dose délivrée (6/100) | FOR 6 → **4,5 mcg** ; BUD 100 → **80 mcg** | **FAIT CONFIRMÉ** (bula) |
| Colorants de l'enveloppe | bleu brillant, rouge allura, jaune orangé (6/200) ; bleu brillant, érythrosine (12/400) | **FAIT CONFIRMÉ** (bula) — **enveloppe uniquement**, pas le contenu |
| Présentations | 15, 30, 60 gélules, avec inhalateur ou en recharge | **FAIT CONFIRMÉ** |
| Masse de poudre par gélule | **25,56 ± 0,79 mg** (n = 20, mesurée sur le 12/400) | **FAIT CONFIRMÉ** (J Bras Pneumol 2012) |

### Performance aérodynamique et uniformité publiées — **données complètes**

`FAIT CONFIRMÉ` — Andrade-Lima M, Pereira LFF, Fernandes ALG. *Equivalência farmacêutica da
formulação combinada de budesonida e formoterol em cápsula única com dispositivo inalador de pó.*
J Bras Pneumol 2012;38(6):748-756. Étude in vitro réalisée au laboratoire accrédité T&E Analítica
(Campinas), **sous supervision directe de deux techniciens de l'ANVISA**.

**Méthodes** : dosage HPLC-UV ; uniformité de dose délivrée par **DUSA-DPI** (Westech) ;
APSD par **impacteur en cascade d'Andersen (ACI modèle 8301-60, Copley)** ; teneur en eau par
Karl Fischer ; contrôles microbiologiques. Débit de référence cité : **90 L/min**.
**Définition explicite du texte** : *fine particle fraction* = dose de particules fines **divisée
par la dose délivrée totale** (l'ambiguïté de dénominateur est donc levée).

| Variable | **Test** : gélule **unique** BUD/FOR 400/12, Aerocaps® | **Réf.** : BUD seul, gélule séparée | **Réf.** : FOR seul, gélule séparée |
|---|---|---|---|
| Masse de gélule, mg (n = 20) | **25,56 ± 0,79** | 25,35 ± 1,08 | 25,19 ± 0,70 |
| *RSD de masse* `calcul interne` | **3,09 %** | 4,26 % | 2,78 % |
| Teneur, % | BUD 111,41 · FOR 103,80 | BUD 110,59 | FOR 104,51 |
| Dose délivrée, µg (n = 30) | BUD **293,24 ± 12,91** · FOR **10,23 ± 0,47** | BUD 353,04 ± 11,48 | FOR 11,07 ± 0,60 |
| *RSD de dose délivrée* `calcul interne` | BUD **4,40 %** · FOR **4,59 %** | BUD 3,25 % | FOR 5,42 % |
| Dose délivrée / dose étiquetée | BUD **73 %** · FOR **85 %** | BUD 88 % | FOR 92 % |
| Uniformité de teneur, % (n = 10) | BUD **103,68 ± 1,68** · FOR **97,93 ± 1,98** | BUD 107,20 ± 5,83 | FOR 100,00 ± 3,23 |
| ***RSD d'uniformité de teneur*** `calcul interne` | **BUD 1,62 % · FOR 2,02 %** | **BUD 5,44 %** | **FOR 3,23 %** |
| Dose de particules fines, µg (% de la dose délivrée) | BUD **140,67 (44,71 %)** · FOR **6,18 (56,13 %)** | BUD 181,53 (53,56 %) | FOR 5,46 (52,05 %) |
| *FPD en % de la dose étiquetée* `calcul interne` | BUD **35,2 %** · FOR **51,5 %** | BUD 45,4 % | FOR 45,5 % |

**Les trois enseignements, par ordre d'importance :**

1. **La gélule combinée est plus uniforme que les deux gélules séparées qu'elle remplace.**
   RSD d'uniformité de teneur : **formotérol 2,02 % en combiné contre 3,23 % en mono-produit** ;
   **budésonide 1,62 % contre 5,44 %**. C'est l'inverse exact de l'intuition qui a conduit notre
   site à séparer les deux formulations — et c'est mesuré sur des produits commerciaux, sous
   supervision de l'autorité.
2. **Le formotérol gagne aussi en masse fine absolue** : FPD **6,18 µg** en combiné contre
   **5,46 µg** en gélule séparée, malgré une dose délivrée plus faible (10,23 contre 11,07 µg).
   `INFÉRENCE HAUTE CONFIANCE` : cohérent avec une saturation des sites de haute énergie du
   lactose par le budésonide, 33 fois plus abondant, qui laisse au formotérol des sites plus
   faibles dont il se détache mieux.
3. **25 mg est la norme de la classe, y compris pour un mono-produit formotérol** : la gélule de
   référence « formotérol seul » pèse **25,19 mg** — une formulation à 0,048 % m/m dans 25 mg,
   c'est-à-dire exactement notre cas, existe donc aussi en mono-produit commercial.

**Cibles chiffrées pour nos essais, issues du marché** :
RSD de masse ≈ 3 % · RSD d'uniformité de teneur ≤ 2 % atteignable (notre critère de 5 % est
prudent) · RSD de dose délivrée ≈ 4,5 % · dose délivrée 73–85 % · FPF 45 % (BUD) et 56 % (FOR).

## 3. Inde

| Produit | Titulaire | Forme | Dosages | Excipients déclarés | Device | Confiance |
|---|---|---|---|---|---|---|
| **Foracort Rotacaps** | Cipla | gélule | FOR 6 µg + BUD 100 / 200 / 400 µg | lactose | Rotahaler | **FAIT CONFIRMÉ** (notice Cipla) |
| **Formonide** | Lupin | gélule | FOR 6 µg + BUD 100 / 200 / 400 µg | lactose | Rotahaler | **FAIT CONFIRMÉ** |
| Budamate / génériques | divers | gélule | idem, + versions avec glycopyrronium | lactose | Rotahaler | **FAIT CONFIRMÉ** |
| Masse de poudre par gélule | — | — | — | — | — | **INCONNU** (non déclarée en Inde) |

> Le marché indien est **entièrement en 6 µg de formotérol**. Notre dosage **12 µg** est le
> format turc/brésilien. `INFÉRENCE HAUTE CONFIANCE` : à 12 µg, la contrainte d'uniformité est
> **deux fois moins sévère** qu'à 6 µg — d'autres industriels font déjà plus difficile que nous.

---

## 4. Europe / monde — pour contraste (produits sans carrier ou multidose)

| Produit | Titulaire | Architecture | Lactose | Enseignement |
|---|---|---|---|---|
| **Symbicort Turbuhaler** | AstraZeneca | agglomérats sphéronisés, **sans carrier grossier** | 0,81 mg (100/6) · 0,73 mg (200/6) · **0,49 mg (400/12)** par dose délivrée `FAIT CONFIRMÉ` | architecture inaccessible (re-micronisation + sphéronisation, brevet HU228622B1, densité versée cible 0,30–0,36 g/mL) |
| **BF Spiromax** | Teva / Pharmachemie | multidose carrier-based | PSD revendiquée : d10 20–65, d50 80–120, d90 130–180 µm, **fines < 10 µm : < 10 %** `FAIT CONFIRMÉ` | **fenêtre granulométrique de référence** pour un carrier BUD/FOR — voir `04-lactoses.md` |
| **Seebri® / Ultibro® Breezhaler** | Novartis | gélule carrier-based | **23,5–23,6 mg de lactose + stéarate de magnésium** `FAIT CONFIRMÉ` | **précédent réglementaire du MgSt** dans une gélule DPI à ~25 mg — utile si branche de secours |

---

## 5. Synthèse du « fingerprint » reconstruit

**Ce que l'on peut affirmer :**
- Une gélule BUD/FOR **12/200 et 12/400**, **25,000 mg dans les deux cas**, **lactose pour seul
  excipient**, gélatine, blister Alu/Alu, 24 mois, **existe et est autorisée depuis 2013** — et
  les deux dosages y partagent manifestement le même bulk.
- Une gélule unique BUD/FOR atteint **FPF 44,7–56,1 %**, **dose délivrée 73–85 %** et **RSD
  d'uniformité de teneur de 1,6–2,0 %**, **sans pénaliser le formotérol — en l'améliorant**.
- Un mono-produit **formotérol 12 µg** existe aussi en gélule de **25,19 mg** : notre
  concentration de 0,048 % m/m est une norme de classe, pas une singularité.
- Le système carrier est **accordé au device** (25 mg en gélule vs 13 mg en multidose chez le
  même fabricant).

**Ce que l'on ne peut pas affirmer** (et qu'il ne faut pas citer en interne comme un fait) :
le grade de lactose employé, le taux de fines, l'architecture de prémélange, le mélangeur,
les temps de mélange, la taille de lot de ces produits. **Tous INCONNUS.**

**Ce que l'on en déduit pour le projet** : notre cahier des charges n'est pas ambitieux — il est
**standard**. Le travail à faire n'est pas d'inventer une formule, mais de faire converger
**notre** procédé vers ce que le marché fait déjà.
