#!/usr/bin/env python
# -*- coding: utf-8 -*-
import settings
import web
import json
from weibo import APIClient
from util import WeiboUtil
from dao import SinaDao
import sys
from util import StringUtil
from datetime import datetime,timedelta
import jieba.analyse
import random
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
    '/getfriendsloc','GetFriendsLoc',
    '/getweekweibo','GetweekWeibo',
    '/getrepostnum','GetrepostNum',
    '/getinfluence','GetInfluence'
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
        settings.LOGIN_INFO['USERID'] = i.userid
        settings.LOGIN_INFO['PASSWD'] = i.passwd
        SinaDao.clean_info_db()
        userinfo = WeiboUtil.get_userinfo_by_screen_name(i.screen_name)
        SinaDao.user_info(userinfo)

        SinaDao.clean_use_db()
        r = WeiboUtil.get_weibo_by_user_id(userinfo['idstr'])
        SinaDao.save_weibo_info(r)
        weibo_id = WeiboUtil.get_weibo_id(r)
        
        SinaDao.clean_newest_db()
        newest_weibo_id = weibo_id[0]
        
        SinaDao.save_newest_repost(newest_weibo_id)
        
        repost = WeiboUtil.get_repost_by_weiboid(weibo_id)
        comment = WeiboUtil.get_comment_by_weiboid(weibo_id)
        SinaDao.repost_user_info(repost)
        SinaDao.comment_user_info(comment)
        
        SinaDao.clean_location_db()
        friend_location = WeiboUtil.get_friend_location_by_screen_name(i.screen_name)
        print friend_location
        SinaDao.friend_location(friend_location)

        return render.userinfo()
        # return render.repost()
        # return render.comment()
#获取用户信息
class GetUserInfo:
    def GET(self):
        data = SinaDao.getmyinfo()
        if data['verified']:
            data['verified'] = u'是'
        else:
            data['verified'] = u'否'

        stime = data['created_at'].split(" ")
        

        data['created_at'] = str(stime[5])+u"年"+str(StringUtil.converttime(stime[1]))+u"月"+str(stime[2])+u"日"+StringUtil.convertweek(stime[0])+stime[3]
        print data
        result = {}
        for i in data:
            result[str(i)]=data[i]
        return str(result).replace('\'','\"')
#获取粉丝地理位置
class GetFriendsLoc:
    def GET(self):
        loc_lists = SinaDao.getfriendlocinfo()
        result = '['
        for i in loc_lists:
            result += "['"+ i + "'," + str(loc_lists[i])+ "],"
        result=result[:-1] + ']'
        return result
#获取用户粉丝转发和评论用户微博数
class GetFriend:
    def GET(self):
        print '+++++++='
        friend_infos = SinaDao.getfriendinfo()
        print friend_infos
        name = '['
        reports = '['
        commites = '['
        
        
        
        for i in friend_infos:
            print i
            # if i['Repost_Intimacy']+i['Req']
            name += "'"+str(i['screen_name']) +"',"
            reports += str(i['Repost_Intimacy'])+","
            commites += str(i['Comment_Intimacy'])+","
            # result += "{'screen_name':i['screen_name'],'reposts_count':i['Repost_Intimacy'],'comments_count':i['Comment_Intimacy']},"
        name=name[:-1] + ']'
        reports=reports[:-1] + ']'
        commites=commites[:-1] + ']'
        result='['+name+','+reports+','+commites+']'
        print result
        return result
