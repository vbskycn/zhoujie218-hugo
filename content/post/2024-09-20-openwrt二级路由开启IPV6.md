---
title: "openwrt二级路由开启IPV6"
date: "2024-09-20"
categories: 
  - "diannaowangruo"
tags: 
  - "ipv6"
  - "openwrt"
  - "二级路由"
  - "路由"
url: "/archives/2645.html"
---

# openwrt二级路由开启IPV6

有了公网IPV4，还想要ipv6,便研究了一下公网IPV6。网上大部分是将光猫改为桥接，然后路由拨号，获取公网IPV6地址，但目前不想这样做。研究一下，openwrt下二级路由下的IPV6获取。

按照网上的说明，二级路由一般使用中继的方式获取，照猫画虎，试了一下

![image-20240920122325221](https://img-cloud.zhoujie218.top/2024/09/20/66ecf8c2a4387.png)

## 1、首先wan6设置

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f1a5015.png)

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f3e65ad.png)

## 2、然后lan口设置

![](https://i-blog.csdnimg.cn/blog_migrate/0c65d6c195af6b6f3d5f4f0daea32dd0.png)

全部中继模式

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f299a4c.png)

## 3、使用TTYD或SSH进入后台(重要)

修改/etc/config/dhcp,增加以下内容

![image-20240920121451712](https://img-cloud.zhoujie218.top/2024/09/20/66ecf6bf9fedd.png)

```yaml
config dhcp 'wan'
    option interface 'wan'
    option ignore '1'
    option ra 'relay'
    option dhcpv6 'relay'
    option ndp 'relay'
    option master '1'
```

## 4、openwrt设备重启，打开网络适配器信息，正常可以看到ipv6了

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f1a517f.png)

可是打开ipv6 test网站，却无法测试通过，显示无ipv6地址，什么鬼？

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f5d4e0a.png)

一番尝试之下，发现将wan/wan6防火墙的入站改为接受，可以通过，肯定是防火墙拦截了。

5、同样打开后台，在/etc/config/firewall中增加以下规则

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f68cc08.png)

好了，这下终于可以测过了

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f6f38e7.png)

公网IP,公网IP，使用别的网络应该也可以ping通，遂打开手机4G网络，ping电脑获取到的ip,什么情况，ping不通？？

又是防火墙的问题？？

后台执行以下几条指令，把ip6tables全干掉

```null
ip6tables -P INPUT ACCEPTip6tables -P FORWARD ACCEPTip6tables -P OUTPUT ACCEPT
```

正常ping通

![](https://img-cloud.zhoujie218.top/2024/09/20/66ecf5f7eddfd.png)
