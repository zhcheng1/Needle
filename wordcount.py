import string
from operator import itemgetter
import os


def wordcount(get_file):
    if os.path.isfile(get_file) is False:
        print "Not a valid file."

    #build table for translating punctuations to spaces
    punct = "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~'"
    space = " " * len(punct)
    trantab = string.maketrans(punct, space)

    #build a new dictionary
    word_count = {}

    #open a file
    with open(get_file, "r") as test_file:
        # remove all punctuation
        for line in test_file:
            line = line.translate(trantab).split()
            # turn all words into lowercase, and add them into a dict
            for word in line:
                word = word.lower()
                if word != '':
                    if word not in word_count.keys():
                        word_count[word] = 1
                    else:
                        word_count[word] += 1

    #sort the word_count dictionary by values
    sorted_word_count = sorted(word_count.items(), key=itemgetter(1), reverse=True)

    #print word:count pairs
    print "Highest frequency word-count pair:", sorted_word_count[0]


if __name__ == '__main__':
    import sys
    wordcount(sys.argv[1])