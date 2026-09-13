# Plateforme HTML — Cahier d'essais BUD/FOR

`cahier-essais.html` est la source de la plateforme publiée comme Artifact :
**https://claude.ai/code/artifact/63d37e61-5874-4600-bc69-e8395cae0ae1**

## Ce que la page fait

| Onglet | Contenu | Interactif |
|---|---|---|
| **Chemin critique** | état des 4 portes · les 3 modifications testées · la séquence E1 → E4 avec hypothèse, ce que chaque essai élimine et ses critères GO/NO-GO · branches conditionnelles L3–L7 | — |
| **Lots &amp; saisie** | relevé d'homogénéité **10 positions × 25 mg** pour chaque lot (L0 → L7) | **oui** — RSD BUD, RSD FOR, RSD de masse, teneurs, **corrélation de Pearson BUD ↔ FOR**, diamètre effectif du formotérol déduit du RSD, verdicts et interprétation, formule et procédé recalculés selon échelle / dosage / répartition |
| **Calculs de lot** | taux de remplissage de l'Inversina tracé à l'échelle avec les bandes de guidance constructeur · masse d'agglomérat ↔ part d'une dose · RSD ↔ diamètre effectif · limite statistique du formotérol | — |
| **Repères &amp; décision** | tableau comparatif gélule unique vs deux gélules séparées · arbre de décision · questions bloquantes | — |

## Persistance

La page déclare la capacité **`db`** : les relevés saisis sont **partagés entre les membres de
l'organisation** qui ouvrent la page, et **l'artefact devient interne à l'organisation** (il ne
peut plus être partagé publiquement) — ce qui convient à des données de lot.
Si la capacité n'est pas disponible dans une vue, la page bascule silencieusement sur le stockage
local du navigateur ; l'état est indiqué en haut à droite.

Modèle de données : un document par lot, `essais/<L0…L7>`, corps
`{lot, dose, scaleKg, split, sampleMg, rows[], seeded, updatedAt}`.

## Le jeu d'exemple

Le lot L2 s'ouvre avec un **jeu d'exemple explicitement étiqueté**, pour que la page montre ce
qu'elle fait dès l'ouverture. Le bouton « Vider le relevé » le supprime.
**Ce ne sont pas des résultats réels.**

## Mise à jour

Modifier `platform/cahier-essais.html`, puis republier le fichier sur la **même URL** d'artefact
(ne pas en créer un second).
