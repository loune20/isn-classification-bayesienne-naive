#ouvrir CSV :

import csv
reader = csv.DictReader(open('Dataset_30reviews.csv')) #ouvrir fichier csv

# dico = [dict(row) for row in reader] #creation d'une liste de dictionnaires
# print (dico)

for row in reader:
   print(row['reviews.rating'], row['reviews.text']) #afficher une ou plusieurs colonnes




# compter mots et frequence :

number = {}
freq_word = {}

com = "oui oui non mais pas oui or non"
word_list = com.split() #creation d'une liste en separant chaque mot par un espace

for mot in word_list :
    number[mot] = word_list.count(mot) 

print ("nombre de mots :", number)

for mot in number :
    freq_word[mot] = word_list.count(mot)/len(number)
    
print ("frequence :", freq_word)
