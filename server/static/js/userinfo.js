// Generated by CoffeeScript 1.7.1
var root;

root = typeof exports !== "undefined" && exports !== null ? exports : this;

$(function() {
  $.ajax({
    'type': 'get',
    'contentType': 'application/json',
    'url': '/sina/getuserinfo',
    'success': function(data) {
      var table_data, tmp;
      alert(data);
      data = eval("(" + data + ")");
      alert(typeof data);
      alert(data);
      table_data = [];
      tmp = [];
      alert(data['idstr']);
      tmp.push(data['idstr']);
      tmp.push(data['screen_name']);
      tmp.push(data['location']);
      tmp.push(data['followers_count']);
      tmp.push(data['friends_count']);
      tmp.push(data['statuses_count']);
      alert(tmp);
      table_data.push(tmp);
      $("#userinfo-list").dataTable().fnAddData(table_data);
    }
  });
});
