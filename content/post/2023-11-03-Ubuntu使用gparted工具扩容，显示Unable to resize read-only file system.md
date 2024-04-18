---
title: "Ubuntu使用gparted工具扩容，显示Unable to resize read-only file system"
date: "2023-11-03"
categories: 
  - "diannaowangruo"
tags: 
  - "ubuntu"
  - "扩容"
  - "磁盘"
url: "/archives/2567.html"
---

### 一、问题

#### 出现提示：无法调整只读文件系统的大小，只能在挂载时调整文件系统的大小

![](https://img-cloud.zhoujie218.top/2023/11/03/654469d07f2ba.webp)

### 二、解决步骤

#### 第一步：查看只读文件系统的详细信息，点击Information

![](https://img-cloud.zhoujie218.top/2023/11/03/654469d8880a7.webp)

#### 第二步：查看该磁盘挂载的文件夹目录（注意：挂载的位置用 ， 隔开，容易忽略 / ）

我的挂在位置为：/ 和 /var/[snap](https://so.csdn.net/so/search?q=snap&spm=1001.2101.3001.7020)/firefox/common/host-hunspell

![](https://img-cloud.zhoujie218.top/2023/11/03/654469db5a99b.webp)

#### 第三步：以root权限打开终端，重新挂载文件夹目录的读写权限

以我的为例：

> sudo -i  
> mount -o remount -rw /  
> mount -o remount -rw /var/snap/firefox/common/host-hunspell

![](https://img-cloud.zhoujie218.top/2023/11/03/654469de55622.webp)

#### 第四步：刷新gparted中的设备后，就可以调整文件系统大小了

![](https://img-cloud.zhoujie218.top/2023/11/03/654469e18c674.webp)

#### 安装gparted

```
apt-get install gparted
gparted
```