#获取了一周的微薄 返回值里面包含创建时间和微薄内容
class GetweekWeibo:
    def GET(self):
        now_time = datetime.now()
        week_ago = now_time - timedelta(7)
        weibo_lists = SinaDao.getweibo()
        time = str(week_ago).split(' ')[0].split('-')
        new_weibo_lists=[]
        for weibo_list in weibo_lists:
            weibo_time = weibo_list['create_time'].split(' ')

            #weibo_time[5] is year weibo_time[1] is month weibo_time[2] is day
            if  int(weibo_time[5])==int(time[0]) and StringUtil.converttime(weibo_time[1])==int(time[1]) and int(weibo_time[2])>=int(time[2]) :
                new_weibo_lists.append(weibo_list)
            elif int(weibo_time[5])>int(time[0]) :
                    new_weibo_lists.append(weibo_list)
            elif int(weibo_time[5])==int(time[0]) and StringUtil.converttime(weibo_time[1])>int(time[1]):
                new_weibo_lists.append(weibo_list)
        result=[]
        result.append([len(new_weibo_lists)])
        result.append(jiebafenci(new_weibo_lists))
        result.append(WeiboUtil.trends_weekly())
        result = str(result).replace("u'","'")
        
        return result
#通过jieba进行分词 返回一个dict，里面是分词的结果，返回出现次数最多的10个单词 返回类型为list
def jiebafenci(new_weibo_lists):
    hot_words={}
    text=[]
    for new_weibo_list in new_weibo_lists:
        text.append(new_weibo_list['text'])
    all_text=','.join(text)
    tags = jieba.analyse.extract_tags(all_text, topK=10)
    return tags
# class GetIntimacy:
#     def GET(self,uid):
        # SinaDao.clean_use_db()
        # weibo_id = WeiboUtil.get_weiboid_by_user_id(uid)
        # repost = WeiboUtil.get_repost_by_weiboid(weibo_id)
        # comment = WeiboUtil.get_comment_by_weiboid(weibo_id)
        # SinaDao.repost_user_info(repost)
        # SinaDao.comment_user_info(comment)
        
class GetrepostNum:
    def GET(self):
        weibo_id = SinaDao.get_newest_repost()
        r = WeiboUtil.statuses_count(weibo_id)[0]
       
        # r = WeiboUtil.statuses_count('3706902724217725')[0]
        comments = int(r['comments'])
        reposts = int(r['reposts'])

        data = [[comments],[reposts]]
        return data


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


class GetInfluence:
    def GET(self):
        data = SinaDao.getmyinfo()
        # print data
        repost_count = SinaDao.getfriendinfo()
        # print repost_count
        idstr = data['idstr']
        screen_name = data['screen_name']
        allrepost=0
        for i in repost_count:
            allrepost+=i['Repost_Intimacy']
        #把reposts的值存在oldcontroller中  不过这个坏处就是需要每次点击这个方法才会好使
        Ie = data['friends_count']*data['statuses_count']
        Ic = allrepost*data['friends_count']
        Ia = Ie + Ic
        Ib = 1

        # influence = '{u"Ie":'+str(Ie)+',u"Ic":'+str(Ic)+',u"Ia":'+str(Ia)+',u"I":'+str(I)+'}'
        SinaDao.old_save_info(idstr,screen_name,Ie,Ic,Ia,Ib)
        influences = SinaDao.get_old_info()
        data=[]
        
        for influence in influences:
            print "====="
            print influence
            data.append({"screen_name":unicode(str(influence['screen_name']), "utf-8"),
                "Ie":str(influence['Ie']),
                "Ic":str(influence['Ic']),
                "Ia":str(influence['Ia']),
                "I":str(influence["Ib"])})
        # print data
        result={}
        result['data']=data
        return result



# class GetUserInfo:
#     def GET(self):
#         data = SinaDao.getmyinfo()
#         if data['verified']:
#             data['verified'] = u'是'
#         else:
#             data['verified'] = u'否'

#         stime = data['created_at'].split(" ")
        

#         data['created_at'] = str(stime[5])+u"年"+str(StringUtil.converttime(stime[1]))+u"月"+str(stime[2])+u"日"+StringUtil.convertweek(stime[0])+stime[3]
#         print data
#         result = {}
#         for i in data:
#             result[str(i)]=data[i]
#         return str(result).replace('\'','\"')



app = web.application(urls, locals())