import csv #importing csv python library
      
reader = csv.DictReader(open('curated_short_reviews_Video_Games_5.csv')) #opening file
        
data_original = [] #creating empty list
for row in reader: #for each row in our csv file
    data_original.append([row['reviewText'], row['overall']]) #adding at the end of the list a tuple of the summary and the rating extracted from the csv file
    

for i in range(len(data_original)):
    if data_original[i][1] == "1":
        data_original[i][1] = False
    elif data_original[i][1] == "5":
        data_original[i][1] = True
    else:
        print("Error : one of the comment has an overall that's neither 1 or 5")

#VERIFIER ENCHAINEMENT AVEC UN DATASET

def preProcessing(data_original):    
    my_list = []
    data_treated = []
    index = []
    ponctuation = ['.',',',';',':','!','?','/','*','-','+','&','"','(',')','[',']','{','}','_','°','=','#',"'"]
    common = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than','also','might']
    for i in range(len(data_original)): #Populate empty list
        data_treated.append(None)
        my_list.append(data_original[i][0])
        my_list[i] = my_list[i].lower() #put all in lowercase
        for j in range(len(ponctuation)):
            my_list[i] = my_list[i].replace(ponctuation[j],'')
        my_list[i] = my_list[i].split()
        for j in range(len(my_list[i])):
            for k in range(len(common)):
                if my_list[i][j] == common[k] : #find common
                    index.append(j)
                    index.sort()
                    index.reverse()
        for l in range(len(index)):
            del(my_list[i][index[l]])
        index = []
        my_list[i]=" ".join(my_list[i])
        data_treated[i] = [my_list[i],data_original[i][1]]
    return(data_treated)


def frequencyOfWords (data_set) : #function that calculates the frequency of each word in all comments

    words_list = []
    comments_list = []
    freq_word = {}
    number_of_words = {}
    word_counter = {}
    
    for i in range (len(data_treated)) :
        comments_list.append(data_set[i][0].split()) #list of all comments with the words of each comment (separated by a space)
        words_list = words_list + data_set[i][0].split() #list of all words in all comments separated by a space
    
    for word in words_list :
        number_of_words[word] = words_list.count(word) #count number of each word in all comments
    
    for word in number_of_words :
        word_counter[word] = 0 #create a dictionary with all the words as keys, and 0 as value
        for i in range (len(data_treated)) :
            if word in comments_list[i] : #count number of comments containing the word
                word_counter[word] += 1 #dictionary with the word and the number of comments containing the word
        freq_word[word] = word_counter[word]/len(data_treated) #frequency of comments containing the word
        
        if freq_word[word] <= 0.1 :
            del freq_word[word] #delete words with a frequency <= 0.1 in the list freq_word

    return (freq_word)


def frequencyOfWordsPos (data_set) : #function that calculates the frequency of each word in all comments

    words_list_pos = []
    comments_list = []
    freq_word_pos = {}
    number_of_words = {}
    word_counter = {}
    
    for i in range (len(data_treated)) :
        comments_list.append(data_set[i][0].split()) #list of all comments with the words of each comment (separated by a space)
        if data_set[i][1] == True :
            words_list_pos = words_list_pos + data_set[i][0].split() #list of all words in all comments separated by a space
    
    for word in words_list_pos :
        number_of_words[word] = words_list_pos.count(word) #count number of each word in all comments
    
    for word in number_of_words :
        word_counter[word] = 0 #create a dictionary with all the words as keys, and 0 as value
        for i in range (len(data_treated)) :
            if word in comments_list[i] : #count number of comments containing the word
                word_counter[word] += 1 #dictionary with the word and the number of comments containing the word
        freq_word_pos[word] = word_counter[word]/len(data_treated) #frequency of comments containing the word
        
        if freq_word_pos[word] <= 0.1 :
            del freq_word_pos[word] #delete words with a frequency <= 0.1 in the list freq_word_pos

    return (freq_word_pos)


data_treated = preProcessing(data_original) #text data pre-processing
freq_words = frequencyOfWords(data_treated) #calculate the frequency of each word in all comments of data_treated
print(freq_words)
freq_words_pos = frequencyOfWordsPos(data_treated)
print(freq_words_pos)


data_original = [("ourselves , are here in between the monkey is great", True), ("once upon a time the wizard was very happy it is a good news", False), ("blabla is a very good friend", True)]
data_treated = preProcessing(data_original)
print(data_original)
print(data_treated)