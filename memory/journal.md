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
