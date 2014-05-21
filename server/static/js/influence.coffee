$ ->
	$.ajax {
		'type': 'get',
		'contentType':'application/json',
		'url': '/sina/getinfluence',
		'success': (data) ->
			alert(data)
			data = data.replace(/u"/g,'"')
			# data = data.replace('\'','\"')
			alert(data)
			data = JSON.parse(data)
			alert(data)
			$("#Ie").html(data.Ie)
			$("#Ic").html(data.Ic)
			$("#Ia").html(data.Ia)
			$("#I").html(data.I)
			return
	}
	return