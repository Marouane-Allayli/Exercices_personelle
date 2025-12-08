# Consommation de carburant en L/10 années lumière
CONSOMMATION = 8

def calculer_carburant(distance: float, reserve_carburant: float) -> str:
    """
    Fonction qui permet de calculer si le carburant à bord du vaisseau permet de réaliser un voyage spatial.
    :param distance: la distance à parcourir pour se rendre à destination en années lumière.
    :param reserve_carburant: la quantité de carburant actuelle dans le vaisseau en litres.
    :return: Le résultat de l'évaluation du voyage.
    """
    try:
        if distance < 0 or reserve_carburant < 0:
            print(f"La distance ou la réserve de carburant ne peuvent pas être négatifs.")
            return None

    except TypeError:
        return None

    carburant_consomme = distance * CONSOMMATION / 10

    if carburant_consomme * 2 <= reserve_carburant:
        return "Vous avez suffisament de carburant pour faire l'aller-retour."

    elif carburant_consomme > reserve_carburant:
        return "Vous manquerez de carburant en cours de chemin!"

    else:
        return "Vous pouvez vous rendre à destination, mais pas revenir."


if __name__ == '__main__':
    while True:
        try:
            distance_voyage = float(input("Quelle est la distance à parcourir (en années lumière) : "))
            carburant = float(input("Quel est votre niveau actuel de carburant (en litres) : "))
            break
        except ValueError:
            print("Impossible de faire le calcul avec les informations données")

    print(calculer_carburant(distance_voyage, carburant))
