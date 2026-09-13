# Petites échelles — 1 kg et 3 kg, avant tout passage industriel

> **Ce document intègre une information interne décisive reçue le 2026-09-13 :**
> le **mono-produit formotérol utilise ML001 seul** ; le **mono-produit budésonide utilise un
> mélange SV003 + ML001**. Elle corrige la recommandation de carrier de la version précédente
> du dossier (voir ADR-015).

---

## 1. Ce que cette information change

### 1.1 Le prémix formotérol se fait sur ML001, pas sur SV003

La version précédente proposait un prémix FOR à 1 % sur **SV003**. C'était une erreur de ma part :
le seul système de carrier dont on sache, en interne, qu'il rend le formotérol homogène et
aérosolisable est **ML001 seul**. Le prémix doit donc être fait sur **ML001**, exactement le
matériau du mono-produit qui fonctionne. On ne change pas ce qui marche.

**Lecture physico-chimique** — cette pratique interne est cohérente avec la théorie, et c'est
rassurant : ML001 est le seul des trois grades à posséder une vraie population fine
(**D10 = 3–7 µm**), et le plus cohésif (Carr > 25 %). À 0,048 % m/m, le formotérol a besoin
d'un grand nombre de sites et d'un environnement de fines — c'est exactement ce que ML001 apporte.
`INFÉRENCE HAUTE CONFIANCE`

### 1.2 L'architecture recommandée devient le **double prémix**

Elle n'est plus « la plus robuste mais la plus lourde » : elle devient **la réunion de deux
procédés déjà validés en interne**.

| Brique | Contenu | Statut |
|---|---|---|
| **Prémix FOR** | FOR + **ML001** | = le mono-produit formotérol, simplement plus concentré |
| **Base BUD** | BUD + **SV003 + ML001** | = le mono-produit budésonide, inchangé |
| **Combinaison finale** | prémix FOR incorporé dans la base BUD | **la seule vraie nouveauté du procédé** |

C'est l'argument le plus fort du plan révisé : **chaque API reste dans le système de carrier qui a
déjà démontré qu'il fonctionnait pour lui**, et l'on ne teste plus qu'une chose — l'étape de
combinaison.

### 1.3 Une nouvelle cause probable de l'échec historique

`INFÉRENCE HAUTE CONFIANCE` — Si le combiné historique a été fabriqué **sur le carrier du
budésonide** (SV003 + ML001, donc pauvre en ML001 comparé au FOR mono qui est à 100 % ML001),
alors **le formotérol a été privé de l'environnement de fines dont dépend son mono-produit**.

C'est une cause distincte de la co-agglomération, parfaitement compatible avec elle, et elle
s'ajoute à l'arbre des causes en **TRÈS PLAUSIBLE** (voir `05-arbre-causes.md`, cause 5.3).
Elle impose de tester **le taux de ML001 du bulk combiné** dès le premier étage d'essais.

### 1.4 La limite honnête du prémix

`calcul interne` — Le prémix FOR à 1 % ne représente que **4,80 % de la masse du lot**, à toutes
les échelles. Après dilution dans la base BUD, le formotérol se retrouve donc majoritairement au
contact de **SV003**, quel que soit le carrier du prémix.

**Le prémix protège le formotérol pendant sa désagglomération ; il ne garantit pas qu'il conserve
son environnement de fines après dilution.** C'est précisément pourquoi le taux de ML001 du bulk
final doit être une variable d'essai, et non un paramètre hérité du budésonide.

---

## 2. Le vrai paramètre d'échelle n'est pas la masse, c'est le volume de cuve

`calcul interne`, densité versée du bulk ≈ 600–630 g/L :

| Masse de lot | Volume de poudre | Dans la cuve **20 L** | Cuve idéale (≈ 50 %) | Plage 40–60 % |
|---|---|---|---|---|
| **1 kg** | 1,67 L | **8 %** ⛔ | **3,3 L** | 2,8 – 4,2 L |
| **3 kg** | 5,00 L | **25 %** ⚠️ | **10,0 L** | 8,3 – 12,5 L |
| **6 kg** | 10,00 L | **50 %** ✅ | 20,0 L | 16,7 – 25,0 L |
| 9 kg | 15,00 L | **75 %** ⚠️ | 30,0 L | 25,0 – 37,5 L |

