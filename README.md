xweibo
======

###Startup

安装项目运行所需工具

```
#运行项目需要node环境
#进入项目根目录执行
npm install
#如果网络条件不好的话，可以开启goAgent，执行
npm install --proxy http://127.0.0.1:8087
```

安装运行所需库

```
#进入项目根目录执行
bower install
```

执行以下命令启动server，默认端口是80，如需修改，可以在Gruntfile.js中进行配置
```
sudo grunt server
```
