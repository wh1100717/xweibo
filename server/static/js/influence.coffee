$ ->
	initData = ->
		data = []
		time = (new Date()).getTime()
		data.push {x: time + i*1000, y: 0} for i in [-19..0]
		return data
	Highcharts.setOptions {
		global: {useUTC: false}
	}
	$('#container-status-realtime').highcharts {
		chart: {
			type: 'spline',
			animation: Highcharts.svg
			marginRight: 20
			events: {
				load: ->
					series = this.series
					setInterval ->
						x = (new Date()).getTime()
						$.ajax {
							'type': 'get',
							'contentType': 'application/json'
							'url': '/sina/getrepostnum'
							'success': (data) ->
								
								data = eval(data)
								# console.log data
								# data = parseFloat data
								series[0].addPoint [x, parseInt data[0]], true, true
								series[1].addPoint [x, parseInt data[1]], true, true
								return
						}
						return
					, 600000
					return

			}
		}
		title: {
			text: '实时数据分析'
		}
		xAxis: {
			type: 'datetime'
			tickPixelInterval: 150
		}
		yAxis: {
			title: {
				text: 'Value'
			}
			plotLines: [{
				value: 0
				width: 1
				color: '#808080'
			}]
		}
		tooltip: {
			formatter: ->
				return """
				<b>#{this.series.name}</b><br/>
				#{Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x)}<br/>
				#{Highcharts.numberFormat(this.y, 2)}
				"""
		}
		legend: {
			enabled: true
		}
		exporting: {
			enabled: false
		}
		series: [{
			name: 'comments'
			data: initData()
		},{
			name:'reposts'
			data:initData()
			}]
	}

	return
