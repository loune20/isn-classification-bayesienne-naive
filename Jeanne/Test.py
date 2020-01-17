import csv
reader = csv.DictReader(open('Dataset_30reviews.csv'))
for row in reader:
    print(row['reviews.rating'], row['reviews.text'])