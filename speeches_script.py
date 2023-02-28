#!/usr/bin/env python
import sys, os, re
from afinn import Afinn

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return text
round1 = lambda x: clean_text(x).strip()


def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    af = Afinn()
    speech = os.getenv('prez_speeches')
    try:
        total = 0
        wordcount = 0
        while line:
            line = round1(line)
            for word in pattern.findall(line):
                total += afn.score(word)
                wordcount += 1
    #         print ("LongValueSum:" + word.lower() + "t”+"1")
            line = sys.stdin.readline()
        print("DoubleValueSum:" + str(speech) + "t"+ str(total/wordcount))
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
