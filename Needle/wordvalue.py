import string
import os


def wordvalue(file_name):
    if os.path.isfile(file_name) is False:
        print 'not a valid file'
    else:
        #build table for translating punctuations to spaces
        punct = string.punctuation
        space = " " * len(punct)
        trantab = string.maketrans(punct, space)

        sen_value = {}
        #open a file, break into sentences
        f = file(file_name)
        test_file = f.read().split("  ")
        # get rid of the punctuation and uppercase, then sum up the word value, write into a dict
        for sentence in test_file:
            sentences_tran = sentence.translate(trantab)
            sentences_low = sentences_tran.lower()
            sen = "".join(sentences_low.split())
            sen_sum = sum(ord(c)-96 for c in sen)
            sen_value[sentence] = sen_sum
        print sen_value
        f.close()


if __name__ == '__main__':
    import sys
    wordvalue(sys.argv[0])