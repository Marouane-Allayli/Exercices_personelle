import random


def creation_navire_pirate() -> dict:
    """
    Demande les caractéristiques du navire pirate et crée un dictionnaire avec ces caractéristiques.
    :return: Un dict avec les caractéristiques du navire pirate
    """

    # Demander les caractéristiques du navire pirate, avec validation
    while True:
        vitesse = input("Entrez la vitesse en nœuds [1-8] : ")
        try:
            vitesse = float(vitesse)
            if vitesse < 1 and 8 < vitesse:
                raise ValueError
        except ValueError:
            print("La vitesse doit être un nombre entre 1 et 8. Réessayez.")
        else:
            break

    while True:
        canons = input("Entrez le nombre de canons [0-12] : ")
        try:
            canons = int(canons)
            if canons < 0 or 12 < canons:
                raise ValueError
        except ValueError:
            print("Le nombre de canons doit être un nombre entier entre 0 et 12. Réessayez.")
        else:
            break

    while True:
        equipage_regulier = input("Entrez le nombre de membres d'équipage réguliers [10-30] : ")
        try:
            equipage_regulier = int(equipage_regulier)
            if equipage_regulier < 10 or 30 < equipage_regulier:
                raise ValueError
        except ValueError:
            print("Le nombre de membres d'équipage réguliers doit être un nombre entier entre 10 et 30. Réessayez.")
        else:
            break

    while True:
        equipage_elite = input("Entrez le nombre de membres d'équipage d'élite [1-5] : ")
        try:
            equipage_elite = int(equipage_elite)
            if equipage_elite < 1 or 5 < equipage_elite:
                raise ValueError
        except ValueError:
            print("Le nombre de membres d'équipage élite doit être un nombre entier entre 1 et 5. Réessayez.")
        else:
            break

    # Créer et retourner le dict avec les caractéristiques du navire pirate

    return navire_pirate


def type_combat_navire(navire_marchand: dict, navire_pirate: dict) -> str:
    """
    Évalue le type de combat entre un navire marchand et un navire pirate.
    :param navire_marchand: Caractéristiques du navire marchand
    :param navire_pirate: Caractéristiques du navire pirate
    :return: Le type de combat : 'distance', 'abordage' ou 'fuite'
    """
    # Assez vite pour fuir : marchand 2x plus vite que pirate
    if navire_marchand['vitesse'] > navire_pirate['vitesse'] * 2:
        type_combat = 'fuite'
    # Trop vite pour se faire aborder, pas assez vite pour fuir complètement : marchand un peu plus vite que pirate
    elif navire_marchand['vitesse'] > navire_pirate['vitesse']:
        type_combat = 'distance'
    # Trop lent, c'est l'abordage ! : Marchand moins vite que pirate
    else:
        type_combat = 'abordage'


def combat_a_distance(navire_marchand: dict, navire_pirate: dict) -> tuple[str, int]:
    """
    Simule un combat à distance entre un navire marchand et un navire pirate.
    Chaque navire tire sur l'autre jusqu'à ce que l'un des deux soit coulé.
    Ils ont une durabilité de 4 coups reçus chacun.
    Les chances de touchés sont déterminées par la puissance en combat à distance.
    :param navire_marchand: Caractéristiques du navire marchand
    :param navire_pirate: Caractéristiques du navire pirate
    :return: Le navire gagnant et la durée du combat.
    """
    # Calculer la puissance en combat à distance
    puissance_marchand = navire_marchand['canons'] * navire_marchand['vitesse']
    puissance_pirate = navire_pirate['canons'] * navire_pirate['vitesse']

    # Déterminer le navire gagnant, et la durée du combat, 5 minute par coup reçu
    durabilitee_marchand = 4
    durabilitee_pirate = 4
    while durabilitee_marchand > 0 or durabilitee_pirate > 0:
        attaque_marchand = random.randint(1, puissance_marchand)
        attaque_pirate = random.randint(1, puissance_pirate)
        # Celui qui obtient la plus grande puissance touche l'autre
        if attaque_marchand > attaque_pirate:
            durabilitee_pirate -= 1
        elif attaque_pirate > attaque_marchand:
            durabilitee_marchand -= 1
        duree_combat += 5

    # Déterminer le navire gagnant
    navire_gagnant = 'marchand' if durabilitee_marchand > 0 else 'pirate'

    return navire_gagnant, duree_combat


def main():
    navire_marchand = {'vitesse': 4,
                       'canons': 4,
                       'equipage_regulier': 20,
                       'equipage_elite': 2}

    navire_pirate = creation_navire_pirate()

    # Évaluer le type de combat
    type_combat = type_combat_navire(navire_marchand, navire_pirate)

    if type_combat == 'distance':
        combat_a_distance(navire_marchand, navire_pirate)
        print(f"Le navire {navire_gagnant} a gagné le combat en {duree_combat} minutes !")
    elif type_combat == 'abordage':
        # TODO combat_abordage() ** Ceci n'est pas une des erreurs à corriger **
        print("Les marchands ont été abordés ! ** CETTE FONCTIONNALITÉ N'EST PAS ENCORE IMPLÉMENTÉE **")
    elif type_combat == 'fuite':
        print("Les marchands ont fui !")


if __name__ == '__main__':
    main()
