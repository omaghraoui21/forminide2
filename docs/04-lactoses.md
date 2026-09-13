# Lactoses — ML001 / SV003 / SV010, autres grades, autres excipients

## 1. Données fournisseur (FAIT CONFIRMÉ)

Source : DFE Pharma, *Your Inhalation Grade Lactose*, brochure #004, mai 2020. Valeurs
**typiques**, PSD par diffraction laser Sympatec. Toutes les Respitose® sont produites à
**Veghel (Pays-Bas)**, site dédié inhalation, sous GMP.

| Grade | Procédé | Morphologie | D10 (µm) | D50 (µm) | D90 (µm) | Densité tassée (g/L) | Densité versée (g/L) | Indice de Carr |
|---|---|---|---|---|---|---|---|---|
| **Respitose® ML001** | **broyé** | irrégulière | **3 – 7** | 37 – 61 | 124 – 194 | 880 | **570** | **> 25 %** |
| **Respitose® SV003** | **tamisé** | tomahawk, surface lisse | 19 – 43 | 53 – 66 | 75 – 106 | 780 | 630 | **19 %** |
| **Respitose® SV010** | **tamisé** | tomahawk, surface lisse | 35 – 65 | 95 – 125 | 160 – 190 | 830 | **690** | **17 %** |
| *Respitose® ML003* | broyé | irrégulière | 1 – 6 | 20 – 50 | 65 – 140 | 850 | 560 | > 25 % |
| *Respitose® SV001* | tamisé | tomahawk | 120 – 160 | 210 – 250 | 290 – 350 | 810 | 700 | 14 % |
| *Lactohale® LH230* | fin | fine | 1,0 – 3,0 | **< 10** | < 30 | 500 | 310 | > 25 % |
| *Lactohale® LH220* | fin | fine | 1,5 – 3,0 | 11 – 15 | 25 – 40 | 660 | 370 | > 25 % |
| *Lactohale® LH210* | fin | fine | 2,0 – 3,5 | 14 – 19 | 35 – 50 | 680 | 400 | > 25 % |
| *Lactohale® LH300* | fin | micronisée | — | **< 5** | ≤ 10 | 520 | 260 | > 25 % |

`FAIT CONFIRMÉ` — **Lactohale® ML001 et Respitose® ML001 partagent les mêmes valeurs typiques**
(D10 3–7, D50 37–61, D90 124–194, 880/570 g/L), à ceci près que la première est produite à
Kapuni (NZ) et la seconde à Veghel (NL).

**Non renseignés par la brochure** (→ à demander au fournisseur, `memory/questions-ouvertes.md` Q9) :
teneur en eau, surface spécifique BET, % de particules < 10 µm, angle de repos.

## 2. Ce que chaque grade apporte réellement

### Respitose® SV003 — **le carrier par défaut**
- PSD la plus **étroite** des trois (D90/D10 ≈ 2,5–3,5), tomahawk lisse, **Carr 19 %**.
- DFE indique que c'est **le grade le plus demandé au monde**, « pour son profil granulométrique
  unique » `FAIT CONFIRMÉ`.
- C'est **le lactose grossier des exemples budésonide/formotérol de Zambon** `FAIT CONFIRMÉ`.
- **Faiblesse** : D10 19–43 µm → **presque aucune particule sous 10 µm**. Il n'apporte pas de
  fines fonctionnelles.
- **Rôle proposé** : base du bulk, support du prémix formotérol.

### Respitose® SV010 — **le grade d'écoulement et de densité**
- Le plus **coulant** (Carr 17 %) et le plus **dense** (690 g/L) des trois.
- `calcul interne` : à 9 kg il n'occupe que **13,0 L, soit 65 % de l'Inversina 20 L**, contre
  71 % pour SV003 et 79 % pour ML001. **C'est le grade qui donne le plus de marge mécanique au
  mélangeur.**
- **Faiblesse** : D50 ≈ 110 µm → surface développée par gramme la plus faible → **moins de sites
  d'adhésion** pour un actif à 0,048 %, et davantage de risque de ségrégation (surface lisse).
- **Rôle proposé** : fraction de dilution finale et/ou correctif si le dosator Modu-C peine.

### Respitose® ML001 — **le donneur de fines interne (et un piège de densité)**
- Broyé, irrégulier, **cohésif (Carr > 25 %)**.
- **D10 = 3–7 µm** : c'est le **seul des trois** à posséder une population réellement fine.
  `INFÉRENCE HAUTE CONFIANCE` : il apporte de l'ordre de 10 % de matière sous ~5–7 µm, soit une
  fraction utile de fines — mais **ce n'est pas un grade de fines** (D50 37–61 µm) : en ajouter
  10 % n'équivaut pas à ajouter 10 % de fines respirables.
- DFE positionne ML001 comme utile « pour la technologie de remplissage à membrane ou pour
  permettre la formation du bouchon en remplissage gélule » `FAIT CONFIRMÉ` — donc **pertinent
  pour notre Modu-C**, mais par sa cohésion, pas par ses fines.
- ⚠️ **Piège** : densité versée 570 g/L. `calcul interne` — 9 kg de ML001 occupent **15,8 L, soit
  79 % de l'Inversina**. Ajouter du ML001 **dégrade le taux de remplissage**, donc le mélange,
  au moment même où l'on cherche à améliorer l'homogénéité. **Toute décision d'ajouter du ML001
  doit être vérifiée sur le volume, pas seulement sur la FPF.**
- **Rôle proposé** : **5–10 % maximum**, pré-mélangé au carrier **avant** les APIs.

## 3. Matrice de décision

