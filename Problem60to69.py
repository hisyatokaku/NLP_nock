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
                    port=6379,db=0)
    print _.get('Comas')

solve_61()
