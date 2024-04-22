---
title: "centos服务器安装rclone自动挂载无限容量谷歌相册Google photo为磁盘"
date: "2019-12-10"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "rclone"
url: "/archives/1042.html"
---

经常听说有人撸到无限容量的谷歌网络硬盘，或者是 5T 容量的，都是利用学生认证实现的，现在淘宝上也有一大堆，但是感觉这种都不一定稳，随时可能翻车，我自己是用的 **google** drive 个人版的免费 15G 空间，其实也够用了，可以**挂载**到服务器上，当一个普通的本地磁盘样操作，多 15G 随便放点什么都好，还稳定，不怕翻车，**挂载**主要通过 **RCLONE** 这个软件实现，需要服务器或者至少 KVM 架构的 VPS，因为需要用到 FUSE，而一般 OPENVZ 架构是不开启这个功能的，教程如下：

本教程基于 CENTOS 系统

1、安装 EPEL 源（这一步国外 VPS 一般可不用操作）:

```
yum -y install epel-release
```

2、安装一些基本组件和依赖:

```
yum -y install wget unzip screen fuse fuse-devel
```

3、下载 **Rclone** 解压然后进入目录:（64 位系统就下载 **rclone**\-current-linux-amd64.zip，32 位系统就下载 **rclone**\-current-linux-386.zip 替换下面代码中的链接就行了）

```
wget https://downloads.rclone.org/rclone-current-linux-amd64.zip 
unzip rclone-current-linux-amd64.zip
cd rclone-v*
```

注意`cd **rclone**-v*`这一步如果系统执行出错，你可以输入`ls`命令查看一下具体目录名，因为这个是使用最新版本，版本号不一定一样,然后根据真实的目录cd 进去一下

4、接下来运行 **Rclone** 开始配置:

```
./rclone config
```

5、第一步选择 n （n 为新建配置）

```
e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> n
```

6、然后回车输入一个 name,建议这个 name 设置的简单好记一点,比如我们这边叫 gp，这个下面**挂载**磁盘时会用到如下所示:

```
name> gp
```

7、下面选择**挂载**类型-谷歌相册，数字顺序可能会变，记得选 **Google** Photos 的项目

```
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
    "fichier"
 2 / Alias for an existing remote
    "alias"
 3 / Amazon Drive
    "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
    "s3"
 5 / Backblaze B2
    "b2"
 6 / Box
    "box"
 7 / Cache a remote
    "cache"
 8 / Dropbox
    "dropbox"
 9 / Encrypt/Decrypt a remote
    "crypt"
10 / FTP Connection
    "ftp"
11 / Google Cloud Storage (this is not Google Drive)
    "google cloud storage"
12 / Google Drive
    "drive"
13 / Google Photos
    "google photos"
14 / Hubic
    "hubic"
15 / JottaCloud
    "jottacloud"
16 / Koofr
    "koofr"
17 / Local Disk
    "local"
18 / Mega
    "mega"
19 / Microsoft Azure Blob Storage
    "azureblob"
20 / Microsoft OneDrive
    "onedrive"
21 / OpenDrive
    "opendrive"
22 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
    "swift"
23 / Pcloud
    "pcloud"
24 / Put.io
    "putio"
25 / QingCloud Object Storage
    "qingstor"
26 / SSH/SFTP Connection
    "sftp"
27 / Union merges the contents of several remotes
    "union"
28 / Webdav
    "webdav"
29 / Yandex Disk
    "yandex"
30 / http Connection
    "http"
31 / premiumize.me
    "premiumizeme"
Storage> 13
```

8、下面三个选项留空，使用默认，直接回车

```
** See help for google photos backend at: https://rclone.org/googlephotos/ **

Google Application Client Id
Leave blank normally.
Enter a string value. Press Enter for the default ("").

client_id>

Google Application Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").

client_secret>

Set to make the Google Photos backend read only.

If you choose read only then rclone will only request read only access
to your photos, otherwise rclone will request full access.
Enter a boolean value (true or false). Press Enter for the default ("false").

read_only>
```

9、下面两项选 n

```
Edit advanced config? (y/n)
y) Yes
n) No

y/n> n

Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes
n) No

y/n> n
```

10、这里会给出一个让你访问授权的网址，把它复制出来贴浏览器访问，然后一路下一步，最后会给你返回一串验证码

```
If your browser doesn't open automatically go to the following link: https://accounts.google.com/o/oauth2/auth?access_type=offline&client_id=****evjaotbpbab1*.apps.googleusercontent.com&redirect_uri=u***Aoob&response_type=code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fphotoslibrary+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fphotoslibrary&state=****
Log in and authorize rclone for access
```

把给你的验证码贴这里

```
Enter verification code> *******dsadfddsdfdsfdf
```

```
*** IMPORTANT: All media items uploaded to Google Photos with rclone
*** are stored in full resolution at original quality.  These uploads
*** will count towards storage in your Google Account.
```

这一步选y

```
--------------------
[gp]
type = google photos
token = {"access_token":"*******"}
--------------------
y) Yes this is OK
e) Edit this remote
d) Delete this remote

y/e/d> y

Current remotes:

Name                 Type
====                 ====
gp                   google photos
onedrive             onedrive

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
```

这一步选q退出

```
e/n/d/r/c/s/q> q
```

11、然后**挂载**，还是先创建一个本地磁盘，用于映射

```
mkdir -p /gp
```

12、手工**挂载**的话，输入下面命令 注意：此处`./**rclone** mount gp`中的 gp 就是上边设置的 name

```
./rclone mount gp: /gp --allow-other --allow-non-empty --vfs-cache-mode writes
```

手动**挂载**到此就结束了

13、需要开机自动**挂载**的话，继续往下看

13.1、先把 **rclone** 的可执行文件复制到 /usr/bin：

```
cp /root/rclone-v*/rclone /usr/bin/rclone
```

13.2、新建一个 rclonegp.service 文件：

```
vi /usr/lib/systemd/system/rclonegp.service
```

13.3、写入：

```
[Unit]
Description=rclonegp

[Service]
User=root
ExecStart=/usr/bin/rclone mount gp: /gp --allow-other --allow-non-empty --vfs-cache-mode writes
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

13.4、重载 daemon，让新的服务文件生效：

```
systemctl daemon-reload
```

13.5、现在就可以用systemctl来启动**rclone**了：

```
systemctl start rclonegp
```

13.6、设置开机启动：

```
systemctl enable rclonegp
```

14、停止、查看状态可以用：

```
systemctl stop rclonegp
systemctl status rclonegp
```

15、重启你的 VPS，然后查看一下 **rclone** 的服务起来没，接着查看一下盘子挂上去没：

```
reboot
systemctl status rclonegp
df -h
```

16、到这里就完成了

[https://lab.bnxb.com/zhishi/27736.html](https://lab.bnxb.com/zhishi/27736.html)