> **Un lot de 1 kg dans la cuve de 20 L occupe 8 % du volume.** Le lit de poudre ne cascade plus
> correctement : le résultat n'est représentatif **dans aucun sens** — ni pour dire que ça marche,
> ni pour dire que ça ne marche pas.
>
> **Un lot de 1 kg n'est donc légitime qu'avec une cuve de 3 à 4 L.** Si l'Inversina n'accepte pas
> de cuve interchangeable de cette taille (question **Q5**), le 1 kg doit être fait sur un
> mélangeur de paillasse de type Turbula, et être explicitement déclaré comme un essai de
> **formulation**, jamais de procédé.

Et le constat inverse, qui mérite d'être retenu : **6 kg dans la cuve de 20 L tombe pile à 50 %**,
c'est-à-dire exactement la plage recommandée par le constructeur. **Mécaniquement, 6 kg est
l'échelle idéale de cet équipement**, pas 9 kg.

### 2.1 Le prémix ne peut se faire dans l'Inversina 20 L, à aucune échelle

`calcul interne` :

| Lot | Masse du prémix FOR (1 %) | Volume | Remplissage de la cuve 20 L | Cuve de prémix idéale |
|---|---|---|---|---|
| 1 kg | **48,0 g** | 0,08 L | **0,4 %** | ≈ 0,16 L |
| 3 kg | **144,0 g** | 0,24 L | **1,2 %** | ≈ 0,5 L |
| 6 kg | 288,0 g | 0,48 L | 2,4 % | ≈ 1,0 L |
| 9 kg | 432,0 g | 0,72 L | 3,6 % | ≈ 1,4 L |

**Le prémix exige un petit récipient** : cuve Inversina de 0,5 à 2 L si elle existe, sinon
Turbula de paillasse, sinon mélange manuel intensif suivi d'un tamisage. C'est une contrainte
d'équipement qui n'apparaissait pas dans la version précédente du plan.

### 2.2 Le tamisage au Russell n'est pas neutre à 1 kg

`calcul interne` — la rétention d'un tamiseur industriel est une **masse fixe**, donc une perte
**relative** d'autant plus grande que le lot est petit :

| Rétention du Russell | 1 kg | 3 kg | 6 kg | 9 kg |
|---|---|---|---|---|
| 10 g | 1,00 % | 0,33 % | 0,17 % | 0,11 % |
| 20 g | **2,00 %** | 0,67 % | 0,33 % | 0,22 % |
| 50 g | **5,00 %** | 1,67 % | 0,83 % | 0,56 % |

Et cette rétention est probablement **enrichie en fines**, donc en formotérol.
→ **À 1 kg : tamisage manuel** (250 µm, et 212 µm pour le prémix). **À partir de 3 kg : Russell.**
La rétention réelle du Russell reste à mesurer (**Q7**) — une pesée entrée/sortie sur un passage
de lactose seul suffit.

---

## 3. Étage 1 — trois lots de 1 kg *(échelle paillasse)*

**Ce que cet étage démontre** : l'architecture et le **taux de ML001**.
**Ce qu'il ne démontre pas** : rien du procédé industriel — ni le mélange Inversina, ni le Russell,
ni le remplissage.

**Coût total : 1,44 g de formotérol pour les trois lots** — autant qu'**un seul** lot de 3 kg.
C'est l'argument décisif en faveur de cet étage : à 1 kg, on trie trois architectures pour le prix
d'une.

Tous au dosage **12/400** (pire cas formotérol, rapport de masse 33:1).

### Composition des trois lots

| | **E-A** *(témoin)* | **E-B** *(architecture recommandée)* | **E-C** *(carrier enrichi)* |
|---|---|---|---|
| Architecture | co-sandwich : BUD **et** FOR ensemble | double prémix | double prémix |
| Carrier | celui du BUD mono (SV003 + ML001) | celui du BUD mono | **enrichi à ≈ 30 % de ML001** |
| Prémix FOR | aucun | **FOR + ML001, 1 % m/m** | **FOR + ML001, 1 % m/m** |
| Hypothèse testée | reproduit-on le problème ? | séparer les APIs suffit-il ? | le FOR a-t-il besoin de retrouver ses fines ? |

**Masses — lot de 1 kg, 12/400** `calcul interne`

