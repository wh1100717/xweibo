// $(function () { 
//     $('#datatable').highcharts({
//         chart: {
//             type: 'column'
//         },
//         title: {
//             text: '用户微博粉丝转发数及评论数柱状图'
//         },
//         xAxis: {
//             categories: eval(data.screen_name)
//         },
//         yAxis: {
//             title: {
//                 text: '数量'
//             }
//         },
//         series: [{
//             name: '转发数',
//             data: eval(data.reposts_count)
//         }, {
//             name: '评论数',
//             data: eval(data.comments_count)
//         }]
//     });
// });

$(function() {
  $.ajax({
    'type': 'get',
    'contentType': 'application/json',
    'url': '/sina/getfriend',
    'success': function(data) {
        alert(data)
        $('#datatable').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: '用户微博粉丝转发数及评论数柱状图'
        },
        xAxis: {
            categories: eval(data.screen_name)
        },
        yAxis: {
            title: {
                text: '数量'
            }
        },
        series: [{
            name: '转发数',
            data: eval(data.reposts_count)
        }, {
            name: '评论数',
            data: eval(data.comments_count)
        }]
    });
});
