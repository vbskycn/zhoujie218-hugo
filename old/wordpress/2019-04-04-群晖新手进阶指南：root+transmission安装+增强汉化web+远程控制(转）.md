---
title: "群晖新手进阶指南：root+transmission安装+增强汉化web+远程控制(转）"
date: "2019-04-04"
categories: 
  - "luanqibazhao"
  - "diannaowangruo"
  - "wangyesheji"
url: "/archives/611.html"
---

**前言：** **自从论坛918+评测之后，最近论坛里群晖的帖子多了好多，没中评测机会，随便写点希望有人需要** **本文面向新手的进阶教程，尤其适合PT新手同时又有群晖的（白的黑的都行）。** **为什么不用群晖自带的download station挂PT？下载BT、PT文件时也用的transmission。** **玩PT的基本不会下载完就删除下载任务的，download station做种时会另外缓存一份，停止做种了才会释放，相当浪费硬盘空间，而原版transmission在用增强汉化web后功能相当强大，再配合手机app、网页端远程控制功能并不比DS get差甚至更好用，另外有些网友有提到download station下载速度没有原版的transmission，挂种子太多后会出问题等等，因此玩PT用transmission更适合。**

**_本文涉及到：_** **_◎root群晖_** **_◎transmission的离线安装_** **_◎transmission增强汉化web的安装_** **_◎路由器设置端口映射_** **_◎transmission远程控制，包括手机端app、移动网页端控制，PC网页端控制_**

**一、Root群晖** 1.在控制面板中打开SSH

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/193700rh3cyysp56763c2220190404-1.jpg)

2.下载putty，链接: [](https://pan.baidu.com/s/1bqL3EPL)[](https://pan.baidu.com/s/1bqL3EPL)[https://pan.baidu.com/s/1bqL3EPL](https://pan.baidu.com/s/1bqL3EPL) 密码: w1tu 打开软件，填入NAS的IP地址，端口22，选择SSH，点Open

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/193808yga4czr8h3rhcytz20190404-1.jpg)

输入群晖admin账号和密码，出现绿色字体的admin@DiskStation（“DiskStation”会根据你设置群晖时输入内容有所不同）

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/193856vvso9tjy5rx5jzxe20190404-1.jpg)

然后输入sudo su -，再次输入admin密码

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/193922ccjddohzrtschjhj20190404-1.jpg)

出现绿色字体root@DiskStation，输入synouser --setpw root root123456，密码改为“root123456”，这个根据自己喜好设置，不建议设置成为群晖登录密码

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/193951wa7cs48vujs6u3l220190404-1.jpg)

到这里已经获取root权限了，并且修改了root密码为“root123456” 现在可以在ssh中用vi命令作相应的修改，但是会vi命令的基本上不需要看本教程，所以有更简单可视化工具适合新手。 3.下载winscp，链接: [](https://pan.baidu.com/s/1bqL3EPL)[](https://pan.baidu.com/s/1bqL3EPL)[https://pan.baidu.com/s/1bqL3EPL](https://pan.baidu.com/s/1bqL3EPL) 密码: w1tu _**注意：本软件在安装transmission中没有用到，不需要的可以忽略以下**_ 打开软件，如图所示更改相应参数，用户名密码为前面设置的root账号密码

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194047mtxlmzbztqz56qml20190404-1.jpg)

这个地方选是就可以

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194145f95ldz293fvysfp020190404-1.jpg)

左侧为本地目录，右侧为群晖目录

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194156nxjx33319m78mjat20190404-1.jpg)

需要编辑某些配置文件，点左键编辑即可，记得改完点保存

**二、安装原版transmission** 从2017年下半年开始群晖很多机型中添加了SynoCommunity后transmission也没有下载了，所以需要离线下载安装，下载地址[](https://github.com/SynoCommunity/spksrc/files/1417690/transmission_apollolake-6.1_2.92-12.spk.zip)[](https://github.com/SynoCommunity)[https://github.com/SynoCommunity](https://github.com/SynoCommunity) ... 6.1\_2.92-12.spk.zip，链接版本适用于18系列的X86构架的群晖（DS218+ DS418play DS718+ DS918+），下载后解压出spk文件。 1.首先新建downloads共享文件夹 在控制面板-共享文件夹，新建downloads文件夹，（文件夹名字根据自己喜好修改）回收站可以不开启

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194328nwc50bei70w5b40q20190404-1.jpg)

接下来是权限设置，很多其他教程是添加everyone权限，个人感觉没必要，先把admin读写权限勾上

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194414acjg0c9jhyxj9h6g20190404-1.jpg)

再切换到“系统内部用户账号”，把sc-transmisson读写权限勾上，这样软件就可以正常下载了

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194421psxxwnwnlwzw62wg20190404-1.jpg)

