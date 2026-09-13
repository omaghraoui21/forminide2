# Journal de projet

## 2026-09-13 — Session 1 : cadrage, OSINT, brevets, diagnostic, plan d'essais

**Fait :**
- Dépôt initialisé : `GOAL.md`, `CLAUDE.md`, `AGENTS.md`, `RAPPORT.md`, `docs/`, `memory/`,
  `scripts/`, commande `/goal`.
- OSINT produits : Turquie (FORPACK capsair et discair, Neutec), Brésil (ALENIA, Biosintética),
  Inde (Foracort, Formonide), Europe (Symbicort, BF Spiromax, Breezhaler).
- Brevets : EP3175842A1, US9616024/9345664/9987229, US7879833/US8258124, US10449147/US10226421,
  US11642475/BR112016011996, HU228622B1.
- Littérature : Kinnunen 2015 (fines et budésonide), PLOS One 2013 (cinétique de mélange),
  Int J Pharm 2010 (ordre de mélange), CAB/AFM, co-agglomération de deux actifs.
- Calculs : charges, agglomérats, limite statistique, diamètre effectif par RSD, taux de
  remplissage de l'Inversina, quantités par lot (`scripts/calculs_cles.py`).

**Trouvailles décisives :**
1. **FORPACK 12/200 capsair (Turquie)** : KÜB déclarant **lactose 24,7880 mg** → masse totale
   **25,0000 mg**, **lactose pour seul excipient**, autorisé depuis 2013. Notre cible existe.
2. **EP3175842A1** : notre procédé historique est une plateforme brevetée publiée, et la
   **répartition des trois fractions** y est un facteur chiffré (AV de 7,1 à 12,5).
3. **US9616024** : le tamisage à 250 µm est le mécanisme qui rend le mélange bas cisaillement
   suffisant (RSD budésonide 14,3 → 4,6 %) — et démontre qu'un **haut cisaillement est inutile**.
4. **J Bras Pneumol 2012** : en gélule unique, la **FPF du formotérol (56 %) dépasse** celle du
   budésonide (45 %) et celle du formotérol en gélule séparée (52 %).
5. **Calcul** : un RSD de 10 % correspond à des entités de **56 µm** → **invisibles pour le tamis
   de 250 µm** ; et la limite statistique du formotérol est de 0,09 % → la « faible dose » n'est
   pas l'explication.

**Décisions prises :** ADR-001 à ADR-009 (voir `memory/decisions.md`).

**Prochaine action :** obtenir Q2 (titre du formotérol) et Q3/Q4 (archives du lot 9 kg
historique), puis lancer **L0** (prémix formotérol seul, 144 g).

**Non fait / limites de cette session :**
- Texte intégral de l'article brésilien non consulté (résumé seulement) : le dénominateur exact
  de la FPF (dose délivrée ou dose mesurée) reste à vérifier.
