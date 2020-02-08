#ouvrir CSV :

import csv
reader = csv.DictReader(open('Dataset_30reviews.csv')) #ouvrir fichier csv

# dico = [dict(row) for row in reader] #creation d'une liste de dictionnaires
# print (dico)

for row in reader:
   print(row['reviews.rating'], row['reviews.text']) #afficher une ou plusieurs colonnes



#____________________________________________________________________________________________
# compter mots et frequence : (ancienne version)

data_treated = [("first com",True), ("com com bla",False), ("bla com2",True), ("com test",True)]

number_of_com = len(data_treated) #creation of number_of_com as a global variable

def frequencyOfWords (data_set) :

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

print (frequencyOfWords(data_treated))



#____________________________________________________________________________________________
# Probabilité que le commentaire contienne le mot sachant qu’il est positif :

data_treated = [['word1',False], ['word2', True], ['word2', True], ['word3', True]]
freq_word_in_pos = {"word1": 0, "word2": 2/3, "word3": 1/3} #liste par Mathis

pos_score = {}
number_of_pos_com = 0

for i in range (len(data_treated)) :
    if data_treated[i][1] == True : #if the comment is positive
        number_of_pos_com += 1 #count the number of positive comments
prob_pos = number_of_pos_com / len(data_treated) #calculate the probability that a comment is positive

#deja present dans frequencyOfWords, ici pour avoir number_of_words
words_list = []
comments_list = []
number_of_words = {}
    
for i in range (len(data_treated)) :
    comments_list.append(data_treated[i][0].split()) #list of all comments with the words of each comment (separated by a space)
    words_list = words_list + data_treated[i][0].split() #list of all words in all comments separated by a space

for word in words_list :
    number_of_words[word] = words_list.count(word) #count number of each word in all comments

#besoin de creer une liste avec tous les mots (ici number_of_words)
for word in number_of_words :
    pos_score[word] = freq_word_in_pos[word] / prob_pos #probability that the comment contains the word knowing it is positive = word positivity score
 
print(pos_score)