2.安装transmission 在套件中心选择spk文件，点下一步

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194533ujbz6qg2j8ll8ljl20190404-1.jpg)

选择前面新建的downloads文件夹，后面两项可以不设置

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194547ghs50cscaazkpace20190404-1.jpg)

这里输入transmission的账号密码，默认端口是9091

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194630ijh9hptpshtngpk620190404-1.jpg)

最后点应用就安装完成了

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194647q8r2w11lcel1x1jn20190404-1.jpg)

**三、安装增强汉化web**

更新：作者最近又更新了，推荐【通过群晖的“任务计划”自动安装及定期自动更新】这个方式安装，更方便，还能自动更新 见作者wiki:[](https://github.com/ronggang/transmission-web-control/wiki/Installation-For-DSM-Use-Task-CN)[](https://github.com/ronggang/transmission-web-control/wiki/Installation-For-DSM-Use-Task-CN)[https://github.com/ronggang/transmission-web-control/wiki/Installation-For-DSM-Use-Task-CN](https://github.com/ronggang/transmission-web-control/wiki/Installation-For-DSM-Use-Task-CN)

\================================================= _首先要感谢栽培者(ronggang)、DarkAlexWang两位大神的付出，项目地址_[](https://github.com/ronggang/transmission-web-control)[](https://github.com/ronggang/transmission-web-control)[https://github.com/ronggang/transmission-web-control](https://github.com/ronggang/transmission-web-control) 界面截图（前两天又更新了，支持主题了） ![](http://img.zhoujie218.top/wp-content/uploads/2019/04/194951u4d2xxfyx4y0044g20190404-1.png) 官方功能介绍： **在线查看Transmission当前工作情况；** **在线添加新的种子文件或连接；** **在线修改Transmission参数；** **分页浏览方式加载种子；** **多语言环境支持；** **文件拖放添加种子；** **删除指定的种子；** **批量修改 Tracker；** **移动指定种子的数据存放目录；** **可按 Trackers 分组浏览；** **增加对群晖 Download Station 的支持；By - @hitechbeijing** **其他……** 

1.先在套件中心把transmission关闭 2.打开putty，用root账号密码登录 在终端中输入以下两个命令

1. wget https://github.com/ronggang/transmission-web-control/raw/master/release/install-tr-control.sh

_复制代码_

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/195053iszkvhyxtzlvxxoy20190404-1.jpg)

等前一条命令完成后再执行_（注：如要更新新版，执行此命令即可）_

1. sudo bash install-tr-control.sh

_复制代码_

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/195118ks5fzcbsup4euis420190404-1.jpg)

出现completed即可关闭putty，增强web安装成功，除了增强PC网页控制端，手机网页控制端同样功能有所增强。效果如图，更多功能自己摸索，可视化界面又是中文的，操作很简单

**四、路由器相关设置** 如果想在公司给家里的NAS添加下载任务，想要远程控制下载任务等，这就需要对路由器进行相关设置，推荐使用其他的动态DNS，群晖的QC实在是太慢了，路由器的动态DNS设置在这里就不赘述了，本坛的教程很多。 首先要给群晖固定的IP，就需要在DHCP分配静态IP给群晖，同时最好ARP也绑定一下，这样可以远程唤醒 以koolshare X64版lede为例

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/195335bmhu6uhooo7k67o720190404-1.jpg) ![](http://img.zhoujie218.top/wp-content/uploads/2019/04/195338w8uot6vuoqx9n86u20190404-1.jpg)

在端口转发中打开群晖对应的几个端口，见图片

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/195236er9r2zs7zun9ydwn20190404-1.jpg)

到这里就可以通过外网访问transmission了，如果你在家里测试可以关了WIFI，用手机4G网络，在浏览器中输入：“你的动态DNS二级域名:9091”，就可以打开transmission手机网页控制端页面了。 **五、transmission远程控制** 1、PC网页端控制 经过第四步的设置，在外网通过PC在浏览器中输入：“你的动态DNS二级域名:9091”就可以直接控制transmission，完全和局域网本地操作一样，添加、删除、暂停任务，效果图见第三步截图。 2、手机网页端控制 由于苹果会对app审核，带有bt相关的软件都通不过，所以水果机不越狱现在没有可用的BT控制app，可以使用增强版的网页控制端。效果如下图

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/195534y90n1w1wjjoic94j20190404-1.png)

3、安卓app端控制 安卓推荐使用transdroid，可以官网下载，设置也很简单，同时可以添加多台设置，客户端基本上主流PT软件通杀，seedbox也支持。手机app除了网页端的功能外，还能添加PT站的RSS订阅，下载会方便很多。

![](http://img.zhoujie218.top/wp-content/uploads/2019/04/195604n4hqlsw4q4hvvuuh20190404-1.jpg)

**本文到此结束，有不对的欢迎指正，欢迎回帖讨论**