- KÜB de FORPACK 12/400 **capsair** non récupéré (seul le 12/400 discair l'a été) → Q12.
- Aucune donnée interne (lots historiques) n'était disponible dans le dépôt.

---

## 2026-09-13 — Session 2 : fermeture de lacunes OSINT (Exa)

**Outils** : API Exa opérationnelle. **API you.com : HTTP 403 sur `/v1/search` et `/search`**
(clé refusée ou plan inactif) → non utilisable en l'état.

**Fait :**
- Récupéré le **KÜB de FORPACK 12/400 capsair** (URL en minuscules : `...capsair-inhaler-Kapsul-Kub.pdf`).
- Récupéré le **texte intégral** de l'étude d'équivalence brésilienne
  (`jbp.org.br/export-pdf/1765/2012_38_6_10_english.pdf`, 9 pages) — SciELO renvoie 403,
  le miroir JBP fonctionne avec un `Referer`.
- Mis à jour : `RAPPORT.md`, `GOAL.md`, `docs/02`, `docs/annexes/A1`, `docs/annexes/A3`,
  `memory/decisions.md` (ADR-010 à 012), `memory/questions-ouvertes.md`.

**Trouvailles :**
1. **Q12 fermée** — FORPACK **12/400 capsair** : **laktoz 24,588 mg** → **25,0000 mg** au total,
   lactose seul, AMM 250/44 du 06/05/2013. **Le même bulk à 25 mg sert les deux dosages.**
2. **Tableau 1 complet de l'étude brésilienne** : la **gélule combinée est PLUS uniforme que les
   deux gélules séparées** — RSD d'uniformité de teneur **FOR 2,02 % contre 3,23 %**, **BUD
   1,62 % contre 5,44 %** — et le formotérol y délivre **plus** de masse fine (**6,18 contre
   5,46 µg**). C'est l'argument le plus fort du dossier contre la décision historique.
3. **Définition du dénominateur de la FPF levée** : le texte indique explicitement
   *fine particle fraction = fine particle dose / dose délivrée totale*. Les FPD calculés
   précédemment (140,7 µg BUD et 6,18 µg FOR) sont confirmés par le tableau.
4. **Méthodes de référence de la classe** : DUSA-DPI (Westech), **ACI Andersen 8301-60 à
   90 L/min**, Karl Fischer, sous supervision ANVISA.
5. La gélule de référence **« formotérol seul » pèse 25,19 mg** : une formulation à 0,048 % m/m
   dans 25 mg existe aussi en mono-produit commercial.

**Nouvelles questions** : Q13 (disposons-nous d'un ACI ?), **Q14 (quel RSD d'uniformité atteint
notre propre mono-produit formotérol ? — c'est le repère interne qui manque)**.

**Inchangé** : diagnostic, architecture recommandée et séquence expérimentale. Les nouvelles
données **renforcent** la recommandation, elles ne la modifient pas.

---

## 2026-09-13 — Session 3 : équipements, remplissage, et dossiers de lot exécutables

**Fait :**
- Recherche ciblée sur les trois questions d'équipement restantes (Q5, Q10, + Gate 3).
- Rédigé **`docs/09-dossiers-de-lot.md`** : dossiers de lot exécutables **L0, L1 et L2**, avec
  formules corrigées du titre, procédés pas à pas, plans de prélèvement à 10 positions, tableaux
  de relevé, feuille environnement et arbres de décision par lot.
- Mis à jour : `RAPPORT.md` (§A.2d, §J, Gate 3, arbre de décision, §O, achats),
  `docs/08-scale-up.md`, `docs/annexes/A1` (P16 à P18), `memory/questions-ouvertes.md`,
  `memory/decisions.md` (ADR-013, ADR-014), `README.md`.

**Trouvailles :**
1. **Guidance constructeur de l'Inversina** (relayée, fiche primaire non téléchargeable) :
   remplir à **≈ 50 % du volume pour une poudre sèche lourde**, ≈ 2/3 pour une poudre légère ;
   **20–30 rpm** sur le 20 L. Le lactose est une poudre lourde → **le lot de 9 kg (71 %) est
   au-dessus de la recommandation, le lot de 6 kg (48 %) est exactement dessus.** L'hypothèse
   « taux de remplissage » cesse d'être un raisonnement et devient un écart documenté.
   Note : à 25 rpm, nos 15 min = **≈ 375 révolutions** contre ≈ 330 pour EP3175842A1 → procédés
   énergétiquement comparables.
2. **Dispositif RS01** : version standard **faible résistance, 4 kPa à ≈ 100 L/min** ; version
   haute résistance **4 kPa à 65 L/min**. L'écart change complètement la FPF mesurée →
   **identifier notre version avant le premier NGI** (Q10 relevée en criticité haute).
3. **Remplissage par dosator à faible masse** (Faulhammer *et al.*, gélules taille 3, 1–45 mg) :
   la **masse** dépend du matériau (PSD, perméabilité, compressibilité), mais **la variabilité de
   masse n'est pas corrélée aux attributs du matériau** — elle est dominée par les paramètres
   procédé. → **ADR-013** : au Gate 3, régler la machine avant de toucher au carrier.

**Nouvelle question** : Q15 (paramètres actuels du Modu-C MS pour 25 mg).

**Inchangé** : diagnostic, architecture recommandée, séquence en 4 essais. Les trois trouvailles
**renforcent** le dossier — la première en particulier, qui adosse la cause 3.1 à la guidance du
constructeur.

---

## 2026-09-13 — Session 5 : carriers des mono-produits, et les petites échelles

**Information reçue de l'équipe** — décisive et jusqu'ici inconnue :
**mono-produit formotérol = ML001 seul** · **mono-produit budésonide = SV003 + ML001**.

**Ce que ça corrige :**
- **ADR-005 est remplacée par ADR-015.** Le prémix formotérol se fait sur **ML001**, pas sur
  SV003. C'était une erreur de recommandation, prise sans cette donnée.
- L'architecture recommandée devient le **double prémix (D)** : non plus « la plus robuste mais la
  plus lourde », mais **la réunion de deux procédés déjà validés**. La seule nouveauté du procédé
  est l'étape de combinaison.
- **Nouvelle cause 5.3, TRÈS PLAUSIBLE** : si le combiné historique a été fait sur le carrier du
  budésonide, le formotérol a perdu l'environnement de fines dont dépend son mono-produit.

**Réserve honnête posée** : `calcul interne` — le prémix ne pèse que **4,80 % du lot** à toute
échelle. Il protège le formotérol pendant sa désagglomération mais ne garantit pas qu'il conserve
ses fines après dilution. D'où le lot **E-C** (carrier enrichi à ≈ 33 % de ML001).

**Nouveau document `docs/11-petites-echelles.md`** — procédés à 1 kg et 3 kg :
- le vrai paramètre d'échelle est le **volume de cuve**, pas la masse : 1 kg dans la cuve de 20 L
  = **8 %** de remplissage, non représentatif dans aucun sens → **cuve de 3–4 L requise** ;
- **6 kg dans la cuve de 20 L = 50 %**, soit exactement la plage constructeur :
  **mécaniquement, 6 kg est l'échelle idéale de cet équipement**, pas 9 kg ;
- **le prémix ne peut se faire dans l'Inversina 20 L à aucune échelle** (48 à 432 g = 0,4 à 3,6 %
  du volume) → récipient de 0,15 à 1,5 L, Turbula ou mélange manuel ;
- **à 1 kg, tamisage manuel et non Russell** : la rétention est une masse fixe, donc 1 à 5 % de
  perte à 1 kg contre 0,3 à 1,7 % à 3 kg, probablement enrichie en fines donc en formotérol ;
- **étage 1 : trois lots de 1 kg (E-A, E-B, E-C) pour 1,44 g de formotérol au total**, soit le
  coût d'un seul lot de 3 kg, et ils trient deux variables avant d'engager l'équipement industriel.

**Nouvelles questions** : Q16 (ratio SV003:ML001 du BUD mono — bloque le pesage de l'étage 1),
Q17 (masse et RSD des mono-produits), **Q18 (taille de lot et cuve des mono-produits — peut
départager les causes 3.1 et 5.3 sans consommer un gramme d'API)**.

---

## 2026-09-13 — Session 6 : les données de production éliminent une hypothèse

**Informations reçues** : ratio budésonide mono **≈ 50:50 SV003/ML001** (à confirmer) ·
**masse de remplissage 25 mg pour tous les produits** · **taille de lot 9 kg pour les deux
mono-produits** · consigne explicite de ne plus traiter la cuve et l'échelle comme des causes.

**Correction majeure — l'hypothèse « taux de remplissage » est retirée (ADR-017).**
`calcul interne` : le formotérol mono, sur ML001 pur (570 g/L), occupe **78,9 %** de la cuve de
20 L à 9 kg — et il est fabriqué en routine avec succès. Le budésonide mono est à **75,2 %**.
Un actif à 0,048 % m/m est donc distribué de façon homogène dans 9 kg à 79 % de remplissage.
La guidance générique du constructeur (P16) ne résiste pas aux données du site. **Q18, posée
précisément pour ce test, a tranché.**

**Éliminées avec elle** : taille de lot de 9 kg, faible dose en elle-même, énergie et temps de
mélange, les trois tamisages, et l'objection « ML001 ne coule pas assez au dosator » — le
formotérol mono est rempli à 25 mg sur ML001 pur.

**Le diagnostic se réduit à deux causes** : co-agglomération BUD–FOR (33:1 en masse) et perte de
l'environnement de fines du formotérol (100 % → ≈ 52 % de ML001).

**Le plan se réduit en conséquence (ADR-019)** : trois lots de 1 kg (E-A co-sandwich/carrier BUD,
E-B double prémix/carrier BUD, E-C double prémix/carrier FOR 100 % ML001), puis **confirmation
directe à 9 kg**. L'étage 6 kg est supprimé, l'étage 3 kg devient facultatif.
Les niveaux de carrier sont **50 % et 100 %** (ADR-018) : les deux seuls points de l'espace dont
on sache en interne qu'ils fonctionnent. En cas d'arbitrage, **c'est au budésonide de s'adapter** —
à 1,600 % m/m il est 33 fois plus tolérant que le formotérol.

**Documents révisés** : `RAPPORT.md` (§A.2d, §A.3, §J), `docs/05-arbre-causes.md`,
`docs/11-petites-echelles.md` (réécrit, version 2), bandeau de révision sur `docs/10`.
`CLAUDE.md` porte désormais la consigne : **ne jamais ressortir l'hypothèse du taux de remplissage**.

**Questions fermées** : Q17 (25 mg pour tous), Q18 (9 kg pour les deux).
**Nouvelle question Q19, coût nul et très haute valeur** : le combiné historique était-il sur le
carrier du budésonide ou sur celui du formotérol ? Si c'était sur celui du budésonide, la cause
5.3 devient l'explication la plus simple de tout l'échec historique.
