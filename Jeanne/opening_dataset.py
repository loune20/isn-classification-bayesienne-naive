import csv #importing csv python library
      
reader = csv.DictReader(open('data2.csv')) #opening file
        
list_data = [] #creating empty list
for row in reader: #for each row in our csv file
    list_data.append((row['summary'], row['overall'])) #adding at the end of the list a tuple of the summary and the rating extracted from the csv file
    
print(list_data) #print our final result