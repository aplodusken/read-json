# v0.2
import json
import tc
from pathlib import Path

f = open('test.json',)
# print(tc.framestotc(100, 25))
# returns JSON object as
# a dictionary
data = json.load(f)
# Closing file
f.close()

# declare constants
# varaiable for future feature to add sentence length limitation 
SENTENCELEN = 250
# get the offset from the json file
tcoffset = data['startTimeOffset']
# Variable to store name of destinationfile
orgdestfilename = Path(str("/home/micke/git/read-json/" + data['filename']))
destfilename = orgdestfilename.with_suffix('.txt')
# Variable to store FPS value
FPS = 25
# Variable to store what track to add the markers
TRACK = 'V1'
# Variable to store what colors we're adding to the markers
MARKER = 'White'

# test print
#print(destfilename)

f = open(destfilename, "a")
# declare the dictionare allSpeakers with names and speakers
allSpeakers = {}
senlen = 0
row = ''

# populate dictionary allSpekaers with all the speakers in the transcription
for speakers in data['speakers']:
    allSpeakers[speakers['spkid']] = speakers['name']

for segments in data['segments']:
    row = allSpeakers[segments['speaker']] + "\t" + str(tc.framestotc(int(segments['words'][0]['start']+tcoffset) * 25, FPS)) + "\t" + TRACK + "\t" + MARKER + "\t"
    
    for words in segments['words']:
       
        row = row + " " + words['text']
       
    print(row + "\n")
    f.write(row  + "\n")


f.close()

  
