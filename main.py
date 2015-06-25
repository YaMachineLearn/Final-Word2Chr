# coding=utf-8

import chmapUtil as ch

def main():
    UTTER_FILE = "input/utterName.txt"
    WORDS_FILE = "input/test_mfcc_-2_512-4.267.labIdx48.smoothWin3.phoneSeq.possible200.words"
    OUTPUT_FILE = "output/" + WORDS_FILE[6:] + ".chr.csv"
    
    utterFile = open(UTTER_FILE)
    wordsFile = open(WORDS_FILE)
    outFile = open(OUTPUT_FILE, 'w')

    utterLines = utterFile.readlines()
    wordsLines = wordsFile.readlines()

    if len(utterLines) != len(wordsLines):
        print "len(utterLines): ", len(utterLines)
        print "len(wordsLines): ", len(wordsLines)
        print "error: length of utterLines and wordsLines are different"
        quit()

    outFile.write('id,sequence\n')
    for i in xrange(len(utterLines)):
        outFile.write(utterLines[i].rstrip() + ',')
        outFile.write(ch.wordsToChrString(wordsLines[i]) + '\n')

    utterFile.close()
    wordsFile.close()
    outFile.close()

if __name__ == '__main__':
    main()