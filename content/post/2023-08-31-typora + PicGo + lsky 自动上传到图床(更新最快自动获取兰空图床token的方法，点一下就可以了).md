---
title: "typora + PicGo + lsky 自动上传到图床(更新最快自动获取兰空图床token的方法，点一下就可以了)"
date: "2023-08-31"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "lsky"
  - "picgo"
  - "兰空图床"
  - "图床"
url: "/archives/2556.html"
---

# typora + PicGo + lsky 建立主动上传图片

更新最快自动获取兰空图床token的方法，点一下就可以了

# **简介：**

世界上最让人安心的事情是什么，可能每个人心中都有自己的答案。

但我作为一个`developer`，在大量数据泄露的时代，觉得最重要的还是把数据掌握在自己的手上，最让我安心！

近期写`markdown`，上传图片到`博客`时、本地的图片，无法快速的粘贴到博客等各大平台。

大概便是各个博客的图片是受维护的，不能够复制粘贴。

这就想着自己建立`图床`吧。

本次教程分为两大部分，假如不想自己布置和建立图床，能够直接看第三步。

- 一、在[服务器](https://www.6hu.cc/archives/tag/服务器)或NAS中布置浮屠
- 二、建立图床（能够不建立，自己直接我现已建立好的）
- 三、Typora + PicGo 装备

# 一、建立运转环境

本次建立的图床环境是NAS + docker + 浮屠 + Lsky

因为要比较安稳的条件，自己的黑群晖环境不是很安稳。

我的软路由ikuai openwrt都是安稳122天，而黑群晖只99天安稳运转

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3aaa0cd.webp)\]92830130-db4e159ca2f31e8.webp)

为了确保图床的`7*24`小时能拜访，本次就把图床放在`NAS`上了。

## 1.1 NAS-docker装置布置浮屠

在继续阅览前，主张先了解一下再NAS中怎么布置`浮屠`(www.bt.cn/new/index.h…

我在极空间运用的是kangkang223大佬制造的[镜像](https://www.6hu.cc/archives/tag/镜像)（解决了权限问题）。

hub.docker.com/r/kangkang2…

官网浮屠官网（为什么用浮屠，因为装置各种环境太方便了）

hub.docker.com/r/btpanel/b…

好了正式开端：

1. 拉取镜像
    
    ```bash
    docker pull baotaoserver/bt-nginx:latest
    ```
    
2. 基于镜像创立[容器](https://www.6hu.cc/archives/tag/容器)\-基本设置
    

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3a86e56.webp)\]92830136-e20421f1ed677ed.webp)

3、文件夹途径

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3b1bb33.webp)\]92830142-f6c0072e9ccb9fc.webp)

左面是极空间NAS需求创立的文件夹，右边是容器运转后的目录。

做了映射后，后期能在极空间目录找到文件，方便修正，不用每次都sh进去改。

**需求设置的目录：**

- 备份途径：`/www/backup`
- 容器里面的网站数据目录： `/www/wwwroot`
- MySQL数据目录：`/www/server/data`
- vhost文件途径：`/www/server/panel/vhost`

4、网络装备，这儿挑选`host`， 与宿主机（极空间）运用同一IP，待会去路由器开释`8888`端口，就能够经过外网拜访了。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3ad05be.webp)\]92830148-25da098369c8e3c.webp)

5、点击`使用`，等候容器发动。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3a807ca.webp)\]92830154-60cf7f962f97755.webp)

> 注意：布置完结后，请当即登录浮屠面板—>面板设置中修正用户名和暗码并修正安全进口

## 1.2 浮屠登录及修正暗码

一般装置完结后登录的时分需求经过一个专用进口：

我这儿是加了一个btpanel ，所以经过`192.168.1.60:8888/btpanel`

> 其实不知道也没关系，横竖进入服务器输入bt，能够修正进口和暗码登信息

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3a6fd3d.webp)\]92830160-e8779c02a91bf5b.webp)

默许暗码不知道的情况下，就直接进入sh修正暗码

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3d772dc.webp)\]92830166-21468ab3b93ed21.webp)

```bash
# 输入命令，发动菜单
~bt
# 依据菜单挑选 5修正暗码
~5
# 填入新暗码
~输入新暗码...
齐活
```

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3ea1c2d.webp)\]92830172-0bc0a580cc5b584.webp)

经过进口登录

## 1.3 浮屠装置布置环境

进来后二话不说，先把LNMP环境装一下，因为后面布置`lsky`项目都需求用，这个时间会关键

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3ccd88a.webp)\]92830178-874625e356a59ce.webp)

。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae3f13868.webp)\]92830185-c9760b22d9daaf1.webp)

乘着等候的时间，能够检测一下这个目录文件和NAS的文件映射是否建立

上传一个文件，看看NAS中是否有。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae404250f.webp)\]92830192-3e8ecc62dd20c15.webp)

