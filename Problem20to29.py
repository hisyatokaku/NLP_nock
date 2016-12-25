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

