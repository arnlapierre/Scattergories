import random


# 12 cartes sont disponibles pour le jeu.
cartes_disponibles = [i for i in range(1, 13)]


# Sélectionner aléatoirement une carte. La carte choisie ne pourra être rejouée plus tard.
def choisir_carte():
    carte = random.choice(cartes_disponibles)
    cartes_disponibles.remove(carte)
    return carte


# Faces du dé
lettres = "ABCDEFGHIJKLMNOPRSTW"
dé = [i for i in lettres]


def coup_de_dé():
    return random.choice(dé)
