#coding:utf-8
#mongoimport --db NLP --collection artist --type json --file artist.json

import redis
import json


def solve_60():
    db = redis.StrictRedis(host='localhost',
                           port=6379,db=2)
    with open('./artist.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            try :
                db.set(data['name'],data['area'])
            except:
                pass

def solve_61():
    _ = redis.Redis(host='localhost',
                    port=6379,db=2)
    print _.get('Comas')

def solve_62():
    _ = redis.Redis(host='localhost',
                    port=6379,db=2)
    ans = 0
    keys = _.keys(pattern='*')
    for key in keys:
        if _.get(key) == 'Japan':
           ans += 1
    print ans
    return ans

def solve_63():
    DB_NO = 0
    db = redis.Redis(host='localhost',
                    port=6379,db=DB_NO)
    with open('./artist.json','r') as f:
        for line in f:
            data = json.loads(line)
            try:
                db.set(data['name'],data['tags'])
            except:
                pass
    keys = db.keys(pattern="*")
    print "上位10件:\n"
    for key in keys[:10]:
        print "Key:{},Tags:{}".format(key,db.get(key))

solve_63()
