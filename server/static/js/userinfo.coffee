root = exports ? this
$ ->
	$.ajax {
		'type': 'get',
		'url': '/sina/getuserinfo',
		'success': (data) ->
			alert(typeof(data))
			console.log data
			alert(typeof(data))
			alert(data)
			table_data = []
			tmp = []
			alert(data['idstr'])
			tmp.push data['idstr']
			tmp.push data['screen_name']
			tmp.push data['location']
			tmp.push data['followers_count']
			tmp.push data['friends_count']
			tmp.push data['statuses_count']
			alert(tmp)
			table_data.push tmp
			$("#userinfo-list").dataTable().fnAddData table_data
			return
	}
	return