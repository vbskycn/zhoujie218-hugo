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

每个虚拟机都是需要一块硬盘的，实际是从宿主机划分出来的给虚拟机使用的。

PVE虚拟机是基于linux的，它使用LVM管理宿主机磁盘，所以每个虚拟机仅仅是从LVM的VG（volume group卷组）中新建一个固定大小的LV（logical volume），提供给特定的一个虚拟机实例作为虚拟化的硬盘使用。

想实现虚拟机硬盘动态扩容，我们必须明白linux的LVM硬盘管理，因为只有LVM可以实现对一个已有的硬盘分区扩容。

为了说LVM，我们先得搞明白传统的硬盘管理，传统的硬盘管理包含4步：

- 块设备：插在机器上的一块硬盘。
- 硬盘分区：把块设备分成多个分区，每个分区固定大小。
- 文件系统：如果想要使用硬盘某分区，需要在这个分区上制作文件系统，比如：ext4格式。
- 挂载目录：最终把做好的文件系统通过mount命令挂载到某个目录下，就可以读写分区内的数据了。

传统硬盘分区方案的问题是，一旦我们把操作系统安装到某个分区内，那么这个分区大小就无法改变了，随着数据变多硬盘就塞满了。想要扩容的话，我们只能选定某个目录挂载一块新的硬盘，然后把一些较大的数据手动迁移进去，总之我们会因为容量问题严重影响到使用体验。

LVM则可以对一个已有的文件系统（当然对应一个硬盘分区）进行扩容，这就是它厉害的地方。

LVM的使用过程是这样的：

- 块设备：给机器插上新的硬盘。
- 硬盘分区：把块设备分成多个分区（1个分区用尽整块磁盘也可以，无所谓），每个分区的大小也是固定的。
- 创建物理卷（PV）：按照LVM的规则，把每个硬盘分区创建为一个物理卷（physical volume）。
- 创建卷池（VG）：新建的物理卷就像一桶矿泉水，把它们加入到一个VG大池子里面，这样池子里的水（硬件空间）就会变多。
- 创建逻辑卷（LV）：想要划分一块硬盘空间拿来使用，只需要从VG里面取一瓢水出来即可，这个划分出来的硬盘空间叫做一个LV（logical volume）。
- 文件系统：现在可以对LV制作文件系统，比如：ext4格式。
- 挂载目录：现在可以把在做好文件系统的LV挂载到某个目录，就可以访问了。

> 我们在安装操作系统的时候可以选择基于LVM管理硬盘，安装程序默认会把整个硬盘作为1个分区，创建分区对应的PV，创建1个VG并把该PV加入到VG中，然后从VG中划出1个LV格式化ext文件系统，然后把整个操作系统安装到这个LV里。

大家可以看一下[LVM的一个简明教程](https://linux.cn/article-3218-1.html)，了解从一块裸硬盘到一个LV的全过程命令。

## LVM与虚拟机的关系

首先，PVE本身是把宿主机硬盘做成了LVM，新建虚拟机则划分一个LV给它作为虚拟化的硬盘使用。

所以，我们很容易给虚拟机新增更多虚拟化硬盘，只需要在宿主机上划分更多LV挂给KVM即可。

通过宿主机划分更多的LV，可以全部虚拟化成硬盘提供给某个虚拟机，这样可以让虚拟机中识别的硬盘越来越多。

虚拟机内其实并不知道宿主机上的LVM，它看到的只是若干硬盘对应的块设备，所以它自身也需要使用LVM，才能将更多的块设备加入到VG中，并且对已有的LV进行扩容。

#### proxmox ve (PVE) 调整虚拟机(VM)的磁盘大小

proxmox ve resize guest disk

### 第一步

通过web ui中调整磁盘大小功能，先设置分配给虚拟机的磁盘空间，如下图

![QQ20200101-235116@2x](https://img-cloud.zhoujie218.top/piggo/202209131734443.jpeg)

我这里是从105G，调整到205个G

### 第二步

进入虚拟机系统，我这里的系统是CentOS，其他Linux系统应该类似。

查看磁盘信息，可以看到磁盘的总大小已经变化了，但是下边两个分区没有变

```tap
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
第三步
```

给 /dev/sda2分区增加空间，注意里边的命令 resizepart 2 100% ，是把剩余的空间全部给到/dev/sda2

```gradle
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
(parted) resizepart 2
Warning: Partition /dev/sda2 is being used. Are you sure you want to continue?
Yes/No? Y 
End? [113GB]? 100% 
(parted) quit 
信息: You may need to update /etc/fstab.
```

接下来你就可以看到/dev/sda2分区的大小已经变化,看End值

```tap
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

第四步

更新物理卷的大小，当然这里前提是使用了LVM【如果未使用LVM，请跳到最后】

```awk
pvresize /dev/sda2
```

接下来更新逻辑卷的大小

```routeros
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

**请注意：这里需要换一下命令**

```
lvresize --extents +100%FREE --resizefs /dev/mapper/cl-root
```

最后可以看到已经成功了

```awk
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

如果你是非lvm，请使用下面命令

```apache
root@nlp:~# resize2fs /dev/sda2                                           
resize2fs 1.44.1 (24-Mar-2018)
Filesystem at /dev/sda2 is mounted on /; on-line resizing required
old_desc_blocks = 4, new_desc_blocks = 5
The filesystem on /dev/sda2 is now 10354427 (4k) blocks long.
```

![image-20220913173742507](https://img-cloud.zhoujie218.top/2022/09/13/a072ab53a7f36.png)
