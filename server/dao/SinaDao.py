#!/usr/bin/env python
# -*- coding: utf-8 -*-  
from util import MongodbUtil
UserCollection = MongodbUtil.db.user
InfoCollection = MongodbUtil.db.info
LocationCollection = MongodbUtil.db.location
UserWeiboCollection = MongodbUtil.db.userweibo
NewestCollection = MongodbUtil.db.newest
OldCollection =MongodbUtil.db.olduser
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
		print user_info
		if user_info != None:
			user_info['Repost_Intimacy'] = user_info['Repost_Intimacy']+1
			# user_info['Comment_Intimacy'] = 0
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
		user_info = UserCollection.find_one({'idstr':i['user']['idstr']},{'_id':0})
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
		'statuses_count':r['statuses_count'],#微博数
		'created_at':r['created_at'],#用户创建时间
		'verified':r['verified']#是否为加V用户
	}
	InfoCollection.insert(info)
	
	return info
def getmyinfo():
	data = InfoCollection.find_one({},{'_id':0})
	return data

def friend_location(r):
	print len(r['users'])
	for i in r['users']:
		loc = i['location'].split(" ")[0] if i['location']!='' else '其他'
		location = {
			'idstr':i['idstr'],
			'screen_name':i['screen_name'],
			'location':loc
		}

		LocationCollection.insert(location)

def getfriendlocinfo():
	locs = LocationCollection.find({},{'location':1,'_id':0})
	loc_list={}
	for i in locs:
		if loc_list.has_key(i['location']):
			loc_list[i['location']]+=1
		else:
			loc_list[i['location']]=1
	return loc_list	
def getfriendinfo():
	data = UserCollection.find({},{'_id':0,'screen_name':1,'Repost_Intimacy':1,'Comment_Intimacy':1})
	return data

def save_weibo_info(r):
	for i in r['statuses']:
		weibo_info={
			'text':i['text'],
			'create_time':i['created_at']
			}
		UserWeiboCollection.insert(weibo_info)
def getweibo():
	return UserWeiboCollection.find({},{'_id':0})
def old_save_info(strid,screen_name,Ie,Ic,Ia,Ib):
	old_user_info=OldCollection.find_one({'strid':strid})
	if old_user_info == None:
		old_info={
			'screen_name':screen_name,
			'strid':strid,
			'Ie':Ie,
			'Ic':Ic,
			'Ia':Ia,
			'Ib':Ib
		}
		OldCollection.insert(old_info)
	else:
		old_user_info['Ie']=Ie
		old_user_info['Ic']=Ic
		old_user_info['Ia']=Ia
		old_user_info['Ib']=Ib
		OldCollection.update({'strid':strid},old_user_info)

def get_old_info():
	data = OldCollection.find({},{'_id':0,'screen_name':1,'Ie':1,'Ic':1,'Ia':1,'Ib':1})
	return data

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
def save_newest_repost(newest_weibo_id):

	newest_weibo={'newest_weibo_id':newest_weibo_id}
	NewestCollection.insert(newest_weibo)
def get_newest_repost():
	weibo_id=NewestCollection.find()[0]['newest_weibo_id']
	return weibo_id
def clean_newest_db():
	NewestCollection.remove()
def clean_use_db():
	UserCollection.remove()
def clean_info_db():
	InfoCollection.remove()
def clean_location_db():
	LocationCollection.remove()