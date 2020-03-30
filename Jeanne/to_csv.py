with open('commentaires.csv', 'w') as csvfile:
    fieldnames = ['notes', 'pos com']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for comment in data_original:
        comment_analysis = newCommentAnalysis(comment)
        if comment[1]:
            note=5
        else:
            note=1
        writer.writerow({"notes": note, "pos com": comment_analysis})