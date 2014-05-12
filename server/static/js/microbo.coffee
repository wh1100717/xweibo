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
            $("#weekweibonum").html("最近一周一共公布了"+data[0]+"个微薄")
            $("#myweibokey").html("<thead><tr><th>我的微薄最近一周的高频词top10</th><th>当前微薄一周热门词汇top10</th></tr></thead><tbody>"+tmp+"</tbody>")

            return
    }
    return
