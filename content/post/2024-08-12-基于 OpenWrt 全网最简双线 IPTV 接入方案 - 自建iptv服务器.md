---
title: "基于 OpenWrt 全网最简双线 IPTV 接入方案 - 自建iptv服务器"
date: "2024-08-12"
categories: 
  - "diannaowangruo"
tags: 
  - "iptv"
  - "openwrt"
  - "组播"
url: "/archives/2639.html"
---

## 介绍

该方案不需要拿到光猫管理员（虽然折腾半天拿到了发现可以不用），也不需要设置 VLAN，因为是双线接入只会多占用一个软路由端口，简单几步配置就能支持 IPTV。

### 限制

因为非常简单所以有一些限制：

1. 需要软路由上还有空闲的网口
2. 只在成都电信测试通过，不确定其它区域和运营商都可以。因为是发现本地 IPTV 是不需要拔号，也不需要特定 IP 的，和网上各种复杂教程完全不一样。
3. 本文完全通过无线访问，如果要使用机顶盒，需要再多一个端口桥接，或者 omcproxy 一类的工具，不在本文范围。

### 拓扑情况

![](https://img-cloud.zhoujie218.top/2024/08/12/66b9947310631.png)

简单介绍一下拓扑情况，光纤入户通过光猫再到安装 OpenWrt 的软路由，光猫使用桥接通过 OpenWrt 拔号上网（光猫使用路由模式直接拔号也没有影响）。光猫的上网口接入软路由的 WAN（eth0）口，IPTV 接入软路由的 eth1，后面会进行配置，还有一个 Wifi 作为 AP 让其它设备接入。

影响本次的就是需要软件路由上有个空闲的网口，并接入光猫的 IPTV 口。否则需要单线复用的方式，获取光猫管理员创建 VLAN，共用软路由的 WAN 口，这种复杂的方式本文不会涉及。

如果不符合上述条件的，可以退出本文搜索其它更合适的方式。

## 操作步骤

### 释放网口

在 `网络 -> 接口` 中找到 `LAN` 编辑，在物理设置里面把用于 IPTV 的物理端口 `eth1`取消勾选。后面括号中应该是 `lan`，因为是后面补截的屏所以这里已经是 `IPTV` 。

![](https://img-cloud.zhoujie218.top/2024/08/12/66b994933f6b0.png)

### 新建 IPTV 接口

在 `网络 -> 接口` 中创建新接口，命名 `IPTV`（其它名字也可以方便记忆），协议选择`静态 IP`。

如图配置 IP 地址，不要和你当前路由同一网段就行，图中的 `192.168.168.123` 是随便设置的一个 IP。

![](https://img-cloud.zhoujie218.top/2024/08/12/66b99497292b2.png)

在`高级设置`里面把跃点数设置为 `50` ，`WAN`口设置的 `20`。

![](https://img-cloud.zhoujie218.top/2024/08/12/66b9949ad7fb0.png)

在`物理设置` 里面选择刚刚释放用于 IPTV 的 `eth1`。

![](https://undefapp.com/content/images/2023/01/iptv-interface-physical.png)

最后在 `防火墙` 里新建一个 `iptv` ，保存并应用

![](https://img-cloud.zhoujie218.top/2024/08/12/66b9949d9cc84.png)

### 启用 udpxy

因为使用的 OpenWrt 版本中已经集成 `udpxy`，所以可以直接使用，如果未集成需要到 `系统 -> 软件` 中进行安装。  
进入 `服务 -> udpxy`，启用并按图中进行配置，`BindIP` 为 OpenWrt 软路由 IP 或者 `0.0.0.0` 也可以，`SourceIP` 使用上面的 IPTV 的接口`eth1`，保存并应用。

![](https://img-cloud.zhoujie218.top/2024/08/12/66b994a9c55c2.png)

### 然后就没有然后了

## 验证

### 验证 udpxy

输入 `http://<router-ip>:4022/status` 如果看到如下界面，说明配置成功。`router-ip` 为软路由的 ip 地址，也是图中接受客户端的地址。组播地址 `192.168.168.123` 即为上面 IPTV 接口配置的静态 IP。

![](https://img-cloud.zhoujie218.top/2024/08/12/66b9947a5df53.png)

### 播放验证

可以从 [https://github.com/imDazui/Tvlist-awesome-m3u-m3u8](https://github.com/imDazui/Tvlist-awesome-m3u-m3u8?ref=undefapp.com) 找到很多直播源，根据区域下载 [四川成都电信udp组播直播源.m3u8](https://raw.githubusercontent.com/imDazui/Tvlist-awesome-m3u-m3u8/master/m3u/%E5%9B%9B%E5%B7%9D%E6%88%90%E9%83%BD%E7%94%B5%E4%BF%A1udp%E7%BB%84%E6%92%AD.m3u?ref=undefapp.com)，从中找到任意一个地址，如 CCTV-1 的 `http://0.0.0.0:0000/udp/239.93.0.184:5140` 修改为 `http://<router-ip>:4022/udp/239.93.0.184:5140`，使用播放器打开该 URL 即可正常播放。  
部分 `m3u` 文件中的地址是 `igmp://239.93.1.23:6000` ，只需要把协议去掉在前面加上 `http://<router-ip>:4022/udp` 就可以，最终播放地址是 `http://<router-ip>:4022/udp/239.93.1.23:6000`。

![](https://img-cloud.zhoujie218.top/2024/08/12/66b994b0e5d53.png)

单个测试成功之后，就可以批量修改替换 `m3u` 中的地址，使用播放器加载修改后的文件。

### 流量查看（可选）

如果 OpenWrt 上有安装 netdata，在对应网口上也能看到在播放 IPTV 的时候，流量都是通过 `eth1`

![](https://img-cloud.zhoujie218.top/2024/08/12/66b9947b1075b.png)

## 挖坑

个人主要使用 Kodi 来播放 IPTV，后面补一篇教程。

~Plex 通过 xteve 应该也能支持，测试后可以再补一篇。~ 已填坑[Plex + xTeVe 加载 IPTV 直播 - 自建多媒体平台](https://undefapp.com/plex-xteve-jia-zai-iptv-zhi-bo-zi-jian-duo-mei-ti-ping-tai/)

本文转至：[https://undefapp.com/ji-yu-openwrt-quan-wang-zui-jian-shuang-xian-iptv-jie-ru-fang-an-zi-jian-duo-mei-ti-ping-tai/](https://undefapp.com/ji-yu-openwrt-quan-wang-zui-jian-shuang-xian-iptv-jie-ru-fang-an-zi-jian-duo-mei-ti-ping-tai/)
