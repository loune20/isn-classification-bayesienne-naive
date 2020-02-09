data_treated = [['word1',False], ['word2', True], ['word2', True], ['word3', True]]

words_list = []   
for i in range (len(data_treated)) :
    words_list = words_list + data_treated[i][0].split() #list of all words (after pre-processing, in all comments)