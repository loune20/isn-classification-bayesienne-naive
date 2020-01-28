#LOUISE :
import csv #importing csv python library
      
reader = csv.DictReader(open('data2.csv')) #opening file
        
list_data = [] #creating empty list
for row in reader: #for each row in our csv file
    list_data.append((row['review'], row['overall'])) #adding at the end of the list a tuple of the summary and the rating extracted from the csv file
    
print(list_data) #print our final result

for i in range len(list_data):
    if list_data[1] == 1:
        list_data[1] = False
    elif list_data[1] == 5:
        list_data[1] = True
    else:
        print("Error : one of the comment has an overall that's neither 1 or 5")

#JEANNE :
number_of_com = len(list_data) #creation of number_of_com as a global variable

#data_treated = [("first com",True), ("com com bla",False), ("bla com2",True), ("com test",True)]

def frequency_of_words (data_set) : #function

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
