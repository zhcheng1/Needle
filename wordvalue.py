import string
import os


def wordvalue(file_name):
    try:
        file(file_name).read()
    except IOError:
        print "Not a valid file."
    else:
        #build table for translating punctuations to spaces
        punct = string.punctuation
        space = " " * len(punct)
        trantab = string.maketrans(punct, space)

       #open a file, break into sentences
        f = file(file_name)
        test_file = f.read().split("  ")
        # get rid of the punctuation and uppercase, then sum up the word value
        for sentence in test_file:
            sentences_tran = sentence.translate(trantab)
            sentences_low = sentences_tran.lower()
            sen = "".join(sentences_low.split())
            # loop over each character, find their ASCII value and ignore digits
            sen_sum = sum(ord(c)-96 for c in sen if c.isalpha())
            # slice
            print "%s, %d" % (sentence[:-1], sen_sum)
        f.close()


if __name__ == '__main__':
    import sys
    wordvalue(sys.argv[1])