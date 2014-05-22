#!/usr/bin/env python
# -*- coding: utf8 -*-
from weibo import APIClient
import urllib2,urllib
import datetime
import settings
def get_client():
    LOGIN_INFO=settings.LOGIN_INFO
    client = APIClient(app_key=LOGIN_INFO['APP_KEY'], app_secret=LOGIN_INFO['APP_SECRET'], redirect_uri=LOGIN_INFO['CALLBACK_URL'])
    starturl = client.get_authorize_url()
    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
    urllib2.install_opener(opener)
    postdata = {"client_id": LOGIN_INFO['APP_KEY'],
             "redirect_uri": LOGIN_INFO['CALLBACK_URL'],
             "userId": LOGIN_INFO['USERID'],
             "passwd": LOGIN_INFO['PASSWD'],
             "isLoginSina": "0",
             "action": "submit",
             "response_type": "code",
             }

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
               "Host": "api.weibo.com",
               "Referer": starturl
             }

    req  = urllib2.Request(
                           url = LOGIN_INFO['AUTH_URL'],
                           data = urllib.urlencode(postdata),
                           headers = headers
                           )

    resp = urllib2.urlopen(req) 
    code = resp.geturl()[-32:]
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in 


    print "token: %s will expires in %s" % (access_token, datetime.datetime.fromtimestamp(expires_in).strftime('%Y-%m-%d %H:%M:%S'))
    
    client.set_access_token(access_token, expires_in)
    return client
#    #for obj in client.get.statuses__user_timeline().__getattr__('statuses'):
#    #    tid = obj.__getattr__('id')
#    #    text = obj.__getattr__('text')
#    #    created_at = obj.__getattr__('created_at')
#    #    print "%d: %s %s" % (tid, created_at, text)
#    r = client.users.show.get(uid=1621200391)
#    print json.dumps(r, ensure_ascii=False)   

def get_weibo_by_user_id(uid):
    client = get_client()
    r = client.statuses.user_timeline.get(uid=uid)
    # weibo_id = []
    # for i in r['statuses']:
    #     weibo_id.append(i['id'])
    return r
    # print weibo_ids
    # for weibo_id in weibo_ids:
    #     r1 = client.statuses.repost_timeline.get(id=weibo_id)
    #     SinaDao.save_user_info(r1['reposts'])
    #     print r1
def get_weibo_id(r):
    weibo_id = []
    for i in r['statuses']:
        weibo_id.append(i['id'])
    return weibo_id
def get_repost_by_weiboid(weibo_id):
    client = get_client()
    repost = []
    for wid in weibo_id:
        r = client.statuses.repost_timeline.get(id=wid)
        
        repost = repost+r['reposts']
    return repost

def get_comment_by_weiboid(weibo_id):
    client = get_client()
    comment = []
    for wid in weibo_id:
        r = client.comments.show.get(id=wid)
        # comment = []
        # comment.append(r['comments'])
        comment = comment + r['comments']
    return comment

def get_userinfo_by_screen_name(my_screen_name):
    client = get_client()
    user_info = client.users.show.get(screen_name=my_screen_name)
    return user_info

def get_friend_location_by_screen_name(my_screen_name):
    client = get_client()
    print my_screen_name
    friend_location = client.friendships.followers.get(screen_name=my_screen_name,count=200)
    print friend_location
    return friend_location
def trends_weekly():
    
    client = get_client()
    r = client.trends.weekly.get()
    topkey = []
    topkey_lists=r['trends']
    time = topkey_lists.keys()[0]
    topkey_lists_by_time = topkey_lists[time]
    for i in topkey_lists_by_time:
        topkey.append(i['name'])
    return topkey

def statuses_count(weibo_id):
    client = get_client()
    r = client.statuses.count.get(ids=weibo_id)
    return r
def zhaoqing_influence():
    users_counts
    