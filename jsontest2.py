# v0.1
import json
import tc

f = open('test.json',)
# print(tc.framestotc(100, 25))
# returns JSON object as
# a dictionary
data = json.load(f)

# declare constants
SENTENCELEN = 250
tcoffset = data['startTimeOffset']
FPS = 25
TRACK = 'V1'
MARKER = 'White'

print(tcoffset)

# declare the dictionare allSpeakers with names and speakers
allSpeakers = {}
senlen = 0
row = ''
# populate dictionary allSpekaers with all the speakers in the transcription
for speakers in data['speakers']:
    allSpeakers[speakers['spkid']] = speakers['name']

for segments in data['segments']:
    row = allSpeakers[segments['speaker']] + "\t" + str(tc.framestotc(int(segments['words'][0]['start']+tcoffset) * 25, 25)) + "\t" + TRACK + "\t" + MARKER + "\t"
    
    for words in segments['words']:
       
        row = row + " " + words['text']
       
    print(row)


  
# Closing file
f.close()