等候一会后，总算都装好了，确认一下`NGINX`相关服务是不是都发动正常了。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae400813b.webp)\]92830198-9520b9326830042.webp)

假如Nginx发动失利，能够看看日志。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae415aa7e.webp)\]92830204-7bdfe49a5786634.webp)

提示`80端口`占用了

测验修正这儿(..default.conf & phpfpm.status.conf)的端口80改其他的不占用的。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae436124b.webp)\]92830210-d1fe5a56dbe3969.webp)

# 二、布置兰空图床

运用的`兰空图床`www.lsky.pro/

看看官网的教程也能够，也很明晰明了了，我就在烦琐一下吧。

## 2.1 按要求【装置扩展】

官网中写的装置要求逐个核对

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae43558b3.webp)\]92830216-5c81cac3394f3c2.webp)

在浮屠环境中只需求点点点即可

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae473de2f.webp)\]92830223-b7024a051859eb1.webp)

点击**【禁用函数】**，把 `exec`、`shell_exec`、`readlink`、`symlink`、`putenv`、`chown` 这六个被禁用的函数删掉，也便是取消禁用

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae44ad4a9.webp)\]92830229-6a12e6278b8e670.webp)

## 2.2 创立网站

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae45ea134.webp)\]92830235-13bb6d026c14832.webp)

现在经过192.168.8.60:16080 能够拜访到这个空项目了，应该会有个欢迎界面(index.html)。

> 假如需求外网拜访，还需求在[防火墙](https://www.6hu.cc/archives/tag/防火墙)设置端口映射。

\[外链图片转存失利,源站可能有防盗链机制,主张将图片保存下来直接上传(img-j7i3Ra9N-1692342956135)(NAS%E6%90%AD%E5%BB%BA%E5%9B%BE%E5%BA%8A%E6%9C%8D%E5%8A%A1.assets/image-20230817155718521.png)\]

## 2.3 布置兰空图床项目

这是源码地址：

github.com/lsky-org/ls…

打开下载`lsky-pro-2.1.zip`

假如你**不是**开发者，**请不要**下载名称为 `Source Code` 的压缩包，此为中心[源代码](https://www.6hu.cc/archives/tag/源代码)，需求自己装置拓展。

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae471c4e9.webp)\]92830242-b51fa31e35f5844.webp)

下载后放到项目中

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae46f2b85.webp)\]92830248-a95504569133406.webp)

解压一下

1. 将装置包上传至站点目录然后解压，将站点的运转目录指向程序的 `public` 文件夹
    
    > nginx 需求设置伪静态，内容如下
    
    ```js
    location / {
     try_files $uri $uri/ /index.php?$query_string;
    }
    ```
    
2. 将程序地点目录的一切文件夹、子文件夹、文件的权限，用户组和一切者改为 `www`，权限改为 `0755`
    
    > 通常情况下，Web 站点目录的一切者和用户组为 `www:www`
    

项目就能够运转了。

装备好域名今后，拜访站点 **主页** ，程序会主动跳转至装置页面，环境检测经过今后即可经过引导进行装置。

**在开端之前，我自己建立的图床img.deepe.ren，自己注册账号，然后用自己的token，这样图片便是隐私的。**

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae475f412.webp)\]92830255-b784f9bb4bc2cc1.webp)

# 三、typora + PicGo + lsky 建立主动上传图片

效果演示：

PicGo拖文件上传

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4918df9.webp)\]92830261-ba059fb06e74297.webp)

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4903bc7.webp)\]92830269-9c2b0a3f34c5c82.webp)

Typora拖转主动转化

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae49c5c91.webp)\]92830277-e1e443099cb3c87.webp)

## 3.1、装置PicGo插件

**打开`Typroa`界面，在菜单栏找到`文件`—>`偏好设置`**

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4b52071.webp)\]92830284-4013c027dde7ddb.webp)

在

点击PicGo(app)装置

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4b5dfd6.webp)\]92830290-bab92566f7d4ca5.webp)

然后点击下面的下载，等候一会…

> 特别提醒：装置的时分记得将**装置途径**存起来，后面要用

## 3.2 在PicGo装置lankong的插件

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4c1fc8f.webp)\]92830296-fbdc8b92c388f73.webp)

## 3.3 装备lankong

```json
// 版本挑选 V2
Lsky pro version:V2
// 服务器填入 
Server：https://img.deepe.ren
// 验证token (要依据自己账号获取)
Auth token：Bearer 1|hCKcAdIFxxxxxxxxxxxxxxxxxxIvSqJZ7q
```

装备完结：

