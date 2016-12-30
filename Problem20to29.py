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

def solve_25():
    target = solve_20().split("\n")
    field= re.compile(u'([^\|]*?)\s=\s([^=]*)')
    dict = {}
    for line in target:
        res = field.search(line)
        if res != None:
            dict[res.group(1)] = res.group(2)
    for k,v in dict.iteritems():
        print k,v


def solve_26():
    target = solve_20().split("\n")
    field = re.compile(u'([^\|]*?)\s=\s([^=]*)')
    dict = {}
    for line in target:
        res = field.search(line)
        if res != None:
            dict[res.group(1)] = re.sub("'{3}","",res.group(2))
    for k, v in dict.iteritems():
        print k, v

def solve_27():
    target = solve_20().split("\n")
    field = re.compile(u'([^\|]*?)\s=\s([^=]*)')
    dict = {}
    for line in target:
        res = field.search(line)
        if res != None:
            value = re.sub("'{3}","",res.group(2))
            value2 = re.sub(r"\[\[(.*?)\]\]",r"\1",value)
            value3 = re.sub(r"(.*)\|(.*?)",r"\2",value2)
            dict[res.group(1)] = value3
    for k, v in dict.iteritems():
        print k, v

def solve_28():
    target = solve_20().split("\n")
    field = re.compile(u'([^\|]*?)\s=\s([^=]*)')
    dict = {}
    for line in target:
        res = field.search(line)
        if res != None:
            value = re.sub(r"\{\{lang\|(.*?)\|(.*?)\}\}",r"\2",res.group(2))
            value = re.sub("'{3}","",value)
            value = re.sub(r"\[\[(.*?)\]\]",r"\1",value)
            value = re.sub(r"\[\[(.*)\|(.*)\]\]",r"\2",value)
            value = re.sub(r"<(.*?)>",r"",value)
            dict[res.group(1)] = value
    for k, v in dict.iteritems():
        print k, v