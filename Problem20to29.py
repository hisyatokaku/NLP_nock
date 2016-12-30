#coding:utf-8
import re
import json

def solve_20():
    with open('jawiki-country.json','r') as f:
        articles = f.readlines()
        for sub_article in articles:
            tmp = json.loads(sub_article)
            if u'イギリス' in tmp['title']:
                #print tmp['text']
                return tmp['text']

def solve_21():
    target = solve_20().split("\n")
    cate = re.compile('Category')
    for line in target:
        res = cate.search(line)
        if res is not None:
            print line

def solve_22():
    target = solve_20().split("\n")
    category = re.compile('[\[]{1,}(Category:)(.*)')
    #category = re.compile('(Category:)(.*)')
    for line in target:
        res = category.search(line)
        if res is not None:
            print res.group()

def solve_23():
    target = solve_20().split("\n")
    eq = re.compile('=')
    seq = re.compile('==')
    for line in target:
        res = eq.findall(line)
        if len(res) > 1 and seq.search(line) is not None:
            print line,"レベル:{}".format(len(res)/2 - 1)

def solve_24():
    target = solve_20().split("\n")
    fi = re.compile(u'(ファイル:|File:)(.*?)\|')
    for line in target:
        res = fi.search(line)
        if res is not None:
            print res.group(1),res.group(2)
