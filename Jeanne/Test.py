#ouvrir CSV :

import csv
reader = csv.DictReader(open('Dataset_30reviews.csv')) #ouvrir fichier csv

# dico = [dict(row) for row in reader] #creation d'une liste de dictionnaires
# print (dico)

for row in reader:
   print(row['reviews.rating'], row['reviews.text']) #afficher une ou plusieurs colonnes



#____________________________________________________________________________________________
# compter mots et frequence :

number_of_words = {}
freq_word = {}
words_list = []
word_counter = {}

data_set = (("first com",True), ("com com com2",False), ("com3",True), ("com test",True))
number_of_com = len(data_set)

for i in range (0, number_of_com) : #create a list of all the words 
    com = data_set[i][0] 
    words_list = words_list + com.split() #add words separated by a space to the list
    
print (words_list)

for word in words_list : 
    number_of_words[word] = words_list.count(word) #count number of each word in all comments
    
for word in number_of_words :
    word_counter[word] = 0 #create a dict with all the words as keys

#A CORRIGER : compte le nb total de mots et pas uniquement nb de coms avec mot :
for word in word_counter :
    for i in range(0, number_of_com) :
        if word in data_set[i][0] :
            word_counter[word] = word_counter[word] + 1

    freq_word[word] = word_counter[word]/number_of_com #word frequency in comments

print ("word_counter :", word_counter)
print ("nombre de mots :", number_of_words)
print ("frequence :", freq_word)
