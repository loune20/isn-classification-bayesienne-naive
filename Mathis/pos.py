def frequencyOfWordsInPos (data_set): #function that calculates the frequency of each word in all comments
    comments_list_of_pos = [] #list with the (pre-processed) text of each com positive
    comments_pos =0
    freq_word_in_pos = {}
    word_counter = {} #dictionary with the word and the number of comments positive containing the word
    
    for i in range(len(data_set)):
        if data_set[i][1] == True :
            comments_list_of_pos.append(data_set[i][0])
            comments_pos += 1
    for word in words_list:
        word_counter[word] = 0 #create a dictionary with all the words as keys, and 0 as value
        for i in range (comments_pos):
            if word in comments_list_of_pos[i]: #count number of comments positive containing the word
                word_counter[word] += 1 
        freq_word_in_pos[word] = word_counter[word]/len(data_set) #frequency of comments positive containing the word
        
    return (freq_word_in_pos)