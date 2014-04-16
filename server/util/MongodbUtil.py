#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
import settings

config = settings.__mongo_config__

client = MongoClient(config['host'], config['port'])
db = client[config['db']]

def getNextSequence(name):
	ret = db.counters.find_and_modify(query={'_id':name}, update={'$inc':{'seq':1}}, upsert=True, new=True)
	return ret['seq']
