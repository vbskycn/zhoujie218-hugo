---
title: "群晖NAS安装Transmission并替换TWC增强中文界面"
date: "2019-03-09"
categories: 
  - "diannaowangruo"
tags: 
  - "群晖"
url: "/archives/580.html"
---

群晖如何使用BT下载，那就使用Transmission，它是BitTorrent客户端的一种，是一个跨平台的后端程序，用户界面简洁。

具体安装方法如下：

一、首先安装Transmission这个BT下载程序。

1、进入群晖点击套件中心--设置--套件来源，点新增添加一个源：[](http://packages.synocommunity.com/)[http://packages.synocommunity.com/](http://packages.synocommunity.com/) 后保存。

![1.jpg](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-f3cc154123534420190309-2.jpg "点击查看原图")

2、然后点击左侧社群，等待软件刷新出来，然后上方搜索后点击安装，完成后设置。

![2.jpg](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-1560154123583220190309-2.jpg "点击查看原图") ![3.jpg](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-799b154123590320190309-2.jpg "点击查看原图")

3、按照以上2张图设置后下一步即可完成Transmission的安装，然后就可以用群晖IP:9091进行访问。

二、再安装TWC增强中文界面，中文增强界面有好几种安装方式，这里介绍2种常用方法。项目地址是：[](https://github.com/ronggang/transmission-web-control，界面欣赏)[https://github.com/ronggang/transmission-web-control，界面欣赏](https://github.com/ronggang/transmission-web-control，界面欣赏)

![6.png](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-f19c154123698720190309-2.png "点击查看原图")

1、通过群晖SSH终端安装：

a、确认开启SSH功能。

![4.png](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/09dd154123654520190309-2.png "点击查看原图")

b、终端使用以root用户登录到你的系统- ，脚本以下假设你已经使用root用户;（方法自行搜索） 记住当前路径（如/ volume1 /），以后用到，因为wget下载的文件会保存到当前目录; **获取最新的安装脚本：** wget [](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh)[https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh) 请留意执行结果，如果出现install-tr-control-cn.sh.1之类的提示，表示文件已存在，请使用 rm install-tr-  control-cn.sh\*删除之前的脚本再重新执行上面的命令; 如果提示https电子杂志失败，请使用以下命令获取安装脚本： wget [](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh)[https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh) --no-check-certificate 如果提示文件已存在，通过可以rm install-tr-control-cn.sh进行删除后再执行下载;在或者wget后面添加-N参数，如： wget -N [](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh)[https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh) --no-check-certificate c、执行安装脚本 执行安装脚本（系统-如果不请立即获取iTunes bash命令，尝试请将bash对划线sh）： bash install-tr-control-cn.sh 出现如果Permission denied之类的提示，表示没有权限，可尝试添加执行权限： chmod +x install-tr-control-cn.sh 如果命令成功执行，将出现以下界面：

![5.png](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-8266154123678720190309-2.png "点击查看原图")

安装-TR-控制-CN 按照提示，输入相应的数字，按回车即可; 如果无法正常显示中文，请尝试设置SSH客户端编码为UTF-8 安装完成后，用浏览器访问Transmission Web Interface（如：http：//192.168.1.1：9091 /）即可看到新的界面;如果无法看到新界面，可能是浏览器缓存了，请按Ctrl + F5强制页面刷新或清空缓存后再重新打开。

2、通过群晖的“任务计划”自动安装及定期自动更新，该方法可以实现全程自动安装及更新，而无需使用其他工具；

a、下载最新的安装脚本 从以下地址下载最新的安装脚本； [](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh)[https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh](https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control-cn.sh) 注：安装脚本的版本需要 1.2.0 及以上； 通过 File Station 将安装脚本上传到群晖NAS一个指定目录中，如 /volume1/MyFolder/install-tr-control-cn.sh；

b、设置脚本文件的执行权限 默认下载的脚本没有执行权限，通过任务计划无法执行，所以需要设置权限； 通过 File Station 将安装脚本 install-tr-control-cn.sh 设置为可 运行 ，请确认设置后的结果为： 如果以后重新下载了安装脚本，需要重新设置权限；

![9.jpg](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-30e6154123774320190309-2.jpg "点击查看原图")

c、创建任务计划 依次打开 DSM 的 “控制面板” -> “任务计划”； 选择 “新增” -> “计划的任务” -> “用户定义的脚本” ； 任务名称用英文，如：AutoUpdateTrWebControl，用户帐号选择 root 并选中 已启动；

![8.png](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-602e154123735720190309-2.png "点击查看原图")

计划时间可根据自己需要来设置，如想保持最新的版本，可以设置定期执行； 在 “任务设置” 的 “运行命令” -> “用户定义的脚本” 中输入：

![9.png](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/03/thum-7afb154123735720190309-2.png "点击查看原图")

脚本最后一定要加入 auto ，要不然脚本不会自动下载；注：auto 前有一个空格；

d、执行任务 任务创建好后就可以执行了，可以手工运行，选中该任务，点击 “运行”，脚本将会自动下载最新的发行版本，执行过程根据网络情况而定，如果不发生错误，过几分钟后就可以访问 [](http://IP:9091)[http://IP:9091](http://IP:9091) 查看结果。
