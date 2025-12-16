import statistics




def generer_liste_ponderee(classes):
    """
    Fonction pour générer la liste complète des heures selon les effectifs
    :param classes:
    :return:
    """
    heures = []

    for donnes in classes :
            borne_inferieur = donnes[0]
            borne_superieur = donnes[1]
            effectif =donnes [2]

            moyenne = (borne_inferieur + borne_superieur) / 2

            for i in range(effectif):
                    heures.append(moyenne)


    return heures

def Calcule_moyenne(heures):
    heures_additioner = 0
    nombre_eleve = len(heures)

    for heure in heures:
        heures_additioner = heures_additioner + heure

    moyenne = heures_additioner / nombre_eleve

    return moyenne

def


# Exemple de données classes retournées après lecture du fichier : classes et effectifs


if __name__ == "__main__":

    classes = [
    (0, 5, 300),
    (5, 10, 400),
    (10, 15, 500),
    (15, 20, 330),
    (20, 25, 250),
    (25, 30, 160),
    (30, 35, 40),
    ]

    heures = generer_liste_ponderee(classes)
    Calcule_moyenne(heures)