| Composant | E-A | E-B | E-C |
|---|---|---|---|
| Budésonide | 16,00 g | 16,00 g | 16,00 g |
| Formotérol (corrigé du titre) | 0,480 g | 0,480 g | 0,480 g |
| **Prémix FOR** (FOR + ML001 à 1 %) | — | **48,00 g** | **48,00 g** |
| ML001 du prémix | — | 47,52 g | 47,52 g |
| SV003 | *selon ratio BUD mono* | *selon ratio BUD mono* | ≈ 655 g |
| ML001 du carrier | *selon ratio BUD mono* | *selon ratio BUD mono* | ≈ 281 g |
| **ML001 total (% du lactose)** | *≈ 10 %* | **≈ 14,3 %** | **≈ 33 %** |
| **Total** | 1 000,00 g | 1 000,00 g | 1 000,00 g |

> Le ratio SV003:ML001 du mono-produit budésonide est **à récupérer avant de figer ces masses**
> (**Q16**). Le tableau ci-dessus suppose 90:10 pour E-A et E-B ; avec 80:20 le ML001 total
> passe à ≈ 23,9 %, ce qui rapprocherait E-B de E-C et **affaiblirait le contraste entre les deux
> lots** — d'où l'importance de la question.

### Procédé — 1 kg, sur mélangeur de paillasse

**Étape 0 — prémix formotérol (48,00 g), dans un récipient de 0,15 à 0,5 L**
1. Relever HR et T°. Ioniseur en marche.
2. Peser **23,8 g de ML001**, déposer dans le récipient.
3. Peser **0,480 g de FOR** par différence, contenant verre ou inox **mis à la terre**.
4. Déposer le FOR **au centre**, sans contact avec les parois.
5. Recouvrir des **23,8 g** de ML001 restants — **sandwich**.
6. Mélange **3 min**.
7. **Peser** → **tamisage manuel 212 µm** → **repeser**.
8. Mélange **15 min**.
9. **Contrôle libératoire du prémix** : 10 prises de 25 mg, assay FOR, RSD.
   **Ne jamais engager un prémix dont le RSD n'est pas connu.**

**Étape 1 — base budésonide**
10. Préparer le carrier : SV003 + ML001 au ratio retenu, mélange **15 min**, **tamisage manuel
    250 µm**, mélange **5 min**. *(carrier pré-conditionné : les fines sont en place avant l'API)*
11. Prélever **70 %** du carrier. Déposer la moitié dans la cuve.
12. Étaler **BUD 16,00 g**.
13. Recouvrir de l'autre moitié — **sandwich**.
14. Mélange **5 min** → pesée → **tamisage manuel 250 µm** → pesée → mélange **15 min**.

**Étape 2 — combinaison** *(la seule étape réellement nouvelle du procédé)*
15. Étaler **la totalité du prémix FOR (48,00 g)** sur la base budésonide.
16. Recouvrir avec **20 %** du carrier.
17. Mélange **3 min** → pesée → tamisage 250 µm → pesée → mélange **15 min**.

**Étape 3 — dilution finale**
18. Ajouter les **10 %** de carrier restants.
19. Mélange **3 min** → pesée → tamisage 250 µm → pesée → **mélange 15 min**.
    *(on ne termine jamais sur un tamisage)*

**Pour E-A** : étapes 0, 2 et 15–17 supprimées ; BUD **et** FOR sont déposés ensemble à l'étape 12,
et le lactose est réparti 3 : 3 : 3 comme dans le procédé historique.

### Analyses et décision

10 prises de **25 mg** par lot, assay **BUD et FOR sur la même prise**, plus le bilan matière de
chaque tamisage.

| Comparaison | Lecture |
|---|---|
| **E-A échoue, E-B réussit** | la séparation des APIs est la clé → passer E-B à 3 kg |
| **E-B échoue, E-C réussit** | le formotérol a besoin de son environnement de fines → le taux de ML001 est la clé, et la cause 5.3 est confirmée |
| **E-B et E-C réussissent** | prendre **E-B** (moins de ML001 = meilleur écoulement au dosator et meilleure densité au scale-up) |
| **E-A réussit aussi** | le problème historique n'est pas la formulation → aller directement à l'étage 3 (6 kg) |
| **Les trois échouent** | le problème est en amont ou dans le mélange — relire le RSD du prémix (étape 9) avant toute autre hypothèse |

**Corrélation BUD ↔ FOR** à calculer sur chaque lot : `r ≥ 0,6` = signature de co-agglomération.

---

## 4. Étage 2 — un ou deux lots de 3 kg *(premier passage sur les équipements industriels)*

**Ce que cet étage démontre** : que l'architecture gagnante survit à l'**Inversina** et au
**Russell 250 µm**. **Ce qu'il ne démontre pas** : la mécanique de mélange à 9 kg (25 % de
remplissage contre 75 %).

