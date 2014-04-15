#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from util import SqliteUtil
def save_weibo_info(weibo_info_lists):
	SqliteUtil.checkTableExist()
	sql="insert into weibo_info (text,created_data,reposts_count,comments_count,attitudes_count) values (?,?,?,?,?)"
	SqliteUtil.execute_sql(sql,weibo_info_lists)
	return "success"

def save_user_info(user_info_lists):
	SqliteUtil.checkTableExist()
	sql="insert into weibo_info (user_id,screen_name,city_name,followers_count,friends_count,statuses_count) values (?,?,?,?,?,?)"
	SqliteUtil.execute_sql(sql,user_info_lists)
	return "success"