![image-20230831232300077](https://img-cloud.zhoujie218.top/2023/08/31/64f0b0561832b.webp)

#### 3.3.1 怎么获取token

在浏览器中打开**LskyPro管理界面**（前面建立的）`https://img.deepe.ren`，找到获取`tokens接口`、`upload上传接口`：

```arduino
https://img.deepe.ren/api/v1
```

\[外链图片转存失利,源站可能有防盗链机制,主张将图片保存下来直接上传(img-j6jPSmBC-1692342956138)(C:/Users/xiaozepeng/AppData/Roaming/Typora/typora-user-images/image-20230818110323536.png)\]

经过`tokens接口`获取token，下面`email` `password`填写自己的账号暗码

\[外链图片转存失利,源站可能有防盗链机制,主张将图片保存下来直接上传(img-U1Z6uBrq-1692342956139)(C:/Users/xiaozepeng/AppData/Roaming/Typora/typora-user-images/image-20230818135529177.png)\]

获取到的token: `2|hCKcAdIF38tEBlxxxxxxxxxxxxxxxxxxxxxxxx6W1IvSqJZ7q`

然后依据文档在前面要参加前缀 `Bearer`

\[外链图片转存失利,源站可能有防盗链机制,主张将图片保存下来直接上传(img-PjcVIxC9-1692342956139)(C:/Users/xiaozepeng/AppData/Roaming/Typora/typora-user-images/image-20230818135641245.png)\]

回到lankong装备填上结果。

## 这里有快速的方法

添加代码 直接在 /resources/views/common/api.blade.php 文件里合适的位置添加以下代码

```
<div>
                <p class="text-lg text-gray-700 font-semibold">Tonken获取</p>
                <script src="//lib.baomitu.com/jquery/1.12.4/jquery.min.js"></script>
                <form id="token" action="{{ request()->getSchemeAndHttpHost() }}/api/v1/tokens" method="POST">
                    <div class="my-2 text-sm">
                        <div class="form-group qqlogin" style="display: none;">
                            <div class="input-group-addon">邮箱</div>
                            <input type="email" id="email" name="email" value="{{ Auth::user()->email }}">
                        </div>
                        <div style="display: inline-flex;position: relative;">
                            <div class="px-4 py-3 text-right sm:px-6" style="color: #555;background-color: #eee;border: 1px solid #ccc;">密码</div>
                            <input type="password" id="password" name="password" placeholder="输入你的密码">
                            <a href="javascript:;" class="button px-4 py-3 sm:px-6" style="color: #fff;background-color: #337ab7;border-color: #2e6da4;margin-left:10px;">
                                <div>点击获取</div>
                            </a>
                        </div>
                        <div class="list-group">
                            <x-code>
                                <span style="color:tomato;user-select: none;">token：</span><span id="tokenCode"></span>
                            </x-code>
                        </div>
                </form>
                <script>
                    $(document).ready(function() {
                        $("#token .button").click(function() {
                            var url = $("#token").attr("action");
                            var email = $("#email").val();
                            var password = $("#password").val();
                            $.ajax({
                                type: 'post',
                                url: url,
                                data: {
                                    email: email,
                                    password: password
                                },
                                success: function(data) {
                                    if (data.status == true) {
                                        $("#tokenCode").html('Bearer ' + data.data.token)
                                    } else {
                                        if (data.message == "password 不能为空。") {
                                            $("#tokenCode").html("密码不能为空！")
                                        } else if (data.message == "The email address or password is incorrect.") {
                                            $("#tokenCode").html("请确认密码是否正确！")
                                        }
                                    }
                                },
                                error: function() {
                                    $("#tokenCode").html("请求过于频繁，请稍后再试！")
                                }
                            });

                        });
                    });
                </script>
            </div>
```

添加位置 刷新后台 建议使用强制刷新Ctrl+F5

![image-20230831231857987](https://img-cloud.zhoujie218.top/2023/08/31/64f0af643fcab.webp)

![](https://img-cloud.zhoujie218.top/2023/08/31/64f0af2a10f5b.webp)

## 效果

![image-20230831231953139](https://img-cloud.zhoujie218.top/2023/08/31/64f0af9b496a5.webp)

## 3.4 PicGo测验上传

拖个图片测验一下

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4c10441.gif)\]92830308-e6ddee438375b8a.gif)

## 3.5 Typora装备

装备的当地挑选`PicGo(app)`复制picGo装置途径下的`PicGo.exe`途径

我的装置途径`C:\Users\xiaozepeng\AppData\Local\Programs\PicGo`

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4d1a27c.webp)\]92830327-dd8507495903777.webp)

typora拖图片测验

\[![NAS + 宝塔 + typora + PicGo + lsky 搭建自动上传图片](https://img-cloud.zhoujie218.top/2023/08/31/64f0ae4ea55a4.webp)\]92830339-9357ffeb3b387b6.webp)

这样上传的图片是在云端，后续发布在`掘金` `csdn` `社区` 就再也需求手动上传了。
