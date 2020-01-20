import csv
reader = csv.DictReader(open('Dataset_30reviews.csv')) #ouvrir fichier csv

# dico = [dict(row) for row in reader] #creation d'une liste de dictionnaires
# print (dico)

for row in reader:
   print(row['reviews.rating'], row['reviews.text']) #afficher une ou plusieurs colonnes