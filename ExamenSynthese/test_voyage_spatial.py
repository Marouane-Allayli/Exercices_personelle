from ExamenSynthese.voyage_spatial import *



def test_calculer_carburant_negatif():
    reserve_carburant = -1

    resultat = calculer_carburant(1,reserve_carburant)

    assert resultat is None


def test_carburant_vide():
    reserve_carburant = 0
    resultat = calculer_carburant(100,reserve_carburant)

    assert resultat == "Vous manquerez de carburant en cours de chemin!"



def test_distance_negatif():
    distance = -2

    resultat = calculer_carburant(distance,1000)

    assert resultat is None

def test_distance_vide():
    distance = 0

    resultat = calculer_carburant(distance,1000)

    assert resultat is "Vous avez suffisament de carburant pour faire l'aller-retour."

