#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
from weibo import APIClient
from util import WeiboUtil
from dao import SinaDao


urls = (
    '/user_show/(.*)','GetUserShow',
    '/public_timeline/(.*)','GetPublic',
    '/user_timeline/(.*)','GetUserIds'
)

class GetUserShow:
    def GET(self,uid_info):
        client = WeiboUtil.get_client()
        r = client.users.show.get(uid=uid_info)
        return json.dumps(r)
class GetPublic:
    def GET(self,strcount):
        client = WeiboUtil.get_client()
        r = client.statuses.public_timeline.get(count=strcount)
        #a = json.dumps(r['statuses'])
        # print len(r['statuses'])
   
        
        # weibo_info_lists=[]
        # for i in range(len(r['statuses'])):
        #     tmp=r['statuses'][i]
        #     weibo_info_lists.append((tmp['text'],tmp['created_at'],tmp['reposts_count'],tmp['comments_count'],tmp['attitudes_count']))
        
        # return sinaDao.save_weibo_info(weibo_info_lists)

        # user_info_lists = []
        # for i in range(len(r['statuses'])):
        #     tmp = r['statuses'][i]
        #     user_info_lists.append(tmp['user_id'],tmp['screen_name'],tmp['city_name'],tmp['followers_count'],tmp['friends_count'],tmp['statuses_count'])

        # return sinaDao.save_user_info(user_info_lists)
        return r
#user_timeline.get()获取某一用户发过的微薄id
#get_repost_timeline()获取微薄转发后的微薄id
#get_comments_show()获取微薄评论者id
class GetUserIds:
    def GET(self,strscreen_name):
        client = WeiboUtil.get_client()
        ids = []
        for i in range(1,21):
            r = client.statuses.user_timeline.ids.get(screen_name = strscreen_name,count = 100,page = i)
            if len(r['statuses']) == 0:
                break
            ids = ids + r['statuses']
        return get_repost_timeline(ids)
        # get_comments_show(ids)

#get_repost_timeline获取所有转发id
# def get_repost_timeline(strids):
#     print "weibochangdu:"+str(len(strids))
#     client = WeiboUtil.get_client()
#     all_report_ids = []
#     for strid in strids:
#         report_ids = []
#         print strid
#         for i in range(1,11):
#             r = client.statuses.repost_timeline.ids.get(id=strid,count = 200,page = i)
#             print r
#             if len(r['statuses']) == 0:
#                 break
#             report_ids.append(r['statuses'])
#         # get_info_by_id(report_ids)
#         # get_comments_show(report_ids)
#         #如果没有转发id跳出 如果有继续

        
#         all_report_ids.append(report_ids)
#         get_repost_timeline(report_ids)
#     return all_report_ids



def get_repost_timeline(strids):
    client = WeiboUtil.get_client()    
    all_report_ids=[]    
    for strid in strids:        
        report_ids = []        
        for i in range(1,11):            
            r = client.statuses.repost_timeline.ids.get(id=strid,count = 200,page = i)  
            print r
            print r['statuses']                      
            if len(r['statuses']) == 0:                
                break            
            report_ids=report_ids+r['statuses']        
    # get_info_by_id(report_ids)        
    # get_comments_show(report_ids)        
    #如果没有转发id跳出 如果有继续        
        if len(report_ids) != 0:
            all_report_ids=all_report_ids+report_ids+get_repost_timeline(report_ids)
    return all_report_ids 


#get_comments_show通过id获取评论id
def get_comments_show(comment_ids):
    client = WeiboUtil.get_client()
    for comment_id in comment_ids:
        for i in range(1,41):
            r = comments.show.get(id = comment_id,page = i,count = 50)
            #SinaDao.save_comment_user_info(r)


            
#get_info_by_id通过转发id获取用户id
def get_info_by_id(report_ids):
    client = WeiboUtil.get_client()
    for report_id in report_ids:
        r = client.statuses.show.get(report_id)
        return r
        #SinaDao.save_report_user_info(r)



app = web.application(urls, locals())