| Grade | Rôle possible | Avantage BUD | Avantage FOR | Risque principal | Utilisation proposée |
|---|---|---|---|---|---|
| **ML001** | donneur de fines, modulateur de cohésion, aide au bouchon dosator | **++** co-agglomérats BUD–fines co-déposés (Kinnunen 2015) | **+** saturation des sites de haute énergie → détachement facilité | écoulement ; **densité 570 → 79 % de remplissage à 9 kg** ; fines libres ségrégeantes | **5–10 %**, pré-mélangé au carrier, **jamais seul** |
| **SV003** | **carrier principal** | référence des exemples BUD/FOR publiés | surface suffisante, PSD étroite → peu de ségrégation par taille | pas de fines < 10 µm | **base par défaut** du bulk et du prémix FOR |
| **SV010** | carrier de dilution / correctif d'écoulement | neutre | **–** moins de sites disponibles | uniformité du FOR, ségrégation (surface lisse) | **fraction de dilution** (2e et 3e portions) et plan B écoulement |

## 4. Comparaison des systèmes

| Système | Verdict | Motif |
|---|---|---|
| **ML001 seul** | **Non** | Carr > 25 %, 79 % de remplissage à 9 kg, incompatible avec un dosator à 25 mg |
| **SV003 seul** | **Oui — point de départ** | seul avec précédent publié BUD/FOR ; compromis flux/surface ; densité acceptable |
| **SV010 seul** | Oui, en secours | meilleur écoulement **et** meilleur remplissage mélangeur ; mais le plus pauvre en sites |
| **ML001 / SV003** (ex. 8 / 92) | **Oui — 1re optimisation** | apporte des fines sans achat ; densité du mélange ≈ 625 g/L, remplissage 9 kg ≈ 72 % (quasi inchangé) `calcul interne` |
| **ML001 / SV010** (ex. 8 / 92) | Oui — alternative | la densité élevée de SV010 compense celle de ML001 ; à préférer si l'écoulement devient critique |
| **SV003 / SV010** | Oui, autre finalité | élargit la PSD **sans ajouter de fines** ; permet de viser la fenêtre Spiromax (d10 20–65 / d50 80–120 / d90 130–180) |
| **Ternaire ML001 + SV003 + SV010** | **Phase 2 uniquement** | justifié seulement si l'on a besoin **simultanément** de fines, de sites et d'écoulement. Exemple conceptuel : **20 SV003 / 72 SV010 / 8 ML001** |

## 5. Autres grades — maximum 3, seulement si une porte GO/NO-GO les déclenche

| Grade | Fabricant | PSD | Morphologie | **Fonction absente qu'il apporte** | Problème qu'il résout | Raison de l'acheter | Priorité |
|---|---|---|---|---|---|---|---|
| **Lactohale® LH230** | DFE Pharma | D10 1–3 / D50 < 10 / D90 < 30 µm | fine | **vraies fines respirables** — ML001 ne descend qu'à D10 3–7 µm et a un D50 de 37–61 µm | FPD faible malgré une CU correcte | c'est la population que le trio disponible **ne contient pas** ; mécanisme documenté (S5) et fenêtre chiffrée (4–15 %) | **1** |
| **Lactohale® LH210 / LH220** | DFE Pharma | D50 14–19 / 11–15 µm | fine | **fines non respirables** : saturent les sites actifs **sans** contribuer à la FPD ni déplacer le MMAD | uniformité et ségrégation du formotérol sans perturber l'APSD | permet de séparer l'effet « sites » de l'effet « co-dépôt » — impossible avec LH230 seul | 2 |
| **Respitose® SV001** | DFE Pharma | D50 210–250 µm, Carr 14 % | tomahawk grossier | **squelette très coulant** | RSD de masse au dosator Modu-C à 25 mg | uniquement si le Gate 3 échoue pour cause d'écoulement | 3 |

> **Aucun de ces grades ne doit être commandé avant qu'une porte ne l'ait déclenché.**
> Demander en revanche **dès maintenant** des échantillons gratuits de LH230 (délai fournisseur).

## 6. Autres excipients

| Excipient | Mécanisme | Bénéfice attendu | Risque | Impact stabilité | Impact réglementaire | Niveau de preuve sur BUD/FOR | **Classement** |
|---|---|---|---|---|---|---|---|
| **Stéarate de magnésium** | agent de contrôle des forces ; revêtement partiel du carrier, réduit l'énergie de surface | ↑ FPF, ↓ adhésion, ↑ protection contre l'humidité | **l'ordre d'ajout est critique** (fines puis MgSt : FPF 46,55 % ; MgSt puis fines : 33,86 %) ; sur-mélange délétère ; effet dépendant de la nature de l'API (favorable au salmétérol cohésif, sans effet sur la fluticasone adhésive) | modifie le mouillage et la dissolution ; à suivre sur 24 mois | **précédent solide** : Seebri®/Ultibro® Breezhaler = lactose ~23,5–23,6 mg **+ MgSt** en gélule `FAIT CONFIRMÉ` | **Rescue option** |
| **Leucine** | modificateur de surface, anti-adhérent | ↑ dispersibilité | — | — | acceptable en inhalation mais nouvel excipient au dossier | utilisée **exclusivement en spray drying** dans les brevets BUD/FOR (Zambon) — **aucun exemple en mélange à sec** | **Non applicable** (pas de spray dryer) |
| Phospholipides, autres acides aminés | modification de surface | — | — | — | dossier lourd | aucune sur BUD/FOR en mélange à sec | **Non nécessaire** |

**Position de l'équipe** : le premier objectif est **une formulation lactose seul**, conforme aux
produits commercialisés (FORPACK : un seul excipient, le lactose). Tout excipient supplémentaire
est une dette réglementaire et analytique qui doit être payée par un gain mesuré, pas espéré.
