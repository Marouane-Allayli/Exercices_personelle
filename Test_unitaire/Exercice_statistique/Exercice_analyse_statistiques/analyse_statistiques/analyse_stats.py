

def generer_liste_ponderee(classes : list[tuple[int, int, int]]):
    """
    Fonction pour générer la liste complète des heures selon les effectifs
    :param classes:
    :return:
    """
    heures = []
    # Une liste d'une classe (10, 15, 500)
    # ==> borne_inf = 10, borne_sup = 15, borne_sup = 500
    for borne_inf, borne_sup, effectif in classes:
        if effectif < 0:
            effectif = 0

        milieu = (borne_inf + borne_sup) / 2
        for i in range(effectif):
            heures.append(milieu)

        # Code plus compact.
        # heures_classe = [milieu] * effectif
        # heures.extend(heures_classe)
    return heures

classes = [
    (0, 5, 0),
]


heures_donnees = generer_liste_ponderee(classes)
print(heures_donnees)