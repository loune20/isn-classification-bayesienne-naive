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


#VERIFIER ENCHAINEMENT AVEC UN DATASET

def preProcessing(data_original):    
    my_list = []
    ponctuation = ['.',',',';',':','!','?','/','*','-','+','&','"','(',')','[',']','{','}','_','°','=','#',"'"]
    data_treated = []
    common = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
    index = []
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


def frequencyOfWords (data_set) :

    words_list = []
    comments_list = []
    freq_word = {}
    number_of_words = {}
    word_counter = {}
    
    for i in range (len(data_treated)) :
        comments_list.append(data_set[i][0].split()) #list of lists with words (separated by a space) of each comment
        words_list = words_list + data_set[i][0].split() #list of all words in all comments separated by a space
    
    for word in words_list :
        number_of_words[word] = words_list.count(word) #count number of each word in all comments
    
    for word in number_of_words :
        word_counter[word] = 0
        for i in range (len(data_treated)) :
            if word in comments_list[i] : #count number of comments containing the word
                word_counter[word] += 1
        freq_word[word] = word_counter[word]/len(data_treated) #frequency of comments containing the word
        
        if freq_word[word] <= 0.3 :
            del freq_word[word] #delete words with a frequency <= 0.3    

    return (freq_word)

data_original = [("ourselves are here in between the monkey is great", True), ("once upon a time the wizard was very happy it is a good news", False), ("blabla is a very good friend", True)]
data_treated = preProcessing(data_original)
freq_words = frequencyOfWords(data_treated)
