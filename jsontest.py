import json

  
# Opening JSON file
f = open('test.json',)
  
# returns JSON object as
# a dictionary
data = json.load(f)

print(data['segments'])
for row in data['segments'][0]['words']
    print(row['words'][0])
    #print(data['segments'][1]['words'][1]['text']) 
    #row = 0
    #rows = len(data['segments'])
    #print()
# Iterating through the json
# list
    ##row_string = row['speaker']
    ##row_string += "\t"
    ##row_string += str(row['words'][0]['start'])
    ##row_string += "\t"
    ##row_string += "white \t"

    ##for i in row['words']:
     ##   row_string += i['text']
     ##   row_string += " "
    
    ##print(row_string)
  
# Closing file
f.close()