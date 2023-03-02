#!/usr/bin/env python
import sys, os, re, string
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
    afinn = Afinn(language='en')
   # prez_name = 'hdfs://cluster-9dfa-m/user/yuezhang/speeches/adams.tar.gz'
    prez_name = os.environ['mapreduce_map_input_file']
    prez_name = prez_name.split('/')[-1]
    prez_name = prez_name.split('.')[0]
    try:
        total_score = 0
        word_num = 0
        while line:
            line = round1(line)
            for word in pattern.findall(line):
                score = afinn.score(word)
                total_score = total_score + score
                word_num = word_num + 1
            line = sys.stdin.readline()
        valence = total_score / word_num
        print("DoubleValueSum:" + str(prez_name) + "\t" + str(valence))
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
