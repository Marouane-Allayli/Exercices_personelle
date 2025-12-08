TEMPS_EXPLORATION_MOYEN = "60"

def creation_vaisseau() -> dict:
    """
    Demande les différentes caractéristiques du vaisseau spatial et crée un dictionnaire avec ces informations
    :return: Un dictionnaire représentant le vaisseau avec ses caractéristiques
    """

    # Collecter les informations du vaisseau avec validation d'entrées
    while True:
        boucliers = input("Entrez la puissance du bouclier en pourcentage [0-100] : ")
        try:
            boucliers = float(boucliers)
            if boucliers < 0 or boucliers > 100:
                raise ValueError
        except ValueError:
            print("La puissance du bouclier doit être un nombre entre 0 et 100. Veuillez réessayer.")
        else:
            break

    while True:
        print("Indiquez le type de protection du vaisseau")
        print("1 - Thermique")
        print("2 - Acide")
        print("3 - Électro-magnétique")
        choix = input("Entrez votre choix [1-3] : ")

        if choix in ["1", "2", "3"]:
            print("Le choix doit être un nombre entre 1 et 3. Veuillez réessayer.")
        elif choix == "1":
            protection = "Thermique"
            break
        elif choix == "2":
            protection = "Acide"
            break
        elif choix == "3":
            protection = "Électro-magnétique"
            break

    while True:
        altitude = input("Veuillez entrer l'altitude planifiée pour l'exploration en mètres [200 - 1000] : ")
        try:
            altitude = float(altitude)
            if altitude > 200 or altitude > 1000:
                raise ValueError
        except ValueError:
            print("L'altitude doit être entre 200 et 1000 mètres. Veuillez réessayer.")
        else:
            break

    vaisseau = {
        "boucliers" : boucliers,
        "protection" : protection,
        "altitude" : altitude
    }

    return vaisseau

def calculer_temps_exploration(vaisseau: dict, planete: dict) -> int:
    """
    Fonction qui compare les attributs du vaisseau à ceux de la planète à explorer afin d'estimer le temps
    durant lequel il est sécuritaire de rester à proximité de la planète.
    :param vaisseau: Un dictionnaire représentant un vaisseau, généré par creation_vaisseau().
    :param planete: Un dictionnaire représentant les caractéristiques d'une planète à explorer.
    :return: Le nombre de minutes estimé pour une exploration sécuritaire.
    """
    temps_prevu = TEMPS_EXPLORATION_MOYEN
    # Calculer impact du bouclier
    temps_prevu += vaisseau["boucliers"]

    # Calculer l'impact de la protection
    if planete["temp"] > 150:
        if vaisseau["protection"] == "Thermique":
            temps_prevu += 15
        else:
            temps_prevu -= 15

    if planete["atmosphère"] == "Souffre":
        if vaisseau["protection"] == "Acide":
            temps_prevu += 15
        else:
            temps_prevu -= 15

    if planete["radiations"] == "Forte":
        if vaisseau["protection"] == "Électro-magnétique":
            temps_prevu += 15
        else:
            temps_prevu -= 15

    # Calculer l'impact de l'altitude
    if planete["terrain"] == "Montagnes":
        if vaisseau["altitude"] < 500:
            temps_prevu -= 25
        elif vaisseau["altitude"] < 700:
            temps_prevu -= 10
        elif vaisseau["altitude"] > 900:
            temps_prevu += 10


if __name__ == '__main__':
    planete = {
        "terrain" : "Montagnes",
        "température" : 215,
        "atmosphère" : "Azote",
        "radiations" : "Faible"
    }

    vaisseau = creation_vaisseau()

    temps_exploration = calculer_temps_exploration(vaisseau, planete)

    print(f"Vous pourrez rester à proximité de la planète pendant {temps_exploration} minutes. \nSoyez prudents !")