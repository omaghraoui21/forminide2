#!/usr/bin/env python3
"""
Calculs de référence du projet bulk DPI Budésonide/Formotérol.

Reproduit toutes les valeurs chiffrées marquées `calcul interne` dans les documents du dépôt.
Aucune dépendance externe.   Usage :  python3 scripts/calculs_cles.py
"""
import math

# --- Données d'entrée -------------------------------------------------------
FILL_MG = 25.0e-3          # g de poudre par gélule
BUD = {"200": 200e-6, "400": 400e-6}   # g par gélule
FOR_ = 12e-6                # g par gélule (formotérol fumarate dihydraté)
RHO_API = 1.3               # g/cm3, densité vraie approx. d'un corticoïde/sel organique
# Densités versées DFE Pharma (g/L), brochure #004 mai 2020
POURED = {"ML001": 570, "SV003": 630, "SV010": 690, "SV003+8%ML001": 625}
BLENDER_L = 20.0            # volume de la cuve Inversina


def sep(t):
    print("\n" + t + "\n" + "-" * len(t))


def charges():
    sep("1. Charges massiques et rapports")
    for k, b in BUD.items():
        print(f"  BUD {k} µg : {b/FILL_MG*100:6.3f} % m/m   |   "
              f"FOR : {FOR_/FILL_MG*100:.4f} % m/m   |   ratio BUD:FOR = {b/FOR_:.1f}:1")
    print(f"  Lactose (dosage 200) : {(FILL_MG-BUD['200']-FOR_)*1e3:.4f} mg/gélule")
    print(f"  Lactose (dosage 400) : {(FILL_MG-BUD['400']-FOR_)*1e3:.4f} mg/gélule")
    print("  Référence marché FORPACK 12/200 : lactose 24,7880 mg -> total 25,0000 mg (FAIT CONFIRMÉ)")


def masse_agglomerat(d_um, rho_eff):
    """Masse (µg) d'un agglomérat sphérique de diamètre d_um et de masse volumique effective."""
    r_cm = d_um * 1e-4 / 2
    return 4 / 3 * math.pi * r_cm ** 3 * rho_eff * 1e6


def agglomerats():
    sep("2. Un agglomérat survivant porte quelle fraction d'une dose de formotérol ?")
    print("   d (µm) |  masse ρ=0,4 |  masse ρ=0,6 |   % d'une dose de 12 µg")
    for d in (355, 250, 212, 150, 100, 56, 35):
        m4, m6 = masse_agglomerat(d, 0.4), masse_agglomerat(d, 0.6)
        print(f"   {d:6d} | {m4:8.3f} µg | {m6:8.3f} µg |   {m4/12*100:5.1f} – {m6/12*100:5.1f} %")
    print("  -> le Russell 250 µm laisse passer des entités portant jusqu'à ~41 % d'une dose.")


def statistique():
    sep("3. Limite statistique du mélange (le formotérol est-il dosable ?)")
    for d in (1.5, 2.5, 4.0):
        mp = masse_agglomerat(d, RHO_API)           # µg par particule primaire
        n = 12 / mp
        print(f"  FOR d={d:.1f} µm -> {mp:.2e} µg/particule, {n:.2e} particules/dose, "
              f"RSD statistique minimal = {100/math.sqrt(n):.3f} %")
    print("  -> tout RSD mesuré > ~1 % est d'origine agglomérat/ségrégation, jamais statistique.")

    sep("4. À quel diamètre effectif correspond un RSD observé ?")
    for rsd in (0.02, 0.05, 0.10, 0.15):
        n = 1 / rsd ** 2
        munit = 12 / n                               # µg par entité
        v = munit * 1e-6 / RHO_API                   # cm3
        d = (6 * v / math.pi) ** (1 / 3) * 1e4       # µm
        print(f"  RSD {rsd*100:4.0f} %  ->  {n:6.0f} entités/dose, {munit:.3f} µg/entité, "
              f"d_effectif ≈ {d:3.0f} µm")
    print("  -> un RSD de 10 % correspond à des entités de ~56 µm : invisibles pour un tamis 250 µm.")


def remplissage():
    sep(f"5. Taux de remplissage de l'Inversina ({BLENDER_L:.0f} L)")
    masses = [3, 4.5, 6, 6.3, 7.2, 8.1, 9]
    print("   masse |" + "".join(f" {g:>16s} |" for g in POURED))
    for kg in masses:
        line = f"  {kg:5.1f} kg |"
        for g, rho in POURED.items():
            v = kg * 1000 / rho
            line += f"  {v:5.1f} L = {v/BLENDER_L*100:3.0f} % |"
        print(line)
    print("  -> à 9 kg : 65 % (SV010), 71 % (SV003), 79 % (ML001). L'étape la plus difficile")
    print("     du procédé est exécutée dans les pires conditions mécaniques.")


def lots():
    sep("6. Quantités par lot (dosage 12/400 et 12/200), répartition 7:2:1")
    for kg in (3, 6, 9):
        tot = kg * 1000.0
        for dose, b in BUD.items():
            bud_g = tot * b / FILL_MG
            for_g = tot * FOR_ / FILL_MG
            lac_g = tot - bud_g - for_g
            premix = for_g * 100                      # prémix à 1 % m/m
            f1, f2, f3 = lac_g * 0.7, lac_g * 0.2, lac_g * 0.1
            print(f"  {kg} kg / 12-{dose} : BUD {bud_g:7.2f} g | FOR {for_g:5.2f} g | "
                  f"lactose {lac_g:8.1f} g | prémix FOR (1 %) {premix:6.1f} g | "
                  f"fractions {f1:7.1f} / {f2:6.1f} / {f3:6.1f} g")


def analytique():
    sep("7. Faisabilité analytique (prise d'essai à l'échelle de la dose)")
    for v_ml in (2, 5, 10):
        print(f"  1 dose (25 mg) extraite dans {v_ml:2d} mL -> FOR {12/v_ml:5.2f} µg/mL | "
              f"BUD200 {200/v_ml:6.1f} µg/mL | BUD400 {400/v_ml:6.1f} µg/mL")
    print("  -> la sensibilité n'est pas la contrainte ; la contrainte est la TAILLE de la prise d'essai.")


if __name__ == "__main__":
    print("=" * 78)
    print("  Calculs de référence — bulk DPI Budésonide/Formotérol 25 mg/gélule")
    print("=" * 78)
    charges(); agglomerats(); statistique(); remplissage(); lots(); analytique()
    print("\nToutes ces valeurs sont marquées `calcul interne` dans les documents du dépôt.\n")
