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

Neutec commercialise également la gamme en 12/400 capsair (gélule) — même architecture, charge de
budésonide doublée. `INFÉRENCE HAUTE CONFIANCE` : lactose ≈ 24,588 mg pour conserver 25,000 mg
(non vérifié sur le KÜB correspondant → **à confirmer**).

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
| Masse de poudre par gélule | — | **INCONNU** (non déclarée au Brésil) |

### Performance aérodynamique publiée

`FAIT CONFIRMÉ` — Andrade-Lima M, Pereira LFF, Fernandes ALG. *Équivalence pharmaceutique de
l'association budésonide + formotérol en gélule unique avec dispositif inhalateur de poudre.*
J Bras Pneumol 2012;38(6). Étude in vitro, HPLC + uniformité de dose délivrée + APSD.

| Paramètre | **Test** : association fixe, **gélule unique**, Aerocaps® | **Référence** : BUD et FOR en **deux gélules séparées**, Aerolizer® |
|---|---|---|
| Teneur budésonide | 111,0 % | 110,5 % |
| Teneur formotérol | 103,8 % | 104,5 % |
| Dose délivrée budésonide | **293,2 µg** | 353,0 µg |
| Dose délivrée formotérol | **10,2 µg** | 11,1 µg |
| **FPF < 5 µm — budésonide** | **45 %** | 54 % |
| **FPF < 5 µm — formotérol** | **56 %** | 52 % |
| Conclusion des auteurs | teneurs, uniformité de dose et diamètres aérodynamiques **appropriés** pour les deux formulations | |

**Interprétations** :
- `calcul interne` — rapport dose délivrée / dose mesurée : **73,3 %** (BUD, sur 400 µg) et
  **85,0 %** (FOR, sur 12 µg). → **Cible réaliste pour notre Gate 3 : ≥ 70 %.**
- `calcul interne` — si la FPF est rapportée à la dose délivrée, FPD ≈ **132 µg** (BUD) et
  **5,7 µg** (FOR). *(Le dénominateur exact — dose délivrée ou dose mesurée — n'est pas
  explicité dans le résumé ; à vérifier sur le texte intégral avant toute utilisation
  réglementaire.)* `INFÉRENCE FAIBLE CONFIANCE` sur le FPD absolu, `FAIT CONFIRMÉ` sur les FPF.
- **Le point le plus important du dossier OSINT** : dans la gélule **unique**, la FPF du
  formotérol (56 %) est **supérieure** à celle du budésonide (45 %) **et supérieure** à celle du
  formotérol en gélule **séparée** (52 %).
  → **CONSÉQUENCE POUR NOS ESSAIS** : la combinaison, correctement formulée, **n'abîme pas le
  formotérol — elle l'améliore**. Un échec sur le formotérol dans un bulk combiné est donc un
  problème de procédé, jamais une fatalité du couple.
- La **formulation de référence de cette étude est exactement la solution de repli adoptée
  historiquement par notre site** (deux gélules séparées). L'industrie a démontré publiquement
  qu'on peut faire aussi bien — et mieux sur le formotérol — en gélule unique.

---

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
- Une gélule BUD/FOR **12/200 et 12/400**, **25,000 mg**, **lactose pour seul excipient**,
  gélatine, blister Alu/Alu, 24 mois, **existe et est autorisée depuis 2013**.
- Une gélule unique BUD/FOR atteint **FPF 45–56 %** et **dose délivrée 73–85 %**, sans pénaliser
  le formotérol.
- Le système carrier est **accordé au device** (25 mg en gélule vs 13 mg en multidose chez le
  même fabricant).

**Ce que l'on ne peut pas affirmer** (et qu'il ne faut pas citer en interne comme un fait) :
le grade de lactose employé, le taux de fines, l'architecture de prémélange, le mélangeur,
les temps de mélange, la taille de lot de ces produits. **Tous INCONNUS.**

**Ce que l'on en déduit pour le projet** : notre cahier des charges n'est pas ambitieux — il est
**standard**. Le travail à faire n'est pas d'inventer une formule, mais de faire converger
**notre** procédé vers ce que le marché fait déjà.
