# v0.5
import json
# import tc
from pathlib import Path
import sys
import codecs


def framestotc(someframes, fps):

    s, f = divmod(int(someframes), fps)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return '{1:02d}:{2:02d}:{3:02d}:{4:02d}'.format(d, h,m,s,f)

# open the input file and name it f
f = open(sys.argv[1],)

# returns JSON object as a dictionary and store it in the data variable
data = json.load(f)
print(data)
# Closing file f
f.close()

# get the offset from the json file
tcoffset = data['startTimeOffset']

# Variable to store name of destination file
orgdestfilename = Path(str(data['filename']))
destfilename = orgdestfilename.with_suffix('.txt')
# Variable to store FPS value
FPS = 25
# Variable to store what track to add the markers
TRACK = 'V1'
# Variable to store what colors we're adding to the markers
MARKER = 'White'

# open a new file for storing the result text encoding mac-roman
f = codecs.open(destfilename, "a", "mac-roman")
# declare the dictionare allSpeakers with names and speakers
allSpeakers = {}
# senlen = 0
row = ''

# populate dictionary allSpekaers with all the speakers in the transcription
for speakers in data['speakers']:
    allSpeakers[speakers['spkid']] = speakers['name']

# print(allSpeakers)

# iterat over json data
for segments in data['segments']:
    # set the formatting of the start row of data the avid markers file
    row = allSpeakers[segments['speaker']] + "\t" + str(framestotc(float(segments['words'][0]['start']+tcoffset) * 25, FPS)) + "\t" + TRACK + "\t" + MARKER + "\t" + "(" + allSpeakers[segments['speaker']] + ") "
    # Add sentence word by word from json data
    for words in segments['words']:
        

        row = row + " " + words['text']

    # write row of data to file
    f.write(row  + "\n")

    
# close the file
f.close()

print("KLAR!")