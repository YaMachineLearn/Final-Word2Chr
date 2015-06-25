# coding=utf-8

CHMAP_FILE = "timit.chmap"

CH_MAP = dict()

with open(CHMAP_FILE) as mapFile:
    for line in mapFile:
        splitLine = line.split()
        CH_MAP[splitLine[0]] = splitLine[1]

def wordsToChrString(wordsString):
    #input: 'the i is'
    #output: '裚騿寋'
    chrList = list()
    for word in wordsString.split():
        chrList.append(CH_MAP[ word.split('~')[0] ])
    return ''.join(chrList)
