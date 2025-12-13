import random
from http.cookiejar import uppercase_escaped_char


def surnom_debut(banque_debut):
    choix = random.choice(banque_debut)
    nom_debut = choix.capitalize()
    return nom_debut

def surnom_fin(banque_fin):
    choix = random.choice(banque_fin)
    nom_fin = choix.capitalize()
    return nom_fin

def surnom_finale(debut,fin):

    surnom = f"{debut} {fin}"
    print(surnom)
    return surnom

def creation_nom_famille():
    nom_famille = input("Nom de famille: ")
    verification_nom_famille(nom_famille)
    return nom_famille

def verification_nom_famille(nom_famille):

    if nom_famille != nom_famille.capitalize():
        creation_nom_famille()
    elif len(nom_famille) <= 3 :
        creation_nom_famille()


































if __name__ == '__main__':
    nom_debut =["tempête", "cyclone", "ouragan", "tornade", "typhon", "orage", "éclair", "couteau",
                "sabre", "épée", "fleuret","rapière", "dague", "poignard"]
    nom_fin = ["rouge", "bleu", "vert", "jaune", "noir", "blanc", "orange", "violet",
                  "rose", "tueur", "assassin", "meurtrier","exterminateur", "massacreur", "carnage", "boucher"]
    debut_surnom = surnom_debut(nom_debut)
    debut_fin = surnom_fin(nom_fin)
    surnom_finale(debut_surnom,debut_fin)

    nom_famille = creation_nom_famille()
    verification_nom_famille(nom_famille)



