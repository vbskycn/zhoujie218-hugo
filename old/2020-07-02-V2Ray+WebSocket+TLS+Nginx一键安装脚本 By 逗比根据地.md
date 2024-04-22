---
title: "V2Ray+WebSocket+TLS+Nginx一键安装脚本 By 逗比根据地"
date: "2020-07-02"
categories: 
  - "diannaowangruo"
tags: 
  - "v2ray"
url: "/archives/1771.html"
---

近期发现GFW防火墙再次升级！更换服务器重新搭建SS/SSR也会出现使用几分钟后就被阻断的情况，不同于以前的封IP/端口直接一刀切的阻断方式，而是疑似将本地IP+服务端IP临时拉入GFW黑名单致使本地ping服务端IP出现短暂性的超时，且其他区域无影响，一会儿又恢复了。

SS/SSR梯子大规模被封是因为SS/SSR的流量特征早就已经被精准识别，我尝试了多个SSR类混淆方案均会受到阻断。

而逗比根据地的V2Ray+WebSocket+TLS+Nginx脚本是将V2Ray梯子的流量特征伪装成正常网站HTTPS流量，以更好的混淆/绕过GFW检测防止被阻断。

经测试V2Ray+WebSocket+TLS+Nginx方案暂未出现被阻断的情况！

## **一、准备工作**

首先要有一台国外VPS/云服务器，推荐购买 [**搬瓦工VPS（低至49.99美元/年，优惠码+支付宝购买中文教程）**](http://www.wangchao.info/1711.html)。

之后需要一个域名，这类用途不建议在国内注册，海外服务商推荐 [**NameSilo**](https://www.namesilo.com/?rid=eb6f663id)（支付支付宝），.top或.xyz仅$0.99约合人民币7元/年，续费价格透明便宜，物美价廉！

## **二、一键安装脚本**

脚本适用于：Debian 9+ / Ubuntu 18.04+ / Centos7+

两个安装方式**（不兼容，二选一）**

**1.Vmess+websocket+TLS+Nginx+Website（推荐）**

bash <(curl -L -s https://raw.githubusercontent.com/wulabing/V2Ray\_ws-tls\_bash\_onekey/master/install.sh) | tee v2ray\_ins.log

**2.Vmess + HTTP2 over TLS**

bash <(curl -L -s https://raw.githubusercontent.com/wulabing/V2Ray\_ws-tls\_bash\_onekey/master/install\_h2.sh) | tee v2ray\_ins\_h2.log

 

**执行安装前先将域名解析A记录到VPS/云服务器IP，可解析www或任意其他二级域名，解析域名与安装配置域名一致即可，安装脚本配置端口选择443（默认）。**

安装成功后如下所示：

\[caption id="attachment\_1772" align="alignnone" width="441"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-29.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-29.png) \[/caption\]

**脚本管理命令**

启动 V2ray：

systemctl start v2ray

停止 V2ray：

systemctl stop v2ray

启动 Nginx：

systemctl start nginx

停止 Nginx：

systemctl stop nginx

**脚本相关目录**

Web 目录：

/home/wwwroot/levis

V2ray 服务端配置：

/etc/v2ray/config.json

V2ray 客户端配置：

执行安装时所在目录下的 v2ray\_info.txt

Nginx 目录：

/etc/nginx

证书目录：

/data/v2ray.key 和 /data/v2ray.crt

## **三、v2rayN Windows客户端下载/配置**

**Windows客户端下载地址：[http://down.wangchao.info/soft/v2rayN.zip](http://down.wangchao.info/soft/v2rayN.zip)**

打开软件，点击：服务器→添加\[VMess\]服务器：

\[caption id="attachment\_1773" align="alignnone" width="731"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-30.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-30.png) \[/caption\]

填上你设置的对应数据，请务必完全参照服务端返回的数据，服务端和客户端必须一致，如**地址（域名）**、**端口**、**用户ID**、**路径**等，**加密方式**一般为auto，**传输协议**为ws，**伪装类型**一般为none，**伪装域名**留空，开启tls和不安全传输，设置完保存。

右键V2RayN的系统栏小图标，点击**启用Http代理**，**Http代理模式**选择第二个**PAC模式**，最后再打开V2RayN软件面板，在**检查更新**里选择**更新PAC**。

到此，V2Ray就全部配置完成了。
