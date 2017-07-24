#coding: utf-8
import random
from nltk.corpus import stopwords
Stopwords = stopwords.words('english')
from nltk.stem.wordnet import WordNetLemmatizer

def solve_70():
    pos = open('rt-polaritydata/rt-polarity.pos').readlines()
    neg = open('rt-polaritydata/rt-polarity.neg').readlines()

    w = open('sentiment.txt', 'w')

    for i, (p_sent, n_sent) in enumerate(zip(pos, neg)):
        pos[i] = "+1 " + p_sent
        neg[i] = "-1 " + n_sent

    sum = pos + neg
    random.shuffle(sum)
    for i in sum:
        w.write(i)
    w.close()

def solve_71(word):
    return True if word in Stopwords else False

def solve_72():

    class Preprocess():

        def __init__(self, lines):
            self.lmtzr = WordNetLemmatizer()
            self.lines = []
            for line in lines:
                try:
                    line = unicode(line)
                except:
                    pass

                line = line.replace('\n')
                line = line.split(' ')
                self.lines.append(line)

        def __call__(self, lines):
            pass

        def clean_str(self, string):
            pass

        def remove_stopword(self, words):
            for s_word in Stopwords:
                if s_word in words:
                    filter(lambda w: w != s_word, words)
            return words

        def lemmatization(self, lines):
            result = []
            for (j, line) in enumerate(lines):
                    #print "cant decode line:", line
                line = line.replace('\n', '')
                lines[j] = line.split(' ')
                line = lines[j]
                for (i, word) in enumerate(line):
                    try:
                        line[i] = str(self.lmtzr.lemmatize(word))
                        # print 'changed {} to {}'.format(word, line[i])
                    except:
                        line[i] = word
                result.append(' '.join(line))
            return result

    raw_lines = open('sentiment.txt').readlines()

    processor = Preprocess()
    after_lines = processor.lemmatization(raw_lines)



solve_72()
