$ ->
    $.ajax {
        'type': 'get',
        'contentType':'application/json',
        'url': '/sina/getfriend',
        'success': (data) ->
            alert(data)
            alert('---')
            data = eval(data)
            # data = JSON.parse(data)
            alert(data[0])

            $('#container').highcharts {
                chart: {
                    type: 'column'
                },
                title:{text:'用户微博转发及评论情况'},
                xAxis: {
                categories: data[0]
                },
            yAxis: {
                title: {
                    text: '数量'                 
                    }
                },
            series: [{                                 
                name: '转发数',                          
                data: data[1]                   
            }, {
                name: '评论数',
                data: data[2]
            }]
            } 
            tmp = ""
            alert(data[0].length)
            for i in [0..(data[0].length-1)]

                    tmp = tmp+"<tr><th>"+data[0][i]+"</th><td>"+data[1][i]+"</td><td>"+data[2][i]+"</td></tr>"
            
            $("#datatable").html("<thead><tr><th>用户昵称</th><th>转发数</th><th>评论数</th></tr></thead><tbody>"+tmp+"</tbody>")    
 
        #         chart: {
        #             type: 'column'                         
        #         },
        #     title: {
        #         text: 'My first Highcharts chart'      
        #         },
            
        # });
            return
    }
    
    # 分类数据饼状图Ajax初始化
    $.ajax {
        'type': 'get',
        'url': '/sina/getfriendsloc',
        'success': (data) ->
            alert(data)
            $('#container-platform').highcharts {
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false
                },
                title:{text:'粉丝地理位置分布'},
                subtitle:{text:'地理位置分布情况饼状图'},
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
                        name: {'percent': '百分比', 'count': '粉丝数'},
                        data: eval(data)
                    }
                ]
            }
            setTimeout ->
                console.log $('.highcharts-contextmenu').html()
            , 2000
            

            return        
    }
    # $.ajax {
    #     'type': 'get',
    #     'contentType':'application/json',
    #     'url': '/sina/getfriend',
    #     'success': (data) ->
    #         data = data.replace(/u"/g,'"')
    #         data = JSON.parse(data)
            
            
    # }
    

    # $("#datatable").dataTable
    # $.ajax {
    #     'type': 'get',
    #     'contentType':'application/json',
    #     'url': '/sina/getfriend',
    #     'success': (data) ->
    #         alert(data)
    #         # data = eval(data)
            
    #         # data = data.replace(/u"/g,'"')
    #         # data = JSON.parse(data)
    #         # alert(date)
    #         # tmp = ""
    #         # for i in data
    #         #     tmp = tmp+"<tr><th>"+i[0]+"</th><td>"+i[1]+"</td><td>"+i[2]+"</td></tr>"
    #         # $("#datatable").html("<thead><tr><th></th><th>转发数</th><th>评论数</th></tr></thead><tbody>"+tmp+"</tbody>")    
    #         # $("#screen_name").html(data.screen_name)
    #         # $("#reposts_count").html(data.Repost_Intimacy)
    #         # $("#comments_count").html(data.Comment_Intimacy)
    #         data = data.replace(/u"/g,'"')
    #         data = JSON.parse(data)
    #         alert(data)
    #         # $("#datatable").dataTable().fnAddData table_data
    #         return
    #     }
    #     return
    

    # #平台数据饼状图Ajax初始化
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