# Plan d'essais révisé — trois lots de 1 kg, puis 9 kg

> **Version 2 — 2026-09-13.** Remplace la version 1, qui traitait le taux de remplissage de la
> cuve comme une cause probable de l'échec historique. **Cette hypothèse est éliminée** :
> voir §1. Le plan en est considérablement raccourci.

---

## 1. Ce que disent les données de production, et ce qu'elles éliminent

`FAIT INTERNE CONFIRMÉ` (2026-09-13) :

| | Formotérol mono | Budésonide mono |
|---|---|---|
| **Carrier** | **ML001 seul** | **SV003 + ML001 ≈ 50:50** *(à confirmer — Q16)* |
| **Masse par gélule** | **25 mg** | **25 mg** |
| **Taille de lot** | **9 kg** | **9 kg** |
| Densité versée `calcul interne` | 570 g/L | 598 g/L |
| **Remplissage de l'Inversina 20 L** | **78,9 %** | **75,2 %** |
| Statut | **fabriqué en routine, avec succès** | **fabriqué en routine, avec succès** |

> **Un actif à 0,048 % m/m est distribué de façon homogène dans 9 kg, à 79 % de remplissage,
> en routine.**

### Ce que cela élimine définitivement

| Hypothèse | Pourquoi elle tombe |
|---|---|
| **Taux de remplissage de la cuve** | 79 % est la condition **normale** de fabrication du formotérol mono, et elle fonctionne. La guidance générique du constructeur ne résiste pas aux données du site |
| **Taille de lot de 9 kg** | c'est l'échelle de production courante des **deux** mono-produits |
| **La faible dose en elle-même** | 4,32 g de formotérol dans 9 kg, en routine |
| **Énergie de mélange, nombre de révolutions, 15 min par étape** | identiques sur les mono-produits qui réussissent |
| **Les trois tamisages au Russell 250 µm** | identiques sur les mono-produits qui réussissent |
| **Écoulement au dosator d'un carrier riche en ML001** | le formotérol mono est rempli à **25 mg sur ML001 pur** — l'objection « ML001 ne coule pas assez » est **empiriquement fausse** |

**Les échecs historiques étaient des échecs de développement initiaux, pas une limite
d'équipement.** Le procédé, l'échelle et les équipements sont validés par la production courante.

### Ce qui reste — deux causes, et elles seules

Entre le **formotérol mono qui fonctionne** et le **combiné qui a échoué**, il ne reste que deux
différences :

| # | Cause | Différence avec le mono-produit qui marche |
|---|---|---|
| **1.1** | **Co-agglomération BUD–FOR** | 144 g de budésonide arrivent dans le même sandwich, soit **33 × la masse du formotérol** |
| **5.3** ★ | **Perte de l'environnement de fines** | le carrier passe de **100 % à ≈ 52 % de ML001** si le combiné hérite du système du budésonide |

ML001 est le seul des trois grades à posséder une vraie population fine (**D10 = 3–7 µm**). Pour
un actif à 0,048 % m/m, ce n'est pas un détail : c'est ce qui fournit les sites d'adhésion et
l'environnement de co-agglomération favorable. Le mono-produit formotérol est sur **100 % ML001** —
ce n'est probablement pas un hasard.

> **Question à coût nul, très haute valeur (Q19)** : le combiné historique a-t-il été fabriqué
> sur le carrier du budésonide ou sur celui du formotérol ? Si c'était sur celui du budésonide,
> la cause 5.3 devient l'explication la plus simple de tout l'échec.

---

## 2. Le plan : trois lots de 1 kg, puis confirmation à 9 kg

Deux causes, deux variables, **trois lots** :

```
E-A   co-sandwich    · carrier BUD  (≈ 52 % ML001)   ← reproduit la tentative historique
E-B   double prémix  · carrier BUD  (≈ 52 % ML001)   ← E-A vs E-B = effet ARCHITECTURE
E-C   double prémix  · carrier FOR  (100 % ML001)    ← E-B vs E-C = effet CARRIER
```

**Pourquoi ces deux niveaux de carrier et pas un intermédiaire** : 50 % et 100 % sont les deux
seuls points de l'espace dont on sache, en interne, qu'ils fonctionnent — chacun pour un API.
Tester entre les deux, c'est tester un point inconnu ; tester les bornes, c'est mesurer une pente
entre deux points connus.

**Et si les deux APIs ne peuvent pas être satisfaits en même temps, c'est au budésonide de
s'adapter** : à 1,600 % m/m, il est **33 fois plus tolérant** que le formotérol à 0,048 %.

**Pourquoi 1 kg** : les trois lots consomment **1,44 g de formotérol au total**, le coût d'un seul
lot de 3 kg. Ce n'est plus une question de représentativité mécanique — c'est de l'économie d'API
et de la vitesse de tri.

