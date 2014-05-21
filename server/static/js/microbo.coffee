$ ->
    $.ajax {
        'type': 'get',
        'contentType':'application/json',
        'url': '/sina/getweekweibo',
        'success': (data) ->
            alert(data)
            # data = data.replace("u\'",'"')
            alert(typeof(data))
            data = eval(data)
            # data = JSON.parse(data)
            alert(data[0])
            alert(data[2])
 
            tmp = ""
            alert(data[1].length)
            for i in [0..9]

                    tmp = tmp+"<tr><th>"+data[1][i]+"</th><td>"+data[2][i]+"</td></tr>"
            alert(tmp)
            # $("#weekweibonum").html("<thead><tr><th>姓名</th><th>转发数</th><th>评论数</th></tr></thead><tbody>"+str(data[0])+"</tbody>")    
            $("#weekweibonum").html("最近一周共发布了"+data[0]+"个微薄")
            $("#myweibokey").html("<thead><tr><th>我的微薄最近一周的高频词top10</th><th>当前微薄一周热门词汇top10</th></tr></thead><tbody>"+tmp+"</tbody>")

            return
    }
    return


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
                    , 6000000
                    return

            }
        }
        title: {
            text: '实时数据分析'
        }
        xAxis: {
            type: '时间'
            tickPixelInterval: 150
        }
        yAxis: {
            title: {
                text: '数量'
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
            name: '评论数'
            data: initData()
        },{
            name:'转发数'
            data:initData()
            }]
    }

    return