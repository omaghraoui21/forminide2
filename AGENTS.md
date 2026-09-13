# AGENTS.md — L'équipe virtuelle et ses désaccords

Ce projet est instruit par une équipe de spécialistes simulés. Chacun a un **mandat**, un
**critère de décision propre** et un **biais connu**. Les désaccords ne sont pas arbitrés en
silence : ils sont **actés** ci-dessous et transformés en expériences.

## 1. Composition

| Agent | Mandat | Critère de décision | Biais à surveiller |
|---|---|---|---|
| **DPI formulation scientist** | Architecture de la formule | FPD des deux APIs | Sur-ingénierie de la formule |
| **Expert low-dose blending** | Le formotérol à 0,048 % | RSD à l'échelle de la dose unitaire | Ignore l'aérosolisation |
| **Powder technologist** | Écoulement, densités, ségrégation | Carr/Hausner, test de ségrégation | Sous-estime l'API |
| **Lactose inhalation expert** | Choix et rôle des grades | PSD, fines, surface | Veut acheter un nouveau grade |
| **Aerosol scientist** | APSD, détachement | FPF, MMAD | Veut des fines partout |
| **Mixing / scale-up expert** | Énergie, taux de remplissage, révolutions | Représentativité d'échelle | Veut tout refaire à l'échelle finale |
| **Patent scientist** | Liberté d'exploitation, exemples reproductibles | Exemples avec chiffres | Confond revendication et exemple |
| **Pharmaceutical OSINT analyst** | Reconstruire ce que font les autres | Niveau de confiance | Sur-interprète une notice |
| **Industrial pharmacist** | Faisabilité atelier, opérateur, GMP | Nombre de manipulations | Conservatisme |
| **Statisticien DOE** | Plan d'essais, puissance | Nombre d'hypothèses éliminées par lot | Veut un plan factoriel complet |
| **Stability scientist** | Humidité, amorphe, 24 mois | Sensibilité à l'eau du FOR | Bloque tôt sur la stabilité |

## 2. Désaccords actés (à trancher par l'expérience, pas par l'autorité)

### D1 — Grande ou petite première fraction de lactose ?
- **Expert low-dose blending** : commencer **concentré** (petite fraction, ratio API/lactose
  élevé) maximise le cisaillement inter-particulaire et casse les agglomérats — dilution
  géométrique classique.
- **Patent scientist** : les seules données publiques chiffrées disponibles (EP3175842A1,
  0,41 % m/m de principe actif, répartition 1re:2e:3e fraction) donnent le **meilleur AV avec
  une grande première fraction (7:2:1 → AV 7,1)** et le pire avec une petite première fraction
  suivie d'une grosse dilution finale (5:1:4 → AV 12,5).
- **Résolution proposée** : les deux ont raison sur des étapes différentes. On **sépare la
  désagglomération (petite, concentrée, tamisée) de la distribution (grande, douce, tumbling)** :
  prémix FOR concentré ~1 % m/m, puis incorporation dans une **grande** première fraction 7:2:1.
  → C'est le cœur de l'architecture B recommandée. **Testé par L2.**

### D2 — Quel API doit toucher le carrier en premier ?
- **Expert low-dose blending** : le **formotérol d'abord**, pour qu'il occupe une position
  bien distribuée avant l'arrivée d'une masse 17 à 33 fois supérieure de budésonide.
- **Aerosol scientist** : le **budésonide d'abord**, pour qu'il sature les sites de haute
  énergie ; le formotérol se posera alors sur des sites faibles et se détachera mieux
  (meilleur FPD FOR).
- **Résolution** : non tranchable sur la littérature. **Testé de front par L2 (FOR d'abord)
  contre L3 (BUD d'abord, prémix FOR en dernier).**

### D3 — Le tamisage 250 µm est-il protecteur ou destructeur ?
- **Industrial pharmacist / patent scientist** : protecteur. US9616024 (Norton Healthcare)
  montre, données à l'appui, que tamiser l'API à 250 µm avant mélange fait passer le RSD du
  budésonide de 14,3 % à 4,6 % et la récupération du formotérol de 91,4 % à 99,6 %.
- **Aerosol scientist** : destructeur en fin de procédé — un tamis est aussi un **classificateur
  granulométrique**, il peut retenir des fines et défaire l'ordered mixture.
- **Résolution** : les deux sont compatibles. Tamisage **oui en amont et en intermédiaire**,
  **jamais en dernière opération** : on ne termine jamais sur un tamisage (toujours une
  ré-homogénéisation courte après). **Vérifié par bilan matière + assay avant/après tamis sur L2.**

### D4 — Combien de temps mélanger ?
- **Mixing expert** : 15 min/étape est cohérent avec la plateforme publiée (Turbula 22 rpm,
  15 min/étape) et avec l'optimum publié pour un tumbler (15 min).
- **Aerosol scientist** : 3 × 15 min cumulés entrent dans le régime des *press-on forces*
  (la littérature situe l'essentiel de l'évolution dans les 120 premières minutes, la
  désagglomération dans les 0–10 min et la compression sur 0–60 min) → risque de perte de FPD.
- **Résolution** : ne pas allonger ; **mesurer**. Étude cinétique **embarquée dans L2**
  (prélèvements à 5, 10, 15 et 25 min à l'étape finale) — coût marginal nul, pas de lot dédié.

### D5 — Deux carriers différents, un par API ?
- **Lactose inhalation expert** : séduisant (chaque API son support optimal).
- **Powder technologist** : deux populations de PSD/densité différentes dans un même bulk
  = **moteur de ségrégation par percolation** au transfert et au remplissage dosator.
- **Résolution** : **repoussé en phase 2**, et seulement si les deux grades ont des PSD
  proches. Pas dans le screening.

## 3. Règle de conduite de l'équipe

1. Un désaccord non résolu devient une **variable d'essai**, jamais un compromis moyen.
2. Un spécialiste peut opposer un **veto motivé** (ex. : le stability scientist sur l'humidité),
   il doit alors nommer la donnée qui lèverait son veto.
3. Toute conclusion d'équipe est datée et versée dans `memory/decisions.md`.
