# Hand-off R&D reçu (archivé)

> Document d'orientation de formulation transmis au démarrage du projet, archivé **tel quel**
> comme référence contractuelle. Toute divergence entre ce document et le reste du dépôt doit
> être signalée et tranchée explicitement, jamais résolue en silence.

## 1. Objectif
Développer un bulk DPI permettant ultérieurement de remplir **une seule gélule** contenant :
- Formotérol 12 µg + Budésonide 200 µg
- Formotérol 12 µg + Budésonide 400 µg

Masse de remplissage préférentielle : **≈ 25 mg/gélule**, **gélule taille 3**.

Hors périmètre de cette phase : blister, conditionnement secondaire, dossier réglementaire
complet, device final. Mission : **FORMULATION → CARRIER → PRÉMÉLANGE → MÉLANGE → TAMISAGE → BULK**.

## 2. Problème à résoudre
Les mono-produits Budésonide et Formotérol sont déjà fabriqués séparément avec succès. Des essais
historiques de formulation combinée à grande échelle ont rencontré des difficultés, ce qui a
conduit l'équipe historique à conserver deux formulations séparées. Le projet doit comprendre :
(1) pourquoi les mono-produits fonctionnent ; (2) pourquoi le mélange combiné a posé problème ;
(3) si la cause est le lactose, les interactions API/API/carrier, l'ordre d'incorporation, le
scale-up, le tamisage ou le mélange ; (4) comment contourner le problème avec le minimum de
modifications industrielles.

## 3. APIs
Achetés **déjà micronisés** (budésonide, formotérol). Pas de jet milling, d'air-jet milling, de
co-micronisation ni de spray drying interne. **Les PSD (D10/D50/D90) seront fournies
ultérieurement** ; le développement ne doit pas être bloqué en attendant. À réception, elles
devront servir à réévaluer : adhésion API–carrier, agglomération, ségrégation, compétition entre
APIs, choix du lactose, besoin éventuel de fines supplémentaires.

## 4. Lactoses disponibles
Respitose **ML001**, **SV003**, **SV010** — premier espace formulationnel à exploiter avant tout
nouvel achat. Le projet reste ouvert à un autre grade, un lactose plus fin ou plus grossier, un
lactose engineered/co-processed, MgSt, leucine ou un autre excipient inhalation approprié,
**uniquement si un besoin réel est démontré**.

## 5. Équipements
- Mélange : **Inversina ≈ 20 L**, charge industrielle maîtrisée jusqu'à ≈ 9 kg.
- Tamisage : **Russell, maille 250 µm**.
- Remplissage ultérieur : **Harro Höfliger Modu-C MS** (la poudre devra rester compatible avec un
  remplissage à 25 mg).

## 6. Procédé historique 3 kg
Dilution fractionnée en trois étapes de 1 kg.
- **Étape 1** : ≈ 1 kg de lactose, totalité de l'API en disposition lactose/API/lactose
  (« sandwich ») → mélange manuel ≈ 3 min → tamisage → transfert Inversina → mélange ≈ 15 min.
- **Étape 2** : + ≈ 1 kg → mélange manuel ≈ 3 min → tamisage → Inversina ≈ 15 min.
- **Étape 3** : + ≈ 1 kg → mélange manuel ≈ 3 min → tamisage → Inversina ≈ 15 min.
Masse finale ≈ 3 kg. Ce procédé fonctionnait correctement pour les formulations séparées.

## 7. Premiers scale-up 6 et 9 kg
Reproduction de sous-lots de 3 kg : **6 kg** = deux ensembles ; **9 kg** = trois ensembles, puis
combinaison. Stratégie conservatrice mais multipliant manipulations, sous-lots, tamisages,
transferts et temps opérateur.

## 8. Procédé 9 kg adapté
Dilution séquentielle par fractions d'environ 3 kg.
- **Étape 1** : ≈ 3 kg de lactose, API en sandwich → mélange automatisé/Inversina ≈ 5 min →
  Russell 250 µm → Inversina ≈ 15 min.
