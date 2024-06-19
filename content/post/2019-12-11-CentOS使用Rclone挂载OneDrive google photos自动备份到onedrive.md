---
title: "CentOS使用Rclone挂载OneDrive google photos自动备份到onedrive"
date: "2019-12-11"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
url: "/archives/1070.html"
---

服务器上CentOS大部分未安装图形界面，但是Rclone必须要在有内置浏览器的电脑才能正常完成授权，因此这里使用的办法是先在本地Windows电脑安装Rclone并获取授权后的token，再将其复制到CentOS的服务器上。

### Windows 安装Rclone

- Windows客户端：[rclone-v1.41-windows-amd64.zip](https://downloads.rclone.org/v1.41/rclone-v1.41-windows-amd64.zip "rclone-v1.41-windows-amd64.zip")

下载后将其解压，并将`rclone.exe`移动到`C:WindowsSystem32`这个目录，这样就可以使用rclone命令了，如下截图。

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file.png))

在cmd窗口继续输入命令**`rclone config`**进行配置，输入`n`新建一个远程，并取一个名字，比如`onedrive`

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-1.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-1.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-1.png))

继续下一步，选择需要挂载的云存储，Onedrvie是16，随着版本的变化可能会改变，自己灵活变通即可。

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-2.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-2.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-2.png))

`client_id`/`client_secret`直接留空并回车，然后选择OneDrive版本，教育版或商业版请选择`b`，个人版选择`p`

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-3.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-3.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-3.png))

浏览器会自动打开`[http://localhost:53682/](http://localhost:53682/)` 并进行授权，如果授权成功会返回`token`，请务必将`token`记录并保存后面还要使用。

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-4.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-4.png)\[!\[\](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-5.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-4.png)[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-5.png))

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-5.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-5.png))

### CentOS安装Rclone

直接使用官方的一键安装命令即可，输入下面的命令：

```
curl https://rclone.org/install.sh | sudo bash
```

### CentOS挂载Onedrive

接下来操作方法和windows完全一样，就不重复了，唯一的区别是“Use auto config?”这里选择`n`，并输入之前获取的`token`

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-6.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-6.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-6.png))

### 总结

Rclone支持挂载20多种网盘，不过大多数网盘都是国外的，在国外VPS上使用效果更佳，用来备份数据这些还是挺不错的。

利用 rclone 挂载 OneDrive for Business 为 Linux 磁盘空间,  
可以利用 OneDrive for Business 为 Linux增加 5TB 的空间.

个人版也可以挂载,按提示挂载即可.  
本文详细的讲讲挂载OneDrive for Business.

**步骤注意事项:**

1. 客户端授权
    
    - 同时在远端和本地端都下载rclone,萌咖使用的是Windows,所有也下载了Windows版的.
        
    - 将Windows版的rclone.exe解压至临时目录,萌咖的临时目录是`Z:`.
        
    - ```
        
        |  | :: 运行以下命令 |
        |  | cd /d Z: |
        |  | rclone authorize "onedrive" |
        ```
        
    - 选择Business版本,并按**Y**,弹出浏览器后登陆,等待返回 access token.
        
    - 右键标记全部的 access token,按 CTRL + C 进行复制.(就是 {“access\_token”: … }, 两个花括号及中间的部分. )
        
    - 粘贴到记事本中,整理好.
        
    - 远端运行rclone config 选择Business版本,并按**N**,粘贴刚刚复制的 access token.
        
    - 配置完毕!
        
2. 错误提示
    
    - | | Fatal error: failed to mount FUSE fs: fusermount: exec: "fusermount": executable file not found in $PATH |
        
        ```
        
        
        * 出现原因:
        ```
        
    
    没有安装 fuse ,自行安装就可以了. 解决办法:
    
    - ```
        
        |  | \# Debian/Ubuntu |
        |  | apt-get install fuse |
        |  | \# CentOS |
        |  | yum install fuse |
        ```
        
3. - | | NOTICE: One drive root 'test': poll-interval is not supported by this remote |
        
        ```
        
        
        * 出现原因
        ```
        
    
    就是个提示而已,可以忽略.
    

