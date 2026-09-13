# forminide2 — Bulk DPI combiné Budésonide / Formotérol (capsule unique 25 mg)

Dépôt de travail R&D formulation : développement d'un **bulk DPI unique** permettant de
remplir une capsule contenant **Formotérol 12 µg + Budésonide 200 µg ou 400 µg** dans
**≈ 25 mg de poudre** (capsule taille 3, dispositif de type Aerolizer).

> **Périmètre de cette phase** : FORMULATION → CARRIER → PRÉMÉLANGE → MÉLANGE → TAMISAGE → BULK.
> Hors périmètre : blister, conditionnement secondaire, dossier réglementaire complet, device final.

## Par où commencer

| Si vous voulez… | Lisez |
|---|---|
| **Savoir quoi faire, étape par étape** | [`docs/10-marche-a-suivre.md`](docs/10-marche-a-suivre.md) |
| La réponse courte et la décision | [`RAPPORT.md`](RAPPORT.md) — section **R** |
| La séquence expérimentale minimale (GO/NO-GO industriel) | [`docs/07-sequence-minimale.md`](docs/07-sequence-minimale.md) |
| Pourquoi le combiné 9 kg a échoué | [`RAPPORT.md`](RAPPORT.md) §A + [`docs/05-arbre-causes.md`](docs/05-arbre-causes.md) |
| Ce que font les concurrents | [`docs/02-produits-commercialises.md`](docs/02-produits-commercialises.md) |
| Les brevets exploitables | [`docs/03-brevets.md`](docs/03-brevets.md) |
| ML001 / SV003 / SV010 | [`docs/04-lactoses.md`](docs/04-lactoses.md) |
| Les protocoles de lots à fabriquer | [`docs/06-protocole-lots.md`](docs/06-protocole-lots.md) |
| **Les dossiers de lot prêts à exécuter (L0, L1, L2)** | [`docs/09-dossiers-de-lot.md`](docs/09-dossiers-de-lot.md) |
| Le scale-up 3 → 6 → 9 kg | [`docs/08-scale-up.md`](docs/08-scale-up.md) |
| Chaque donnée avec sa source et son niveau de confiance | [`docs/annexes/A1-registre-preuves.md`](docs/annexes/A1-registre-preuves.md) |
| Les calculs (agglomérats, RSD, taux de remplissage) | [`docs/annexes/A2-calculs.md`](docs/annexes/A2-calculs.md) + [`scripts/calculs_cles.py`](scripts/calculs_cles.py) |

## Architecture du dépôt

```
GOAL.md                  Objectif, critères de succès, critères d'arrêt (north star)
CLAUDE.md                Contrat de travail pour toute session agent (règles, mémoire, style)
AGENTS.md                L'équipe virtuelle de spécialistes et leurs désaccords actés
RAPPORT.md               Livrable principal A → R
docs/                    Dossiers thématiques détaillés
  00-hand-off.md         Le DOF/hand-off reçu, archivé tel quel
  01-diagnostic.md       Reconstruction du procédé + mécanismes physiques
  02-produits-commercialises.md   OSINT produits + formulation fingerprints
  03-brevets.md          Brevets, exemples extraits, classement d'applicabilité
  04-lactoses.md         ML001/SV003/SV010, autres grades, autres excipients
  05-arbre-causes.md     Arbre de causes classé + test le moins cher par cause
  06-protocole-lots.md   Lots L0 → L6 : hypothèse, composition, procédé, réponses
  07-sequence-minimale.md  Chemin le plus court vers une décision industrielle
  08-scale-up.md         3 → 6 → 9 kg, fill ratio, énergie de mélange
  09-dossiers-de-lot.md  Dossiers de lot exécutables L0/L1/L2 + plans de prélèvement
  10-marche-a-suivre.md  Quoi faire, dans quel ordre, sous quelle condition
platform/               Source de la plateforme HTML de saisie (Artifact)
  annexes/               Registre de preuves, calculs, méthode analytique
memory/                  Mémoire de projet (décisions, questions, journal)
scripts/                 Calculs reproductibles
.claude/commands/goal.md Commande /goal
```

## Règle d'or du dépôt

Toute affirmation technique porte un **niveau de confiance** :
`FAIT CONFIRMÉ` · `INFÉRENCE HAUTE CONFIANCE` · `INFÉRENCE FAIBLE CONFIANCE` · `INCONNU`.
Aucune déduction OSINT n'est présentée comme une donnée officielle. Voir `CLAUDE.md`.
