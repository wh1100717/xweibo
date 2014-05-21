$ ->
	$.ajax {
		'type': 'get',
		'contentType':'application/json',
		'url': '/sina/getuserinfo',
		'success': (data) ->
			alert(data)
			data = data.replace(/u"/g,'"')
			alert(data)
			data = JSON.parse(data)
			# alert(data)
			$("#statuses_count").html(data.statuses_count)
			$("#screen_name").html(data.screen_name)
			$("#friends_count").html(data.friends_count)
			$("#idstr").html(data.idstr)
			$("#followers_count").html(data.followers_count)
			$("#location").html(data.location)
			$("#verified").html(data.verified)
			$("#created_at").html(data.created_at)
			return
	}
	return