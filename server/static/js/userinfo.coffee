root = exports ? this
$ ->
 
    $.ajax {
        'type': 'get',
        'url': '/sina/getuserinfo',
        'success': (data) ->
        	console.log data
        	alert(data)
        	# tmp.push(data['id'])
			# tmp.push(data['data']['id'])
			# tmp.push(data['name'])
			# tmp.push(data['loc'])
			# tmp.push(data['fun'])
			# tmp.push(data['see'])
			# tmp.push(data['num'])
			# table_data.push tmp
			# $("#device-list").dataTable().fnAddData table_data
			# $('[data-rel=tooltip]').tooltip({'html':true})
            # return            
    }