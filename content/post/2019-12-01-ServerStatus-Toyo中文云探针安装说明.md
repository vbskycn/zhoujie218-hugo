---
title: "ServerStatus-Toyo中文云探针安装说明"
date: "2019-12-01"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "status"
url: "/archives/1002.html"
---

[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/09/unnamed-file-34-1024x286.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/09/unnamed-file-34.png)

[![的GitHub](https://camo.githubusercontent.com/b0224997019dec4e51d692c722ea9bee2818c837/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6d6173686170652f6170697374617475732e737667)](https://camo.githubusercontent.com/b0224997019dec4e51d692c722ea9bee2818c837/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6d6173686170652f6170697374617475732e737667)

- ServerStatus-Toyo版是一个酷炫高逼格的云探针，云监控，服务器云监控，多服务器探针〜，该云监控（云探针）是ServerStatus（[https://github.com/tenyue/ ServerStatus](https://github.com/tenyue/ServerStatus)）项目的优化/修改版。
- 在线演示：[https](https://tz.toyoo.pw/) : [//tz.toyoo.pw](https://tz.toyoo.pw/)
- 我的博客：[https](https://doub.io/shell-jc3/) : [//doub.io/shell-jc3/](https://doub.io/shell-jc3/)

# [](https://github.com/vbskycn/ServerStatus-Toyo#%E7%9B%AE%E5%BD%95%E4%BB%8B%E7%BB%8D)目录介绍：

- 客户客户端文件
- 服务器服务端文件
- 网站文件

# [](https://github.com/vbskycn/ServerStatus-Toyo#%E6%9B%B4%E6%96%B0%E8%AF%B4%E6%98%8E)更新说明：

- 2018.08.21，修改新样式，效果见[https://tz.toyoo.pw](https://tz.toyoo.pw/)
- 2017.10.12，负载优化，并支持CentOS6系统
- 2017.10.10，修改负载的增量：当前服务器上链接SSR等软件的IP总和（只要软件监听IPv6那么就能统计，例如SSH）
- 2017.04.30，优化手机显示式样
- 2017.04.29，移除主机名设定
- 2017.04.27，增加一键部署脚本

# [](https://github.com/vbskycn/ServerStatus-Toyo#%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B)安装教程：

[http://www.nbdog.com/8364.html](http://www.nbdog.com/8364.html)

bash <(curl -s -L https://git.io/v2ray.sh)

如果提示 curl: command not found ，那是因为你的小鸡没装 Curl
ubuntu/debian 系统安装 Curl 方法: `apt-get update -y && apt-get install curl -y` centos 系统安装 Curl 方法: `yum update -y && yum install curl -y` 安装好 curl 之后就能安装脚本了

执行下面的代码下载并运行脚本。

wget -N --no-check-certificate https://softs.loan/Bash/status.sh && chmod + x status.sh

＃如果上面这个脚本无法下载，尝试使用备用下载： 
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/status.sh && chmod + x status.sh

下载脚本后，根据需要安装客户端或服务端：

＃显示客户端管理菜单
bash status.sh c

＃显示服务端管理菜单 
bash status.sh

运行脚本后会出现脚本操作菜单，选择并输入`1`就会开始安装。

一开始会提示你输入网站服务器的域名和端口，如果没有域名可以直接回车代表使用 `本机IP:8888`

## [](https://github.com/vbskycn/ServerStatus-Toyo#%E7%AE%80%E5%8D%95%E6%AD%A5%E9%AA%A4)简单步骤：

首先安装服务端，安装过程中会提示：

是否由脚本自动配置HTTP服务（服务端的在线监控网站）\[Y / n\]

＃如果你不懂，那就直接回车，如果你想用其他的HTTP服务自己配置，那么请输入Ñ并回车。
＃注意，当你曾经安装过服务端，同时没有卸载球童（HTTP服务） ，那么重新安装服务端的时候，请输入n并回车。

然后添加或修改初始示例的例程配置，注意用户名每个例程配置都不能重复，其他的参数都无所谓了。

然后安装客户端，根据提示填充服务端的IP和前面添加/修改对应的RPC用户名和密码（用于和服务端验证），然后启动就好了，有问题请贴出详细步骤+日志（如果有）联系我。

# [](https://github.com/vbskycn/ServerStatus-Toyo#%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)使用说明：

进入下载脚本的目录并运行脚本：

＃客户端管理菜单
./status.sh c
＃服务端管理菜单 
./status.sh小号

然后选择你要执行的选项即可。

ServerStatus一键安装管理脚本\[vx.xx\]
-东洋| doub.io/shell-jc3-

0.升级脚本
————————————
1.安装服务端
2.卸载服务端
————————————
3.启动服务端
4.停止服务端
5.重新启动服务端
————————————
6.设置服务端配置
7.查看服务端信息
8.查看服务端日志
————————————
9.切换为客户端菜单

当前状态：服务端已安装并已启动

请输入数字\[0-9\]：

# [](https://github.com/vbskycn/ServerStatus-Toyo#%E5%85%B6%E4%BB%96%E6%93%8D%E4%BD%9C)其他操作

### [](https://github.com/vbskycn/ServerStatus-Toyo#%E5%AE%A2%E6%88%B7%E7%AB%AF)客户端：

启动：服务状态-客户启动

停止：服务状态-客户端停止

重启：服务状态-客户端重启

查看状态：服务状态-客户状态

### [](https://github.com/vbskycn/ServerStatus-Toyo#%E6%9C%8D%E5%8A%A1%E7%AB%AF)服务端：

启动：服务状态服务器启动

停止：服务状态-服务器停止

重启：服务状态-服务器重启

查看状态：服务状态-服务器状态

### [](https://github.com/vbskycn/ServerStatus-Toyo#caddyhttp%E6%9C%8D%E5%8A%A1)球童（HTTP服务）：

启动：服务盒启动

停止：服务车停

重启：服务盒重启

查看状态：服务车状态

球童配置文件：/ usr / local / caddy / caddy

默认脚本只能一开始安装的时候设置配置文件，更多的Caddy使用方法，可以参考这些教程：[https](https://doub.io/search/caddy) : [//doub.io/search/caddy](https://doub.io/search/caddy)

——————————————————————————————————————

安装目录：/ usr / local / ServerStatus

网页文件：/ usr / local / ServerStatus / web

配置文件：/usr/local/ServerStatus/server/config.json

客户端查看日志：tail -f tmp / serverstatus\_client.log

服务端查看日志：tail -f /tmp/serverstatus\_server.log

# [](https://github.com/vbskycn/ServerStatus-Toyo#%E5%85%B6%E4%BB%96%E8%AF%B4%E6%98%8E)其他说明

网络实时流量单位为：G = GB / s，M = MB / s，K = KB / s

服务器总流量单位为：T = TB，G = GB，M = MB，K = KB

### [](https://github.com/vbskycn/ServerStatus-Toyo#centos7%E7%B3%BB%E7%BB%9F-%E8%B4%9F%E8%BD%BD%E6%98%BE%E7%A4%BA%E5%BC%82%E5%B8%B8%E7%9A%84%E9%97%AE%E9%A2%98)CentOS7系统负载显示异常的问题

CentOS7系统默认可能没有安装netstat依赖，因此会造成IP检测（负载）错误，手动安装即可： `yum install net-tools -y`

# [](https://github.com/vbskycn/ServerStatus-Toyo#%E7%9B%B8%E5%85%B3%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%E6%84%9F%E8%B0%A2)相关开源项目，感谢：

- ServerStatus：[https](https://github.com/BotoX/ServerStatus) : [//github.com/BotoX/ServerStatus](https://github.com/BotoX/ServerStatus)
- mojeda：[https](https://github.com/mojeda)：[//github.com/mojeda](https://github.com/mojeda)
- mojeda的ServerStatus：[https](https://github.com/mojeda/ServerStatus) : [//github.com/mojeda/ServerStatus](https://github.com/mojeda/ServerStatus)
- BlueVM的项目：[http](http://www.lowendtalk.com/discussion/comment/169690#Comment_169690) : [//www.lowendtalk.com/discussion/comment/169690#Comment\_169690](http://www.lowendtalk.com/discussion/comment/169690#Comment_169690)
