#coding:utf-8
FILE = 'nlp.txt'
import re
from stemming.porter2 import stem
from pycorenlp import StanfordCoreNLP

#カッコをつけることで\1などで参照できる

def solve_50():
    lines = open(FILE,'r').readlines()
    ans = []
    for line in lines:
        line = re.sub(r'([\.\;\:\?\!])\s([A-Z])',r'\1\n\2',line)
        #print line,
        if line!= '\n':
            ans.append(line)
    return ans

def solve_51():
    txt_list = solve_50()
    txt = ''.join(txt_list)
    txt = txt.replace(' ','\n')
    txt = txt.replace('.','.\n')
    return txt

def solve_52():
    txt = solve_51()
    txt_list = txt.split("\n")
    for word in txt_list:
        print word,"    ",stem(re.sub("[\.\,\:\;\!]","",str(word)))

def solve_53():
    #cmd = 'java -mx4g -cp "*" ./stanford-corenlp-full-2016-10-31/edu.stanford.nlp.pipeline.StanfordCoreNLPServer'
    #execute cmd before running.
    nlp = StanfordCoreNLP('http://localhost:9000')
    lines = solve_50()

    for text in lines:
        output = nlp.annotate(text,properties={'annotators': 'tokenize,ssplit,pos,depparse,parse',
                                           'outputFormat':'json'})
        print output['sentences'][0]['parse']
    # nlp.annotateがjson以外は出せないっぽいのでxmlじゃなくてjsonで対応する

def solve_54():
    nlp = StanfordCoreNLP('http://localhost:9000')
    lines = solve_50()
    for text in lines:

        output = nlp.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,lemma,parse',
                                            'outputFormat': 'json'})

        # output['sentences'][0] -> tokens, index, enhancedDependencies, basicDependencies, parse, enhancedPlusPlusDependencies
        # output['sentences'][0]['tokens'] ->
        # format is "dict", each.
        # annotator ref: http://qiita.com/yubessy/items/0a4a59550cfddb79cdb5

        words = output['sentences'][0]['tokens']

        print '単語','lemma','品詞'
        for word in words:
            print word['word'],'    ',word['lemma'],'    ',word['pos']

def solve_55():
    nlp = StanfordCoreNLP('http://localhost:9000')
    lines = solve_50()
    for text in lines:
        output = nlp.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,lemma,parse,ner',
                                            'outputFormat': 'json'})

        for i in output['sentences'][0]['tokens']:
            if i['ner'] != 'O':
                print i['word']

def solve_56():
    nlp = StanfordCoreNLP('http://localhost:9000')
    lines = solve_50()
    for text in lines[0:2]:
        output = nlp.annotate(text,properties={'annotators':'tokenize,ssplit,pos,lemma,parse',
                                               'outputFormat':'json'
                                               })

        print output

solve_56()