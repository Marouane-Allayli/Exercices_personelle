import pytest
from Test_unitaire.Exercice_statistique.Exercice_analyse_statistiques.analyse_statistiques.analyse_stats import generer_liste_ponderee



def test_generer_liste_ponderee():
    classe = [(0, 5, 3)]
    heures_attendues = [2.5,2.5,2.5]
    heures_obtenues = generer_liste_ponderee(classe)

    assert heures_obtenues == heures_attendues


def test_generer_liste_ponderee2():
    classe = [(2, 8, 0)]
    heures_attendues = []
    heures_obtenu = generer_liste_ponderee(classe)

    assert heures_obtenu == heures_attendues

def test_generer_liste_ponderee3():



