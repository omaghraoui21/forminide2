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

- **Date** : 2026-09-13 · **Statut** : ACTIVE
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
