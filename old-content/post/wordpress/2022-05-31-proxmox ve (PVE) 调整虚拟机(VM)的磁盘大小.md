---
title: "proxmox ve (PVE) 调整虚拟机(VM)的磁盘大小"
date: "2022-05-31"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "centos"
  - "pve"
  - "硬盘"
url: "/archives/2410.html"
---

#### proxmox ve (PVE) 调整虚拟机(VM)的磁盘大小

proxmox ve resize guest disk

### 第一步

通过web ui中调整磁盘大小功能，先设置分配给虚拟机的磁盘空间，如下图

![QQ20200101-235116@2x](https://img.zhoujie218.top/piggo/202205311647499.jpeg)

我这里是从105G，调整到205个G

### 第二步

进入虚拟机系统，我这里的系统是CentOS，其他Linux系统应该类似。

查看磁盘信息，可以看到磁盘的总大小已经变化了，但是下边两个分区没有变

```
[root@localhost ~]# fdisk -l

磁盘 /dev/sda：220.1 GB, 220117073920 字节，429916160 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0x000c264f

   设备 Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200   220200959   109050880   8e  Linux LVM

磁盘 /dev/mapper/centos-root：109.5 GB, 109517471744 字节，213901312 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节

磁盘 /dev/mapper/centos-swap：2147 MB, 2147483648 字节，4194304 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
```

### 第三步

给 /dev/sda2分区增加空间，注意里边的命令 resizepart 2 100% ，是把剩余的空间全部给到/dev/sda2

```
[root@localhost ~]# parted /dev/sda
GNU Parted 3.1
使用 /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print
Model: ATA QEMU HARDDISK (scsi)
Disk /dev/sda: 220GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  标志
 1      1049kB  1075MB  1074MB  primary  xfs          启动
 2      1075MB  113GB   112GB   primary               lvm

(parted) resizepart 2 100%
(parted) quit
信息: You may need to update /etc/fstab.
```

接下来你就可以看到/dev/sda2分区的大小已经变化,看End值

```
[root@localhost ~]# fdisk -l

磁盘 /dev/sda：220.1 GB, 220117073920 字节，429916160 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0x000c264f

   设备 Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200   429916159   213908480   8e  Linux LVM

磁盘 /dev/mapper/centos-root：109.5 GB, 109517471744 字节，213901312 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节

磁盘 /dev/mapper/centos-swap：2147 MB, 2147483648 字节，4194304 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
```

### 第四步

更新物理卷的大小，当然这里前提是使用了LVM

```
pvresize /dev/sda2
```

接下来更新逻辑卷的大小

```
[root@localhost ~]# lvresize --extents +100%FREE --resizefs /dev/mapper/centos-root
  Size of logical volume centos/root changed from <102.00 GiB (26111 extents) to <202.00 GiB (51711 extents).
  Logical volume centos/root successfully resized.
meta-data=/dev/mapper/centos-root isize=512    agcount=15, agsize=1900032 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0 spinodes=0
data     =                       bsize=4096   blocks=26737664, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal               bsize=4096   blocks=3711, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 26737664 to 52952064
```

最后可以看到已经成功了

```
[root@localhost ~]# fdisk -l

磁盘 /dev/sda：220.1 GB, 220117073920 字节，429916160 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0x000c264f

   设备 Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200   429916159   213908480   8e  Linux LVM

磁盘 /dev/mapper/centos-root：216.9 GB, 216891654144 字节，423616512 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节

磁盘 /dev/mapper/centos-swap：2147 MB, 2147483648 字节，4194304 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节

[root@localhost ~]# df -h
文件系统                 容量  已用  可用 已用% 挂载点
devtmpfs                 908M     0  908M    0% /dev
tmpfs                    919M     0  919M    0% /dev/shm
tmpfs                    919M  8.6M  911M    1% /run
tmpfs                    919M     0  919M    0% /sys/fs/cgroup
/dev/mapper/centos-root  202G   93G  110G   46% /
/dev/sda1               1014M  282M  733M   28% /boot
tmpfs                    184M     0  184M    0% /run/user/0
```

如果你是非lvm，可以尝试下边的命令，不过我没测试过

```
resize2fs /dev/sda2
```

[Proxmox VE](https://www.d3tt.com/node/proxmox) Steve 发布于 880天前 被查看 9403 次
