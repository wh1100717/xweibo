#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from util import MongodbUtil
UserCollection = MongodbUtil.db.user
InfoCollection = MongodbUtil.db.info
# def save_weibo_info(weibo_info_lists):
# 	SqliteUtil.checkTableExist()
# 	sql="insert into weibo_info (text,created_data,reposts_count,comments_count,attitudes_count) values (?,?,?,?,?)"
# 	SqliteUtil.execute_sql(sql,weibo_info_lists)
# 	return "success"

# def save_user_info(user_info_lists):
# 	SqliteUtil.checkTableExist()
# 	sql="insert into weibo_info (user_id,screen_name,city_name,followers_count,friends_count,statuses_count) values (?,?,?,?,?,?)"
# 	SqliteUtil.execute_sql(sql,user_info_lists)
# 	return "success"
#转发用户信息
def repost_user_info(r):

	for i in r:

		user={
			'idstr' : i['user']['idstr'],
			'screen_name' : i['user']['screen_name']
		}
		user_info = UserCollection.find_one({'idstr':i['user']['idstr']})
		# print user_info
		if user_info != None:
			user_info['Repost_Intimacy'] = user_info['Repost_Intimacy']+1
			user_info['Comment_Intimacy'] = 0
			UserCollection.update({'idstr':i['user']['idstr']},{"$set":user_info})
		else:
			user['Repost_Intimacy'] = 1
			user['Comment_Intimacy']= 0
			UserCollection.insert(user)

#评论的用户信息
def comment_user_info(r):
	for i in r:
		user = {
			'idstr':i['user']['idstr'],
			'screen_name':i['user']['screen_name']
		}
		user_info = UserCollection.find_one({'idstr':i['user']['idstr']})
		if user_info == None:
			user['Comment_Intimacy'] = 1
			user['Repost_Intimacy'] = 0
			UserCollection.insert(user)
		# elif user_info.has_key('Comment_Intimacy'):
		# 	user_info['Comment_Intimacy'] = user_info['Comment_Intimacy']+1
		# 	UserCollection.update({'idstr':i['user']['idstr']},{"$set":user_info})
		else:
			user_info['Comment_Intimacy'] = user_info['Comment_Intimacy']+1
			UserCollection.update({'idstr':i['user']['idstr']},{"$set":user_info})

#用户信息
def user_info(r):
	info = {
		'idstr':r['idstr'],
		'screen_name':r['screen_name'],
		'location':r['location'],
		'followers_count':r['followers_count'],#粉丝数
		'friends_count':r['friends_count'],#关注数
		'statuses_count':r['statuses_count'] #微博数
	}
	InfoCollection.insert(info)
	return info

# def get_intimacy():
# 	user_infos = UserCollection.find()
# 	for user_info in user_infos:
# 		repost_intimacy = user_info['Repost_Intimacy']
# 		comment_intimacy = user_info['Comment_Intimacy']
		
# 		user_info['Intimacy']= repost_intimacy+comment_intimacy
# 		UserCollection.update({'idstr':user_info['idstr']},{"$set":user_info})


# def get_comment_intimacy():
# 	comment_intimacy = user_info['Comment_Intimacy']

# 	return comment_intimacy

def clean_db():
	UserCollection.remove()