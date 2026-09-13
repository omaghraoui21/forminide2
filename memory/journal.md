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