> **Limite explicite** : un lot de 1 kg **trie des formulations, il ne qualifie pas un procédé.**
> Aucune conclusion de procédé ne sera tirée de cet étage. La qualification se fait à **9 kg**,
> l'échelle réelle, que le site maîtrise.

---

## 3. Formules — 1 kg, dosage 12/400

*(le 12/400 est le pire cas pour le formotérol : rapport de masse BUD:FOR = 33:1)*
`calcul interne` · masses en grammes · ratio BUD mono supposé **50:50, à confirmer (Q16)**

| Composant | **E-A** | **E-B** | **E-C** |
|---|---|---|---|
| Budésonide micronisé | 16,00 | 16,00 | 16,00 |
| Formotérol fumarate dihydraté *(corrigé du titre)* | 0,480 | 0,480 | 0,480 |
| **Prémix FOR 1,0 % m/m** *(FOR + ML001)* | — | **48,00** | **48,00** |
| ↳ dont ML001 | — | 47,52 | 47,52 |
| SV003 | 491,76 | 468,00 | **0** |
| ML001 hors prémix | 491,76 | 468,00 | 936,00 |
| **ML001 total, en % du lactose** | **50,0 %** | **52,4 %** | **100,0 %** |
| **Total** | **1 000,00** | **1 000,00** | **1 000,00** |

**Répartition du lactose** : E-A en **3 : 3 : 3** (procédé historique) ; E-B et E-C en **7 : 2 : 1**.

---

## 4. Procédés

### Contraintes d'équipement à cette échelle

| Opération | Contrainte | Raison |
|---|---|---|
| **Prémix (48 g)** | **récipient de 0,15 à 0,5 L** — Turbula, petite cuve, ou mélange manuel intensif | `calcul interne` : 48 g dans la cuve de 20 L occupent **0,4 %** du volume. Aucun mélange n'y a lieu |
| **Lot de 1 kg** | **cuve de 3 à 4 L** si elle existe, sinon mélangeur de paillasse | 1 kg dans 20 L = 8 % de remplissage. Suffisant pour trier des formulations, pas pour qualifier un procédé |
| **Tamisage** | **manuel (250 µm ; 212 µm pour le prémix)** | la rétention du Russell est une **masse fixe** : `calcul interne` 1 à 5 % de perte à 1 kg contre 0,3 à 1,7 % à 9 kg, probablement enrichie en fines donc en formotérol |

### E-B et E-C — procédé détaillé

**Étape 0 — prémix formotérol (48,00 g)**
1. Relever HR et T°. Ioniseur en marche.
2. Peser **23,8 g de ML001**, déposer dans le récipient de prémix.
3. Peser **0,480 g de FOR** par différence, contenant verre ou inox **mis à la terre**.
4. Déposer le FOR **au centre**, sans contact avec les parois.
5. Recouvrir des **23,8 g** de ML001 restants — **sandwich**.
6. Mélange **3 min** → peser → **tamisage manuel 212 µm** → repeser → mélange **15 min**.
7. **Contrôle libératoire** : 10 prises de 25 mg, assay FOR, RSD.
   **Ne jamais engager un prémix dont le RSD n'est pas connu.**

