import json
f = open('test.json',)
  
# returns JSON object as
# a dictionary
data = json.load(f)
#print(data['segments'][1]['words'][1]['text']) 

for segments in data['segments']:
    #print(segments['words'])
        for words in segments['words']:
            print(words['text'])



  
# Closing file
f.close()