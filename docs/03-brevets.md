# Patent intelligence — exemples extraits et classement d'applicabilité

Règle appliquée : **on ne lit pas seulement les revendications, on extrait les exemples.**
Un brevet dont les exemples ne sont pas reproductibles chez nous est classé « incompatible »,
même si ses revendications sont séduisantes.

Classement : **① Directement applicable** · **② Adaptable** · **③ Intéressant pour le mécanisme
seulement** · **④ Incompatible avec nos équipements**

---

## ① EP3175842A1 — « Dry powder mixing process »

| | |
|---|---|
| Déposant | Alfred E. Tiefenbacher GmbH & Co. KG / Naonopharm Ltd |
| Priorité | **2015-12-03** |
| Statut | demande publiée — **vérifier le statut et les revendications délivrées avant toute exploitation revendiquée** |

**Procédé revendiqué** — c'est, mot pour mot, le procédé maison :
1. première portion du carrier lactose dans le mélangeur ;
2. **totalité** de l'actif par-dessus ;
3. deuxième portion du carrier par-dessus (**sandwich à 3 couches**) ;
4. mélange, puis **tamisage optionnel** ;
5. **troisième portion** du carrier, mélange, tamisage optionnel.

**Conditions** : **Turbula® 22 rpm, 15 minutes par étape de mélange**. Le carrier est divisé en
**trois portions non nécessairement égales**.

**Actifs exemplifiés** : bromure de tiotropium monohydraté (exemples chiffrés, **0,41 % m/m**) ;
la description cite aussi terbutaline, salbutamol, salmétérol, **formotérol**, **budésonide**,
ciclésonide, mométasone, fluticasone, béclométasone, ipratropium.

**Exemples — effet de la répartition des trois portions** :

| Exemple | 1re : 2e : 3e | Assay (%) | RSD (%) | AV |
|---|---|---|---|---|
| 3 | **7 : 2 : 1** | 100,4 | **2,9** | **7,1** |
| 2 | 5 : 2 : 3 | 99,9 | 3,3 | 7,8 |
| 5 | 4 : 1 : 5 | 101,0 | 3,2 | 7,7 |
| 6 | 2 : 1 : 7 | 101,5 | 4,1 | 10,0 |
| 4 | 5 : 1 : 4 | 102,2 | 4,8 | 12,5 |

*(taille de lot et FPF non fournies dans le document)*

**SOURCE → DONNÉE → CONFIANCE → INTERPRÉTATION → CONSÉQUENCE**
Brevet EP3175842A1 → la répartition du carrier en trois portions modifie l'AV d'un actif à
0,41 % m/m dans un rapport de 1 à 1,8, à formule et procédé constants → **FAIT CONFIRMÉ** (sur
le tiotropium ; **INFÉRENCE HAUTE CONFIANCE** pour la transposition au formotérol) → la
répartition est un **facteur de procédé de premier ordre**, gratuit → **passer de 3:3:3 à 7:2:1
dès le lot E3**, et ne plus considérer la répartition comme un simple détail logistique.

⚠️ **Liberté d'exploitation** : priorité 2015. Si notre procédé « sandwich + trois fractions »
est antérieurement et publiquement exploité en interne, une antériorité d'usage peut exister.
**À instruire par le conseil PI** (`memory/questions-ouvertes.md` Q8). Ce point ne conditionne
pas le développement.

---

## ① US9616024 / US9345664 / US9987229 — « Process for preparing a medicament »

| | |
|---|---|
| Déposant | **Norton Healthcare Ltd** (groupe Teva/Ivax) |
| Priorité | **2003-09-02** → protection très probablement **expirée** (INFÉRENCE HAUTE CONFIANCE) |

**Problème résolu** (cité par le brevet) : *le budésonide, molécule hydrophobe, était
traditionnellement réputé nécessiter un **mélangeur à haut cisaillement** pour former un mélange
homogène avec le lactose.* Le brevet démontre qu'un **tamisage préalable formant des agglomérats
lâches calibrés** permet d'obtenir la même homogénéité en **bas cisaillement**.

