import json

  
# Opening JSON file
f = open('test.json',)
  
# returns JSON object as
# a dictionary
data = json.load(f)
#print(data['segments'][1]['words'][1]['text']) 
row = 0
rows = len(data['segments'])
rower = data['segments']
for words in rower:
    print(words['text'])
# Iterating through the json
# list
row_string = data['segments'][row]['speaker']
row_string += "\t"
row_string += str(data['segments'][row]['words'][0]['start'])
row_string += "\t"
row_string += "white \t"

for i in data['segments'][1]['words']:
    row_string += i['text']
    row_string += " "
    
print(row_string)
  
# Closing file
f.close()