**Étape 1 — carrier pré-conditionné**
8. E-B : SV003 468,00 g + ML001 468,00 g · E-C : ML001 936,00 g.
9. Mélange **15 min** → tamisage manuel 250 µm → mélange **5 min**.
   *(les fines sont en place avant l'arrivée du moindre API)*

**Étape 2 — base budésonide, fraction 1 (70 % du carrier)**
10. Déposer la moitié de la fraction 1.
11. Étaler **BUD 16,00 g**.
12. Recouvrir de l'autre moitié — **sandwich**.
13. Mélange **5 min** → peser → tamisage 250 µm → repeser → mélange **15 min**.

**Étape 3 — combinaison** *(la seule étape réellement nouvelle du procédé)*
14. Étaler **la totalité du prémix FOR (48,00 g)**.
15. Recouvrir avec la fraction 2 (**20 %** du carrier).
16. Mélange **3 min** → peser → tamisage 250 µm → repeser → mélange **15 min**.

**Étape 4 — dilution finale**
17. Ajouter la fraction 3 (**10 %** du carrier).
18. Mélange **3 min** → peser → tamisage 250 µm → repeser → **mélange 15 min**.
    **On ne termine jamais sur un tamisage.**

### E-A — témoin

Procédé historique intégral : **BUD 16,00 g et FOR 0,480 g déposés ENSEMBLE** dans le sandwich de
la première fraction, lactose réparti **3 : 3 : 3**, tamisage et mélange 15 min à chaque étape.
Ni prémix, ni couche barrière, ni carrier pré-conditionné.

---

## 5. Analyses et lecture

10 prises de **25 mg** par lot · assay **BUD et FOR sur la même prise** · bilan matière à chaque
tamisage · HR/T° relevées · **corrélation de Pearson BUD ↔ FOR** calculée sur chaque lot.

| Comparaison | Ce qu'elle établit |
|---|---|
| **E-A → E-B** | l'effet de **l'architecture** (séparer les deux APIs) |
| **E-B → E-C** | l'effet du **carrier** (rendre au formotérol son environnement de fines) |
| `r(BUD, FOR) ≥ 0,6` sur E-A | **signature directe de la co-agglomération** |
| `r` qui s'effondre de E-A à E-B | l'architecture a bien supprimé la co-agglomération |

| Résultat | Décision |
|---|---|
| E-A échoue · E-B réussit | l'architecture suffit → **prendre E-B** (moins de ML001 = plus proche du produit budésonide existant) |
| E-B échoue · E-C réussit | **le carrier est la clé** — cause 5.3 confirmée. Passer le combiné sur le carrier du formotérol |
| E-B et E-C réussissent | prendre **E-B**, et garder E-C en réserve si la FPD du formotérol déçoit au NGI |
| E-A réussit aussi | l'échec historique ne tenait ni à l'architecture ni au carrier → relire Q4 (masse de prise d'essai historique) avant toute autre hypothèse |
| Les trois échouent | relire d'abord le **RSD du prémix** (étape 7). Si le prémix est bon et que les trois lots échouent, la cause est dans l'étape de combinaison elle-même |

---

## 6. Confirmation à 9 kg

Directement à l'échelle de production, **sans étage intermédiaire obligatoire**.
`calcul interne` · 9 kg, 12/400 :

| Composant | Carrier BUD (≈ 52 % ML001) | Carrier FOR (100 % ML001) |
|---|---|---|
| Budésonide | 144,0 g | 144,0 g |
| Formotérol | 4,32 g | 4,32 g |
| **Prémix FOR 1,0 %** | **432,0 g** *(dont ML001 427,7 g)* | **432,0 g** *(dont ML001 427,7 g)* |
| SV003 | 4 212,0 g | **0 g** |
| ML001 total | 4 639,7 g | **8 851,7 g** |
| **Total** | **9 000,0 g** | **9 000,0 g** |
| Répartition 7 : 2 : 1 | 6 196,2 / 1 770,3 / 885,2 g | idem |
| Prémix, récipient requis | 432 g → **cuve de 1 à 1,5 L** | idem |

Portes 1 à 4 complètes. Échantillonnage à **15 positions** (lit plus profond).

**Un étage 3 kg reste possible** si l'on préfère une confirmation avant d'engager 9 kg de matière,
mais il n'est **plus obligatoire** : l'échelle n'est plus un facteur de risque identifié.

---

## 7. Consommation totale

| Étage | Lots | Échelle | FOR | BUD | Lactose | Durée |
|---|---|---|---|---|---|---|
| Screening | E-A, E-B, E-C | 1 kg | **1,44 g** | 48 g | 2,95 kg | 3 jours |
| Confirmation | 1 lot | 9 kg | 4,32 g | 144 g | 8,85 kg | 2 jours |
| Dosage 12/200 | 1 lot | 9 kg | 4,32 g | 72 g | 8,92 kg | 2 jours |
| Lot indépendant | 1 lot | 9 kg | 4,32 g | 144 g | 8,85 kg | 2 jours |
| | | **Total** | **≈ 14,4 g** | **≈ 408 g** | **≈ 29,6 kg** | **≈ 9 jours** |

---

## 8. Questions restantes

| # | Question | Statut |
|---|---|---|
| **Q16** | Ratio SV003 : ML001 du budésonide mono | 🟡 **≈ 50:50 annoncé, à confirmer au bureau.** Les masses de E-A et E-B en dépendent |
| **Q19** | **Le combiné historique était-il sur le carrier du BUD ou sur celui du FOR ?** | ⬜ **coût nul, très haute valeur** — confirme ou réfute la cause 5.3 |
| **Q17b** | Quel RSD d'uniformité atteignent les deux mono-produits à 9 kg ? | ⬜ c'est le **repère interne** : si le formotérol mono est à 2 %, le combiné doit viser 2 %, pas 5 % |
| **Q2** | Titre exact du formotérol | ⬜ **bloque toute pesée** |
| **Q11** | Méthode HPLC simultanée sur prise de 25 mg, statut des épimères | ⬜ **bloque tout dosage** |
| **Q4** | Masse de prise d'essai utilisée historiquement | ⬜ si c'était ~1 g, les résultats historiques sont à relire |
