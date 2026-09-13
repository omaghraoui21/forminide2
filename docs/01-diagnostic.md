# Reconstruction du procédé interne et mécanismes physiques

*(Synthèse détaillée ; la version courte est la section A de `RAPPORT.md`.)*

## 1. Le procédé historique, décomposé en fonctions physiques

### Procédé 3 kg (historique)
Trois cycles identiques de dilution par 1 kg :
1. **Fraction 1** : ≈ 1 kg de lactose, **totalité de l'API en sandwich** (lactose/API/lactose)
   → mélange manuel ≈ 3 min → tamisage → Inversina ≈ 15 min.
2. **Fraction 2** : + ≈ 1 kg → mélange manuel ≈ 3 min → tamisage → Inversina ≈ 15 min.
3. **Fraction 3** : + ≈ 1 kg → mélange manuel ≈ 3 min → tamisage → Inversina ≈ 15 min.

### Scale-up historique
- **6 kg** = deux ensembles de 3 kg, combinés.
- **9 kg** = trois ensembles de 3 kg, combinés.

### Procédé 9 kg adapté
Même logique, fractions de ≈ 3 kg :
1. ≈ 3 kg + totalité de l'API en sandwich → Inversina ≈ 5 min → Russell 250 µm → Inversina 15 min.
2. + ≈ 3 kg → mélange → Russell 250 µm → Inversina 15 min.
3. + ≈ 3 kg → mélange ≈ 3 min → Russell 250 µm → Inversina 15 min.

## 2. Les quatre fonctions physiques que ce procédé remplit

| Fonction | Étape | Effet |
|---|---|---|
| **Confinement de l'API** | sandwich lactose/API/lactose | l'API micronisé n'est jamais libre : pertes, projection et charge électrostatique limitées |
| **Désagglomération calibrée** | tamisage 250 µm | transforme les mottes en **agglomérats de taille bornée** ; c'est le mécanisme central, démontré par US9616024 (RSD budésonide 14,3 % → 4,6 %) |
| **Érosion et distribution** | Inversina 15 min | le tumbler érode les agglomérats et transporte l'actif à l'échelle du lot |
| **Dilution progressive** | 3 fractions successives | chaque ajout ne perturbe qu'une fraction d'un mélange déjà bon ; c'est une dilution géométrique grossière |

**Ce procédé est robuste parce qu'il fait la désagglomération et la distribution en alternance,
et non simultanément.** C'est exactement ce que décrit et revendique EP3175842A1.

## 3. Pourquoi il devient fragile avec deux APIs

Quatre changements de régime, détaillés dans `RAPPORT.md` §A.2 :

1. **La charge d'API de la première fraction passe de 0,14 % (FOR seul) à ≈ 4,9 %** (BUD 400 + FOR).
2. **Les deux poudres micronisées se rencontrent à l'état pur** → co-agglomération ; le FOR,
   17 à 33 fois moins abondant, devient un passager des agglomérats de budésonide.
3. **Le tamis de 250 µm ne protège pas le formotérol** : un agglomérat de 250 µm porte
   27–41 % d'une dose, et les entités responsables d'un RSD de 10 % font ~56 µm — invisibles
   pour le tamis.
4. **La dernière dilution — la plus difficile — est exécutée à 65–79 % de remplissage**,
   là où le mélangeur est le moins efficace, alors que l'ancienne route par sous-lots ne lui
   confiait qu'une simple combinaison de mélanges déjà homogènes.

## 4. Ce qui, dans le procédé, ne doit surtout pas changer

- Le **sandwich** (confinement).
- Le **tamisage 250 µm** en amont et en intermédiaire (désagglomération calibrée).
- Le **mélange bas cisaillement** de 15 min (l'optimum publié en tumbler).
- La **dilution en trois fractions** (l'alternance désagglomération / distribution).
- Le **lactose comme unique excipient** (conforme aux produits commercialisés).
