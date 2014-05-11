$ ->
	$.ajax {
		'type': 'get',
		'contentType':'application/json',
		'url': '/sina/getfriend',
		'success': (data) ->
			data = data.replace(/u"/g,'"')
			data = JSON.parse(data)
			
			return
	}
	return

# $ ->
# 	$.ajax {
# 		'type': 'get',
# 		'contentType':'application/json',
# 		'url': '/sina/getfriend',
# 		'success': (data) ->
# 			alert(data)
# 			data = data.replace(/u"/g,'"')
# 			data = JSON.parse(data)
# 			$("#screen_name").html(data.screen_name)
# 			$("#reposts_count").html(data.Repost_Intimacy)
# 			$("#comments_count").html(data.Comment_Intimacy)
# 			return
# 	}
# 	return