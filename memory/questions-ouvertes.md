# Questions ouvertes — données manquantes

Statut : ⬜ ouverte · 🟡 en cours · ✅ résolue (dater et renseigner la réponse)

| # | Question | Bloque | Propriétaire | Criticité | Statut |
|---|---|---|---|---|---|
| **Q1** | PSD des deux APIs micronisés (D10/D50/D90) + surface spécifique | calibrage de l'agglomération, choix des fines, prédiction de la FPD | Achats / fournisseur API | haute | ⬜ |
| **Q2** | **Titre exact du formotérol** : fumarate dihydraté ou base ? facteur de correction ? | **toutes les pesées et tous les assays** | AQ / fournisseur | **haute — bloque L0** | ⬜ |
| **Q3** | **Que s'est-il exactement passé sur le combiné 9 kg historique ?** quel API a échoué, assay ou RSD, avant ou après tamisage, combien de lots, quelles valeurs ? | tout le diagnostic — **la donnée la moins chère et la plus informative du projet** | R&D / archives | **très haute** | ⬜ |
| **Q4** | **Quelle était la masse de prise d'essai** utilisée historiquement pour juger l'homogénéité ? | si ~1 g, les « succès » mono-produits sont peut-être des artefacts | Labo / archives | **très haute** | ⬜ |
| **Q5** | Fiche technique Inversina : vitesse(s) de rotation, **cuves interchangeables disponibles**, taux de remplissage recommandé | tout le plan de scale-up ; possibilité de screener à 3 kg dans une petite cuve | Production / fournisseur | haute | 🟡 *guidance constructeur relayée obtenue : **≈ 50 % du volume pour une poudre sèche lourde**, ≈ 2/3 pour une poudre légère ; **20–30 rpm** pour le 20 L. **Fiche primaire à récupérer en interne** (la machine est sur site) et cuves interchangeables toujours à confirmer.* |
| **Q6** | HR et température de la salle de mélange (historique et actuelles) | interprétation de la variabilité inter-lots ; sensibilité du formotérol à l'eau | Production | moyenne | ⬜ |
| **Q7** | Configuration exacte du Russell : type d'agitateur, débit, matériau, pertes typiques | décisions de tamisage, bilan matière | Production | moyenne | ⬜ |
| **Q8** | Liberté d'exploitation sur EP3175842A1 et US11642475 (antériorité d'usage interne ?) | une éventuelle revendication — **pas** le développement | Conseil PI | moyenne | ⬜ |
| **Q9** | Teneur en eau et surface spécifique BET des trois grades de lactose ; conditions de stockage | stabilité 24 mois, cohésion | Achats / DFE | basse | ⬜ |
| **Q10** | Référence exacte du dispositif type Aerolizer disponible (RS01 modèle ?) et sa **résistance** | débit de test NGI pour ΔP = 4 kPa | R&D / device | **haute — avant Gate 4** | 🟡 *Le RS01 existe en **version standard faible résistance : 4 kPa à ≈ 100 L/min** et en **version haute résistance : 4 kPa à 65 L/min**. L'écart change complètement la FPF mesurée → **identifier notre version et mesurer la résistance avant le premier NGI**. Repère de comparabilité : l'étude de référence travaille à l'ACI, 90 L/min.* |
| **Q11** | Le budésonide est un mélange d'épimères 22R/22S — que fait la méthode HPLC (somme, pic unique) ? | validité de tous les assays | Labo | moyenne — **avant L0** | ⬜ |
| ~~**Q12**~~ | ~~Lactose déclaré pour FORPACK 12/400 capsair~~ | — | — | — | ✅ **2026-09-13 — FERMÉE** : KÜB, **laktoz 24,588 mg**, total **25,0000 mg**, AMM 250/44. Le même bulk à 25 mg sert les deux dosages. |

**Règle** : aucune de ces questions n'empêche de lancer **L0, L1 et L2**, sauf **Q2** (titre du
formotérol) et **Q11** (méthode), indispensables avant toute pesée et tout dosage.

## Questions ajoutées le 2026-09-13 (session 2)

| # | Question | Bloque | Propriétaire | Criticité | Statut |
|---|---|---|---|---|---|
| **Q13** | Disposons-nous d'un **impacteur d'Andersen (ACI)** en plus du NGI ? L'étude de référence de la classe est en ACI à 90 L/min | comparabilité directe de nos résultats au benchmark marché | Labo | basse | ⬜ |
| **Q14** | Le mono-produit **formotérol** maison pèse-t-il lui aussi ~25 mg par gélule, et quel RSD d'uniformité de teneur atteint-il ? | c'est **notre propre repère interne** : s'il est à ~3 %, le combiné doit viser ≤ 3 %, pas 5 % | R&D / AQ | **haute** | ⬜ |
| **Q15** | Paramètres actuels du **Modu-C MS** pour un remplissage à 25 mg : diamètre de dosator, taille de chambre de dosage, hauteur du lit de poudre, pré-compression, vitesse | le Gate 3 : la variabilité de masse dépend **davantage des réglages machine que du carrier** (Faulhammer *et al.*) — sans ces paramètres, un mauvais RSD serait imputé à tort à la formule | Production | moyenne — **avant Gate 3** | ⬜ |

## Questions ajoutées le 2026-09-13 (session 5) — après l'information sur les carriers des mono-produits

| # | Question | Bloque | Propriétaire | Criticité | Statut |
|---|---|---|---|---|---|
| **Q16** | Ratio SV003 : ML001 du mono-produit budésonide | les masses de E-A et E-B | R&D / production | haute | 🟡 **≈ 50:50** annoncé le 2026-09-13, **à confirmer au bureau**. Les masses de E-A/E-B sont calculées sur cette base et devront être refaites si le ratio réel diffère |
| **Q17** | Masse de remplissage des mono-produits | — | — | — | ✅ **FERMÉE 2026-09-13 : 25 mg pour tous les produits.** Le **RSD d'uniformité atteint** par chaque mono-produit reste à obtenir (voir Q17b) |
| **Q17b** | **Quel RSD d'uniformité de teneur atteignent les deux mono-produits à 9 kg ?** | le repère interne : si le formotérol mono est à 2 %, le combiné doit viser 2 %, pas 5 % | R&D / AQ | **haute** | ⬜ |
| **Q18** | Taille de lot et cuve des mono-produits | — | — | — | ✅ **FERMÉE 2026-09-13 : 9 kg pour les deux.** Conséquence : `calcul interne` 78,9 % de remplissage pour le formotérol mono (ML001 pur) et 75,2 % pour le budésonide mono → **la cause « taux de remplissage » est éliminée** (ADR-017) et la cause « carrier » (5.3) devient prioritaire |

## Question ajoutée le 2026-09-13 (session 6)

| # | Question | Bloque | Propriétaire | Criticité | Statut |
|---|---|---|---|---|---|
| **Q19** | **Le combiné historique a-t-il été fabriqué sur le carrier du budésonide (≈ 50 % ML001) ou sur celui du formotérol (100 %) ?** | c'est la **confirmation directe ou la réfutation de la cause 5.3**. Si le combiné a été fait à 50 % de ML001, l'hypothèse « le formotérol a perdu ses fines » devient l'explication la plus simple de tout l'échec historique | R&D / archives | **très haute — coût nul** | ⬜ |
