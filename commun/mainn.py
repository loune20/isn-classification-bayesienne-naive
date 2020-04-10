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
    data_treated = []  # List of the processed text of each com and the associated rate
    
    for comment in data_original:
        text_comment = comment[0].lower()  # Lowercase all comments and add in text_comment 
        for p in ponctuation:  # Remove all punctuation signs
            text_comment = text_comment.replace(p, '')
        text_comment = text_comment.split()  # Split list to individually find stop-words
        for word in text_comment.copy():  # For each word of the comment
            if word in common:  # Remove all stop-words
                text_comment.remove(word)
        text_comment = ' '.join(text_comment)  # Reform a "comment" with all significant word of a comment and spaces between them
        data_treated.append([text_comment, comment[1]])  # Add to data_treated a list with the preprocessed comment and its rate
        
    return(data_treated)


def frequencyOfWords(data_treated):  # Function that calculates the frequency of each word in all comments
    word_frequency = {}  # List with the frequency of each word in all comments
    number_of_comments_with_word = {}  # Dictionary with the word and the number of comments containing the word
    number_of_comments = len(data_treated)

    for word in significant_words.copy():  # For each significant word
        number_of_comments_with_word[word] = 0  # Create a dictionary with all the words as keys and 0 as value
        for comment in data_treated:
            if word in comment[0]:  # Count how many comments contain the word
                number_of_comments_with_word[word] += 1
        word_frequency[word] = number_of_comments_with_word[word]/number_of_comments  # Calculating frequency of comments containing the word
        if word_frequency[word] <= 0.08:  # Delete the words with a frequency too low
            del word_frequency[word]
            significant_words.remove(word)  # Update the list of significant words

    return (word_frequency)


def calculatePosScore(data_treated):  # Function that calculates the positivity score of each word in comments
    text_positive_comment = []  # List with all the (pre-processed) text of each positive com
    word_frequency_in_positive = {} # List with the frequency of each word in all positive comments
    number_of_comments_with_word = {}  # Dictionary with the word and the number of positive comments containing it
    word_positivity_score = {} # Dictionnary with the word and its positivity score
    number_of_positive_comments = 0
    number_of_comments = len(data_treated)

    for comment in data_treated: # For each comment
        if comment[1]:  # If the comment is positive
            text_positive_comment.append(comment[0])  # Filling up text_positive_comment
            number_of_positive_comments += 1
    for word in significant_words:  # For each significant word
        number_of_comments_with_word[word] = 0  # Filling up dictionary with all the words as keys and 0 as value
        for positive_comment in text_positive_comment:  # For each positive comment
            if word in positive_comment:  # Count number of positive comments containing the word
                number_of_comments_with_word[word] += 1
        word_frequency_in_positive[word] = number_of_comments_with_word[word]/number_of_comments  # Frequency of positive comments containing the word
        word_positivity_score[word] = word_frequency_in_positive[word] / (number_of_positive_comments / number_of_comments)  # Filling up word_positivity_score with the probability that the comment contains the word knowing it is positive

    return(word_positivity_score)


def newCommentAnalysis(new_comment):  # Calculate positivity of a new comment ; new_comment is ["comment", rating]
    comment_positivity = 1 # Positivity score of the comment, must be 1 before calculations
    has_significant_word = False
    new_comment_text = new_comment[0]
    
    new_comment_text = new_comment_text.lower()  # Lowercase the comment
    for p in ponctuation:  # Remove all punctuation signs
        new_comment_text = new_comment_text.replace(p, '')
    new_comment_text = new_comment_text.split()  # Split the words of the comment
    
    for word in new_comment_text:  # Calculate the probability that the comment is positive
        if word in significant_words:
            has_significant_word = True
            comment_positivity = comment_positivity * (word_positivity_score[word]/word_frequency[word])
    
    if has_significant_word == False:
        print("Sorry, I can't analyse this comment beacause it contains no significant word...")
        return(None)
    else:
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

# Creating a list of all the significant words processed
significant_words = []
for comment in data_treated:  # Filling up the list with all the words (after pre-processing, in all comments)
    significant_words = significant_words + comment[0].split()
for word in significant_words:  # For each word (except stop-words)
    if significant_words.count(word) > 1:  # Delete duplicate words
        significant_words.remove(word)

# Calculate the frequency of each word in all comments of data_treated
word_frequency = frequencyOfWords(data_treated)

# Calculate the frequency of each word in all positive comments of data_treated
word_positivity_score = calculatePosScore(data_treated)

# Analyze a new comment
comment_analysis = newCommentAnalysis([""" This great""",False])

# Printing
if comment_analysis:
    print(comment_analysis)
