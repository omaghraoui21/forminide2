# Journal des décisions (ADR)

Format : **contexte → décision → raison → conséquence → réversibilité**.
Une décision n'est jamais réécrite : on en ajoute une nouvelle qui remplace la précédente,
en la citant.

---

## ADR-001 — Le procédé historique est conservé comme base

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Contexte** : le combiné 9 kg a échoué historiquement ; la tentation est de repartir d'un
  procédé neuf.
- **Décision** : conserver le sandwich, les trois fractions, le tamisage 250 µm, l'Inversina
  15 min et le lactose comme unique excipient.
- **Raison** : ce procédé fonctionne sur les mono-produits **et** correspond à une plateforme
  publiée et chiffrée (EP3175842A1) ; le mécanisme du tamisage est démontré (US9616024).
- **Conséquence** : toutes les modifications proposées sont marginales et gratuites.
- **Réversibilité** : élevée.

## ADR-002 — Les deux APIs ne sont plus jamais placés dans le même sandwich

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Contexte** : dans le co-sandwich, BUD représente 17 à 33 fois la masse de FOR.
- **Décision** : prémix formotérol dédié à ≈ 1 % m/m, tamisé, **avant** toute rencontre avec le
  budésonide ; le budésonide est ensuite déposé en couche séparée par une barrière de lactose.
- **Raison** : co-agglomération documentée sur un couple corticoïde/β2 analogue (P13) ;
  architecture des seuls brevets publiant des exemples corticoïde + formotérol (P7, prémix
  0,82 % m/m) ; arithmétique des agglomérats (A2 §2 et §4).
- **Conséquence** : une manipulation supplémentaire, un point de contrôle qualité en plus.
- **Réversibilité** : élevée (L1 reste le témoin).

## ADR-003 — La répartition du lactose passe de 3:3:3 à 7:2:1

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Contexte** : la répartition n'avait jamais été considérée comme un paramètre.
- **Décision** : première fraction 70 %, deuxième 20 %, troisième 10 %.
- **Raison** : (a) meilleure valeur d'AV publiée pour un actif à 0,41 % m/m (P5 : AV 7,1 contre
  12,5) ; (b) réduit de 33 % à 10 % la masse incorporée par l'étape qui travaille à 71 % de
  remplissage du mélangeur (A2 §5).
- **Conséquence** : une seule modification corrige deux causes racines ; coût nul.
- **Réversibilité** : totale.

## ADR-004 — Le procédé ne se termine jamais par un tamisage

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Décision** : conserver les trois tamisages, mais toujours les faire suivre d'une
  ré-homogénéisation.
- **Raison** : un tamis est aussi un classificateur granulométrique ; le bénéfice du tamisage
  (P6) s'obtient en amont, pas en sortie.
- **Réversibilité** : totale. **Vérification prévue** : assay avant/après le tamisage final de L2.

## ADR-005 — Le carrier de départ est SV003, sans fines ajoutées

- **Date** : 2026-09-13 · **Statut** : ⛔ **REMPLACÉE par ADR-015**
- **Décision** : screening sur SV003 seul ; ML001 (8 %) seulement si le Gate 4 le déclenche.
- **Raison** : SV003 est le carrier grossier des exemples BUD/FOR publiés (P8) ; ajouter des
  fines dès le premier lot **confondrait** l'effet architecture et l'effet carrier ; et le ML001
  dégrade le taux de remplissage à 9 kg.
- **Réversibilité** : totale (lot L4 prévu).

## ADR-006 — Le screening se fait à 3 kg, la décision industrielle à 6 puis 9 kg

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Décision** : L0 au format prémix réel ; L1–L5 à 3 kg ; L6 à 6 puis 9 kg.
- **Raison** : les variables d'architecture sont indépendantes de l'échelle, mais **3 kg ne
  représente pas la mécanique de mélange du 9 kg** (24 % contre 71 % de remplissage).
- **Conséquence** : interdiction de conclure « industrialisable » à partir de lots de 3 kg.
- **Réversibilité** : élevée. **À réévaluer** si l'Inversina accepte des cuves interchangeables (Q5).

## ADR-007 — Le dosage de screening est le 12/400

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Décision** : screening au 12/400, confirmation au 12/200.
- **Raison** : 12/400 est le pire cas pour le formotérol (ratio de masse 33:1) ; 12/200 est le
  pire cas pour l'uniformité du budésonide (0,8 % m/m). On traite le formotérol d'abord parce
  qu'il est le sujet du projet.
- **Réversibilité** : totale.

## ADR-008 — Aucun excipient supplémentaire en phase 1

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Décision** : lactose seul. MgSt = branche de secours ; leucine = écartée.
- **Raison** : les produits commercialisés équivalents ne déclarent **que du lactose** (P1) ;
  la leucine n'est documentée qu'en spray drying, que nous n'avons pas.
- **Réversibilité** : élevée (précédent réglementaire MgSt disponible, P14).