**说到最后:**  
自启动和自动后台挂载,参照 [**\[教程\] rclone使用小记**](https://moeclub.org/2017/11/28/500/), 有 rclone 基本用法和自启动脚本.

新建小鸡鸡，安装 rclone，配置连接 Google Photos、OneDrive……第一次同步，执行下面命令：

> 温馨提示：Google Photos 下一般有三个大目录 media、album 和 shared-album，而 media 还分按年（by-year）、按月（by-month）和按日（by-day），如果不指定，会三种分类都会备份下来，照片就会有两份重复。一般建议 by-month 方式。

```
|  | /usr/bin/rclone sync gphotos:media/by-month odrive:gphotos/media/by-month > /dev/null 2>&1 & |
|  | /usr/bin/rclone sync gphotos:album odrive:gphotos/album > /dev/null 2>&1 & |
|  | /usr/bin/rclone sync gphotos:shared-album odrive:gphotos/shared-album > /dev/null 2>&1 & |
```

初次同步完成，crontab 定时执行命令同步即可，如（分别按月备份相片、相册）：

```
|  | 0 2 \* \* \* /usr/bin/rclone sync gphotos:media/by-month odrive:gphotos/media/by-month > /dev/null 2>&1 & |
|  | 0 5 \* \* \* /usr/bin/rclone sync gphotos:album odrive:gphotos/album > /dev/null 2>&1 & |
|  | 0 8 \* \* \* /usr/bin/rclone sync gphotos:shared-album odrive:gphotos/shared-album > /dev/null 2>&1 & |
```

附 rclone 卸载方法：

```
sudo rm /usr/bin/rclone && sudo rm /usr/local/share/man/man1/rclone.1
```

以及删除对应配置即可，配置文件 rclone.conf 一般在 /root/.config/rclone/rclone.conf

**实际挂载**

**`rclone config`**

onedrive: new – name – n – 23onedrive -n -n id -1 -0 -y

**继续输入命令进行挂载**

```
|  | #安装fuse |
|  | yum -y install fuse |

|  | apt-get install fuse -y |
|  | #创建挂载目录 |

|  | mkdir -p /root/onedrive |
|  | mkdir -p /root/gphotos |
```

```
|  | #挂载 |
|  | rclone mount remote:path/to/files /home/onedrive |
|  | #如果需要后台保持运行，使用下面的命令 |
|  | nohup rclone mount remote:path/to/files /home/onedrive & |
```

解释下上面的参数：

- remote：远程名，之前我们设置的是onedrive
- path/to/files：远程文件路径(也就是Onedrive路径)，可设置为`/`
- /home/onedrive：本地磁盘路径

不出问题的情况下，输入`df -h`就可以看到Onedrive成功挂载。

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-7.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-7.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-7.png))

实际运行记录

**rclone 安装**  
执行命令：curl [https://rclone.org/install.sh](https://rclone.org/install.sh) | sudo bash

**后台自动挂载onedrive**  
**nohup /usr/bin/rclone mount onedrive:/ /root/onedrive –copy-links –no-gzip-encoding –no-check-certificate –allow-other –allow-non-empty –umask 000 &**  
**后台自动挂载gphotos**  
**nohup /usr/bin/rclone mount gphotos:/ /root/gphotos –copy-links –no-gzip-encoding –no-check-certificate –allow-other –allow-non-empty –umask 000 &**

温馨提示：Google Photos 下一般有三个大目录 media、album 和 shared-album，而 media 还分按年（by-year）、按月（by-month）和按日（by-day），如果不指定，会三种分类都会备份下来，照片就会有两份重复。一般建议 by-month 方式。

**后台下载相册并上传到gphotos**

nohup /usr/bin/rclone sync gphotos:media/by-month onedrive:gphotos > /dev/null 2>&1 &

初次同步完成，crontab 定时执行命令同步即可，如（分别按月备份相片、相册）：  
crontab -e  
**后台每2小时执行一次**

- _/2_ /usr/bin/rclone sync gphotos:media/by-month onedrive:gphotos > /dev/null 2>&1 &

**后台每天2点执行**

- 2 \* /usr/bin/rclone sync gphotos:media/by-month onedrive:gphotos > /dev/null 2>&1 &

google相册 onedrive网速真的很牛逼，垃圾国外vps，上传下载峰值都能到450M

\[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-8.png)

\]([https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-8.png](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/05/unnamed-file-8.png))

**遇到如下面的报错，是没有安装fuse3,安装后也不行的是路径不对**

```
Fatal error: failed to mount FUSE fs: fusermount: exec: "fusermount3": executable file not found in $PATH
```

**安装fuse3**

```
sudo yum install fuse3
```

添加硬链接，根据实际情况修改

```
sudo ln -s /usr/bin/fusermount /usr/bin/fusermount3
```
