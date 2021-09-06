import random

""" Ce module implante un lancer de dé"""


# Faces du dé
lettres = "ABCDEFGHIJKLMNOPRSTW"
dé = [i for i in lettres]


def coup_de_dé():
    return random.choice(dé)
