my_list = [' A an elephant of the Biggest World','a','AZfydyTeZA']
common = [' a ',' an ',' the ',' of ',' I ',' you ']

for i in range(len(my_list)):
    my_list[i] = my_list[i].lower()#put all in lowercase
    for j in range(len(common)):
        if common[j] in (my_list[i]):#find common word
            my_list[i] = my_list[i].replace(common[j], ' ')#and delete it
print(my_list)