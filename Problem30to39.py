#coding: utf-8
import MeCab
import os
import codecs
from pprint import pprint

FILE = "neko.txt"
parsed = "neko.txt.mecab"

_ = MeCab.Tagger ("-Ochasen")

if not os.path.exists(FILE+".mecab"):
    #lines = " ".join(list(open(FILE,'r').readlines()))
    lines = list(open(FILE,'r').readlines())
    with open(FILE + ".mecab", 'a+') as f:
        for line in lines:
            f.write(_.parse(line))

def solve_30(output=False):
    lines = list(open(parsed,'r').readlines())
    sentences , single = [],[]
    for line in lines:
        if line == "EOS\n":
            if len(single) != 0:
                sentences.append(single)
            single = []
            continue
        if len(line) == 0:
            continue
        node = line.split('\t')
        #node:[表層、カナ、原型、品詞、品詞1]
        #print node[0].decode('string-escape')
        dic_ = {
        "surface":str(node[0]).decode('string-escape'),
        "base":str(node[2]).decode('string-escape'),
        "pos":node[3],
        "pos1":node[4]
        }
        single.append(dic_)

    if output:
        with codecs.open('mecab_map.txt','w','sjis') as f:
            for sentence in sentences:
                if len(sentence) == 0:
                    continue
                f.write((str(sentence).replace(",",",\n")+"\n"))
    return sentences

def solve_31():
    mapped = solve_30()
    for i in mapped:
        if len(i) != 0:
            for j in i:
                if '動詞-' in j['pos']:
                    print j['surface']

def solve_32():
    mapped = solve_30()
    for i in mapped:
        if len(i) != 0:
            for j in i:
                if '動詞-' in j['pos']:
                    print j['base']

def solve_33():
    mapped = solve_30()
    for i in mapped:
        if len(i) != 0:
            for j in i:
                if '名詞' in j['pos']:
                    print j['base'],j['pos1']

solve_33()