- Architecture retenue à l'étage 1, **répartition 7 : 2 : 1**.
- Prémix FOR **144,0 g** (FOR 1,440 g + ML001 142,56 g), toujours dans un **petit récipient**.
- **Cuve de 8 à 10 L si elle existe** (→ 50–60 % de remplissage, mécanique du 9 kg reproduite pour
  un tiers de l'API). Sinon cuve de 20 L, en sachant que l'on est à 25 %.
- **Russell 250 µm** à partir d'ici, avec **pesée entrée/sortie systématique**.
- Mesures embarquées : prélèvements **avant et après** le tamisage final, **cinétique 5/10/15/25 min**.
- Portes 1 et 2 sur tous les lots ; portes 3 et 4 sur le seul lot gagnant.

**Deuxième lot à 3 kg, seulement si nécessaire** : soit l'architecture alternative restée
ex æquo à l'étage 1, soit le dosage **12/200** (pire cas budésonide).

---

## 5. Étages 3 et 4 — 6 kg puis 9 kg

| Étage | Masse | Remplissage cuve 20 L | Ce qu'il teste |
|---|---|---|---|
| **3** | **6 kg** | **50 %** ✅ | la profondeur de lit, dans la plage constructeur. **C'est l'échelle mécaniquement idéale de cet équipement.** |
| **4** | 9 kg | 75 % ⚠️ | robustesse mécanique hors plage recommandée — **essai de procédé, pas de formulation** |

Si 6 kg passe et 9 kg reste marginal : augmenter les révolutions de la seule dernière étape ;
si insuffisant, **figer la taille industrielle à 6 kg**. C'est une décision économique, pas
formulatoire — et elle est cohérente avec la recommandation du constructeur.

---

## 6. Séquence complète et consommation

| Étage | Lots | Échelle | Équipement | FOR consommé | Durée |
|---|---|---|---|---|---|
| 1 | E-A, E-B, E-C | 1 kg | paillasse (cuve 3–4 L ou Turbula), tamis manuels | **1,44 g** | 3 jours |
| 2 | 1 à 2 lots | 3 kg | Inversina (cuve 8–10 L si possible) + Russell | 1,44 – 2,88 g | 2–3 jours |
| 3 | 1 lot | 6 kg | Inversina 20 L (50 %) + Russell | 2,88 g | 1–2 jours |
| 4 | 1 lot | 9 kg | Inversina 20 L (75 %) + Russell | 4,32 g | 1–2 jours |
| 5 | 12/200 + confirmation | 3 à 6 kg | industriel | 2,88 – 4,32 g | 2–3 jours |
| | | | **Total** | **≈ 13 à 16 g** | **≈ 9 à 13 jours** |

L'étage 1 ajoute **trois lots pour 1,44 g de formotérol** — le coût d'**un seul** lot de 3 kg —
et il trie l'architecture **et** le taux de ML001 avant d'engager le moindre équipement industriel.
C'est le meilleur achat du plan.

---

## 7. Questions à fermer avant de peser quoi que ce soit

| # | Question | Pourquoi elle bloque |
|---|---|---|
| **Q16** | **Quel est le ratio SV003 : ML001 du mono-produit budésonide ?** | il fixe les masses de E-A et E-B, et le contraste avec E-C |
| **Q17** | **Quelle est la masse de remplissage des deux mono-produits** (25 mg ?), et le RSD d'uniformité qu'ils atteignent ? | c'est le repère interne : si le FOR mono est à 3 %, le combiné doit viser 3 %, pas 5 % |
| **Q18** | **À quelle taille de lot les deux mono-produits sont-ils fabriqués**, et dans quelle cuve ? | si le FOR mono est fabriqué à 9 kg en ML001 pur (79 % de remplissage) et qu'il marche, la cause « taux de remplissage » perd du poids et la cause « carrier » en gagne |
| **Q5** | Cuves interchangeables de l'Inversina : 0,5–2 L pour les prémix, 3–4 L pour le 1 kg, 8–10 L pour le 3 kg | conditionne la représentativité de tous les petits lots |
| **Q7** | Rétention réelle du Russell (pesée entrée/sortie sur du lactose seul) | fixe le seuil à partir duquel le Russell est utilisable |

> **Q18 est la plus intéressante des trois nouvelles** : elle peut départager deux causes de
> l'échec historique sans consommer un gramme d'API.
