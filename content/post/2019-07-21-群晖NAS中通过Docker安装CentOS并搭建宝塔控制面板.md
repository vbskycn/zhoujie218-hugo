---
title: "群晖NAS中通过Docker安装CentOS并搭建宝塔控制面板"
date: "2019-07-21"
categories: 
  - "diannaowangruo"
tags: 
  - "bt"
  - "宝塔"
url: "/archives/700.html"
---

群晖NAS中可以在套件中心安装Docker，让原来只是NAS的机器装上Linux Centos系统和Web控制面板

首先用浏览器打开群晖DSM的WEB页面，地址为：ip地址:5000,登陆进去后打开“套件中心”，搜索“Docker”并安装

打开“Docker”，左侧找到“注册表”，搜索“CentOS”，双击第一个的带官方标准和星数量5K的，然后选择标准为“latest”，就是最新版的CentOS 7.6 1809版本，点击选择后，会在左侧“映像”中下载

下载完成群晖右上角的消息有提醒下载已完成，此版本容量大小为202MB

在“映像”页面，选择"centos:latest",然后点击左上角的“启动”，容器名称自定义，不可以有空格，如果有空格请使用这个横杠“-”代替

点击“高级设置”，点击“卷”，点击“添加文件夹”，为了更方便的管理查看备份存储宝塔面板的数据，我这边将宝塔的目录存储在本地的docker文件夹下面的BT-Panel文件夹下面的www文件夹内，无文件夹可以自由添加文件夹，同时桌面的File Station也可以创建和查看文件夹，选择完成后，“转载路径”输入“/www”，意思就是将宝塔控制面板的www文件夹映射搭配本地的docker/BT-Panel/www文件夹内，不操作此步骤则数据都在Docker程序自身目录下

宝塔面板默认有三个端口，控制面板端口8888，http端口80和https端口443，我们这边点击“网络”选项，勾选“使用与Docker Host相同网络”，这里我们就不进行端口映射了，如果有需求，那么左侧为自定义本地地址，右侧分别为宝塔的8888，80，443端口。

配置完成后点击应用

然后点击容器，双击CentOS7或点击后选择左上角的详情，启动容器中的CentOS7终端机

接下来进去宝塔官网，地址为 [](https://www.bt.cn/)[https://www.bt.cn/](https://www.bt.cn/) ，网页中选择Linux版然后点立即安装

找到Linux 面板 安装命令

yum install -y wget && wget -O install.sh [](http://download.bt.cn/install/install_6.0.sh)[http://download.bt.cn/install/install\_6.0.sh](http://download.bt.cn/install/install_6.0.sh) && sh install.sh

复制安装命令，然后进去终端机，先按键盘的Ctrl+A，然后再按Ctrl+V才能粘贴，不然无法粘贴，粘贴完成回车

提示是否安装，输入Y

安装完成后出现地址，输入账号和密码即可正常登陆宝塔面板，默认情况完成后是你的外网ip，改成你的内网ip即可

启宝塔服务，进入宝塔web管理，将php，mysql，apache等服务重新启动，不然可能出现一些未知错误

bt default linux宝塔获取默认账号密码 ，用于忘记登录密码的zz，比如我 history 查看linux历史命令 /etc/init.d/bt start 启动宝塔命令
