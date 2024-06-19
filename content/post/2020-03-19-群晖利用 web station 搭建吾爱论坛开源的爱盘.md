---
title: "群晖利用 web station 搭建吾爱论坛开源的爱盘"
date: "2020-03-19"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
url: "/archives/1528.html"
---

做为个人网盘使用，它是一个非常好的选择，比起\_h5ai更加的优秀 吾爱破解论坛的网盘就是这个，就是他们开源的程序 开源仓库地址：[](https://github.com/ganlvtech/down_52pojie_cn)[https://github.com/ganlvtech/down\_52pojie\_cn](https://github.com/ganlvtech/down_52pojie_cn)

## 特点

- 单页应用
    - 一次性加载，响应迅速
    - 支持通过导航栏定位
    - 支持浏览器前进、后退
- 静态页面
    - 一次性列举出服务器文件列表，之后不用每次都列举文件
    - 服务器支持静态页面即可，可部署与 GitHub Pages
    - 页面可以保存
- 搜索文件
    - 普通搜索
    - 支持模糊搜索
    - 支持正则表达式搜索
- 可以为文件或文件夹添加描述

**注意：**如果你的服务器文件过多，不适合一次性列举出全部文件，那么最好不要使用本应用。

![www.zhoujie218.top.1.2.png](https://ae01.alicdn.com/kf/Hb51414d8d81d4c80a0fad71c004de9017.png "www.zhoujie218.top.1.2.png")

原创教程转载请注明：[](https://www.zhoujie218.top)[](https://www.zhoujie218.top)[https://www.zhoujie218.top](https://www.zhoujie218.top)

**对于大神可能很简单，对于我这种小白还是记录下安装过程中的坑比较好**

**1.扫描文件教程链接没有了** **要修改phpconfigconfig.php 里面的路径,运行phpscan.php才会生成list**

**2.不生成列表文件** **要给目录 http用户群可写权限**

**3.子目录刷新报错** **这个要加默认首页 /index.html,但是在群晖里加比较坑** **因为群晖nginx的配置文件是不确定的，但是我们也有办法，请看下面，共三步**

一，在终端里执行以下命令并找到配置文件内相应的路径（需要root用户） cat /etc/nginx/app.d/server.webstation-vhost.conf

![www.zhoujie218.top.1.png](https://ae01.alicdn.com/kf/Hd866dc5b33c444e0b21b70592720e7f8r.png "www.zhoujie218.top.1.png")

二，因为可能有好几个站点设置，首先确认对应的端口号，然后找到对应的配置文件目录。如上图红框。 执行如下命令（替换下面绿色为你自己刚才找到的目录名）

echo -e "index index.html index.htm index.cgi index.php index.php5 /\_h5ai/public/index.php;" > /usr/local/etc/nginx/conf.d/4433e100-6c59-4121-afcb-dc7a553552ce/user.conf.pan

三，重载web服务 sudo nginx -s reload

刷新你的网站目录，应该就成下面的样子了

![www.zhoujie218.top.1.2.png](https://ae01.alicdn.com/kf/Hb51414d8d81d4c80a0fad71c004de9017.png "www.zhoujie218.top.1.2.png")

[1](https://www.lanzous.com/iafr5pc)
