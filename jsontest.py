import json
# returns JSON object as
# a dictionary
f = open('test.json',)
data = json.load(f)

#for speakers in data['speakers']:
#    print(speakers['name'])
#    print(speakers['spkid'])

#print(data['speakers']['name'])

allSpeakers = dict(zip(data['speakers'][1]['name'],data['speakers'][1]['spkid']))

print(allSpeakers)


#for segments in data['segments']:
#    #print(segments['words'])
#        for words in segments['words']:
#            print(words['text'])



  
# Closing file
f.close()