**Procédé revendiqué** : (1) tamiser l'actif à travers une maille de 50–3000 µm pour former des
agglomérats lâches ; (2) combiner avec le carrier ; (3) mélanger jusqu'à ce que **≥ 90 % de
l'actif soit sous 50 µm**.

### Exemple 1 — Budésonide
Lactose grossier (fraction tamisée 63–90 µm), budésonide micronisé (< 10 µm), **50 g**, **9,6 % m/m**.
Mélange géométrique, **Turbula T2C, gear 3, 10 min**. Budésonide tamisé à **250 µm** avant mélange ;
mélange final tamisé à 355 µm.

| Variante | RSD | Récupération |
|---|---|---|
| tamisée (blend 1) | **4,6 %** | 88,5 % |
| **non tamisée** (blend 2) | **14,3 %** | 79,6 % |
| tamisée + tamisage final (blend 3) | **1,5 %** | 82,0 % |

### Exemple 2 — Formotérol
Lactose grossier 63–150 µm, formotérol fumarate dihydraté micronisé (< 10 µm), **100 g**,
**0,265 % m/m**, même procédé.

| Variante | RSD | Récupération |
|---|---|---|
| non tamisée | 1,2 % | 91,4 % |
| **tamisée 250 µm** | **0,9 %** | **99,6 %** |

### Exemple 4 — EDA (5 lots) : FPF 51–65 %, RSD 8,3–11,1 %, récupération 91,7–94,0 %
(Turbula gear 3, **20 min**, tamisage final < 355 µm)

### Exemple 6 — Salbutamol, étude de mélange en trois étapes
Lactose tamisé à l'air 75–100 µm ; salbutamol tamisé à 250 ou 355 µm. Trois conditions :
Turbula 22 rpm, Turbula 46 rpm, mélangeur à cisaillement ~1400 rpm. Prélèvements à
1, 3, 5, 10, 15, 20, 30 min.
- **Turbula : optimum à 15 min** ; cisaillement : optimum à 5 min.
- Agglomérats **< 355 µm → FPF 43,6–42,2 %** vs **< 250 µm → FPF 38,5–31,2 %**.
- **L'augmentation du temps de mélange diminue la FPF.**

**Critère d'homogénéité du brevet : RSD ≤ 5 %** (HPLC, prises multiples).

**CONSÉQUENCES POUR NOUS** :
1. Notre tamisage à 250 µm **est** le mécanisme qui rend l'Inversina suffisante → **le conserver**.
2. **Ne jamais acheter un mélangeur à haut cisaillement** pour le budésonide : ce brevet montre
   que c'est inutile.
3. **15 min en tumbler est un optimum, pas un plancher** → ne pas allonger.
4. Donnée contre-intuitive à garder : si notre FPD est faible **malgré** une bonne CU, une maille
   **plus grossière** (355 µm) sur l'étape de désagglomération peut améliorer la FPF. À ne tester
   qu'en dernier recours, car cela dégrade le pire cas d'agglomérat de formotérol.

---

## ② US7879833 / US8258124 — « Combination medicament » (corticoïde + formotérol)

| | |
|---|---|
| Déposant | Nycomed GmbH → **Covis Pharma** |
| Priorité | **2002-12-12** → **expiré** (INFÉRENCE HAUTE CONFIANCE) |
| Actifs | **ciclésonide + R,R-formotérol** (pas budésonide) |

**Pourquoi c'est le brevet le plus pertinent du dossier** : ce sont les **seuls exemples publics
chiffrés d'une association corticoïde + formotérol en poudre sèche par voie de mélange
classique**, et ils font tous un **prémix formotérol dédié**.

### Exemple 1 — Gélule d'inhalation (**notre format**)
- Ciclésonide micronisé 400 mg ; **formotérol fumarate dihydraté micronisé 119 mg** ;
  lactose monohydraté Ph. Eur. **36,1 g + 63,0 g** (deux portions).
- Mélange **Turbula, en deux portions** ; **tamisage 0,71 mm** ; transfert en mélangeur planétaire.
- **25 mg en gélule taille 3.** → 100 µg de ciclésonide + 24 µg de R,R-formotérol par bouffée.

