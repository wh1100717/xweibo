#!/usr/bin/env python
# -*- coding: utf-8 -*-

def converttime(month):
	strmonth = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'June':6,'July':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
	return strmonth[month]
def convertweek(week):
	strweek = {'Mon':u'星期一','Tue':u'星期二','Wed':u'星期三','Thu':u'星期四','Fri':u'星期五','Sat':u'星期六','Sun':u'星期日'}
	return strweek[week]