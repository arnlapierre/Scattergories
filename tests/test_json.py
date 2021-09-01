import json

num_carte_départ = 1


def afficher_questions(num_carte):
    with open("Questions_Scattergories.json",) as fich:
        data = json.load(fich)

    num_carte = str(num_carte)
    print(num_carte)
    for i, j in enumerate(data[num_carte]):
        print(f"{i + 1}. {j}")

def carte_suivante():
    global num_carte_départ
    if num_carte_départ == 12:
        num_carte_départ = 1
    else:
        num_carte_départ += 1

def main():
    global num_carte_départ
    afficher_questions(num_carte_départ)
    carte_suivante()
    afficher_questions(num_carte_départ)
    carte_suivante()
    carte_suivante()
    carte_suivante()
    carte_suivante()
    carte_suivante()
    carte_suivante()
    carte_suivante()
    carte_suivante()
    carte_suivante()
    carte_suivante()
    print(num_carte_départ)
    carte_suivante()
    print(num_carte_départ)
    afficher_questions(num_carte_départ)


if __name__ == "__main__":
    main()