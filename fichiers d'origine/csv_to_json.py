import pandas as pd
import json


df = pd.read_csv("Questions Scattergories.csv", sep=";")

liste_1_to_12 = [i for i in range(1, 13)]
dico_cartes = {str(i):[] for i in range(1, 13)}

for i, j in enumerate(df.Carte):
    for key, values in dico_cartes.items():
        if str(j) == key:
            values.append(df.Question[i])

print(dico_cartes)

with open("Questions_Scattergories.json", "w") as outfile:
    json.dump(dico_cartes, outfile, indent=4, ensure_ascii=False)