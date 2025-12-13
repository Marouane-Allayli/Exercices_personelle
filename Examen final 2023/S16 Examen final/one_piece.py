chapeau_de_paille = ['Zoro', 'Nami', 'Usopp', 'Sanji',
              'Chopper', 'Robin', 'Franky', 'Brook']

mechants_capitaines = ['Buggy', 'Kuro', 'Eustass', 'Arlong',
                       'Morgan', 'Blackbeard']


def ami_ou_ennemi(personnage: str) -> tuple[str, int]:
    """
    Fonction qui permet de savoir si un personnage est un ami ou un ennemi.
    :param personnage: Le personnage à vérifier
    :return: Un message et, si le personnage est connu, la longueur du nom du personnage
    """
    # vérifier les allégeances
    if personnage in chapeau_de_paille:
        message = "C'est un ami !"
    elif personnage in mechants_capitaines:
        message = "C'est un ennemi !"
    else:
        message = "Je ne connais pas ce personnage !"
    return (message, len(personnage))


def main():
    personnage = input("Entrez un personnage de l'univers OnePiece : ").strip().capitalize()
    message, longeur_nom = ami_ou_ennemi(personnage)
    print(f"{personnage} : {message}")


if __name__ == '__main__':
    main()