## ADR-009 — Aucun secret dans le dépôt

- **Date** : 2026-09-13 · **Statut** : ACTIVE
- **Contexte** : des clés API ont été fournies en session pour la recherche documentaire.
- **Décision** : elles ne sont **pas** écrites dans le dépôt ; usage en variable d'environnement
  uniquement.
- **Réversibilité** : sans objet.

## ADR-010 — Les critères d'acceptation sont ancrés sur un benchmark de marché, pas sur une convention

- **Date** : 2026-09-13 (session 2) · **Statut** : ACTIVE
- **Contexte** : les critères de Gate 1 à 4 avaient été fixés par convention (RSD ≤ 5 %,
  FPF ≥ 30 %). Le texte intégral de l'étude d'équivalence brésilienne fournit désormais les
  valeurs **mesurées sur un produit commercial équivalent**, sous supervision de l'ANVISA.
- **Décision** : conserver les seuils de phase (prudents) mais **afficher systématiquement le
  repère marché à côté** : RSD d'uniformité de teneur **1,62 % (BUD) / 2,02 % (FOR)** ; RSD de
  masse de gélule **3,09 %** ; RSD de dose délivrée **4,40 / 4,59 %** ; dose délivrée
  **73 % / 85 %** ; FPF **44,7 % / 56,1 %** ; FPD **140,7 µg / 6,18 µg**.
- **Raison** : un seuil conventionnel ne dit pas si l'on est bon ; un repère mesuré, oui. Un RSD
  formotérol de 4,5 % « passe » notre critère tout en étant **deux fois pire que le marché**.
- **Conséquence** : un lot qui passe les gates mais reste loin du repère n'est pas un succès,
  c'est un candidat à optimiser. Voir `docs/annexes/A3-plan-analytique.md` §4 bis.
- **Réversibilité** : totale.

## ADR-011 — La stratégie « un seul bulk, deux dosages » est confirmée par le marché

- **Date** : 2026-09-13 (session 2) · **Statut** : ACTIVE
- **Contexte** : la question restait ouverte de savoir s'il fallait deux architectures distinctes
  pour le 12/200 et le 12/400.
- **Décision** : une seule architecture de bulk, deux dosages obtenus par simple échange
  budésonide ↔ lactose.
- **Raison** : `FAIT CONFIRMÉ` — FORPACK capsair déclare **24,7880 mg** de lactose en 12/200 et
  **24,588 mg** en 12/400, soit **25,0000 mg dans les deux cas**, avec le lactose pour seul
  excipient et le même device. Le même industriel fait donc exactement cela.
- **Conséquence** : le lot **L7 (12/200)** n'a plus à démontrer une architecture, seulement que
  la charge de budésonide plus faible (0,800 % au lieu de 1,600 %) reste homogène.
- **Réversibilité** : élevée.

## ADR-012 — L'argument de clôture du débat interne est l'uniformité, pas seulement la FPF

- **Date** : 2026-09-13 (session 2) · **Statut** : ACTIVE
- **Contexte** : le site a séparé les deux formulations pour protéger l'uniformité.
- **Décision** : opposer à cette décision historique la donnée mesurée, et non un raisonnement.
- **Raison** : `FAIT CONFIRMÉ` — sur produits commerciaux, la **gélule combinée est plus
  uniforme que les deux gélules séparées** qu'elle remplace : RSD d'uniformité de teneur
  **2,02 % contre 3,23 %** pour le formotérol et **1,62 % contre 5,44 %** pour le budésonide ;
  et le formotérol y délivre **plus** de masse fine (6,18 contre 5,46 µg).
- **Conséquence** : la séparation historique n'a pas acheté l'uniformité qu'elle devait protéger.
  L'échec est donc imputable à l'architecture de prémélange, pas au principe de la combinaison.
- **Réversibilité** : sans objet (constat).

## ADR-013 — Au Gate 3, les réglages machine passent avant le carrier

- **Date** : 2026-09-13 (session 3) · **Statut** : ACTIVE · **Remplace** la consigne initiale du
  Gate 3 (« revenir au carrier/flux (SV010) »).
- **Contexte** : le Gate 3 (remplissage Modu-C à 25 mg) renvoyait directement au carrier en cas
  de RSD de masse insuffisant.
- **Décision** : distinguer deux cas. **Masse moyenne de 25 mg inatteignable** → sujet carrier
  (densité tassée, perméabilité à l'air, compressibilité). **Masse moyenne correcte mais RSD
  élevé** → **régler d'abord les paramètres machine** (chambre de dosage, hauteur du lit de
  poudre, pré-compression, vitesse) ; ne changer de carrier qu'ensuite.
- **Raison** : `FAIT CONFIRMÉ` — Faulhammer *et al.* (Int J Pharm 2014 ; Drug Dev Ind Pharm 2015),
  sur gélules taille 3 et 1–45 mg : la **masse de remplissage** est corrélée à la taille de
  particule, la perméabilité et la compressibilité, mais **aucune corrélation n'est trouvée entre
  les attributs du matériau et la variabilité de masse**, qui est dominée par les paramètres
  procédé.
