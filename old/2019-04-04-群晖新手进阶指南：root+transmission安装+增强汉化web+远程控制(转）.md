---
title: "群晖新手进阶指南：root+transmission安装+增强汉化web+远程控制(转）"
date: "2019-04-04"
categories: 
  - "luanqibazhao"
  - "diannaowangruo"
  - "wangyesheji"
url: "/archives/611.html"
---

## 1 添加套件源

1.1 用管理员 ad­min 账号登录 DSM 桌面，打开 “套件中心”，点击 “设置” ---> “常规”，选择 “任何发行者”；

![](https://img-cloud.zhoujie218.top/2023/08/ec9d47220bd841f5de548b32984ba3be.jpeg)

1.2 “套件中心”，“设置” ---> “套件来源”，点击 “新增”，位置填入第三方源的网址，完成即可完成第三方源的添加

![](https://img-cloud.zhoujie218.top/2023/08/70bcf7226b338ce3af4674eb1797ae53.jpeg)

第三方源网址：

[https://packages.synocommunity.com](https://link.zhihu.com/?target=https%3A//packages.synocommunity.com) //（建议选择这个，支持HTTPS）  
[http://packages.pcloadletter.co.uk](https://link.zhihu.com/?target=http%3A//packages.pcloadletter.co.uk)  
[http://www.cphub.net](https://link.zhihu.com/?target=http%3A//www.cphub.net)  
[http://synology.sysco.ch](https://link.zhihu.com/?target=http%3A//synology.sysco.ch)  
[http://packages.quadrat4.de](https://link.zhihu.com/?target=http%3A//packages.quadrat4.de)  
[http://synology.acmenet.ru](https://link.zhihu.com/?target=http%3A//synology.acmenet.ru)  
[http://cytec.us/spk](https://link.zhihu.com/?target=http%3A//cytec.us/spk)  
[http://spk.naefmarco.ch/spkrepo/packages/](https://link.zhihu.com/?target=http%3A//spk.naefmarco.ch/spkrepo/packages/)  
[http://spk.nas-mirror.de/spkrepo/packages](https://link.zhihu.com/?target=http%3A//spk.nas-mirror.de/spkrepo/packages)  
[http://spk.unzureichende.info/](https://link.zhihu.com/?target=http%3A//spk.unzureichende.info/)  
[http://packages.synocommunity.com/?beta=1](https://link.zhihu.com/?target=http%3A//packages.synocommunity.com/%3Fbeta%3D1)

1.3 刷新 “套件中心”，找到 “社群”。这个就是第三方源

![](https://img-cloud.zhoujie218.top/2023/08/636aa7851ce672ddce17d7ded81627b0.jpeg)

## 2 安装Transmission

2.1 在 “套件中心” 的 “社群” 找到 “Trans­mis­sion”，点击 “安装套件”，会自动下载安装

![](https://img-cloud.zhoujie218.top/2023/08/9b0f25deed3ac4b1db7c7b2e072d8af7.jpeg)

2.2 Trans­mis­sion 下载设置

Down­load di­irec­tory：下载文件存储目录（设置前需要事先建立好文件夹）

Watch di­rec­tory：保存种子存储目录，留空表示禁用（可以填写下载文件存储目录）

In­com­plete di­rec­tory：未完成下载目录，留空表示禁用（建议不填写，留空）

![](https://img-cloud.zhoujie218.top/2023/08/4f9ec1f204d82b69db906478a93f7135.jpeg)

2.3 设置用户账号和密码（每次进入 TR 需要输入的用户名和密码）

![](https://img-cloud.zhoujie218.top/2023/08/77c381dfdd1d4fe359f661503c0452fd.jpeg)

2.4 权限提示，直接 “下一步”

![](https://img-cloud.zhoujie218.top/2023/08/f88107e341508a6bd9bb4c7ae918c8a9.jpeg)

2.5 安装完成后后，打开 “套件中心” ---> “Trans­mis­sion”，找到 URL，可以直接打开 Web UI（如果你用内网地址安装，则显示内网地址）

![](https://img-cloud.zhoujie218.top/2023/08/8f49964c8aa7dcb306cabc83ec514367.jpeg)

2.6 文件夹权限设置（这个步骤非常重要，否则你的 TR 下载不了）

打开 “控制面板” ---> “共享文件夹” ---> “down­loads”（刚才安装 Trans­mis­sion 创建的下载文件夹名称），点击 “编辑”，选择 “本地群组”，选择 “sc-down­load” 设置为可读写

![](https://img-cloud.zhoujie218.top/2023/08/1a78e3725efffc7c9dde592a47a0445b.jpeg)

打开 “File sta­tion”，“down­loads” 文件夹右击，选择 “属性”，新增 “Every­one” 账号，权限选择 “读取” 和 “写入”，勾上 “应用到这个文件夹、子文件夹及文件”，确定

![](https://img-cloud.zhoujie218.top/2023/08/4308c2198756ae13727cf7a029ae3179.jpeg)

![](https://img-cloud.zhoujie218.top/2023/08/e38106dd63b61a119bef35d8aeb63eca.jpeg)

## 3 完成安装Transmission

3.1 Trans­mis­sion 安装完成后打开界面如下，是英文界面，你可以把它进行汉化

![](https://img-cloud.zhoujie218.top/2023/08/5949a2ec221bebcf6296ba2cd776f355.jpeg)

3.2 首先确认系统已安装 Trans­mis­sion，并且已开启 SSH 功能：

![](https://img-cloud.zhoujie218.top/2023/08/0a4a0fe2e93cb833e78f79caa562a410.jpeg)

* * *

> 接下来4-5是汉化方案1，通过Putty更新的  
> 6是汉化方案2，通过cmd更新的（个人推荐此方案，更简洁）  
> 可以任选一个

* * *

**4 通过Putty获取ROOT权限**

此处参考如下教程：

[群晖NAS教程第十九节www.ptyqm.com/27850.html](https://link.zhihu.com/?target=http%3A//www.ptyqm.com/27850.html)

4.1 使用putty登陆群晖，没有这个软件的先下载一个。

**putty下载链接：** [https://pan.baidu.com/s/1EfOsWFlnOiRWASoZAG6vuA](https://link.zhihu.com/?target=http%3A//www.ptyqm.com/wp-content/themes/begin/go.php%3Furl%3DaHR0cHM6Ly9wYW4uYmFpZHUuY29tL3MvMUVmT3NXRmxuT2lSV0FTb1pBRzZ2dUE%3D)，提取码：zmwv

打开putty，在主机名称输入群晖的局域网IP地址，然后点击下面的【打开】。

![](https://img-cloud.zhoujie218.top/2023/08/33004de3b722d42c377306355037d915.jpeg)

4.2 弹出一个黑色的窗口，输入管理员账号：admin，按回车，然后输入admin的密码，要注意的是，输入密码的时候，光标是不会动的，你尽管输就行。

![](https://img-cloud.zhoujie218.top/2023/08/0d201601b75210512950a5d41109332a.jpeg)

4.3 切换到root权限。输入"sudo su -"，按回车，然后也是输入admin的密码。

![](https://img-cloud.zhoujie218.top/2023/08/0d9a2b96570268abad2bde32423b12d6.jpeg)

**5 进行汉化Transmission**

5.1 在Putty的root状态中，继续输入如下内容，指令执行完毕后如下图：

wget [https://gitee.com/zgrm/transmission-web-control/raw/master/release/install-tr-control-cn.sh](https://link.zhihu.com/?target=https%3A//gitee.com/zgrm/transmission-web-control/raw/master/release/install-tr-control-cn.sh)

![](https://img-cloud.zhoujie218.top/2023/08/6a11c658dea348b997f6ca4439037e30.jpeg)

5.2 继续输入下面这句执行指令，成功的话，会弹出下图：

bash install-tr-control-cn.sh

![](https://img-cloud.zhoujie218.top/2023/08/9e7dbb3a87be52b40f73078659d063e1.jpeg)

记住：这个时候，进入群晖套件，启动Transmission套件

启动完成后，在返回Putty，输入数字时候，选择1，回车

然后看到下图的“结束”，就证明汉化完成了

![](https://img-cloud.zhoujie218.top/2023/08/ca109ca0732e7d50c56cbbad500f15c0.jpeg)

5.3 汉化完成界面

如下，开心不！~~~

![](https://img-cloud.zhoujie218.top/2023/08/51c123b00e16cb65055169966c8be1df.jpeg)

**6** 另一个汉化方法（该方法在2022年6月25日刚运行成功）

6.1 上面的第3步做完后，将trans套件关闭，然后直接在电脑上进入shh

[HHUI：小白教程：如何SSH进入NAS管理4 赞同 · 2 评论文章](https://zhuanlan.zhihu.com/p/399394743)

进入后获取到root权限

6.2 然后输入：

wget [https://www.huakings.cn/mp202003/install-tr-control-cn.sh](https://www.huakings.cn/mp202003/install-tr-control-cn.sh)

运行得到下方的结果

![](https://img-cloud.zhoujie218.top/2023/08/084e4d7eda7511d7892992ef5d55ba43.jpeg)

6.3 再输入：

chmod +x install-tr-control-cn.sh

6.4 这时候没有反应，再输入：

bash install-tr-control-cn.sh

运行得到下方的结果

![](https://img-cloud.zhoujie218.top/2023/08/ec48865d0e10b90b9b62724b7d593bf5.jpeg)

6.5 此时，看到1-9的选项，就成功一大半了，先不要做操作；回到NAS套件，启动trans套件

然后再输入1，回车

![](https://img-cloud.zhoujie218.top/2023/08/db83a7b511edd354759c1ded9c6f3cfb.jpeg)

看到这个界面，就成功了

6.6 打开你的trans网页端，如果界面还没变化，就Ctrl+F5强制刷新，就看到美美的中文界面了

![](https://img-cloud.zhoujie218.top/2023/08/ec99434aa90179b10da524d009ec43a6.jpeg)
