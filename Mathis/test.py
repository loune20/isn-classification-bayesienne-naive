def preProcessing(data_original):    
    my_list = []
    data_treated = []
    for i in range(len(data_original)): #Populate empty list
        my_list.append(None)
        data_treated.append(None)
    for i in range(len(data_original)):
        my_list[i] = data_original[i][0]
    common = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
    index = []
    for i in range(len(my_list)):
        my_list[i] = my_list[i].lower()#put all in lowercase
        my_list[i] = my_list[i].split()
        for j in range(len(my_list[i])):
            for k in range(len(common)):
                if my_list[i][j] == common[k] :#find common
                    index.append(j)
                    index.sort()
                    index.reverse()
        for l in range(len(index)):
            del(my_list[i][index[l]])
        index = []
        my_list[i]=" ".join(my_list[i])
        data_treated[i] = [(my_list[i],data_original[i][1] )]
    return(data_treated)



data_original = [("ourselves are here in between the monkey is great", True), ("once upon a time the wizard was very happy it is a good news", False), ("blabla is a very good friend", True)]
data_treated = preProcessing(data_original)
print(data_original)
print(data_treated)