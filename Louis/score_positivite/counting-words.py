data_treated = [['word1',False], ['word2', True], ['word2', True], ['word3', True], ['word2', True]]

words_list = []   
for i in range (len(data_treated)):
    words_list = words_list + data_treated[i][0].split() #list of all words (after pre-processing, in all comments)
for word in words_list:
    if words_list.count(word) > 1:
        words_list.remove(word)
