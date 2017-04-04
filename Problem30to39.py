#coding: utf-8
import MeCab
import os
import codecs
import matplotlib.pyplot as plt
import numpy as np

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
                if '名詞' in j['pos'] and 'サ変接続' in j['pos']:
                    print j['base']

def solve_34():
    mapped = solve_30()
    for i in mapped:
        if len(i) != 0:
            for one,two,thr in zip(i,i[1:],i[2:]):
                if ('名詞' in one['pos']) and ('名詞' in thr['pos']) and (two['base'] == 'の'):
                    print one['base'],two['base'],thr['base']

def solve_35():
    mapped = solve_30()
    maxlen = 0
    tmp , ans = [],{}
    for i in mapped:
        if len(i) != 0:
            for word in i:
                if '名詞' in word['pos']:
                    tmp.append(word['base'])
                else:
                    if len(tmp) > maxlen:
                        maxlen = len(tmp)
                        ans[str(len(tmp))] = ' '.join(tmp)
                    tmp = []
    print ans[str(max(map(int,sorted(ans,key = lambda x:x[0]))))]


def solve_36():

def solve_36(isprint=False):
    from collections import Counter
    mapped = solve_30()
    wlist = []
    for i in mapped:
        for word in i:
            wlist.append(word['base'])
    ans = Counter(wlist).items()
    ans = (sorted(ans, key=lambda x: x[1], reverse=True))
    word,num = zip(*ans)
    if isprint:
        for w,n in zip(word,num):
            print w,n
    return word,num

def solve_37():

    from collections import Counter
    mapped = solve_30()
    wlist = []
    for i in mapped:
        for word in i:
            wlist.append(word['base'])
    ans = Counter(wlist)
    word,num = zip(*ans.most_common(10))
    print word
    x = np.arange(10)
    plt.bar(x,list(num),align='center')
    plt.xticks(x,[unicode(k,'utf-8') for k in word])

    #plt.savefig('./36.png')

solve_36()

    plt.show()
    #plt.savefig('./36.png')

def solve_38():
    word , num = solve_36(isprint=False)
    plt.hist(num)
    plt.xlabel('Frequency')
    plt.ylabel('Counts')
    plt.show()

def solve_39():
    word, num = solve_36(isprint=False)
    x = range(1,len(num)+1)
    y = num
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel('log(Grade)')
    plt.ylabel('log(Frequency)')

    plt.plot(x,y)
    plt.grid(which="both")
    plt.show()




