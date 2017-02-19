#coding:utf-8
import random

def solve_0(string = "stressed"):
    print string[::-1]

def solve_1(string = u"パタトクカシーー"):
    print string[::2]

def solve_2(str1 = u"パトカー", str2 = u"タクシー"):
    print ''.join([a+b for a,b in zip(str1,str2)])

def solve_3(string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."):
    string = string.replace(',','')
    string = string.replace('.','')
    string = string.split()
    print [len(i) for i in string]

def solve_4(string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."):
    string = string.replace('.','')
    string = string.replace(',','')
    string = string.split()
    TARGET = [0,4,5,6,7,8,14,17,18]
    dict = {}
    for (i,word) in enumerate(string):
        if i not in TARGET:
            dict[word[:2]] = i
        else:
            dict[word[:1]] = i
    #for k,v in sorted(dict.iteritems(),key=lambda x:x[1]):
    #    print k,v

def solve_5(string = "I am an NLPer", n = 2 ):
    if isinstance(string,str):
        string = string.replace('.', '')
        string = string.replace(',', '')
        string = string.split()
    if isinstance(string,list):
        pass
    print [string[i:i+n] for i in range(len(string)) if len(string)-i >= n]


def solve_6(str1 = 'paraparaparadise', str2 = 'paragraph',n=2):
    bigram1 = [str1[i:i+n] for i in range(len(str1)) if len(str1)-i >= n]
    bigram2 = [str2[i:i+n] for i in range(len(str2)) if len(str2)-i >= n]

    print "和集合:",list(set(bigram1).union(bigram2))
    print "積集合:",list(set(bigram1).intersection(bigram2))
    print "差集合:",list(set(bigram1).difference(bigram2))

def solve_7(x=12,y='気温',z='22.4'):
    print "{}時の{}は{}".format(x,y,z)

def cipher(string):
    res = ''
    for char in string:
        if char.islower():
            code = chr(219-ord(char))
        else:
            code = char
        res+=code
    return res

def solve_8(string='Mypassword'):
    print cipher(string)
    print cipher(cipher(string))

def shuffle_char(string):
    if len(string) <= 4:
        return string
    else:
        _ = list(string[1:])
        random.shuffle(_)
        return string[0]+''.join(_)

def solve_9(string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."):
    string = string.split()
    for word in string:
        print shuffle_char(word),

