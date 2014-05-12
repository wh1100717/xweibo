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
					series = this.series[0]
					setInterval ->
						x = (new Date()).getTime()
						$.ajax {
							'type': 'get',
							'contentType': 'application/json'
							'url': '/sina/getrepostnum'
							'success': (data) ->
								console.log data
								data = parseFloat data
								series.addPoint [x, data], true, true
								return
						}
						return
					, 1000
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
			enabled: false
		}
		exporting: {
			enabled: false
		}
		series: [{
			name: 'Random data'
			data: initData()
		}]
	}
	return
