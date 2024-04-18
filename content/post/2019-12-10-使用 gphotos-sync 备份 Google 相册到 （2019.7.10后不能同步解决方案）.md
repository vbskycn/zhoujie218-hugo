---
title: "使用 gphotos-sync 备份 Google 相册到 （2019.7.10后不能同步解决方案）"
date: "2019-12-10"
categories: 
  - "diannaowangruo"
tags: 
  - "google"
  - "gphotos"
  - "photos"
  - "rclone"
  - "sync"
url: "/archives/1033.html"
---

2019年7月 Google 更新政策，Google Photos 与 Google Drive 不会双向同步，之前通过 Google Drive，使用 [rclone 备份 Google Photos](https://cyhour.com/825/) 这个方法就失效了。在[博友](https://cyhour.com/go/aHR0cHM6Ly93d3cuZGF4aWJsb2cuY29tL-S9v-eUqGdwaG90b3Mtc3luY-Wkh-S7vWdvb2dsZS3nm7jlhowv "https://www.daxiblog.com/使用gphotos-sync备份google-相册/")那里看到了新工具：[gphotos-sync](https://cyhour.com/go/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L2dwaG90b3Mtc3luYy8 "https://pypi.org/project/gphotos-sync/") · [GitHub](https://cyhour.com/go/aHR0cHM6Ly9naXRodWIuY29tL2dpbGVza25hcC9ncGhvdG9zLXN5bmM "https://github.com/gilesknap/gphotos-sync") 折腾一圈，发现 gphotos-sync 无法直接保存照片到使用 rclone 挂载的 OneDrive 上（2019.10.14，后记，博友 @NSFW 缓解了这个问题，加--db-path参数，把数据库文件保存在本地即可运行2分钟左右）。放弃……

接着找[大硬盘 VPS](https://cyhour.com/1110/)，不得不说，[BuyVM](https://cyhour.com/go/aHR0cHM6Ly9teS5mcmFudGVjaC5jYS9hZmYucGhwP2FmZj0zMTE2JnBpZD0xNDM5 "https://my.frantech.ca/aff.php?aff=3116&pid=1439") 这货真心便宜。

## 安装 Python 3

gphotos-sync 需要 Python 3，CentOS 自带 Python 2，得安装，方法参考：[CentOS 7 编译安装 Python 3.7.4](https://cyhour.com/1115)

嫌麻烦的话还是一键脚本安装吧，比如：[Python 3.6一键安装脚本 for CentOS/Debian](https://cyhour.com/go/aHR0cHM6Ly93d3cubW9lcmF0cy5jb20vYXJjaGl2ZXMvNTA3Lw "https://www.moerats.com/archives/507/")

```
#CentOS系统
wget https://www.moerats.com/usr/shell/Python3/CentOS_Python3.6.sh && sh CentOS_Python3.6.sh

#Debian系统
wget https://www.moerats.com/usr/shell/Python3/Debian_Python3.6.sh && sh Debian_Python3.6.sh
```

## 安装 gphotos-sync

官网：[Google Photos Sync](https://cyhour.com/go/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L2dwaG90b3Mtc3luYy8 "https://pypi.org/project/gphotos-sync/")，目前版本 2.9.2。执行下面命令安装即可：

```
pip3 install gphotos-sync
```

安装完成，执行 gphotos-sync --help 就能看到帮助信息▼展开

## 申请 Google Photos 访问 API client id

### 创建项目

打开 [Google Developer Console](https://developers.google.com/console/ "https://developers.google.com/console/") 控制台，创建一个新项目，如：google-photos-sync

![ 1095-google-new-project ](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/12/使用-gphotos-sync-备份-google-相册到-（2019-7-10后不能同步解决方案）20191210.png)

### 在 google-photos-sync 项目中激活 Photos Library API

进入 API 库，搜索 Google Photos，激活 Photos Library API。

![ 1095-google-photos-api ](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/12/使用-gphotos-sync-备份-google-相册到-（2019-7-10后不能同步解决方案）20191210-1.png)

### 创建 OAuth 同意屏幕

填写应用名称，然后保存即可。（其余信息不用理会）

![ 1095-google-screen-auth ](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/12/使用-gphotos-sync-备份-google-相册到-（2019-7-10后不能同步解决方案）20191210-2.png)

### 创建 OAuth 客户端 ID

凭据（Credentials）菜单，创建「OAuth 客户端 ID」（OAuth client ID）凭证。

![ 1095-google-new-credentials ](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/12/使用-gphotos-sync-备份-google-相册到-（2019-7-10后不能同步解决方案）20191210-3.png)

「应用类型」一定要选择「其他（Other）」，点击创建。

![ 1095-google-client-id-others ](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/12/使用-gphotos-sync-备份-google-相册到-（2019-7-10后不能同步解决方案）20191210-4.png)

创建完成，点击凭证右侧下载按钮把 json 格式凭证信息下载并重命名为：client\_secret.json

![ 1095-google-download-json ](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/12/使用-gphotos-sync-备份-google-相册到-（2019-7-10后不能同步解决方案）20191210-5.png)

### client\_secret.json 上传到指定路径

这个文件，不同操作系统类型，放置到不同目录：

- Mac OS X：~/Library/Application Support/gphotos-sync/
- Linux：~/.config/gphotos-sync/
- Windows：C:Users\\AppDataLocalgphotos-syncgphotos-sync

## rclone 挂载 OneDrive 到 VPS

如果先备份到大硬盘 VPS，则不需要将 OneDrive 挂载到 VPS，rclone sync 同步到 OneDrive 更稳定。[rclone](https://cyhour.com/go/aHR0cHM6Ly9yY2xvbmUub3JnL2NvbW1hbmRzL3JjbG9uZV9tb3VudC8 "https://rclone.org/commands/rclone_mount/") 安装、配置挺简单，可参看旧文：

[使用 rclone 将 Google Photos 同步备份至 OneDrive](https://cyhour.com/1114/)

去年，是使用 rclone 将 Google Drive 文件同步至 OneDrive 实现备份 Google Photos，今年7月份，Google 更新政策，Google Drive 与 Goog...

[![](https://cn.gravatar.com/avatar/0a5737fa7d7cf6abde7754cf7ef187aa?s=16&d=monsterid&r=g)老杨](https://cyhour.com/author/y/ "查看作者 老杨 发布的所有文章")

[评论 14](https://cyhour.com/1114/#comments)

[使用 rclone 将 Google Drive 文件同步至 OneDrive](https://cyhour.com/825/)

前几天上了博友「灵尘居」的 Office 365 车，1T OneDrive 到手，手机照片一直喂 Google AI，挺方便的，以前还会同步一份到家里的垃圾西数 NAS，不过并不太自动，后来就懒得弄...

[![](https://cn.gravatar.com/avatar/0a5737fa7d7cf6abde7754cf7ef187aa?s=16&d=monsterid&r=g)老杨](https://cyhour.com/author/y/ "查看作者 老杨 发布的所有文章")

[评论 8](https://cyhour.com/825/#comments)

### rclone mount 挂载 OneDrive

可能会报错：

> Fatal error: failed to mount FUSE fs: fusermount: exec: "fusermount": executable file not found in $PATH

解决办法：

```
yum -y install fuse    ##Centos
apt-get -y install fuse    ##Debian/Ubuntu
```

#### 挂载命令

```
/usr/bin/rclone mount OneDrive:GooglePhotos /root/GooglePhotos --allow-other --allow-non-empty --buffer-size 256M --vfs-cache-mode writes --write-back-cache -v &
```

参考文章：[解决Rclone挂载Google Drive时上传失败和内存占用高等问题](https://cyhour.com/go/aHR0cHM6Ly93d3cubW9lcmF0cy5jb20vYXJjaGl2ZXMvODc3Lw "https://www.moerats.com/archives/877/")

#### 卸载磁盘

```
fusermount -qzu /root/GooglePhotos
```

#### 开机自动挂载

参考文章：[在Debian/Ubuntu上使用rclone挂载Google Drive网盘](https://cyhour.com/go/aHR0cHM6Ly93d3cubW9lcmF0cy5jb20vYXJjaGl2ZXMvNDgxLw "https://www.moerats.com/archives/481/")

代码：▼展开

请根据实际修改下面三个参数：

> NAME="" #配置 rclone 时输入的 Name REMOTE="" #远程网盘里的文件夹 LOCAL="" #VPS 本地挂载目录

然后保存为 startrclone 文件，上传到 VPS，/root 目录下。

执行下面命令添加开机自启：

```
mv startrclone /etc/init.d/startrclone
chmod +x /etc/init.d/startrclone
chkconfig --add startrclone
chkconfig startrclone on
update-rc.d -f startrclone defaults #Debian/Ubuntu
bash /etc/init.d/startrclone start
```

重启一下 VPS，然后 df -h 即可检查有没有自动加载。

## 启动 gphotos-sync 备份 GooglePhotos 相册

两个方法：一是 gphotos-sync 直接备份到前面挂载到 VPS 上的 OneDrive 目录，优点是几乎不占用 VPS 空间（不需要大硬盘 VPS）；二是 gphotos-sync 把 GooglePhotos 相册下载到 VPS 本地，然后 rclone sync 同步到 OneDrive，优点是更稳定，缺点需要大硬盘 VPS。

### gphotos-sync 直接备份到挂载到 VPS 上的 OneDrive 目录

```
/usr/local/bin/gphotos-sync /root/GooglePhotos/ --db-path /root/gpsync --flush-index --use-hardlinks
```

其中 /root/GooglePhotos/ 是 OneDrive 挂载到 VPS 的目录（保存 Google 照片），/root/gpsync 为数据库保存目录，自己指定一个就行。

首次启动，会提示 Google 账号授权，根据提示信息的网址，复制到浏览器打开后进行授权，把生成的 token 填写到命令窗口即可。

![ 1095-google-first-auth ](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/12/使用-gphotos-sync-备份-google-相册到-（2019-7-10后不能同步解决方案）20191210-6.png)

如无意外，gphotos-sync 就开始进行索引、下载、备份照片，以年月的形式来保存照片。第一次同步时间会比较长，数据大，容易出错，最好配合 --skip-index 参数以及 crontab 定时自动运行，否则 Google API 很容易超额（[Google API 额度查询](https://console.developers.google.com/iam-admin/quotas?service=photoslibrary.googleapis.com "https://console.developers.google.com/iam-admin/quotas?service=photoslibrary.googleapis.com")）。

比如运行一次：

```
/usr/local/bin/gphotos-sync /root/GooglePhotosAPI/ --db-path /root/gpsync --flush-index --use-hardlinks --max-retries 12 --max-threads 16
```

索引完，自动挂掉，然后 crontab 定时根据第一次索引自动重试下载

```
*/30 * * * * /usr/local/bin/gphotos-sync /root/GooglePhotosAPI/ --db-path /root/gpsync --skip-index --use-hardlinks  --max-retries 12 --max-threads 16 >/dev/null 2>&1 &
```

初次同步完成，可以修改定时任务，自动备份，比如，每天凌晨4点执行备份：

```
crontab -e
0 4 * * * /usr/local/bin/gphotos-sync /root/GooglePhotos/ --db-path /root/gpsync --flush-index --use-hardlinks --max-retries 12 --max-threads 16 > /dev/null 2>&1 &
```

亲测，次方法不稳定，一般跑两分钟左右，脚本就会出错（\[Errno 5\] Input/output error、ETag does not match current item’s value 等）挂掉，需要不断重启进程。

### gphotos-sync 把 GooglePhotos 相册下载到 VPS 本地，然后 rclone sync 同步到 OneDrive

这方法除了需要大硬盘 VPS，暂时没有其它问题。亲测，[BuyVM 大硬盘 VPS](https://cyhour.com/1110/)，跑了4个多小时，Downloaded 83253 Items, Failed 8……一次跑完 133G……

gphotos-sync 把 GooglePhotos 相册下载到 VPS 本地：

```
screen -S gphotos-sync
/usr/local/bin/gphotos-sync /mnt/256/  --use-hardlinks  --flush-index --max-retries 10 --max-threads 16
```

/mnt/256/ 为 VPS 本地存放 GooglePhotos 数据目录，容量需要够大。

rclone sync 定时把数据同步到 OneDrive：

```
crontab -e
11 */1 * * * /usr/bin/rclone sync /mnt/256/ OneDrive:GooglePhotos >/dev/null 2>&1 &
```

## 参考资料

Google Photos Sync 项目：[gphotos-sync](https://cyhour.com/go/aHR0cHM6Ly9weXBpLm9yZy9wcm9qZWN0L2dwaG90b3Mtc3luYy8 "https://pypi.org/project/gphotos-sync/")

Logix - [How To Backup Google Photos To Your Computer With gphotos-sync](https://cyhour.com/go/aHR0cHM6Ly93d3cubGludXh1cHJpc2luZy5jb20vMjAxOS8wNi9ob3ctdG8tYmFja3VwLWdvb2dsZS1waG90b3MtdG8teW91ci5odG1s "https://www.linuxuprising.com/2019/06/how-to-backup-google-photos-to-your.html")（英文）

## 后记、更新

2019.8.27：Windows 下同步效果不理想，相册一个都没有同步下来，照片也只下载了很少一部分。（估计是 gbk 编码原因）

2019.10.14：博友 @NSFW 解决了 gphotos-sync 无法直接保存照片到使用 rclone 挂载的 OneDrive 这个问题，加 --db-path 参数，把数据库文件保存在本地即可。（效果不大好，没有大盘鸡的话还是直接 [rclone](https://cyhour.com/1114/) 方法稳定点）
