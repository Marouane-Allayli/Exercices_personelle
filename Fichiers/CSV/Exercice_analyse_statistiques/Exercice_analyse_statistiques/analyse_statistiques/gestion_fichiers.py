import csv

def lire_classes_depuis_csv(nom_fichier):
    """
    Lit un fichier CSV contenant les classes et effectifs.
    Chaque ligne doit être : classe_heures;borne_inf;borne_sup;nombre_eleves
    Ignore l'en-tête et les lignes non numériques (comme Total)
    :param nom_fichier: Nom du fichier (incluant le chemin)
    :return: Retourne une liste de tuples : (borne_inf, borne_sup, effectif)
    """
    classes = []
    with open(nom_fichier, newline='', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier, delimiter=';')
        for ligne in lecteur:
            if not ligne or ligne[0] == "classe_heures":
                # Ignorer l'en-tête
                continue
            elif len(ligne) < 4:
                # Ignorer les lignes trop courtes
                continue
            try:
                borne_inf = float(ligne[1])
                borne_sup = float(ligne[2])
                effectif = int(ligne[3])
                ligne_tuple = (borne_inf, borne_sup, effectif)
                classes.append(ligne_tuple)

            except ValueError:
                # ignorer les lignes non numériques (ex: Total)
                continue
    return classes

def sauvegarder_resultats_csv(nom_fichier, resultats):
    """
    Sauvegarde les résultats statistiques dans un fichier CSV.
    'resultats' doit être une liste de tuples ou listes [nom_mesure, valeur]
    """
    try:
            # writer = csv.writer(fichier)
            # writer.writerow(['Mesure', 'Valeur'])
        print(f"Résultats sauvegardés dans {nom_fichier}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

if __name__ == "__main__":
    # Exemple de chemin absolu (à adapter à votre système)
    chemin_absolu = "C:/Users/marou/Downloads/Exercices_personelle/Fichiers/CSV/Exercice_analyse_statistiques/Exercice_analyse_statistiques/analyse_statistiques/Data"
    lire_classes_depuis_csv(chemin_absolu)