- **Conséquence** : évite de sacrifier une architecture de bulk validée pour un problème de
  réglage de dosator. Nouvelle question **Q15** (paramètres actuels du Modu-C).
- **Réversibilité** : totale.

## ADR-014 — Le taux de remplissage cible est celui du constructeur, pas une estimation

- **Date** : 2026-09-13 (session 3) · **Statut** : ACTIVE
- **Décision** : viser **≈ 50 % de remplissage** du mélangeur pour le bulk (poudre sèche lourde),
  conformément à la guidance Bioengineering, et traiter tout dépassement comme un risque documenté.
- **Raison** : `INFÉRENCE HAUTE CONFIANCE` — la guidance constructeur (≈ 2/3 pour une poudre
  légère, **≈ 50 % pour une poudre lourde**, 20–30 rpm sur le 20 L) place le lot de **6 kg à 48 %
  (conforme)** et le lot de **9 kg à 71 % (au-dessus)**. L'hypothèse 3.1 de l'arbre de causes
  cesse d'être un raisonnement pour devenir un écart à une recommandation.
- **Conséquence** : renforce la répartition 7:2:1 (l'étape à fort remplissage n'incorpore plus
  que 10 % de la masse) et le repli « taille industrielle 6 kg ».
- **Réserve** : la fiche primaire n'a pas pu être téléchargée (403). **À confirmer sur la
  documentation interne de la machine avant toute décision engageante** (Q5).
- **Réversibilité** : totale.

## ADR-015 — Chaque API garde le carrier de son mono-produit *(remplace ADR-005)*

- **Date** : 2026-09-13 (session 5) · **Statut** : ACTIVE
- **Contexte** : information interne reçue — le **mono-produit formotérol utilise ML001 seul**,
  le **mono-produit budésonide utilise un mélange SV003 + ML001**. ADR-005 proposait un prémix
  formotérol sur SV003 : c'était une erreur, prise en l'absence de cette donnée.
- **Décision** : le **prémix formotérol se fait sur ML001**, et la base budésonide conserve son
  mélange SV003 + ML001. L'architecture recommandée devient le **double prémix (architecture D)**,
  qui n'est plus « la plus robuste mais la plus lourde » mais **la réunion de deux procédés déjà
  validés en interne** — la seule vraie nouveauté du procédé étant l'étape de combinaison.
- **Raison** : on ne change pas ce qui marche. Et la pratique interne est cohérente avec la
  théorie : ML001 est le seul des trois grades à posséder une vraie population fine (D10 3–7 µm)
  et le plus cohésif (Carr > 25 %) — exactement ce dont un actif à 0,048 % m/m a besoin.
- **Conséquence** : le **taux de ML001 du bulk combiné** devient une variable d'essai de premier
  rang (lots E-B et E-C), et non un paramètre hérité du budésonide. Nouvelle cause 5.3 dans
  l'arbre des causes, classée TRÈS PLAUSIBLE.
- **Réserve honnête** : `calcul interne` — le prémix ne pèse que **4,80 % du lot**. Il protège le
  formotérol pendant sa désagglomération mais **ne garantit pas qu'il conserve son environnement
  de fines après dilution**. D'où E-C.
- **Réversibilité** : totale.

## ADR-016 — Un étage de trois lots de 1 kg avant tout passage industriel

- **Date** : 2026-09-13 (session 5) · **Statut** : ACTIVE
- **Décision** : insérer un **étage 1 kg à trois lots** (E-A témoin, E-B double prémix,
  E-C carrier enrichi en ML001) **avant** les lots de 3 kg.
- **Raison** : `calcul interne` — les trois lots consomment **1,44 g de formotérol au total**,
  soit le coût d'**un seul** lot de 3 kg, et ils trient **deux variables** (architecture et taux
  de ML001) avant d'engager le moindre équipement industriel.
- **Conditions de validité, non négociables** :
  1. **cuve de 3 à 4 L** — dans la cuve de 20 L, 1 kg n'occupe que **8 %** et le résultat n'est
     représentatif dans aucun sens ; à défaut, mélangeur de paillasse et essai déclaré comme
     essai de **formulation**, jamais de procédé ;
  2. **tamisage manuel**, pas le Russell — sa rétention est une masse fixe, donc **1 à 5 % de
     perte à 1 kg** contre 0,3 à 1,7 % à 3 kg, probablement enrichie en fines donc en formotérol ;
  3. **le prémix ne se fait jamais dans l'Inversina 20 L** — 48 g y occupent **0,4 %** du volume.
     Récipient de 0,15 à 0,5 L.
- **Conséquence** : un étage de 1 kg n'a aucune valeur de procédé ; il ne sert qu'à trancher la
  formulation. C'est explicite dans `11-petites-echelles.md`.
- **Réversibilité** : totale.
