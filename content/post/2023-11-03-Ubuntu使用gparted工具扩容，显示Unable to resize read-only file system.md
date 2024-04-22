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

![](/images/2023/11/06fca4b63014035f04ec46427598de93.webp)

### 二、解决步骤

#### 第一步：查看只读文件系统的详细信息，点击Information

![](/images/2023/11/a672965ac8f20b395789ee26f2223969.webp)

#### 第二步：查看该磁盘挂载的文件夹目录（注意：挂载的位置用 ， 隔开，容易忽略 / ）

我的挂在位置为：/ 和 /var/[snap](https://so.csdn.net/so/search?q=snap&spm=1001.2101.3001.7020)/firefox/common/host-hunspell

![](/images/2023/11/8fc436cfbc60f8f74fb13de8fd14195d.webp)

#### 第三步：以root权限打开终端，重新挂载文件夹目录的读写权限

以我的为例：

> sudo -i  
> mount -o remount -rw /  
> mount -o remount -rw /var/snap/firefox/common/host-hunspell

![](/images/2023/11/71f3a3e23279641e8790ad326458307e.webp)

#### 第四步：刷新gparted中的设备后，就可以调整文件系统大小了

![](/images/2023/11/b80f7d9bdd5a3dc65bffe7c7b577e59e.webp)

#### 安装gparted

```
apt-get install gparted
gparted
```
