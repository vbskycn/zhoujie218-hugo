---
title: "使用宝塔安装Auxpi图床程序 并设置ShareX自定义上传"
date: "2019-10-28"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
url: "/archives/849.html"
---

## 简介

Aupxi 是一个集合多家图床 API 的图床程序，可以将图片上传至京东图床、头条图床、搜狐图床、苏宁图床、小米图床、网易图床、掘金图床等等一系列图床，当然也支持上传到本地服务器。

更重要的是，作者提到此图床一个重要功能，就是能够进行图片分发，大概意思就是，当你上传一张图片时，程序会按照各个图床的权重大小，将这一张图片上传到各个图床，当某一个图床挂了之后，会自动跳转到其他正常的图床，保证图片显示正常。

更详细的介绍可以看这里：[](https://www.v2ex.com/t/560833)[https://www.v2ex.com/t/560833](https://www.v2ex.com/t/560833)

不过，要实测需要在后台上传到有分发功能，而且实际上似乎并没有分发……可能有待作者以后完善

项目地址：[](https://github.com/aimerforreimu/auxpi)[https://github.com/aimerforreimu/auxpi](https://github.com/aimerforreimu/auxpi)

官方演示站：[](https://test.demo-1s.com/)[https://test.demo-1s.com/](https://test.demo-1s.com/)

## 安装

![](/images/2019/10/a21d19dd716ddb9fbdd1040cb4cf3324.png)

#### 安装宝塔

首先安装宝塔面板，根据 VPS 系统选择相应命令进行安装：

Centos 系统安装命令：

```
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh
```

Ubuntu/Deepin 系统安装命令：

```
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh
```

Debian安装命令：

```
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && bash install.sh
```

更详细的宝塔安装教程，可查看以下文章：

建站之路 | 宝塔面板安装使用新手教程

建站之路系列很久没更新，主要是没人看，懒得写。不过很久没写文章，也不知道写什么，所以就继续写。本文为新手详细介绍如...

宝塔安装完成后，打开宝塔面板，安装环境。项目 WIKI 里建议的环境为 Nginx + Mysql(5.6) + PHP + phpMyAdmin

#### 创建站点

如下图：

![uud.me-1559046365.jpg](/images/2019/10/689f7d6f64b1ad101b9266e316a8cf5f.jpg "uud.me-1559046365.jpg")

注意选择 **伪静态**

#### 开启SSL（可选）

建议开启，自行设置即可

如下图：

![uud.me-1559046832.jpg](/images/2019/10/fd66d91c3223deb64ffe4fc2c2405e1c.jpg "uud.me-1559046832.jpg") ![uud.me-1559046973.jpg](/images/2019/10/8a4c66922425f546f3dadcf3ce8ac639.jpg "uud.me-1559046973.jpg")

#### 设置反向代理

如下图：

![uud.me-1559047090.jpg](/images/2019/10/8cac7155686898c90e6bafd853b7458d.jpg "uud.me-1559047090.jpg")

注意需要**关闭缓存**

![uud.me-1559047141.jpg](/images/2019/10/f1b1e19dbc26e5b2257dc8f0bb4aefa5.jpg "uud.me-1559047141.jpg")

目标URL填写为 [](http://127.0.0.1/)[http://127.0.0.1](http://127.0.0.1):2333

填写完毕后点击提交

提交后，点击**配置文件** 进行修改：

![uud.me-1559047243.jpg](/images/2019/10/2f021b1d387bea63075ce994204b37ee.jpg "uud.me-1559047243.jpg")

删除红框中的内容：

![uud.me-1559047336.jpg](/images/2019/10/94e56230c55f8b8991eb075f27ef35f1.jpg "uud.me-1559047336.jpg")

#### 下载图床程序

回到 VPS 的远程连接窗口，输入如下命令下载程序：

```
wget -N --no-check-certificate https://raw.githubusercontent.com/aimerforreimu/AUXPI/dev/install.sh && chmod +x install.sh && bash install.sh install
```

见到如下显示，即下载完成，并且已经自动初始化

- ![uud.me-1559048538.jpg](/images/2019/10/620870d7fa25b30c347e42c5587efa33.jpg "uud.me-1559048538.jpg")

#### 创建数据库

回到宝塔面板，创建数据库：

![uud.me-1559048716.jpg](/images/2019/10/1c951c297893e8a9421f9592239aaa9e.jpg "uud.me-1559048716.jpg")

填写好数据库名、数据库用户名、密码，待会要用

#### 修改配置文件

修改 `/root/auxpi/conf`目录下的 `siteConfig.json`文件，填写刚刚创建的数据库信息

```
"db_option": {
    "use_db": true,     
    "db_type": "mysql",       
    "db_host": "127.0.0.1:3306",    #数据库地址，正常不需要修改
    "db_name": "auxpi",             #数据库名称
    "db_user": "root",              #数据库用户名
    "db_pass": "root",              #数据库密码
    "table_prefix": "auxpi_"        #数据表前缀，可不修改
  },
```

然后，再次修改 `/root/auxpi/conf`目录下的 `app.conf`

这里是项目WIKI里没有提到的关键步骤，如果只是修改 `siteConfig.json`文件里的数据库信息之后就进行数据库迁移，会提示错误：**\[ERROR\]:ql: database is closed ===>\[main.go:60\]**

打开`app.conf`，找到以下部分，同样填写创建的数据库信息：

![uud.me-1559049494.jpg](/images/2019/10/76e8343ee4ba265bfb56aa7e34535fe9.jpg "uud.me-1559049494.jpg")

#### 迁移数据库

回到 VPS 会话窗口，输入如下命令：

```
cd /root/auxpi
./auxpi migrate
```

看到 **\[INFO\]: Migrate done** 即代表迁移完成

#### 创建管理员账号

在程序的根目录，输入以下命令创建管理员账号：

此命令含义为创建 密码为 [code>123123123 用户名为:`hello` 邮箱为: `auxpi@0w0.tn`](mailto:code>123123123</code> 用户名为:<code>hello</code> 邮箱为: <code>auxpi@0w0.tn</code)

[`

自行修改

```
./auxpi -mod=admin -name=hello -email=auxpi@0w0.tn -pass=123123123 
```

#### 运行程序

安装至此已经基本完成，为了保证程序在关闭远程连接后继续运行，需要安装 Screen 命令

运行一下命令安装 Screen

Centos 系统安装命令：

```
yum install screen
```

Ubuntu/Debian系统安装命令：

```
apt install screen
```

安装完成后，输入以下命令：

```
screen -S auxpi

#后台运行
screen -dmS auxpi ./auxpi run
```

然后进入 Auxpi 程序根目录，在程序根目录下输入如下命令运行程序：

```
cd /root/auxpi
./auxpi run
```

如无意外就能看到程序正常运行了，之后按下键盘快捷键 **Ctrl + A + D** 挂起 Screen 会话

## 设置站点

运行成功后，就可以打开站点绑定的域名，进入站点，用之前创建的管理员账号登录后台，界面如下：

![uud.me-1559128673.jpg](/images/2019/10/06dac47fa887a422d411e37d942c7159.jpg "uud.me-1559128673.jpg")

点击右上角用户名，进入个人用户后台，然后再次点击左侧菜单栏的 **后台管理** 进入后台：

![uud.me-1559128737.jpg](/images/2019/10/bf3616fb7b941412630ef489c276ff42.jpg "uud.me-1559128737.jpg")

之后根据需求进行设置：

![uud.me-1559128757.jpg](/images/2019/10/6433289e7a666abfffc759900e3c0682.jpg "uud.me-1559128757.jpg")

如果你想使用 API 配合 ShareX 上传的话，似乎需要关闭 **站点设置** 里的 **API认证**：

![uud.me-1559128854.jpg](/images/2019/10/815e98d06fcff82bca45cb35c1470d5d.jpg "uud.me-1559128854.jpg")

关闭后，记得点击右上角的 **保存**

## 配置ShareX

#### 设置自定义目的地

![uud.me-1559128977.jpg](/images/2019/10/1a900458d84b518732b2785218d59e37.jpg "uud.me-1559128977.jpg")

#### 设置Request

需要填写的内容如下：

![uud.me-1559129098.jpg](/images/2019/10/5b4a389cef88b6b5817e39579dc6cc01.jpg "uud.me-1559129098.jpg")`](mailto:code>123123123</code> 用户名为:<code>hello</code> 邮箱为: <code>auxpi@0w0.tn</code)`[要注意一下第2点的URL，需要换成你自己的域名：](mailto:code>123123123</code> 用户名为:<code>hello</code> 邮箱为: <code>auxpi@0w0.tn</code)[](http://yourname/api/v1/upload)[http://yourname/api/v1/upload](http://yourname/api/v1/upload)

另外需要注意的是，**apiSelect** **的值**需要**注意区分大小写**

#### 设置Response

如下图：

![](/images/2019/10/ca0bf0c5f1b33e5602c2c638615f3380.png) ![](/images/2019/10/6ac929bc79b30f0b570669f60d136999.png)

这里共享一份我的图床服务器

{ "Version": "13.0.1", "Name": "免费聚合图床", "DestinationType": "ImageUploader", "RequestMethod": "POST", "RequestURL": "[https://tu.zhoujie218.top/api/v1/upload](https://tu.zhoujie218.top/api/v1/upload)", "Parameters": { "Text": "$json:data.url$" }, "Headers": { "Authorization": "这里写你自己的id" }, "Body": "MultipartFormData", "Arguments": { "apiSelect": "ali" }, "FileFormName": "image", "URL": "$json:data.url$" }

其中 **URL** 部分，如果需要返回 markdown 格式的链接，则填写 ：

```
![$filename]($json:data.url$)
```

如果只需要链接，则填写：

```
$json:data.url$
```

至此设置完成，更多关于 ShareX 的使用教程，可查看教程：[传送门](https://www.uud.me/site-notes/sharex-picgo-weibo.html#ShareX+PicGo%E8%BF%91%E4%B9%8E%E5%AE%8C%E7%BE%8E%E7%9A%84%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)

如果你需要改更默认首页，只需要在反向代理里面加一句

# PROXY-START/

location / { rewrite ^/$ /Ali last; #加在反向代理里面 proxy_pass [http://127.0.0.1:2333](http://127.0.0.1:2333); proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header REMOTE-HOST $remote_addr; }

# PROXY-END/

这样就可以了

![](/images/2019/10/7d8b69b99e26af5b02862f97640fd492.png)`
