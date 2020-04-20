# IMPORTING LIBRARIES
import csv  # Importing csv python library
from random import randint  # Importing randint function from random library
from time import sleep  # Importing sleep function from time library

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
def preProcessing(data_original):
    '''
    Put in lowercase and remove stop-words and punctuation from text comments.
    data_original: [("Comment", rating_boolean), ("Comment2", rating_boolean)]
    return data_treated: [["comment", rating_boolean], ["comment2", rating_boolean]]
    '''

    data_treated = []  # List of the processed text of each comment and the associated rate

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


def frequencyOfWords(data_treated):
    '''
    Calculate the frequency of each word in all comments.
    data_treated: [["comment", rating_boolean], ["comment2", rating_boolean]]
    return word_frequency: {"word": frequency, "word2": frequency}
    '''

    word_frequency = {}  # List with the frequency of each word in all comments
    number_of_comments_with_word = {}  # Dictionary with the word and the number of comments containing the word
    number_of_comments = len(data_treated)

    for word in significant_words.copy():  # For each significant word
        number_of_comments_with_word[word] = 0  # Create a dictionary with all the words as keys and 0 as value
        for comment in data_treated:
            if word in comment[0]:  # Count how many comments contain the word
                number_of_comments_with_word[word] += 1
        word_frequency[word] = number_of_comments_with_word[word]/number_of_comments  # Calculating frequency of comments containing the word
        if word_frequency[word] <= 0.05:  # Delete the words with a frequency too low
            del word_frequency[word]
            significant_words.remove(word)  # Update the list of significant words

    return (word_frequency)


def calculatePosScore(data_treated, rating):
    '''
    Calculate the positivity or negativity score of each word in comments.
    data_treated: [["comment", rating_boolean], ["comment2", rating_boolean]]
    rating: True or False
    return word_positivity_score: {"word": positivity_score, "word2": positivity_score}
    '''

    text_selected_comment = []  # List with all the (pre-processed) text of each positive/negative comment (depends on rating)
    word_frequency_in_selected = {}  # Dictionary with the word and its frequency in all positive/negative comments
    number_of_comments_with_word = {}  # Dictionary with the word and the number of positive/negative comments containing it
    word_positivity_score = {}  # Dictionnary with the word and its positivity score
    number_of_selected_comments = 0  # Number of positive/negative comments
    number_of_comments = len(data_treated)

    for comment in data_treated:  # For each comment
        if comment[1] == rating:  # If the comment is positive/negative
            text_selected_comment.append(comment[0])  # Filling up text_selected_comment
            number_of_selected_comments += 1
    for word in significant_words:  # For each significant word
        number_of_comments_with_word[word] = 0  # Filling up dictionary with all the words as keys and 0 as value
        for comment in text_selected_comment:  # For each positive/negative comment
            if word in comment:  # Count number of positive/negative comments containing the word
                number_of_comments_with_word[word] += 1
        word_frequency[word] = number_of_comments_with_word[word]/number_of_comments  # Frequency of positive/negative comments containing the word
        word_positivity_score[word] = word_frequency[word] / (number_of_selected_comments / number_of_comments)  # Probability that the comment contains the word knowing it is positive/negative

    return(word_positivity_score)


def newCommentAnalysis(new_comment):
    '''
    Calculate the positivity and negativity of a new comment.
    new_comment: "Comment"
    return comment_positivity: probability_of_positive
    return comment_negativity: probability_of_negative
    '''

    comment_positivity = 1  # Positivity score of the comment, must be 1 before calculations
    comment_negativity = 1  # Negativity score of the comment, must be 1 before calculations
    has_significant_word = False

    new_comment = new_comment.lower()  # Lowercase the comment
    for p in ponctuation:  # Remove all punctuation signs
        new_comment = new_comment.replace(p, '')
    new_comment = new_comment.split()  # Split the words of the comment

    for word in new_comment:  # Calculate the probability that the comment is positive or negative
        if word in significant_words:
            has_significant_word = True
            comment_positivity = comment_positivity * (word_positivity_score[word]/word_frequency[word])
            comment_negativity = comment_negativity * (word_negativity_score[word]/word_frequency[word])

    print("pos: ", comment_positivity, "neg: ", comment_negativity)  # A SUPPRIMER

    if has_significant_word is False:  # If none of the words could be analyzed
        print("Désolé, je ne peux pas analyser ce commentaire car il ne contient aucun mot significatif...")
        sleep(1.5)  # Wait 1,5 seconds
        return(None)
    elif comment_positivity > comment_negativity:  # Results of the analysis
        return(5)
    else:
        return(1)


