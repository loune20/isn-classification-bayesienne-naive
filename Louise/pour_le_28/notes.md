# Notes

## A la main
- [ ] Dépouiller set original
- [ ] Convertir en CSV
- [ ] Garder 500 lignes positives et 500 négatives

## En Python
 - [ ] Extraire et transformer en liste
 - [ ] Données de type `data_original = [("com", True),("com2", False)]`


# Code


```python
import csv #importing csv python library
reader = csv.DictReader(open('data2.csv')) #opening file
list_data = [] #creating empty list
for row in reader: #for each row in our csv file
    list_data.append((row['review'], row['overall'])) #appending a tuple of the review and the rating extracted from the csv file
print(list_data) #print our final result
    ```
