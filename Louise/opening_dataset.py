import csv #importing csv python library
      
reader = csv.DictReader(open('data2.csv')) #opening file
        
list_data = [] #creating empty list
for row in reader: #for each row in our csv file
    list_data.append((row['review'], row['overall'])) #adding at the end of the list a tuple of the summary and the rating extracted from the csv file
    
print(list_data) #print our final result

for i in range len(list_data):
    if list_data[1] == 1:
        list_data[1] == False
    elif list_data[1] == 5:
        list_data[1] == True
    else:
        print("Error : one of the comment has an overall that's neither 1 or 5")