def writeNewComment():
    quotes = ["""D’après ce qu’a dit Sébastian Thrun, les mathématiques, les sciences informatiques et l'art sont profondément reliés. Ils proviennent tous de l'expression créative.""",
              """Alan Perlis a dit : « Un programme sans boucle et sans structure de données ne vaut pas la peine d'être écrit. » Et c’est pour ça que j’existe !""",
              """Albert Jacquard a dit : « On peut apprendre à un ordinateur à dire "Je t'aime", mais on ne peut pas lui apprendre à aimer. » J’analyse des sentiments mais est-ce que je peux en ressentir ?""",
              """Comme l’a dit Joseph Finder, je ne suis pas un crack en informatique, loin de là, mais il n'y a pas que les mécaniciens qui savent conduire une voiture.""",
              """Edsger Dijkstra a dit : « Demander si un ordinateur peut penser revient à demander si un humain peut voler. »""",
              """Grace Hopper a dit : « Une mesure exacte vaut l'avis d'un millier d'experts. » Heureusement que mes calculs étaient justes !""",
              """Ray Kurzweil a dit : « D'ici 2029, les ordinateurs auront de l'intelligence émotionnelle. » J’ai l’impression qu’on s’en rapproche…""",
              """Comme l’a dit Alan Turing, les tentatives de création de machines pensantes nous seront d'une grande aide pour découvrir comment nous pensons nous-mêmes.""",
              """Victor Cherbuliez a dit : « Les plus admirables machines ne remplacent pas les intelligences. » Est-il possible que je devienne intelligent ?"""]

    text_comment = input("Veuillez écrire un avis (en anglais) correspondant à une note de 1/5 (négatif) ou de 5/5 (positif) sur un jeu vidéo : ")  # Comment to analyze
    print()
    comment_analysis = newCommentAnalysis(text_comment)  # Analyze the comment

    if comment_analysis == 5:  # Print results of analysis
        print("Je pense que ce commentaire a une note de 5/5 (positif) !")
    elif comment_analysis == 1:
        print("Je pense que ce commentaire a une note de 1/5 (négatif) !")
    else:  # If the comment contained no significant words
        return()

    print()
    sleep(1.5)  # Wait 1,5 seconds
    rating = input("Veuillez entrer la véritable note associée à votre avis (1 pour un avis négatif, 5 pour un avis positif) : ")
    while rating != '1' and rating != '5':  # Error when answering
        rating = input("Votre réponse ne peut pas être prise en compte. Veuillez s'il vous plait entrer une note de 1 ou de 5 : ")

    print()
    if int(rating) != comment_analysis:  # Analysis error
        print("Oh non mon analyse était fausse, j'espère mieux réussir la prochaine fois !")
    else:  # Correct analysis
        print("Super, j'ai eu juste !")
        print(quotes[randint(0, len(quotes)-1)])  # Print random quote from quotes list
    sleep(2)  # Wait 2 seconds

    return()

# MAIN


# User Interaction
program_end = False

print("Que voulez-vous faire ?")
print("Entrer 1 pour calculer la base de données (attention cela va durer plusieurs minutes !)")
print("Entrer 2 pour analyser un commentaire en se basant sur les données déjà calculées")
answer = input()

while answer != '1' and answer != '2':  # Error when answering
    answer = input("Votre réponse ne peut pas être prise en compte. Veuillez s'il vous plait entrer une réponse présente parmi les propositions : ")

print()
if answer == '1':  # Calculate the dataset
    
    # Extracting data from dataset
    reader = csv.DictReader(open('data_videogames(400 lignes).csv'), delimiter=';')  # Opening file
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
            print("Erreur : un des commentaires de la base de données a une note qui n'est ni 1 ni 5")

    # Text data pre-processing
    data_treated = preProcessing(data_original)

    # Creating a list of all the significant words processed
    significant_words = []
    for comment in data_treated:  # Filling up the list with all the words (after pre-processing, in all comments)
        significant_words = significant_words + comment[0].split()
    significant_words = list(dict.fromkeys(significant_words)) # Delete duplicate words
    # Words analysis
    word_frequency = frequencyOfWords(data_treated)  # Calculate the frequency of each word in all comments of data_treated
    word_positivity_score = calculatePosScore(data_treated, True)  # Calculate the frequency of each word in all positive comments of data_treated
    word_negativity_score = calculatePosScore(data_treated, False)  # Calculate the frequency of each word in all negative comments of data_treated
    
    #Entre un commentaire ici !!
    with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(["word", "frequency", "positivity_score", "negativity_score"])
    for word in significant_words:
        writer.writerow([word, word_frequency[word], word_positivity_score[word], word_negativity_score[word]])
    
    
    print("Entrer 1 pour analyser un commentaire")
    print("Entrer X pour quitter")
    answer = input()

    while answer != '1' and answer != 'X' and answer != 'x':  # Error when answering
        answer = input("Votre réponse ne peut pas être prise en compte. Veuillez s'il vous plait entrer une réponse présente parmi les propositions : ")
    
    print()
    if answer == '1':  # Analyze a new comment written by the user
        analyze_new_comment = writeNewComment()
    else:  # End of program
        program_end = True

else:  # Analyze a new comment written by the user
    word_frequency={}
    word_positivity_score={}
    word_negativity_score={}

    reader = csv.DictReader(open('output.csv'), delimiter=';')  # Opening file

    for row in reader:  # Filling up the dictionaries from the csv file with the words as keys
        word_frequency[row['word']] = row['frequency']  # Word frequency as value (from the column 'frequency')
        word_positivity_score[row['word']] = row['positivity_score']  # Word positivity score as value (from the column 'positivity_score')
        word_negativity_score[row['word']] = row['negativity_score']  # Word negativity score as value (from the column 'negativity_score')

    analyze_new_comment = writeNewComment()


while program_end is False:  # To analyze other comments
    print()
    print("Souhaitez-vous analyser un autre commentaire ou quitter ?")
    print("Entrer 1 pour écrire un nouveau commentaire à analyser")
    print("Entrer X pour quitter")
    answer = input()

    while answer != '1' and answer != 'X' and answer != 'x':  # Error when answering
        answer = input("Votre réponse ne peut pas être prise en compte. Veuillez s'il vous plait entrer une réponse présente parmi les propositions : ")
    
    print()
    if answer == '1':  # Analyze a new comment written by the user
        analyze_new_comment = writeNewComment()
    else:  # End of program
        program_end = True

