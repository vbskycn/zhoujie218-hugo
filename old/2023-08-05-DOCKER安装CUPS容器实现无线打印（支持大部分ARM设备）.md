---
title: "DOCKER安装CUPS容器实现无线打印（支持大部分ARM设备）"
date: "2023-08-05"
categories: 
  - "it-related"
  - "diannaowangruo"
tags: 
  - "cups"
  - "docker"
  - "p910nd"
  - "usb"
  - "热插拔"
url: "/archives/2540.html"
---

# 一.锐角云等X86机器

执行代码拉取镜像并运行容器，这里仍然选择`tigerj/cups-airprint`的，因为其他的我都试过识别不了我的`M1005`，不知道是不是个案。而且这个镜像带`avahi`，能实现`airprint`，支持安卓及苹果设备直接使用系统自带打印服务搜索到打印机，非常方便。只是有点瑕疵，让我花了点时间解决了。

```
docker run \
       --name=cups \
       --restart=always \
       --net=host \
       -v /var/run/dbus:/var/run/dbus \
       -v ~/airprint_data/config:/config \
       -v ~/airprint_data/services:/services \
       --device /dev/bus \
       --device /dev/usb \
       -e CUPSADMIN="admin" \
       -e CUPSPASSWORD="password" \
       tigerj/cups-airprint
```

后面步骤都一样，参考老版步骤，选择驱动，共享打印机，直到`cups`里能打印出测试页面。这时如果去电脑或者手机的打印服务里搜索打印机是搜索不到的。接下来执行命令

```
docker exec cups service dbus start

docker exec cups service avahi-daemon start
```

执行之后去电脑或者手机系统自带的打印服务里搜索打印机，怎么样，是不是搜索到了？

这时候打印机能正常工作了，但是不能关，一关，再打开，打印作业就会被挂起，无法继续打印，只有手动重启`cups`，要想实现打印机上电自动重启`cups`，解决方法如下：

在`/etc/udev/rules.d`目录下新建一条规则，如`m1005.rules` 内容如下：

```
ACTION=="add", SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ENV{ID_VENDOR_ID}=="03f0", ENV{ID_MODEL_ID}=="3b17", RUN+="/root/cupsstart.sh"

ACTION=="remove", SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", ENV{PRODUCT}=="3f0/3b17/100", RUN+="/root/cupsstop.sh"
```

这步操作是让系统在发现打印机接入及断开时执行脚本，这段代码也是百度来的，原本`add`和`remove`两段代码是一样的，唯一区别是最后执行的脚本不一样，但是实际执行的时候我发现只有打印机接入能执行`add`这段代码，而打印机断电，不能执行`remove`这段代码，继续百度，从[https://blog.csdn.net/weixin\_30610431/article/details/114562335](https://www.musz.cn/?golink=aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zMDYxMDQzMS9hcnRpY2xlL2RldGFpbHMvMTE0NTYyMzM1)找到了答案，执行 `udevadm monitor --kernel --property --subsystem-match=usb`之后分别给打印机通电和断电，对比输出发现，断电时没有 `MODEL_ID`参数，所以代码不执行了，根据实际输出，将断电代码如上修改之后，就顺利执行了。其中add段代码中的`03f0` `3b17` 两个数据要跟你你的实际修改，这两个参数可以通过执行`lsusb`查看到 然后在`/root`目录里建立两个脚本:`cupsstart.sh`和`cupsstop.sh`

```
#!/bin/sh

docker restart cups

docker exec cups cupsaccept M1005

docker exec cups service dbus start

docker exec cups service avahi-daemon start
```

这个脚本实现系统一发现打印机接入，就重启`cups`容器，并设置打印机接受打印任务，另外将`avahi`服务启动起来。

```
#!/bin/sh

docker exec cups cupsreject M1005
```

这个脚本是实现当打印机断电了，设置打印机拒绝打印任务，为什么要这么设置呢，因为打印机断电之后重新上电，`cups`会接受打印任务，但是却不打印，这时如果重启，重复发送的打印任务全部会打印出来，为了避免这种情况发生，需要在打印机断电之后设置`cups`拒绝打印任务。 好了这样就完美实现，打印机上电自动启动`cups`，断电`cups`拒绝打印任务，并且完美支持`airprint`，安卓，`ios`，电脑都能直接搜索到打印机。

# 二.我家云、贝壳云、N1等arm机器

```
docker run \
       --name=cups \
       --restart=always \
       --net=host \
       -v /var/run/dbus:/var/run/dbus \
       -v ~/airprint_data/config:/config \
       -v ~/airprint_data/services:/services \
       --device /dev/bus \
       --device /dev/usb \
       -e CUPSADMIN="admin" \
       -e CUPSPASSWORD="password" \
       jysky007/cups:v1
```

花了点时间修改了镜像，直接支持`airprint`了。 我既有我家云也有N1，都刷的是荒野无灯大神的小钢炮系统，这个系统非常精简，里面管理热插拔硬件的是`mdev` 这个是简化版的`udev`，研究了许久只实现了打印机上电自动重启`cups`，也可以啦。方法如下：

在`/etc/mdev.conf`文件的最下面添加一行：

```
usb/lp0       0:0 660   @/root/cupsstart.sh
```

然后执行`/etc/init.d/S10mdev restart`重启`mdev`服务。

如为armbian系统，可在`/etc/udev/rules.d`目录下新建文件命名为`99-usb-cups.rules`，文件内容如下：

```
SUBSYSTEM=="usb", ACTION=="add", RUN+="/root/cupsstart.sh"
```

![image-20230805215822538](https://img-cloud.zhoujie218.top/piggo/202308052158714.png)

拔usb就自动执行重启docker命令

如为openwrt系统，可在/etc/hotplug.d/usb/10-usb\_printer文件里面添加2行，内容如下：

```
sleep 10

/etc/rc.d/S70usb_printer restart
```

这表示识别打印机接入，就执行`/root/cupsstart.sh`脚本，脚本内容：

```
#!/bin/sh

docker restart cups
```

记得把脚本权限改成`0777`
