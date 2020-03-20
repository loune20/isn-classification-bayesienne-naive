# IMPORTING LIBRARIES
import csv  # Importing csv python library

# GLOBAL VARIABLES
ponctuation = ['.', ',', ';', ':', '!', '?', '/', '*', '-', '+', '&', '"',
               '(', ')', '[', ']', '{', '}', '_', '°', '=', '# ', "'"]
common = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during',
          'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
          'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from',
          'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
          'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while',
          'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them',
          'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what',
          'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just',
          'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if',
          'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than', 'also', 'might']  # Stop-words the algorithm won't analyse


# FUNCTIONS
def preProcessing(data_original):  # Function that puts in lowercase and removes stop-words and punctuation from a list 
    text_com = []  # List with all the text of each com (without their rates)
    data_treated = []  # List of the processed text of each com and the associated rate
    index = []  # List of indexes of words to remove

    for i in range(len(data_original)):  # For each comment
        data_treated.append(None)  # Populate empty list
        text_com.append(data_original[i][0])  # Fill text_com with only the text of each comment
        text_com[i] = text_com[i].lower()  # Lowercase everything
        for j in range(len(ponctuation)):  # For each punctuation sign
            text_com[i] = text_com[i].replace(ponctuation[j], '')  # Remove punctuation
        text_com[i] = text_com[i].split()  # Split list to individually find stop-words
        for j in range(len(text_com[i])):  # For each word (in each comments)
            for k in range(len(common)):  # For each stop-word
                if text_com[i][j] == common[k]:  # Find stop-words
                    index.append(j)
                    index.sort()
                    index.reverse()  # Words will be removed from last to first, putting them back in order (so that the list index isn't modifed and all words are analysed)
        for l in range(len(index)):  #  For each index of stop-words to remove
            del(text_com[i][index[l]])  # Remove it
        index = []
        text_com[i] = " ".join(text_com[i])  # Reform a "comment" with all significant word of a comment and spaces between them
        data_treated[i] = [text_com[i], data_original[i][1]]  # Create the output list with the preprocessed comment and its rate
    
    return(data_treated)


def frequencyOfWords(data_set):  # Function that calculates the frequency of each word in all comments
    text_com = []  # List with all the (pre-processed) text of each com (without their rates) 
    freq_words = {}  # List with the frequency of each word in all comments
    word_counter = {}  # Dictionary with the word and the number of comments containing the word
    words_to_delete = []  # Intermediary list used to update words_list (global list)

    for i in range(len(data_set)):  # For each comment
        text_com.append(data_set[i][0])  # Filling up text_com

    for word in words_list:  # For all significant word
        word_counter[word] = 0  # Create a dictionary with all the words as keys, and 0 as value
        for i in range(len(data_set)):  # For each comment
            if word in text_com[i]:  # Count how many comments contain the word
                word_counter[word] += 1
        freq_words[word] = word_counter[word]/len(data_set)  # Calculating frequency of comments containing the word
        if freq_words[word] <= 0.08: # If the frequency of a word <= 0.08
            del freq_words[word]  # Delete the word in freq_word
            words_to_delete.append(word)
    
    for word in words_to_delete:
        words_list.remove(word)  # Update the list of significant words
    
    return (freq_words)


def calculatePosScore(data_set):  # Function that calculates the positivity score of each word in comments
    text_com_pos = []  # List with all the (pre-processed) text of each positive com
    freq_word_in_pos = {} # List with the frequency of each word in all positive comments
    word_counter = {}  # Dictionary with the word and the number of positive comments containing the word
    pos_score = {} # Dictionnary with a word and its positivity score
    number_of_pos_com = 0  # Number of positive comments 

    for i in range(len(data_set)): # For each comment
        if data_set[i][1]:  # If the comment is positive
            text_com_pos.append(data_set[i][0])  # Filling up text_com_pos
            number_of_pos_com += 1  # Incrementing number_of_pos_com
    for word in words_list:  # For each significant word
        word_counter[word] = 0  # Filling up dictionary with all the words as keys, and 0 as value
        for i in range(number_of_pos_com):  # For each positive comment
            if word in text_com_pos[i]:  # Count number of positive comments containing the word
                word_counter[word] += 1
        freq_word_in_pos[word] = word_counter[word]/len(data_set)  # Frequency of positive comments containing the word
        pos_score[word] = freq_word_in_pos[word] / (number_of_pos_com / len(data_set))  # Filling up pos_score with the probability that the comment contains the word knowing it is positive

    return(pos_score)


def newCommentAnalysis(new_com):  # Calculate positivity of a new comment ; new_com is ["comment", rating]
    analyzed_words = []  # List of analyzed words which are in the comment
    comment_positivity = 1 # Positivity score of the comment, must be 1 before calculations 
    
    new_com[0] = new_com[0].lower()  # Lowercase the comment
    for i in range(len(ponctuation)):
        new_com[0] = new_com[0].replace(ponctuation[i], '')  # Remove punctuation
    new_com[0] = new_com[0].split()  # Split the words of the comment
    
    for i in range (len(new_com[0])):  # For each word in the comment
        if new_com[0][i] in words_list:  # If the word is significant
            analyzed_words.append(new_com[0][i])  # Add it to the list analyzed_words
    
    for i in range (len(analyzed_words)):  # For each significant word in the comment
        comment_positivity = comment_positivity * (pos_score[analyzed_words[i]]/freq_words[analyzed_words[i]])  # Calculate the probability that the comment is positive
    
    return(comment_positivity)

# MAIN

# Extracting data from dataset
reader = csv.DictReader(open('data_videogames.csv'))  # Opening file
data_original = []  # Creating empty list
for row in reader:  # For each row in our csv file
    data_original.append([row['reviewText'], row['overall']])  # Filling up the list with a tuple of the summary and the rating extracted from the csv file

# Changing 1 and 5 to False and True
for i in range(len(data_original)):
    if data_original[i][1] == "1":
        data_original[i][1] = False
    elif data_original[i][1] == "5":
        data_original[i][1] = True
    else:  # Managing data error
        print("Error : one of the comment has an overall that's neither 1 or 5")

# Text data pre-processing
data_treated = preProcessing(data_original)

# Creating a list of all the processed words
words_list = []
for i in range(len(data_treated)):  # For each comment
    words_list = words_list + data_treated[i][0].split()  # Filling up the list with all words (after pre-processing, in all comments)
for word in words_list:  # For each word (except stop-words)
    if words_list.count(word) > 1:
        words_list.remove(word)  # Delete duplicate words

# Calculate the frequency of each word in all comments of data_treated
freq_words = frequencyOfWords(data_treated)

# Calculate the frequency of each word in all positive comments of data_treated
pos_score = calculatePosScore(data_treated)

# Analyze a new comment
comment_analysis = newCommentAnalysis(['This game was a It has less , less worth rip-off bad bad bad bad , and less  than  2.  The graphics are about the same.  Not',False])

# Printing
print(comment_analysis)