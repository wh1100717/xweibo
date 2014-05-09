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