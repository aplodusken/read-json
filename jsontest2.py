import json
f = open('test.json',)
  
# returns JSON object as
# a dictionary
data = json.load(f)

for speakers in data['speakers']:
    print(speakers['name'])
    print(speakers['spkid'])
allSpeakers = {
    "name": 
}

for segments in data['segments']:
    #print(segments['words'])
        for words in segments['words']:
            print(words['text'])



  
# Closing file
f.close()