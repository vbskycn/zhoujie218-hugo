---
title: "winscp连接vmware ubuntu"
date: "2018-10-21"
categories: 
  - "diannaowangruo"
tags: 
  - "ubuntu"
url: "/archives/563.html"
---

winscp连接vmware ubuntu

windows下通过winscp,putty(ssh) 等连接ubuntu 需安装ssh服务

1、ubuntu桌面版本 默认并没有安装ssh服务，如果通过ssh链接ubuntu，需要自己手动安装ssh-server。判断是否安装ssh服务，可以通过如下命令进行：

$ ssh localhost ssh $ ssh localhost ssh: connect to host localhost port 22: Connection refused 1 2 如上所示，表示没有还没有安装，可以通过apt安装，命令如下：

$ sudo apt-get install openssh-server 1 系统将自动进行安装，安装完成以后，先启动服务：

$ sudo /etc/init.d/ssh start 1 启动后，可以通过如下命令查看服务是否正确启动：

$ ps -e|grep ssh

结果显示为：

1589 ?00:00:00 ssh-agent 2749 ?00:00:00 sshd 2843 pts/000:00:00 ssh 2844 ?00:00:00 sshd 2911 ?00:00:00 sshd 2949 pts/100:00:00 ssh 2950 ?00:00:00 sshd 3015 ?00:00:00 sshd 3272 pts/200:00:00 ssh 3273 ?00:00:00 sshd 3340 ?00:00:00 sshd 3838 ?00:00:00 sshd 3905 ?00:00:00 sshd 1 2 3 4 5 6 7 8 9 10 11 12 13 表明ssh服务已启动了.

2 、设置root用户密码( 可以省略此步骤)

启用root

用sudo passwd root 设置root 用户的密码

用先要求输入普通帐号的密码，然后输入root密码，确认一次。

3查看ubutu (ip)

命令:$ ifconfig

结果:

eth0 Link encap:Ethernet HWaddr 00:0c:29:58:38:46 inet addr:192.168.139.134 Bcast:192.168.139.255 Mask:255.255.255.0 inet6 addr: fe80::20c:29ff:fe58:3846/64 Scope:Link UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1 RX packets:11940 errors:0 dropped:0 overruns:0 frame:0 TX packets:10659 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:1000 RX bytes:12454453 (12.4 MB) TX bytes:1252346 (1.2 MB) Interrupt:19 Base address:0x2024

loLink encap:Local Loopback inet addr:127.0.0.1 Mask:255.0.0.0 inet6 addr: ::1/128 Scope:Host UP LOOPBACK RUNNING MTU:16436 Metric:1 RX packets:1568 errors:0 dropped:0 overruns:0 frame:0 TX packets:1568 errors:0 dropped:0 overruns:0 carrier:0 collisions:0 txqueuelen:0 RX bytes:177890 (177.8 KB) TX bytes:177890 (177.8 KB) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 看到 ip为:192.168.139.134

4 通过 winscp 连接ubuntu

填写 主机名为192.168.139.134 端口默认为22

用户名: **密码:**

## 登录OK

作者：chenxl929 来源：CSDN 原文：[](https://blog.csdn.net/chenxl929/article/details/77802143)[https://blog.csdn.net/chenxl929/article/details/77802143](https://blog.csdn.net/chenxl929/article/details/77802143) 版权声明：本文为博主原创文章，转载请附上博文链接！