### Exemple 2 — Multidose, **double prémix**
- **Formotérol 300 mg prémélangé avec 97,2 g de lactose** (≈ 0,31 % m/m) au Turbula ;
- **ciclésonide 2,5 g prémélangé avec 250 g de lactose** ;
- puis **650 g de lactose** de dilution, mélangeur à pales. Lactose désaggloméré au broyeur à
  tamis au préalable. Tamisage 0,5 mm.

### Exemple 3 — Multidose, **prémix formotérol concentré**
- **Formotérol fumarate dihydraté 60 mg + 7,27 g de lactose** → **prémix à 0,82 % m/m** ;
  tamisage 0,5 mm ; Turbula ; **prémix re-tamisé** ;
- ciclésonide 2,67 g tamisé 0,5 mm + **90 g de lactose** ajoutés **ensuite**.

**SOURCE → DONNÉE → CONFIANCE → INTERPRÉTATION → CONSÉQUENCE**
US7879833/US8258124 exemples 2 et 3 → un prémix dédié du formotérol à **0,3–0,8 % m/m**, tamisé,
est réalisé **avant** toute rencontre avec le corticoïde → **FAIT CONFIRMÉ** → l'architecture
« prémix β2 d'abord » est la pratique documentée du seul déposant ayant publié des exemples sur
ce type d'association → **notre prémix FOR à ≈ 1 % m/m n'est pas une invention à risque, c'est
une transposition directe**. Le lactose est en outre désaggloméré **avant** usage — à reprendre.

---

## ② US10449147 / US10226421 / ES2837040 — Zambon SpA

| | |
|---|---|
| Priorité | 2013-04-10 (US10226421) et **2014-10-08** (US10449147) |
| Actifs | **budésonide + formotérol** |

**Revendications** : trois poudres **spray-dried** (budésonide/leucine/lactose ;
formotérol/leucine/lactose ; diluant leucine/lactose), FPF > 60 %, fraction délivrée > 80 %,
rapport molaire BUD:FOR 15:1 à 40:1, doses 30–180 µg BUD et 1,5–5,5 µg FOR.

**Ce qui est directement transposable — le système carrier** :
- **Respitose® SV003 (grossier) 85–96 %** + **Lacto-Sphere® MM3 (fin) 4–15 %** ;
  **l'optimum cité est 91 : 9**, retenu parce qu'il donne à la fois une fraction délivrée et une
  FPF élevées **tout en gardant le mélange homogène dans le temps**.
- Granulométries : **grossier X50 35–75 µm** ; **fin X50 1,5–10 µm**.
- **Gélules taille 3 HPMC**, inhalateur **RS01 modèle 7 (Plastiape, type Aerolizer)**, MSLI,
  débit donnant 4 kPa. Masse totale **15 mg** par gélule dans l'exemple 3.
- Mélange : les poudres actives sont déposées **entre deux couches préformées de mélange de
  lactose** (**sandwich**), Ultra Turrax T10, 5 min, lot de 3,5 g. Autres mélangeurs listés :
  Turbula, mélangeur en V, double cône, cube, planétaire, etc.

**Ce qui est incompatible** : les actifs sont obtenus par **spray drying** hydro-alcoolique
(70/30 eau/éthanol, Büchi B290) avec **leucine** — nous n'avons ni spray dryer ni justification
d'ajouter de la leucine.

**CONSÉQUENCE POUR NOUS** : si le Gate 4 impose d'ajouter des fines, la **fenêtre publiée
utile est 4–15 % (optimum ≈ 9 %) sur base SV003**. C'est la référence chiffrée qui justifiera
un éventuel achat de Lactohale LH230/LH300 — et, avant cela, un essai avec **8 % de ML001**.

---

## ② US11642475 / BR112016011996B1 — Pharmachemie B.V. (Teva), BF Spiromax

| | |
|---|---|
| Priorité | **2013-12-09** |
| Objet | DPI multidose budésonide/formotérol |

**Carrier revendiqué** : **d10 20–65 µm · d50 80–120 µm · d90 130–180 µm · fines < 10 µm : < 10 %**.
Doses : BUD 50–500 µg (80, 160, 320), FOR 1–20 µg (4,5, 9). Uniformité de dose **± 15 %** sur
la durée de vie du dispositif et de 40 à 90 L/min. Désagglomérateur cyclonique dans le device.

