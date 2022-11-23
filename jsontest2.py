import json

# declare constants
SENTENCELEN = 250
FPS = 25

f = open('test.json',)
  
# returns JSON object as
# a dictionary
data = json.load(f)

# declare the dictionare allSpeakers with names and speakers
allSpeakers = {}

# populate dictionary allSpekaers with all the speakers in the transcription
for speakers in data['speakers']:
    allSpeakers[speakers['name']] = speakers['spkid']



for segments in data['segments']:
    #print(segments['words'])
        for words in segments['words']:
            print(words['text'])



  
# Closing file
f.close()