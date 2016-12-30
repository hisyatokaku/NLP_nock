#coding:utf-8
FILE = 'nlp.txt'
import re

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


