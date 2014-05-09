$ ->
    #分类数据饼状图Ajax初始化
    $.ajax {
        'type': 'get',
        'url': '/sina/getfriendsloc',
        'success': (data) ->
            $('#container-platform').highcharts {
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false
                },
                title:{text:'分类应用数据分析'},
                subtitle:{text:'PolySpider爬取应用所属分类饼状图'},
                tooltip:{pointFormat: '{series.name.percent}: <b>{point.percentage:.1f}%</b><br>{series.name.count}: <b>{point.y}</b><br>'},
                plotOptions:{
                    pie:{
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: true,
                            color: '#000000',
                            connectorColor: '#000000',
                            format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                        },
                        showInLegend: true
                    }
                },
                series:[
                    {
                        type: 'pie',
                        name: {'percent': '百分比', 'count': '应用数'},
                        data: eval(data)
                    }
                ]
            }
            return            
    }
    $.ajax {
        'type': 'get',
        'contentType':'application/json',
        'url': '/sina/getfriend',
        'success': (data) ->
            alert(data)
            data = eval(data)
            
            # data = data.replace(/u"/g,'"')
            # data = JSON.parse(data)
            # alert(date)
            tmp = ""
            for i in data
                tmp = tmp+"<tr><th>"+i[0]+"</th><td>"+i[1]+"</td><td>"+i[2]+"</td></tr>"
            $("#datatable").html("<thead><tr><th></th><th>转发数</th><th>评论数</th></tr></thead><tbody>"+tmp+"</tbody>")    
            return
    }
    #平台数据饼状图Ajax初始化
    # $.ajax {
    #     'type': 'get',
    #     'url': '/api/app/platform_statistic',
    #     'success': (data) ->
    #         $('#container-platform').highcharts {
    #             chart: {
    #                 plotBackgroundColor: null,
    #                 plotBorderWidth: null,
    #                 plotShadow: false
    #             },
    #             title: {
    #                 text: '平台应用数据分析'
    #             },
    #             subtitle: {
    #                 text: 'PolySpider爬取应用所属平台饼状图(忽略版本)'
    #             },
    #             tooltip: {
    #                 pointFormat: '{series.name.percent}: <b>{point.percentage:.1f}%</b><br>{series.name.count}: <b>{point.y}</b><br>'
    #             },
    #             plotOptions: {
    #                 pie: {
    #                     allowPointSelect: true,
    #                     cursor: 'pointer',
    #                     dataLabels: {
    #                         enabled: true,
    #                         color: '#000000',
    #                         connectorColor: '#000000',
    #                         format: '<b>{point.name}</b>: {point.percentage:.1f} %'
    #                     },
    #                     showInLegend: true
    #                 }
    #             },
    #             series: [
    #                 {
    #                     type: 'pie',
    #                     name: {'percent': '百分比', 'count': '应用数'},
    #                     data: eval(data)                    
    #                 }
    #             ]
    #         } 
    #         return           
    # }
    return