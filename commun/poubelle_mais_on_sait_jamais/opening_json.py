#import json
#f = open("set2.json", "r")
##print(f.read())
#y = json.loads(f.read())
#print(y["parking"]["price"])

import json
f = open("set.json", "r")
dataset = json.loads(f.read())
print(dataset)