- **Étape 2** : + ≈ 3 kg → prémélange/mélange → tamisage 250 µm → Inversina ≈ 15 min.
- **Étape 3** : + ≈ 3 kg → mélange initial ≈ 3 min → Russell 250 µm → Inversina ≈ 15 min.
Bons résultats sur les mono-produits → **benchmark industriel interne**.

## 9. Point critique historique
Des difficultés sont apparues lors du développement direct d'une formulation
**Budésonide + Formotérol combinée à l'échelle 9 kg**, contribuant à l'abandon de la gélule
combinée. **La cause scientifique exacte n'est pas connue** — c'est la question centrale.

## 10. Hypothèses à investiguer
A — compétition entre APIs (mêmes sites énergétiques, déplacement mutuel, distribution,
détachement) · B — mauvaise stratégie de prémélange (deux APIs dans le premier sandwich) ·
C — très faible dose de formotérol (prémélange séparé, dilution géométrique ou sérielle,
fraction de lactose spécifique) · D — effet du scale-up (énergie de mélange, taux de remplissage,
mouvement du lit, dispersion des agglomérats) · E — tamisage (désagglomération mais aussi
modification de l'ordered mixture, pertes, redistribution) · F — overmixing (15 + 15 + 15 min) ·
G — carrier non optimal pour une formulation bi-API.

## 11. Question de développement principale
Faut-il continuer à mettre les deux APIs ensemble dès la première fraction ? Créer deux
prémélanges indépendants ? Attribuer des carriers/fractions différents aux deux APIs ? Modifier
la fraction fine/coarse avant d'introduire les APIs ?

## 12. Architectures obligatoires à étudier
A co-sandwich (benchmark) · B prémix formotérol · C prémix budésonide · D double prémix ·
E carriers différenciés · F carrier engineered en amont · G toute architecture publiée supérieure.

## 13. Objectif du premier screening
Quelle architecture résout le mieux le problème bi-API ? Variables prioritaires : architecture de
prémix, grade/rôle du lactose, ordre d'introduction. Secondaires : temps de mélange, tamisage,
ratio précis des grades.

## 14. Dose de formotérol
12 µg dans 25 mg ≈ **0,048 % m/m** avant correction de titre. Rend critiques l'échantillonnage,
l'adsorption sur équipement, les pertes au tamisage, les différences locales de concentration et
la ségrégation. **Tout plan expérimental doit spécifiquement protéger et suivre le formotérol.**

## 15. Philosophie de screening
Phase 1 : 4 à 6 essais max · Phase 2 : 2 à 4 essais d'optimisation · Phase 3 : 1 lot indépendant
de confirmation · Phase 4 : scale-up. Le nombre d'essais n'augmente que si les données le justifient.

## 16. Taille de lot
3, 6 et 9 kg à discuter. Le lot 3 kg est intéressant (historique, procédé connu, proche du
procédé industriel, consommation d'API plus faible). **Ne pas descendre arbitrairement à quelques
centaines de grammes sans démontrer la représentativité.**

## 17. Lactoses
Priorité ML001, SV003, SV010 : cartographier leurs rôles fonctionnels exacts, puis rechercher au
maximum 3 grades externes réellement différenciants. Un achat ne se justifie que s'il apporte une
population granulométrique absente, une surface différente, un niveau de fines différent ou une
amélioration démontrée du carrier engineering.

## 18. Excipients supplémentaires
Étudier MgSt, leucine et autres, classés en : utile immédiatement / rescue option / non
nécessaire. **Le premier objectif est une formulation lactose seul.**

## 19. Analyses
Priorité 1 : assay FOR, assay BUD, homogénéité multi-points, RSD, uniformité spatiale.
Priorité 2 : densité vrac et tassée, Carr, Hausner, écoulement, ségrégation.
Priorité 3 (après remplissage) : dose délivrée, NGI, FPD BUD, FPD FOR, APSD, MMAD.

## 20. Critères de succès de la phase
(1) architecture de prémix ; (2) carrier system ; (3) ordre d'incorporation ; (4) décision de
tamisage ; (5) temps/énergie de mélange rationnel ; (6) taille de lot R&D ; (7) bulk homogène ;
(8) performances aérodynamiques suffisamment prometteuses.
**Sortie : un bulk BUD/FOR crédible, reproductible et prêt pour la phase gélule/device.**
