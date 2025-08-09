---
title: "AdGuard Home 广告拦截列表 adblock 规则和 Hosts 列表(2022年9月5日更新)"
date: "2022-09-05"
categories: 
  - "it-related"
  - "diannaowangruo"
tags: 
  - "adguard"
  - "host"
url: "/archives/2480.html"
---

家里智能设备这么多，每台电脑、手机都安装 AdGuard 也太麻烦了，比如电脑端在浏览器上安装了 AdGuard 插件，但是换个浏览器就没用了，而 AdGuard Windows 客户端又要收费，最可怕的是手机也要装 AdGuard APP 应用……所以我还是觉得《[使用AdGuard Home](https://img-cloud.zhoujie218.top/archives/1784.html)》比较方便。

![](https://img-cloud.zhoujie218.top/piggo/202209050943926.png)

国内的建议使用国内服务器进行搭建，延迟较低。

今天更新一些规则，方便自己和大家使用。

### EasyList

去除国际网页中大多数广告，包括不需要的框架、图像和对象。

- [https://easylist-downloads.adblockplus.org/easylist.txt](https://easylist-downloads.adblockplus.org/easylist.txt)

乘风去广告

- 广告规则 [https://gitee.com/xinggsf/Adblock-Rule/raw/master/rule.txt](https://gitee.com/xinggsf/Adblock-Rule/raw/master/rule.txt)
- 视频规则 [https://gitee.com/xinggsf/Adblock-Rule/raw/master/mv.txt](https://gitee.com/xinggsf/Adblock-Rule/raw/master/mv.txt)

### [privacy-protection-tools](https://github.com/privacy-protection-tools)/**[anti-AD](https://github.com/privacy-protection-tools/anti-AD)**

致力于成为中文区命中率最高的广告过滤列表，实现精确的广告屏蔽和隐私保护。anti-AD 现已支持 AdGuardHome，dnsmasq， Surge，Pi-Hole，smartdns 等网络组件。完全兼容常见的广告过滤工具所支持的各种广告过滤列表格式。

| 文件 | raw | 官网地址 | 适用于 |
| --- | --- | --- | --- |
| `adblock-for-dnsmasq.conf` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/adblock-for-dnsmasq.conf) | [官网地址](https://anti-ad.net/anti-ad-for-dnsmasq.conf) | dnsmasq及其衍生版本 |
| `anti-ad-easylist.txt` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-easylist.txt) | [官网地址](https://anti-ad.net/easylist.txt) | AdGuardHome（DNS过滤） |
| `anti-ad-adguard.txt` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-adguard.txt) | [官网地址](https://anti-ad.net/adguard.txt) | AdGuard（匹配整个URL的域名部分） |
| `anti-ad-domains.txt` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-domains.txt) | [官网地址](https://anti-ad.net/domains.txt) | Pi-Hole或其他。([白名单](https://raw.githubusercontent.com/privacy-protection-tools/dead-horse/master/anti-ad-white-list.txt)) |
| `anti-ad-surge.txt` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge.txt) | [官网地址](https://anti-ad.net/surge.txt) | Surge或其他工具。 |
| `anti-ad-surge2.txt` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt) | [官网地址](https://anti-ad.net/surge2.txt) | Surge或其他工具，DOMAIN-SET 格式性能更好。 |
| `anti-ad-clash.yaml` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-clash.yaml) | [官网地址](https://anti-ad.net/clash.yaml) | Clash Premium。 ([白名单](https://raw.githubusercontent.com/privacy-protection-tools/dead-horse/master/anti-ad-white-for-clash.yaml)) |
| `anti-ad-smartdns.conf` | [link](https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-smartdns.conf) | [官网地址](https://anti-ad.net/anti-ad-for-smartdns.conf) | SmartDNS ([白名单](https://raw.githubusercontent.com/privacy-protection-tools/dead-horse/master/anti-ad-white-for-smartdns.txt)) |

使用官网地址，速度更稳定

使用 anti-AD 能够屏蔽广告域名，能屏蔽电视盒子广告，屏蔽 APP 内置广告，同时屏蔽了一些日志收集、大数据统计等涉及个人隐私信息的站点，能够保护个人隐私不被偷偷上传。

### [banbendalao](https://github.com/banbendalao)/**[ADgk](https://github.com/banbendalao/ADgk)**

- [https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt](https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt)
- [https://raw.iqiq.io/banbendalao/ADgk/master/ADgk.txt](https://raw.iqiq.io/banbendalao/ADgk/master/ADgk.txt)

百度搜索结果内屏蔽百家号

- [https://raw.githubusercontent.com/banbendalao/ADgk/master/kill-baidu-ad.txt](https://raw.githubusercontent.com/banbendalao/ADgk/master/kill-baidu-ad.txt)
- [https://raw.iqiq.io/banbendalao/ADgk/master/kill-baidu-ad.txt](https://raw.iqiq.io/banbendalao/ADgk/master/kill-baidu-ad.txt)

### Youtube 去广告

- [https://gist.githubusercontent.com/Ewpratten/a25ae63a7200c02c850fede2f32453cf/raw/b9318009399b99e822515d388b8458557d828c37/hosts-yt-ads](https://gist.githubusercontent.com/Ewpratten/a25ae63a7200c02c850fede2f32453cf/raw/b9318009399b99e822515d388b8458557d828c37/hosts-yt-ads)

### 广告终结者

广告终结者使用的拦截规则，基于 ChinaList + EasyList 修正维护

- [https://sub.adtchrome.com/adt-chinalist-easylist.txt](https://sub.adtchrome.com/adt-chinalist-easylist.txt)

### I don’t care about cookies

屏蔽网站的 cookies 相关的警告

- [https://www.i-dont-care-about-cookies.eu/abp/](https://www.i-dont-care-about-cookies.eu/abp/)

## [Hosts 过滤器](https://www.dujin.org/tag/hosts-%e8%bf%87%e6%bb%a4%e5%99%a8 "View all posts in Hosts 过滤器")

1. 大圣净化 – 针对国内视频网站  
    `https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts`
2. 1024\_hosts – 1024网站和澳门皇家赌场  
    `https://raw.githubusercontent.com/Goooler/1024_hosts/master/hosts`
3. Google hosts – 提高网站访问速度  
    `https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts`
4. Hblock – 综合多种源集合体屏蔽广告跟踪和恶意软件  
    `https://hblock.molinero.xyz/hosts`
5. Mvps – 屏蔽美欧地区英文网站相关的广告  
    `https://winhelp2002.mvps.org/hosts.txt`
6. neoHosts – 国内屏蔽挖矿统计JS&360&百度&法轮功等  
    `https://hosts.nfz.moe/full/hosts`
7. StevenBlack – 屏蔽国外网站广告-国外维护  
    `https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts`
8. yhosts – 屏蔽国内网站广告-国内维护  
    `https://raw.githubusercontent.com/vokins/yhosts/master/hosts`
9. YousList – 屏蔽韩国网站广告  
    `https://raw.githubusercontent.com/yous/YousList/master/hosts.txt`
