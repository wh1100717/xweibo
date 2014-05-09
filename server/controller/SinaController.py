#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
from weibo import APIClient
from util import WeiboUtil
from dao import SinaDao
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
render = web.template.render('templates/', base='layout')
render_without_layout = web.template.render('templates/')
urls = (
    # '/userinfo/(.*)','GetUserInfo',
    # '/public_timeline/(.*)','GetPublic',
    # '/user_timeline/(.*)','GetUserIds',
    # # '/get_one_weibo/(.*)','GetOneWeibo'
    # '/intimacy/(.*)','GetIntimacy',
    # '/care/','GetCare'
    '/getfriend','GetFriend',
    '/getuserinfo','GetUserInfo',
    '/userinfo','SetUserInfo',
    '/getfriendsloc','GetFriendsLoc'
)
#3706930306101099
# class GetOneWeibo:
#     def GET(self,weibo_id):
#         print weibo_id
#         ids = []
#         ids = [weibo_id]
#         client = WeiboUtil.get_client()
#         report_ids = get_repost_timeline(ids)
#         print report_ids
#         r = get_info_by_id(report_ids)
#         return r

#通过用户id获取该用户被转发的微博列表以及评论列表
# class get_repost_by_user_id:
#     def GET(self,uid):
#         SinaDao.clean_db()
#         client = WeiboUtil.get_client()
#         r = client.statuses.user_timeline.get(uid=uid)
#         weibo_ids = []
#         for i in r['statuses']:
#             weibo_ids.append(i['id'])
#         print weibo_ids
#         for weibo_id in weibo_ids:
#             r1 = client.statuses.repost_timeline.get(id=weibo_id)
#             SinaDao.save_user_info(r1['reposts'])
#             print r1

#     def get_comment_by_weibo_id(weibo_ids):

class SetUserInfo:
    def POST(self):
        i = web.input()
        SinaDao.clean_info_db()
        userinfo = WeiboUtil.get_userinfo_by_screen_name(i.screen_name)
        SinaDao.user_info(userinfo)

        SinaDao.clean_use_db()
        weibo_id = WeiboUtil.get_weiboid_by_user_id(userinfo['idstr'])
        repost = WeiboUtil.get_repost_by_weiboid(weibo_id)
        comment = WeiboUtil.get_comment_by_weiboid(weibo_id)
        SinaDao.repost_user_info(repost)
        SinaDao.comment_user_info(comment)
        
        SinaDao.clean_location_db()
        friend_location = WeiboUtil.get_friend_location_by_screen_name(i.screen_name)
        SinaDao.friend_location(friend_location)

        return render.userinfo()
class GetUserInfo:
    def GET(self):
        data = SinaDao.getmyinfo()
        print data
        result = {}
        for i in data:
            result[str(i)]=data[i]
        return str(result).replace('\'','\"')
class GetFriendsLoc:
    def GET(self):
        loc_lists = SinaDao.getfriendlocinfo()
        result = '['
        for i in loc_lists:
            result += "['"+ i + "'," + str(loc_lists[i])+ "],"
        result=result[:-1] + ']'
        return result
class GetFriend:
    def GET(self):
        friend_infos = SinaDao.getfriendinfo()
        result = '['
        for i in friend_infos:
            # if i['Repost_Intimacy']+i['Req']
            result += "['"+ str(i['screen_name']) + "'," +str(i['Repost_Intimacy'])+","+str(i['Comment_Intimacy'])+"],"
        result=result[:-1] + ']'
        return str(result).replace('\'','\"')

# class GetIntimacy:
#     def GET(self,uid):
        # SinaDao.clean_use_db()
        # weibo_id = WeiboUtil.get_weiboid_by_user_id(uid)
        # repost = WeiboUtil.get_repost_by_weiboid(weibo_id)
        # comment = WeiboUtil.get_comment_by_weiboid(weibo_id)
        # SinaDao.repost_user_info(repost)
        # SinaDao.comment_user_info(comment)
        


# class GetUserShow:
#     def GET(self,uid_info):
#         client = WeiboUtil.get_client()
#         r = client.users.show.get(uid=uid_info)
#         return json.dumps(r)
# class GetPublic:
#     def GET(self,strcount):
#         client = WeiboUtil.get_client()
#         r = client.statuses.public_timeline.get(count=strcount)
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
        # return r
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
        r = client.statuses.show.get(id = report_id)
        return r
        #SinaDao.save_report_user_info(r)



app = web.application(urls, locals())