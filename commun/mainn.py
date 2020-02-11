#For testing purpose only
#data_original = [['word1 okay', False], ['word2 super great', True], ['word2', True], ['word3', True], ['word2', True], ['super great', False]]

#IMPORTING LIBRARIES
import csv #importing csv python library

#GLOBAL VARIABLES
ponctuation = ['.',',',';',':','!','?','/','*','-','+','&','"','(',')','[',']','{','}','_','°','=','#',"'"]
common = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than','also','might']

#FUNCTIONS
def preProcessing(data_original):  #function that puts in lowercase and removes stop-words and punctuation  
    text_com = [] #list with all the text of each com (without their rates) 
    data_treated = [] #List of the processed text of each com and the associated rate
    index = []

    for i in range(len(data_original)): 
        data_treated.append(None) #Populate empty list
        text_com.append(data_original[i][0])
        text_com[i] = text_com[i].lower() #Lowercase evrything
        for j in range(len(ponctuation)):
            text_com[i] = text_com[i].replace(ponctuation[j],'') #Remove punctuation
        text_com[i] = text_com[i].split()
        for j in range(len(text_com[i])):
            for k in range(len(common)):
                if text_com[i][j] == common[k] : #Find stop-words
                    index.append(j)
                    index.sort()
                    index.reverse()
        for l in range(len(index)):
            del(text_com[i][index[l]]) #Remove stop-words
        index = []
        text_com[i]=" ".join(text_com[i])
        data_treated[i] = [text_com[i],data_original[i][1]]
    return(data_treated)

def frequencyOfWords (data_set): #function that calculates the frequency of each word in all comments
    comments_list = [] #list with all the (pre-processed) text of each com (without their rates)
    freq_word = {}
    word_counter = {} #dictionary with the word and the number of comments containing the word
    
    for i in range(len(data_set)):
        comments_list.append(data_set[i][0])

    for word in words_list:
        word_counter[word] = 0 #create a dictionary with all the words as keys, and 0 as value
        for i in range (len(data_set)):
            if word in comments_list[i]: #count number of comments containing the word
                word_counter[word] += 1 
        freq_word[word] = word_counter[word]/len(data_set) #frequency of comments containing the word
        
        if freq_word[word] <= 0.1:
            del freq_word[word] #delete words with a frequency <= 0.1 in the list freq_word

    return (freq_word)

def calculatePosScore(data_set): #function that calculates the positivity score of each word in comments
    comments_list_of_pos = [] #list with the (pre-processed) text of each positive com
    freq_word_in_pos = {}
    word_counter = {} #dictionary with the word and the number of comments positive containing the word
    pos_score = {}
    number_of_pos_com = 0 #number of positive comments
    
    for i in range(len(data_set)):
        if data_set[i][1] == True : #if the comment is positive
            comments_list_of_pos.append(data_set[i][0])
            number_of_pos_com += 1
    for word in words_list:
        word_counter[word] = 0 #create a dictionary with all the words as keys, and 0 as value
        for i in range (number_of_pos_com):
            if word in comments_list_of_pos[i]: #count number of comments positive containing the word
                word_counter[word] += 1 
        freq_word_in_pos[word] = word_counter[word]/len(data_set) #frequency of comments positive containing the word

    for word in words_list :
        pos_score[word] = freq_word_in_pos[word] / (number_of_pos_com / len(data_set)) #probability that the comment contains the word knowing it is positive = word positivity score

    return(pos_score)

#MAIN

#Extracting data from dataset     
reader = csv.DictReader(open('curated_short_reviews_Video_Games_5.csv')) #opening file      
data_original = [] #creating empty list
for row in reader: #for each row in our csv file
    data_original.append([row['reviewText'], row['overall']]) #adding at the end of the list a tuple of the summary and the rating extracted from the csv file

#Changing 1 and 5 to False and True
for i in range(len(data_original)):
    if data_original[i][1] == "1":
        data_original[i][1] = False
    elif data_original[i][1] == "5":
        data_original[i][1] = True
    else:
        print("Error : one of the comment has an overall that's neither 1 or 5")

#Text data pre-processing
data_treated = preProcessing(data_original)

#Creating a list of all the processed words
words_list = []   
for i in range (len(data_treated)):
    words_list = words_list + data_treated[i][0].split() #list of all words (after pre-processing, in all comments)
for word in words_list:
    if words_list.count(word) > 1:
        words_list.remove(word)

#Calculate the frequency of each word in all comments of data_treated
freq_words = frequencyOfWords(data_treated) 

#Calculate the frequency of each word in all positive comments of data_treated
pos_score = calculatePosScore(data_treated)

#Printing etc...
print(pos_score)