**INFÉRENCE HAUTE CONFIANCE** : cette fenêtre est **entre SV003 (d50 53–66) et SV010
(d50 95–125)**. Un mélange SV003/SV010 permet de la viser. Utile comme **cible granulométrique
de référence** si l'on doit justifier un choix de carrier pour un couple BUD/FOR.
⚠️ Revendications liées au device Spiromax → FTO à instruire.

---

## ③ Intéressants pour le mécanisme seulement

| Référence | Apport | Pourquoi pas plus |
|---|---|---|
| **HU228622B1** (AstraZeneca, prio. 1997) | formulation BUD/FOR de **densité versée 0,30–0,36 g/mL** (exemple mesuré : 0,32 g/mL, à partir de 0,0315 partie de formotérol fumarate dihydraté pour 2,969 parties de lactose) | procédé : micronisation séparée, conditionnement, mélange Turbula, **re-micronisation à ~1 bar**, compactage, **sphéronisation**, tamisage 0,5–1,0 mm → hors de portée |
| Littérature **CAB** (AFM, Pharm Res 2004 I & II) | budésonide micronisé : valeur CAB **0,62** (d90 = 4,40 µm) → actif **plutôt cohésif**, tendance à l'auto-agglomération | outil de préformulation, pas un procédé |
| **Kinnunen et al., Int J Pharm 2015;478:53-59** | les **fines de lactose < 4,5 µm** augmentent la FPF **et** le MMAD du budésonide → le médicament est délivré **en agglomérats médicament–fines** co-déposés (confirmé par Raman sur l'étage 2, NGI/Cyclohaler 90 L/min) | explique **pourquoi** les fines aident le budésonide — mécanisme, pas recette |
| **PLOS One 2013, e69263** | Turbula 90 rpm, 0,5 → 780 min : trois processus superposés — désagglomération (0–10 min), **press-on (0–60 min)**, ré-agglomération (> 60 min) ; l'essentiel se joue dans les **120 premières minutes** | justifie de **mesurer** notre cinétique plutôt que de copier une durée |
| **Ordre de mélange ternaire** (Int J Pharm 2010) | à 15 min : aucun effet de l'ordre ; à **30 min** : **fines + carrier d'abord** donne une FPF supérieure à faible concentration d'actif ; à 60 min : l'inverse à 0,5 % | justifie l'architecture F (**carrier pré-conditionné**) et impose de fixer le temps de mélange avant de conclure sur l'ordre |
| **Ordre des ternaires multiples** (J Pharm Investig 2024) | fines 5 % **puis** MgSt 0,5 % → FPF **46,55 %** ; MgSt **puis** fines → **33,86 %** | si le MgSt devient nécessaire, **l'ordre d'ajout est un paramètre critique**, pas un détail |

---

## ④ Incompatibles avec nos équipements

| Voie | Raison |
|---|---|
| Zambon (leucine + spray drying) | pas de spray dryer, pas de justification d'un nouvel excipient |
| AstraZeneca Turbuhaler (sphéronisation) | pas de re-micronisation, pas de sphéroniseur |
| Toute voie « co-micronisation » / particules ingéniérées | exclue par le hand-off |
| Mélangeur à haut cisaillement | non disponible — **et démontré inutile** par US9616024 |

---

## Synthèse : ce que les brevets nous disent de faire, demain matin

1. **Prémix formotérol dédié à ≈ 1 % m/m, tamisé** (Nycomed, ex. 2 et 3). ①②
2. **Répartition du lactose en 7 : 2 : 1** (Tiefenbacher, ex. 3). ①
3. **Conserver le tamisage 250 µm et le mélange bas cisaillement 15 min** (Norton). ①
4. **Ne pas allonger le mélange** (Norton ex. 6 ; PLOS One). ①③
5. **Si fines nécessaires : 4–15 % sur base SV003, optimum ≈ 9 %** (Zambon). ②
6. **Désagglomérer le lactose avant usage** (Nycomed, ex. 2). ②
