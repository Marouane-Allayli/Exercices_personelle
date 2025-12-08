from ExamenSynthese.voyage_spatial import *

def test_calculer_carburant_vide():
    reserve_carburant = 0

    resultat = calculer_carburant(1,reserve_carburant)
    assert