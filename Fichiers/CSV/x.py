

import csv
p =[]
#  lire un fichier
# with open('exercices.csv',"r", encoding="UTF-8") as fichier :
#
#     lecture_doc = csv.reader(fichier)
#
#     for ligne in lecture_doc:
#         print(ligne)
#

# écrire dans un fichier csv
with open("exercices.csv","r",encoding="utf-8") as fichier1:
    lire_fichier = csv.reader(fichier1)



with open("exercices.csv","w",encoding="utf-8") as fichier:

    ecrire = csv.writer(fichier)
    ecrire.writerow(['Colonne1', 'Colonne2'])


