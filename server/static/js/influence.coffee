$ ->
	initData = ->
		data = []
		time = (new Date()).getTime()
		data.push {x: time + i*1000, y: 0} for i in [-19..0]
		return data
	Highcharts.setOptions({global:{useUTC:false}})
	$('#container-status-realtime').highcharts {
		chart:{
			type: 'spline',
			animation: Highcharts.svg,
			marginRight: 10,
			events:{
				load: ->
					series = @series
					setInterval ()-> 
						x = (new Date()).getTime()
						$.ajax {
							'type': 'get',
							'contentType':'application/json',
							'url': '/sina/getrepostnum',
							'success': (data) ->
								alert(data)
								return
						}

						return
					,5000
					return
			},
		}
		title: {text: '实时数据分析'},
		xAxis: {type: 'datetime', tickPixelInterval: 150},
		yAxis: {
			title: {
				text: 'Value'
			},
			plotLines: [{
				color: '#808080'
			}]
		},
		tooltip: {
			formatter: -> '<b>' + this.series.name + '</b><br/>' + Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' + Highcharts.numberFormat(this.y, 0);
		},
		legend: {enabled: true},
		exporting: {enabled: false},
		series: [
			{name: 'xiaomi_crawled_data', data: initData()},
		
		]
	}
	status_chart = $('#container-status-realtime').highcharts();
	status_chart.series[1].hide()

	return
