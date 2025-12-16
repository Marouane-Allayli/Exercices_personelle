import csv
import datetime
import _strptime


def lire_fichier():


    try:
        with open("C:/Users/marou/Downloads/Exercices_personelle/Fichiers/CSV/Exercice_analyse_statistiques/Exercice_analyse_statistiques/analyse_statistiques"
              "/Data/donnees_etudiants.csv",newline="",encoding="utf-8") as fichier:
            donnes = []
            lecteur = csv.DictReader(fichier,delimiter=";")
            for ligne in lecteur:
                date = ligne["date"]
                nom = ligne["nom"]
                heures = ligne['heures_travail']
                revenu_hebdo = ligne["revenu_hebdo"]
                donnes.append({"date":date,"nom":nom,"heures":heures,"revenu_hebdo":revenu_hebdo})

    except FileNotFoundError:
        pass


    try:
        print(donnes)
    except UnboundLocalError:
        pass




if __name__=="__main__":
    lire_fichier()