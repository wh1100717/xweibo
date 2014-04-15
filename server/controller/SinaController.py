#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
from weibo import APIClient
from util import WeiboUtil
from dao import SinaDao


urls = (
    '/user_show/(.*)','GetUserShow',
    '/public_timeline/(.*)','GetPublic'
)

class GetUserShow:
    def GET(self,uid_info):
        client = WeiboUtil.get_client()
        r = client.users.show.get(uid=uid_info)
        return json.dumps(r)
class GetPublic:
    def GET(self,count):
        client = WeiboUtil.get_client()
        r = client.statuses.public_timeline.get(count = 2)
        #a = json.dumps(r['statuses'])
        print len(r['statuses'])
   
        
        weibo_info_lists=[]
        for i in range(len(r['statuses'])):
            tmp=r['statuses'][i]
            weibo_info_lists.append((tmp['text'],tmp['created_at'],tmp['reposts_count'],tmp['comments_count'],tmp['attitudes_count']))
        
        return sinaDao.save_weibo_info(weibo_info_lists)

        user_info_lists = []
        for i in range(len(r['statuses'])):
            tmp = r['statuses'][i]
            user_info_lists.append(tmp['user_id'],tmp['screen_name'],tmp['city_name'],tmp['followers_count'],tmp['friends_count'],tmp['statuses_count'])

        return sinaDao.save_user_info(user_info_lists)

app = web.application(urls, locals())