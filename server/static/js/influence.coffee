$ ->
	$.ajax {
		'type': 'get',
		'contentType':'application/json',
		'url': '/sina/getinfluence',
		'success': (data) ->
			alert(data)
			# alert(data['data'])
			data = data.replace(/u'/g,'\'')

			data = data.replace(/\'/g,'"')
			alert(data)
			data = JSON.parse(data)
			alert(data)



			# $("#screen_name").html(data['data'][0].screen_name)
			# $("#Ie").html(data['data'][0].Ie)
			# $("#Ic").html(data['data'][0].Ic)
			# $("#Ia").html(data['data'][0].Ia)
			# $("#I").html(data['data'][0].I)
			# $("#screen_name1").html(data['data'][1].screen_name)
			# $("#Ie1").html(data['data'][1].Ie)
			# $("#Ic1").html(data['data'][1].Ic)
			# $("#Ia1").html(data['data'][1].Ia)
			# $("#I1").html((1/data['data'][0].Ia*data['data'][1].Ia).toFixed(4))

			tmp = ''
			tmpdatas = data['data']
			stander_Ia = 0
			for tmpdata in tmpdatas
				if tmpdata.screen_name is '喵晓琳'
					stander_Ia = tmpdata.Ia
			alert(stander_Ia)
			for tmpdata in tmpdatas
				if tmpdata.screen_name is '喵晓琳'
					tmp += '<tr>
						<th id="screen_name">'+tmpdata.screen_name+'</th>
						<th id="Ie">'+tmpdata.Ie+'</th>
						<th id="Ic">'+tmpdata.Ic+'</th>
						<th id="Ia">'+tmpdata.Ia+'</th>
						<th id="I">'+1+'</th>
						</tr>'
				else
					tmp += '<tr>
					<th id="screen_name">'+tmpdata.screen_name+'</th>
					<th id="Ie">'+tmpdata.Ie+'</th>
					<th id="Ic">'+tmpdata.Ic+'</th>
					<th id="Ia">'+tmpdata.Ia+'</th>
					<th id="I">'+((1/stander_Ia)*tmpdata.Ia).toFixed(4)+'</th>
					</tr>'

			$("#influence-table").html('<tr>
                    <th >用户昵称</th>
                    <th >用户直接影响力(Ie)</th>
                    <th >用户级联影响力(Ic)</th>
                    <th >用户绝对影响力(Ia)</th>
                    <th>用户相对影响力(I)</th>
                </tr>'+tmp)
			return



			# alert(data)
			# data = data.replace(/u'/g,'\'')
			# data = data.replace(/\'/g,'"')
			# data = JSON.parse(data)
			# # data_list = data['data']
			# # table_data = []
			# for i in [0..9]
			# 	$("#screen_name").html(data['data'][0].screen_name)
			# 	$("#Ie").html(data['data'][0].Ie)
			# 	$("#Ic").html(data['data'][0].Ic)
			# 	$("#Ia").html(data['data'][0].Ia)
			# 	$("#I").html(data['data'][0].I)
			# 	# tmp = []
			# 	# tmp.push d['screen_name']
			# 	# tmp.push d['Ie']
			# 	# tmp.push d['Ic']
			# 	# tmp.push d['Ia']
			# 	# tmp.push d['I']
			# 	# table_data.push tmp
			# # $("#user-influence").dataTable().fnAddData table_data
			# # $('[data-rel=tooltip]').tooltip({'html':true})
			# return


			# alert(data['data'])
			# # data = data.replace("u\'",'"')
			# alert(typeof(data))
			# # data = eval(data['data'])
			# data = JSON.parse(data)
 
			# tmp = ""
			# alert(data['data'].length)
			# for i in [0..data['data'].length-1]
			# 	tmp = tmp+"<tr><th>"+data['data'][i].screen_name+"</th><td>"+data['data'][i].Ie+"</td><td>"+data['data'][i].Ic+"</td><td>"+data['data'][i].Ia+"</td><td>"+data['data'][i].I+"</td></tr>"
			# alert(tmp)
			# # $("#weekweibonum").html("<thead><tr><th>姓名</th><th>转发数</th><th>评论数</th></tr></thead><tbody>"+str(data[0])+"</tbody>")    
			# # $("#title").html("用户影响力列表")
			# $("#influence").html("<thead><tr><th>用户昵称</th><th>用户直接影响力</th><th>用户间接影响力</th><th>用户绝对影响力</th><th>用户相对影响力</th></tr></thead><tbody>"+tmp+"</tbody>")

			# return
	}
	return