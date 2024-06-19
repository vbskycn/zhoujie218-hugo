---
title: "centos 挂载 群晖nfs共享木录"
date: "2020-03-25"
categories: 
  - "diannaowangruo"
tags: 
  - "nfs"
  - "rclone"
url: "/archives/1560.html"
---

群辉开启NFS共享

![Centos挂载群辉的NFS共享文件夹](https://img-cloud.zhoujie218.top/pc/202111011325002.jpeg)

在客户端linux系统中安装NFS客户端工具

![点击复制代码](https://www.imhu.cn/zb_users/plugin/Jz52_code/copy.svg) Bash

```bash
yum install nfs-utils -y
```

在linux中检测开启NFS服务的群辉主机IP

![点击复制代码](https://www.imhu.cn/zb_users/plugin/Jz52_code/copy.svg) Bash

```bash
showmount -e 192.168.137.136
[root@node30 ~]# showmount -e 192.168.137.136
Export list for 192.168.137.136:
/volume1/NFSfile *
[root@node30 ~]#
```

创建目录并挂载

![点击复制代码](https://www.imhu.cn/zb_users/plugin/Jz52_code/copy.svg) Bash

```bash
[root@node30 ~]# mkdir /NFSfile
[root@node30 ~]# mount -t nfs 192.168.137.136:/volume1/NFSfile  /NFSfile -o proto=tcp -o nolock
[root@node30 ~]# df -h
Filesystem                        Size  Used Avail Use% Mounted on
/dev/mapper/centos-root            50G  5.6G   45G  12% /
devtmpfs                          897M     0  897M   0% /dev
tmpfs                             912M     0  912M   0% /dev/shm
tmpfs                             912M  9.0M  903M   1% /run
tmpfs                             912M     0  912M   0% /sys/fs/cgroup
/dev/sda1                        1014M  179M  836M  18% /boot
/dev/mapper/centos-home           147G   33M  147G   1% /home
tmpfs                             183M  8.0K  183M   1% /run/user/42
tmpfs                             183M     0  183M   0% /run/user/0
192.168.137.136:/volume1/NFSfile  6.7G  278M  6.4G   5% /NFSfile
[root@node30 ~]#
```
