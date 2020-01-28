#ouvrir CSV :

import csv
reader = csv.DictReader(open('Dataset_30reviews.csv')) #ouvrir fichier csv

# dico = [dict(row) for row in reader] #creation d'une liste de dictionnaires
# print (dico)

for row in reader:
   print(row['reviews.rating'], row['reviews.text']) #afficher une ou plusieurs colonnes



#____________________________________________________________________________________________
# compter mots et frequence :

data_treated = [("first com",True), ("com com bla",False), ("bla com2",True), ("com test",True)]

global number_of_com
number_of_com = len(data_treated)

def frequency_of_words (data_set) :

    words_list = []
    comments_list = []
    freq_word = {}
    number_of_words = {}
    word_counter = {}
    
    for i in range (number_of_com) :
        comments_list.append(data_set[i][0].split()) #list of lists with words (separated by a space) of each comment
        words_list = words_list + data_set[i][0].split() #list of all words in all comments separated by a space
    
    for word in words_list :
        number_of_words[word] = words_list.count(word) #count number of each word in all comments
    
    for word in number_of_words :
        word_counter[word] = 0
        for i in range (number_of_com) :
            if word in comments_list[i] : #count number of comments containing the word
                word_counter[word] += 1
        freq_word[word] = word_counter[word]/number_of_com #frequency of comments containing the word
        
        if freq_word[word] <= 0.3 :
            del freq_word[word] #delete words with a frequency <= 0.3    

    return (freq_word)

print (frequency_of_words(data_treated))
