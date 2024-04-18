---
title: "AdGuard Home 优化配置"
date: "2020-07-11"
categories: 
  - "diannaowangruo"
tags: 
  - "adguard"
url: "/archives/1784.html"
---

# AdGuard Home 优化配置

![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/chrome_U72f43BnP2-1024x629.png)

 

AdGuard Home 是一款全网广告拦截与反跟踪软件。在您将其安装完毕后，它将保护您所有家用设备，同时您不再需要安装任何客户端软件。随着物联网与连接设备的兴起，掌控您自己的整个网络环境变得越来越重要。 简单的点讲就比如Google的8.8.8.8，阿里云的223.5.5.5，114的114.114.114.114，还有Cloudflare的1.1.1.1，这些都是提供DNS服务的公共DNS服务器。而AdGuard Home在给我们提供DNS服务的同时还提供去广告的功能，

ADGuard Home的主页：https://adguard.com/zh\_cn/adguard-home/overview.html

Github地址：https://github.com/AdguardTeam/AdGuardHome/wiki/Getting-Started#installation

 

以下只是记录，并不是都填上！！！

以下只是记录，并不是都填上！！！

以下只是记录，并不是都填上！！！

 

## 上游 DNS 服务器

tls://dns.adguard.com

tls://dns.quad9.net

tls://dns.google

tls://1.1.1.1

tls://1.0.0.1

https://1.1.1.1/dns-query

https://1.0.0.1/dns-query

119.29.29.29

114.114.114.114

223.5.5.5

101.226.4.6

180.76.76.76

1.2.4.8

168.95.1.1

https://doh.cleanbrowsing.org/doh/adult-filter/

https://doh.cleanbrowsing.org/doh/security-filter/

tls://dns.google

tls://dns.quad9.net

https://doh.securedns.eu/dns-query

https://doh-de.blahdns.com/dns-query

https://ibksturm.synology.me/dns-query

tls://dns.adguard.com

8.8.8.8

tcp://8.8.8.8

tcp://8.8.4.4

tcp://1.1.1.1

tcp://4.2.2.1

4.2.2.3

tcp://4.2.2.3

4.2.2.4

tcp://4.2.2.4

sdns://AgcAAAAAAAAADjE1MC4xMDkuNzQuMTY0ABBoay1kbnMuMjMzcHkuY29tCi9kbnMtcXVlcnk

sdns://AQcAAAAAAAAAEDQ3LjEwMS4xMzYuMzc6MjIgCRIqxqrF-npxg2-xjGLKvzuxvS7hCGgXx\_x\_4K85yHYZMi5kbnNjcnlwdC1jZXJ0LjIzM3B5LmNvbQ

https://dns.rubyfish.cn/dns-query

https://hk-dns.233py.com/dns-query

https://dns10.quad9.net/dns-query

 

## Bootstrap DNS 服务器

Bootstrap DNS 服务器用于解析您指定为上游的 DoH / DoT 解析器的 IP 地址。

1.1.1.1:53

1.0.0.1:53

114.114.114.114:53

8.8.8.8:53

8.8.4.4:53

1.1.1.1:53

208.67.220.220:53

208.67.222.222:53

9.9.9.10

149.112.112.10

2620:fe::10

2620:fe::fe:10

 

> 上游dns的意思是adguardhome查询你要用的网址时用的dns服务器
> 
> Bootstrap DNS 服务器 是adguardhome 查询dns服务器ip时用的dns服务器
> 
> 上游服务器应该设置成响应最快的多个dns地址

 

## 过滤器

AdGuard Home 可以解析基础的 adblock 规则和 Hosts 语法。

 

### 系统自带过滤器

AdGuard Simplified Domain Names filter

https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt

AdAway

https://adaway.org/hosts.txt

hpHosts - Ad and Tracking servers only

https://hosts-file.net/ad\_servers.txt

MalwareDomainList.com Hosts List

https://www.malwaredomainlist.com/hostslist/hosts.txt

 

### 自定义过滤器

neoHosts Full 127.0.0.1 兼容性更好

https://hosts.nfz.moe/127.0.0.1/full/hosts

Easylist 官方规则

https://easylist.to/easylist/easylist.txt

EasyList China 中文补充规则

https://easylist-downloads.adblockplus.org/easylistchina.txt

EasyList Lite 中文精简规则

https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjxlist.txt

EasyPrivacy 隐私保护

https://easylist-downloads.adblockplus.org/easyprivacy.txt

CJX's Annoyance List 去自我推广列表

https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt

ChinaList 国内大部分视频网站的广告过滤 （广告净化器）

【凉凉】http://tools.yiclear.com/ChinaList2.0.txt

【备份】https://raw.githubusercontent.com/hopol/ChinaList2.0/master/ChinaList2.0.txt

乘风 广告过滤规则

https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/ABP-FX.txt

【码云更新】https://gitee.com/xinggsf/Adblock-Rule/raw/master/rule.txt

【MV规则】https://gitee.com/xinggsf/Adblock-Rule/raw/master/mv.txt

Fanboy+Easylist-Merged Ultimate List

https://fanboy.co.nz/r/fanboy-ultimate.txt

StevenBlack

http://sbc.io/hosts/alternates/fakenews-gambling-porn-social/hosts

yhosts

https://raw.githubusercontent.com/vokins/yhosts/master/hosts

大圣净化

https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts

1024\_hosts

https://raw.githubusercontent.com/Goooler/1024\_hosts/master/hosts

neoHosts Full

https://hosts.nfz.moe/full/hosts

Google Host

https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts

ChinaList+EasyList(修正)

http://sub.adtchrome.com/adt-chinalist-easylist.txt

 

### 以下慎用

I don't care about cookies 屏蔽网站 cookies 相关警告！！！

https://www.i-dont-care-about-cookies.eu/abp/

 

 

### 如果你觉得过滤得还不够，也可以在“自定义过滤器规则”按照以下过滤规则自己编写：

||example.org^ – 拦截 example.org 域名及其所有子域名

@@||example.org^ – 放行 example.org 及其所有子域名

127.0.0.1 example.org – 将会把 example.org（但不包括它的子域名）解析到 127.0.0.1

! 注释符号，表示这是一行注释

\# 这也是注释符号，同样表示这是一行注释

/REGEX/ – 正则表达式模式

 

具体请参考《官方说明》

https://kb.adguard.com/en/general/dns-filtering-syntax

 

### 附录

**anti-AD**

目前中文区命中率最高的广告过滤列表，精确的广告屏蔽和隐私保护。已支持AdGuardHome，dnsmasq，Surge，Pi-Hole，SmartDNS等。

Github地址：[https://github.com/privacy-protection-tools/anti-AD](https://github.com/privacy-protection-tools/anti-AD)

https://gitee.com/privacy-protection-tools/anti-ad/raw/master/easylist.txt

 

**halflife**

合并EasylistChina、EasylistLite、CJX'sAnnoyance，以及补充的一些规则

Homepage: https://adf.minggo.eu.org

https://gitee.com/halflife/list/raw/master/ad.txt

 

**yhosts tvbox**

https://github.com/vokins/yhosts

里面有个TVBOX的规则

https://raw.githubusercontent.com/vokins/yhosts/master/data/tvbox.txt

 

**DNS优选**

(挑选最合适的DNS服务器,拒绝DNS劫持)

[![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-40.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-40.png)https://www.lanzous.com/iaik9vi
