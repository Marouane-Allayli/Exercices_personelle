import hashlib

def calculer_coordonnes_x():
    x = int(input("Coordonées x : "))

    if -180 <= x <= 180 :
        if -47 <= x <= 23:
            print("La coordonnée x est dans une zone dangereuse! ")
            calculer_coordonnes_x()
            return None
        else:
            return x
    else:
        print("Coordonnée x invalide!")
        calculer_coordonnes_x()
        return None


def calculer_coordonnes_y():
    y = int(input("Coordonnées y : "))

    if -180 <= y <= 180:
        if 120 <= y <= 142:
            print("La coordonnée y est dans une zone dangereuse! ")
            calculer_coordonnes_y()
            return None
        else:
            return y
    else:
        print("Coordonnée y invalide!")
        calculer_coordonnes_y()
        return None

def creation_message(x,y):
    message_normal = f"Bonjours étrangers, la galaxie est vaste, mais cette planète semble déjà notre coup de cœur. Pourrions-nous établir un accord interstellaire amical ? Nos coordonnées actuelles sont {x,y}. Nous serions ravis de discuter et de collaborer pour explorer cette planète ensemble."
    message_normal_bytes = message_normal.encode()
    message = print(f"message chiffré = {hashlib.sha256(message_normal_bytes).hexdigest()}")
    return message

def trier_cadeaux_objet_neuf(cadeaux):

    cadeaux_objet_neuf = []

    for cadeau in cadeaux:
        if cadeau["etat"] == "Neuf" and cadeau["type"] == "Objet" :
            cadeaux_objet_neuf.append(cadeau["nom"])

    return cadeaux_objet_neuf

def trier_cadeaux_nourriture_fraiche(cadeaux):
    cadeaux_nourriture_fraiche = []

    for cadeau in cadeaux:
        if cadeau["etat"] == "Frais" and cadeau["type"] == "Nourriture":
            cadeaux_nourriture_fraiche.append(cadeau["nom"])

    return cadeaux_nourriture_fraiche

if __name__=="__main__":
    x = calculer_coordonnes_x()
    y = calculer_coordonnes_y()
    creation_message(x,y)

    cadeaux = cadeaux_extra_terrestres = [
    {"nom": "Cristal Luminescent", "type": "Objet", "etat": "Neuf"},
    {"nom": "Fruit Galactique", "type": "Nourriture", "etat": "Frais"},
    {"nom": "Cube Gravitationnel", "type": "Objet", "etat": "Brisé"},
    {"nom": "Nectar Lunaire", "type": "Nourriture", "etat": "Frais"},
    {"nom": "Sphère de Mémoire", "type": "Objet", "etat": "Neuf"},
    {"nom": "Champignon Stellaire", "type": "Nourriture", "etat": "Pourri"},
    {"nom": "Médaillon Interstellaire", "type": "Objet", "etat": "Brisé"},
    {"nom": "Pain d'Étoiles", "type": "Nourriture", "etat": "Frais"},
    {"nom": "Clé Dimensionnelle", "type": "Objet", "etat": "Neuf"},
    {"nom": "Baie Solaire", "type": "Nourriture", "etat": "Pourri"}
]
    objet_neuf = trier_cadeaux_objet_neuf(cadeaux)
    nourriture_fraiche = trier_cadeaux_nourriture_fraiche(cadeaux)

    print("Voici la nourriture fraiche:")
    for nourriture in nourriture_fraiche:
        print(nourriture)
    print("Voici les objets neufs:")
    for objet in objet_neuf:
        print(objet)










































