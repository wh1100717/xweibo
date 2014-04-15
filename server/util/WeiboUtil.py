#!/usr/bin/env python
# -*- coding: utf8 -*-
from weibo import APIClient
import urllib2,urllib
import datetime
import Config
def get_client():
    LOGIN_INFO=Config.LOGIN_INFO
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
