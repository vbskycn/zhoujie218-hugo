---
title: "openwrt用dd命令写盘,用命令修改IP"
date: "2020-07-11"
categories: 
  - "diannaowangruo"
tags: 
  - "lede"
  - "openwrt"
url: "/archives/1776.html"
---

此教程适合openwrt不同固件之间的刷机

首先把下载openwrt固件改名称为op.img（提前把固件改个名字）

一、登陆OPENWRT网页后台进到系统里面点文件传输再点选择文件找到你改过名的固件再点上传【其实就是将img文件上传到’_/tmp/upload/_‘文件夹，你也可以用其他方式上传】 二、这里等他上传完了就好了 \[caption id="attachment\_1780" align="alignnone" width="554"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-34.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-34.png) \[/caption\] 三、SSH登陆路由，我用的是putty软件 \[caption id="attachment\_1781" align="alignnone" width="467"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-35.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-35.png) \[/caption\] 四．输入你登陆路由器用户名和密码 Openwrt用户名root密码就是你登陆路由器密码【注意密码这里输入是看不到的】然后回车 输入命令 _ls /tmp/upload_ 回车查看你刚刚上传的固件我这里看到的就是op.img就表示上传成功了 五、开始写盘 输入命令 dd if=/tmp/upload/op.img of=/dev/sda 回车（op.img为固件的名称） 然后是等待刷写，然后出现下面这两排字母表示刷机成功了 1087522+0 records in 1087522+0 records out 然后输入reboot重启路由器就是你全新的固件了和全新写盘一样效果 \[caption id="attachment\_1782" align="alignnone" width="554"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-36.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-36.png) \[/caption\]

**vi /etc/config/network/  直接修改IP**

**ifconfig  接口  IP  临时修改IP**

homelede固件默认IP 192.168.1.1如需要修改 首先，固件启动后，按回车进入命令窗口： 默认用户名root，密码password 在命令行输入： uci set network.lan.ipaddr='192.168.5.1' uci commit network uci delete dhcp.lan.dhcp\_option uci add\_list dhcp.lan.dhcp\_option='6,192.168.5.1' uci commit network 以上192.168.5.1替换成你想改的IP

固件默认用户及密码 固件用户名：root 密码：password

adGuardHome 用户名 root 密码 root adGuardHome不可直接关闭如需关闭请进入web控制台点禁用保护 遇见网站图片缺失先在adGuardHome禁用保护后查看是否恢复
