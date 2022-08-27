---
title: "群晖利用webstation搭建h5ai教程"
date: "2019-07-23"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "h5ai"
url: "/archives/710.html"
---

设置开启目录浏览 H5AI 的模版

在终端里执行以下命令并找到配置文件内相应的路径 cat /etc/nginx/app.d/server.webstation-vhost.conf

7.1的路径 cat /usr/local/etc/nginx/sites-enabled/server.webstation-vhost.conf

echo -e "index index.html index.htm index.cgi index.php index.php5 /\_h5ai/public/index.php;" > /usr/local/etc/nginx/conf.d/4433e100-6c59-4121-afcb-dc7a553552ce/user.conf.h5ai

将以下两个目录开启777权限 ./software/\_h5ai/private/cache ./software/\_h5ai/public/cache

重载web服务 sudo nginx -s reload

修改模板

notepad ++搜索文件夹 关键字 power 接下来 修改就好 实际就是 ./private/php/pages/index.php info.php ./public/js/scripts.js

h5ai是啥？就是这个http://firmware.koolshare.cn/     [](http://my.zhoujie218.top:8081)[http://my.zhoujie218.top:8081](http://my.zhoujie218.top:8081) 平台, 一般叫做文件目录列表程序。这个是我觉得最赞的一个了。 群晖nginx默认的index文件直接修改重启后会恢复默认（不信你修改后synoservicecfg --restart nginx 试试），自己折腾了一下找到了一个永久修改的方法。这个帖子重点是修改webstation建立的站点默认index文件为h5ai指定格式，其他有此需求的可以也这样操作。 首先选择开放下载的目录并启动站点

![](http://img.zhoujie218.top/wp-content/uploads/2019/07/201647ab2nk5piaxc51ap120190723-1.png)

在终端里执行以下命令并找到配置文件内相应的路径 cat /etc/nginx/app.d/server.webstation-vhost.conf

![](http://img.zhoujie218.top/wp-content/uploads/2019/07/201648q51ulzkn2nsjakj220190723-1.png)

因为可能有好几个站点设置，首先确认对应的端口号，然后找到对应的配置文件目录。如上图红框。 执行如下命令（替换红色为你自己刚才找到的目录名） echo -e "index index.html index.htm index.cgi index.php index.php5 /\_h5ai/public/index.php;" > /usr/local/etc/nginx/conf.d/edb492ad-d4d7-4b98-8727-cf55bbabcde/user.conf.h5ai

到[](https://release.larsjung.de/h5ai/develop/)[https://release.larsjung.de/h5ai/develop/](https://release.larsjung.de/h5ai/develop/)下载最新版的h5ai，并解压到开放下载的目录，目录层级如下图

![](http://img.zhoujie218.top/wp-content/uploads/2019/07/202330f4b941ccgmlm6ogg20190723-1.png)

将以下两个目录开启777权限 ./software/\_h5ai/private/cache ./software/\_h5ai/public/cache

重载web服务 sudo nginx -s reload

http(s)://IP或域名:18081/\_h5ai/public/index.php可以查看 \_h5ai 的全部功能开启情况，默认密码是空的。

http(s)://IP或域名:18081/ 应该能直接打开了，最好修改下\_h5aiprivateconfoptions.json里面的配置内容。 比如搜索定位到"hidden"，添加隐藏目录规则。其他设置参考官方文件说明。 "hidden": \["^.", "^\_h5ai", "^@eaDir"\],

![](http://img.zhoujie218.top/wp-content/uploads/2019/07/201649nrodmdx8r48hdd0720190723-1.png)

同好可以加入TG讨论群t.me/synologyNAS共同探讨分享经验。
