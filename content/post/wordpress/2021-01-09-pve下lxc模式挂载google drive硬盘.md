---
title: "pve下lxc模式挂载google drive硬盘"
date: "2021-01-09"
categories: 
  - "diannaowangruo"
tags: 
  - "rclone"
url: "/archives/1954.html"
---

1、进入母鸡 1.1、以root身份运行 要在母鸡下中获取你的小鸡编号例如：100.conf，请按以下方式编辑100.conf 这里100.conf是你小鸡的编号

root@pve:/etc/pve/nodes/你的host名称/lxc# nano 100.conf

# 最下面加入

# mp0: /root/gg-web-bak,mp=/webbak

lxc.mount.entry = /dev/fuse dev/fuse none bind,create=file Bash 1.2、重启小鸡 编辑id为100的小鸡，也以root身份运行！

root@e9china.net:~# reboot 然后小鸡执行命令

mknod -m 666 /dev/fuse c 10 229 Bash 1.3、配置rclone rclone教程按照这个做：利用Google Drive的无限网盘做数据定时备份 教程的版本比较老，选择google drive的时候自己留意一下编号！ 结束可以正常使用

2、设置开机启动挂载 上面的命令重启以后不会主动挂载我们想要写个开机挂载

2.1、下载并编辑脚本 使用命令：

wget [](https://zhoujie218.top/soft/rcloned)[](https://zhoujie218.top/soft/rcloned)[https://zhoujie218.top/soft/rcloned](https://zhoujie218.top/soft/rcloned) && nano rcloned 增加内容：

在NAME="webbak" #rclone name ^p^m下面增加一行代码

mknod -m 666 /dev/fuse c 10 229 Bash 修改一下内容：

NAME="" #rclone name名，及配置时输入的Name REMOTE='' #远程文件夹，Google Drive网盘里的挂载的一个文件夹 LOCAL='' #挂载地址，VPS本地挂载目录

2.2、执行

# Debian/Ubuntu 系统

apt-get install sudo -y

# 设置自启

mv rcloned /etc/init.d/rcloned chmod +x /etc/init.d/rcloned update-rc.d -f rcloned defaults bash /etc/init.d/rcloned start 检测信息显示rclone启动成功即可。

2.3、重启小鸡 reboot Bash 重启以后看看里面挂载盘是不是正常挂载和写入！
