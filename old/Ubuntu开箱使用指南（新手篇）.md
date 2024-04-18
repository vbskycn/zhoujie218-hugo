---
title: "Ubuntu开箱使用指南（新手篇）"
date: "2023-03-06"
categories: 
  - "diannaowangruo"
url: "ubuntu-ok"
---


### Ubuntu20.04开启ssh服务

```
1 安装ssh服务

apt-get install openssh-server

// 开启防火墙ssh的服务端口

ufw allow ssh

// 查看ssh服务状态

systemctl status ssh

// 关闭ssh服务

systemctl stop ssh

// 开启ssh服务

systemctl start ssh

// 重启ssh服务

systemctl restart ssh

// 设置开启自启

sudo systemctl enable ssh

// 关闭开机自启

sudo systemctl disable ssh

```

![image-20230306133954252](https://img.zhoujie218.top/piggo/202303061339729.png)

### 修改root用户ssh登录配置

`nano /etc/ssh/sshd_config`

```
将port 22前面的#去掉
将PermitRootLogin prohibit-password那一行修改为PermitRootLogin yes，去掉前面的#号
```

ctrl+X  保存并退出

修改root用户登录桌面权限

一、设置root用户密码

使用如下命令设置root用户密码，执行命令后，依次输入当前登录用户密码，要设置的root密码，确认root密码

```text
sudo passwd root
```

二、注释如下两个文件的对应行

文件为/etc/pam.d/gdm-password和/etc/pam.d/gdm-autologin，找到如下代码后在文件前面加入#注释，代码为

```text
auth required pam_succeed_if.so user != root quiet_success
```

编辑文件代码如下

```text
sudo nano /etc/pam.d/gdm-autologin
sudo nano /etc/pam.d/gdm-password
```

三、修改profile文件

修改/root/.profile文件，编辑代码如下

```text
sudo nano /root/.profile
```

注释掉或者删除行

```text
mesg n 2＞ /dev/null || true
```

插入新行

```text
tty -s && mesg n || true
```

注意：当没有执行第一步“设置root用户密码”时，/root/.profile文件是不存在的所以对于新安装的系统来说，第一步是非常重要的。



### 一键配置脚本

以下是一键配置脚本，直接新建rootlogin.sh脚本文件，打开后把以下命令粘贴进去然后，运行脚本文件即可。

```
#!/bin/bash
 
#set root password
sudo passwd root
 
#notes Document content
sudo sed -i "s/.*root quiet_success$/#&/" /etc/pam.d/gdm-autologin
sudo sed -i "s/.*root quiet_success$/#&/" /etc/pam.d/gdm-password
 
#modify profile
sudo sed -i 's/^mesg.*/tty -s \&\& mesg n \|\| true/' /root/.profile
 
#install openssh
sudo apt install openssh-server
 
#delay
sleep 1
 
#modify conf
sudo sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
 
#restart server
sudo systemctl restart ssh
```



### 切换root用户  

`sudo -i`



### ubuntu/debian/kali一键更新所有软件

```
更新软件源:
sudo apt update
一键更新所有软件:
sudo apt dist-upgrade
更新软件源并且更新所有软件:
sudo apt update && sudo apt dist-upgrade

```



