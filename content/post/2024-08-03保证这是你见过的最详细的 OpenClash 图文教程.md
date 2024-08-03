~~~
title: "保证这是你见过的最详细的 OpenClash 图文教程"
date: "2024-08-03"
categories: 
  - "diannaowangruo"
tags: 
  - "24-08"
  - "openwrt"
  - "openclash"
  - "mosdns"
  
url: "/archives/openclash-mosdns-dns.html"
~~~



# 介绍



保证这是你见过的最详细的 OpenClash 图文教程（本教程参靠网友Aethersailor配置教程）



## 本教程所实现的效果



严格按照本教程的内容去设置你的 OpenClash 插件，加一个 Mosdns 即可实现以下功能：

1. **完美的 DNS 解析分流**,大陆域名使用运行商 DNS 或者你设置的 DNS 进行解析，国外域名使用节点服务器的 DNS 进行解析，取得理论上的最佳最快解析结果；
2. **DNS 无污染，无泄漏**；
3. **丰富的分流规则**，具备大陆和国外分流功能，流媒体/ChatGPT 等服务均可以选择特定地区节点分流或者特定节点分流，可以搭配 OpenClash 的流媒体解锁探测功能使用；
4. **节点自动测速优选**；
5. **大陆域名和 IP 均会绕过 OpenClash 内核**，加快访问速度提升下载性能；
6. 在宽带拥有 IPv6 以及机场支持 IPv6 出站的情况下，**实现 OpenClash 和 IPv6 的完美兼容**；
7. 每日自动更新上游规则碎片，一次设置，长期无人值守，不用折腾。即使 OpenClash 出现问题未能启动，也不影响正常上网。

分流非常精确

![image-20240803143122558](https://img-cloud.zhoujie218.top/2024/08/03/66adcebb29c7e.png)

- ### 关于 IPv6 

如果是爱快+OP会泄漏dns，我目前没有搞定，openwrt做主路由可以按下面的教程

在确保你的节点支持 IPv6 出站的情况下，搭配下面的教程实现 OpenClash 和 IPv6 的完美兼容
https://github.com/Aethersailor/Custom_OpenClash_Rules/wiki/OpenWrt-IPv6-设置教程

不清楚自己的节点是否支持 IPv6 的话，可以向机场客服发工单来确定，或者按照教程内容进行设置后测试节点如果不具备 IPv6 出站能力再关闭 OpenClash 的 IPv6 功能



- ### 关于 DNS

  

强烈建议使用运营商通告的 DNS，不论是解析速度还是结果的科学性，都不是第三方 DNS 可以比拟的

三大运营商的 DNS 都不存在对国内域名的污染，而且绝对是你的线路的最优解析结果，根本不需要用第三方 DNS 替代，更不需要用 SmartDNS 或 Mosdns 之类的工具选优，本方案中的Mosdns 的上游只埴一个运营商通告的 DNS就可以了

我这里使用Mosdns 是为了去广告，缓存dns，和一些更灵活的策略，你也可以不用，只用openclash本身的即可。

以本人所在的城市为例，电信和联通线路的 DNS 延迟都非常低，及时是高峰时段，延迟也只有1-2毫秒，白天的话可以稳定只有 1 毫秒的延迟，这时候还去用 DNS 插件很有可能是负优化
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcc1122f80.png) 而且根据本人长期测试，运营商 DNS 提供的国内域名解析服务永远是最优最近的 CDN，和 DNS 插件优选的解析结果一致
按照本人的教程设置后，运行商 DNS 只用于解析中国大陆域名，不存在污染问题，也不用担心运营商 DNS 没有 DoT/DoH 加密。海外域名全部远端解析取得离机场最近的 CDN，更没有污染
除非你是使用的长城宽带之类的存在流量穿透的宽带，DNS 延迟很高或无法正确解析到离你地理位置最近的 CDN，否则根本就没有必要用 DNS 优化插件
**如果你非要认为 1ms 的解析时间差距会明显影响上网体验，那我无话可说，一定要使用第三方 DNS 或者 DNS 优化插件的话，教程中对应步骤会提及如何进行设置**

- ### 关于广告过滤

  我使用的是mosdns中的过滤，可以使用自带的，也可以使用自己设置的。

![image-20240803142801903](https://img-cloud.zhoujie218.top/2024/08/03/66adcdf27c8a5.png)



# OpenClash 图文设置教程



严格按照文字和图片中的内容进行设置，其他选项不清楚如何设置的，照抄即可。
一定要认真阅读，一定要认真阅读，一定要认真阅读，不要跳着看，否则可能会错过关键设置！
OpenWrt 做主路由和旁路由时的设置差异，相关的步骤中会提及，按照你的情况选择就行
不懂的情况下不要自己乱改设置！必须使用本仓库的订阅模板！否则不保证效果正常
个别需要你自己根据实际情况进行选择的步骤，会讲明原理，只要智商正常都能看懂，仔细阅读即可。

## 准备工作



### 查看运行商通告的 DNS



旁路由跳过此步骤
首选确保你的 WAN 口设置中勾选了“自动获取 DNS 服务器”，这样才能获取到运营商下发的 DNS
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcc2c21ef7.png)
然后在 OpenWrt 的首页查看并记录运营商下发给你的 DNS，如果你打算使用其他的国内第三方 DNS，可以跳过此步骤。
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcc37a47bd.png)
如果你使用的是旁路由，自行到主路由中查看运营商 DNS。

### 确保 OpenWrt 可以正常访问 Github



**如果你的 OpenWrt 一直可以正常访问 Github 可以跳过此步骤**
确保你的路由器可以正常访问 Github，你可以提前使用上面的 hosts 一键脚本来合并 [GitHub520](https://github.com/521xueweihan/GitHub520) 加速规则至本机，或者提前在 OpenClash 中启用 Github 地址修改功能
进入**OpenClash > 覆写设置 > 常规设置**，在 Github 地址修改功能的下拉菜单中选择一个 CDN 节点，推荐选择 testingcf，建议根据自己的实际网络情况多做尝试，点击页面下方的“应用配置”即可生效。
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcc3b3d1ef.png)
准备工作完成，开始设置 OpenClash

## 设置 OpenClash 常规设置



以下列出了 OpenClash 的设置内容，每个需要设置的页面均有图文说明，按照教程逐页进行设置即可 所有未提及的页面，均不需要设置

### 模式设置



首先设置运行模式，在页面下方点击切换到 Fake-IP 模式，然后上方的运行模式选择 **Fake-IP（增强）** ，勾选使用 Meta 内核，然后点击页面下方的“保存配置” Fake-IP（增强）模式可以提供最佳的性能，如果出现了 NAT 问题，可以尝试切换为 Fake-IP（混合）模式。记得要勾选 UDP 转发，如果你的固件包含了 Docker 功能，直接选择 Fake-IP（混合）模式即可
为什么使用 Meta 内核？因为 Premium 内核和 TUN 早已不更新，且 Meta 内核有嗅探功能，几乎是唯一选择
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcba397590.png)

### 流量控制



按照图中设置进行勾选设置，并填写大陆域名 DNS 为你的运营商通告的 DNS
如果你不想使用运营商的 DNS，此处可以填写你想使用的国内第三方 DNS，比如 223.5.5.5
如果你使用了 mosdns 之类的 DNS 优化插件，那么这里填写 127.0.0.1:[mosdns 端口号]，比如 127.0.0.1:5335
再次建议使用你的运营商通告的 DNS 来取的最快最准确的国内解析结果！
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcba4e420c.png)

### DNS 设置



设置使用 Dnsmasq 进行转发，顺手点一下“Fake-IP 持久化缓存清理”按钮，不用管是否提示出错，然后点击页面下方的“保存配置”
注意下方的 Dnsmasq 缓存选项，一定要禁用

### 流媒体增强（可选）



此处设置主要用于使 OpenClash 可在流媒体分流时在众多节点中自动选择解锁对应区域的流媒体服务的节点，此功能主要用于在一些流媒体解锁不稳定且混乱的杂牌机场中自动寻找对应的节点。
**如果你所使用的机场的流媒体解锁服务相对比较稳定，或者已经知晓你所使用的机场哪些节点可以解锁你所需要的区域的流媒体服务，则可以跳过此页面的设置，设置完成后在 Clash 的控制面板中自行选择即可。** 如果你要使用自动选择节点的功能，首先勾选你要使用的流媒体服务，比如 Netflix，然后按照本教程的策略组名称在“策略组筛选”中进行填写，本教程中流媒体相关的策略组包括 Netflix、YouTube、Disney+等等
解锁区域填写你要解锁的流媒体服务区域，比如你要解锁新加坡区就填写SG。解锁节点筛选填写需要测试的节点名称的关键词，比如填写“香港|新加坡”就会在包含以上关键词的节点中进行筛选
例如设置了 Netflix 和 SG，如此设置后，OpenClash 启动后就会在你订阅的节点的清单中自动寻找解锁新加坡（SG）区域的 Netflix 服务的节点作为分流策略组“Netflix”的指定节点
设置后记得点击页面下方的“保存配置”，再次提醒此页是可选功能，非必要不使用
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcba72d18d.png)

### IPv6 设置



如果你打算启用 IPv6 功能，并且你的节点支持 IPv6 出站，则按照本仓库的教程中的 IPv6 设置教程完成 OpenWrt 的 IPv6 设置后，再设置此页面即可。
https://github.com/Aethersailor/Custom_OpenClash_Rules/wiki/OpenWrt-IPv6-设置教程
如果你的节点不支持 IPv6 出站，或者你的 OpenWrt 没有开启 IPv6 功能，则禁用“IPv6 流量代理”和“允许 IPv6 类型 DNS 解析”
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbac74300.png)

### GEO 数据库订阅



OpenClash 一些兜底的分流数据库，保持最新没有坏处。按照图中设置即可，具体用途不多做解释，可以自行查找相关资料。
注意，每次数据库更新成功后 OpenClash 会自动重启，建议设置更新时间为不用网的时候，比如凌晨。
设置完后点击页面下方的“保存设置”，然后顺手把三个“检查并更新”按钮都点一遍。在 OpenClash 的“运行日志”页面可以查看更新结果，此操作可以顺带验证你的 OpenWrt 是否能顺利访问Github 或者你在之前设置的 CDN 比如 testingcf
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbac73885.png)

### 大陆白名单订阅



OpenClash 一些兜底的分流名单，保持最新没坏处。按照图中设置即可，具体用途不多做解释，可以自行查找相关资料。
注意，每次白名单更新成功后 OpenClash 会自动重启，建议设置更新时间为不用网的时候，比如凌晨。
设置完后点击页面下方的“保存设置”，然后顺手把“检查并更新”按钮点一下。在 OpenClash 的“运行日志”页面可以查看更新结果，此操作可以顺带验证你的 OpenWrt 是否能顺利访问Github 或者你在之前设置的 CDN 比如 testingcf
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcc4aaa49e.png)

### 版本更新



此页面用于更新 OpenClash 的内核以及 OpenClash 自身
建议选择 dev 版本，然后点击下方的一键更新。在 OpenClash 的“运行日志”页面可以查看更新结果，此操作可以顺带验证你的 OpenWrt 是否能顺利访问Github 或者你在之前设置的 CDN 比如 testingcf
如果使用过程中遇到错误，可以选择 master 版本，再点击一键更新即可切换回稳定版
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcc4dd8de7.png)

至此，OpenClash 中的常规设置设置完成

## 设置 OpenClash 覆写设置



### DNS 设置



OpenWrt 是主路由的情况下，此处勾选按照图中进行勾选。使用运营商通告的 DNS，勾选“追加上游 DNS”。
旁路由不要勾选“追加上游 DNS”
如果你不打算使用运营商通告的 DNS 服务器，则不要勾选“追加上游 DNS”。如果你有 DDNS 服务的域名，填写进下方的 Filter 中。
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbacdccb2.png)
**页面下方有 NameServer、Fallback 和 Default-NameServer 三个服务器分组，在本教程中应当取消全部的服务器勾选。** **如果你坚持不愿意使用运营商提供的 DNS**，则在 NameServer 中保留第一个勾选，并填入你要使用的国内第三方 DNS 的地址，例如 223.5.5.5，并且不要勾选“追加上游 DNS”。
**如果你使用 DNS 优化插件（如 mosdns等）**，则在 NameServer 中保留第一个勾选，并填入 127.0.0.1:[mosdns 端口号]，并且不要勾选“追加上游 DNS”。
**如果你的 OpenWrt 是旁路由**， 则在 NameServer 中保留第一个勾选，并填入运营商 DNS 或者你要使用的其他国内第三方 DNS，并且不要勾选“追加上游 DNS”。
注意 NameServer 只用做 OpenClash 的规则判断的，而且本教程中 OpenClash 配置了绕过大陆功能，所以此处填入多个服务器并没有任何意义，更不要自作聪明的填写国外 DNS 服务器
**再一次强烈建议此处全部取消勾选，配合上面一页设置的“追加上游 DNS”来使用运营商 DNS 从而提高解析速度！（仅限 OpenWrt 是主路由的情况下）**
为什么要取消 Fallback 服务器？在取消 Fallback 服务器勾选的情况下，OpenClash 会把域名发送到远端的机场服务器上进行解析，只有这样才会根据不同区域的节点取得理论上的最佳解析结果
设置完成后，点击页面下方的“保存配置”按钮
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbae886b2.png)
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbafba963.png) ![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbafc5908.png)

### Meta 设置



所有设置按照图中进行即可
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbb454667.png)

### 开发者选项



按照图中内容，找到 Hash Demo 下的对应代码，取消注释并修改 true 为 false
`ruby_edit "$CONFIG_FILE" "['experimental']" "{'sniff-tls-sni'=>false}"`
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbb4ca448.png)



### 配置订阅



在页面中设置一个更新时间，因为本教程中使用的订阅模板使用了大量的第三方规则，而这些规则中的大部分是每天更新的，因此建议同样设置订阅更新时间为每天更新。
OpenClash 在更新订阅的过程中会短暂中断，所以建议设置在不用网的时间段内更新，比如凌晨

设置好后点击“保存配置”，然后点击“添加”按钮，添加一个订阅
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbb55f3f4.png)
按照图中内容填入订阅信息即可

注意，填入的订阅链接，必须是普通的节点订阅链接，或者 V2RayN 使用的订阅链接，不能填入机场提供的 Clash 订阅链接，否则无法转换
配置文件名随意填写。注意订阅转换模板选择“自定义模板”然后在下方填入本仓库的自定义模板地址：

https://raw.githubusercontent.com/vbskycn/myrules/master/Custom/cfg/Custom_Clash_full.ini

注意！必须使用本项目的订阅转换模板才能实现免套娃无 DNS 泄露！
当然了你也可以自写模板或者用其他的无泄漏模板
**注意，某些机场的订阅链接会出现订阅转换后的所有节点均无法使用的情况，请启用此处的“跳过证书验证”功能再重新更新订阅 ** 

![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbb61559e.png)

最后点击下方的“保存配置”返回到配置订阅页面，此时整个设置工作已完成



### **这里强烈建议，自己搭建一个转换服务，不会有节点泄漏的风险，教程在这里**

CF大善人免费提供，几分钟就搭建好了

https://www.youtube.com/watch?v=X7CC5jrgazo&feature=youtu.be



![image-20240803145309980](https://img-cloud.zhoujie218.top/2024/08/03/66add3d93765d.png)



得到了订阅地址，就不用写模板什么的，直接填写入自己的订阅地址设置定时更新就可以了





## 更新配置并启动



点击配置订阅页面中的“更新配置”按钮，OpenClash 即可开始更新配置并启动
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbb75bd00.png)









### 运行日志



在上一步操作中点击“更新配置”后，切换到运行日志页面观察 OpenClash 的启动情况
出现“OpenClash 启动成功，请等待服务器上线！”后，即表示 OpenClash 已经启动成功，但大陆域名绕过内核功能尚在生效中
稍等片刻，出现“提示：检测到 Dnsmasq 正常工作，还原防火墙 DNS 劫持规则...”，则为大陆域名绕过内核功能已经生效
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcc69af5d9.png)



### Dashboard 控制面板



在 OpenClash 的运行状态页面中，点击 Dashboard 控制面板按钮启动控制面板
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbbc79ea4.png)
在控制面版中可以按照个人喜好以及机场节点的情况更改对应分流策略的节点
本仓库的订阅转换模板中包括的策略已经足以应对大部分的分流需求
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbbdf0b7a.png)

至此，OpenClash 已经完美设置完毕！日常使用中几乎不需要打理，相关规则会根据你的设置每日自动更新上游规则，理论上只要不遇到bug，永远不用去人为操作。

## 检验结果



下面检查以下你按照本教程实现的效果吧！
注意，Clash 面板中，“漏网之鱼”策略组不要选择直连！

### 检查 DNS 是否存在泄漏



访问 IPLEAK.NET 检查 DNS 是否存在泄漏
https://ipleak.net/
正常情况下，页面上方应当出现你的机场节点的 IPv4 和 IPv6 地址，页面下方无中国大陆 DNS 出现即为 DNS 无泄漏情况
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbbdcc22a.png)

### 检查 IPv6 分流情况



访问 IPv6 test：https://ipv6-test.com/
网页中的“Address”项目应当显示当前节点的 IPv4 和 IPv6 地址，证明节点的 IPv4 和 IPv6 出站均正常工作
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbbe590ed.png)
分别访问 IPv6 测试网站 test-ipv6 的国内镜像站点和国外镜像站点
国内站点：https://testipv6.cn/
访问国内镜像站点时，检测页面上应当出现你的宽带的 IPv4 和 IPv6 地址以及国内运营商名称（比如 CHINA UNICOM 即为中国联通），并且以10/10的评分通过测试
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbbf96da3.png)
国外站点：http://test-ipv6.com/
访问国外镜像站点时，检测页面上应当出现你的机场节点的 IPv4 和 IPv6 地址以及节点服务器的网络运营商名称（比如 Akari Networks 之类的境外网络运营商），并且以10/10的评分通过测试
注意，由于上游分流规则的变化，国外镜像站点有可能检测到的仍然是国内的 IPv6 地址，忽略这种情况即可，以“IPv6 test”网站的检测结果为准
![img](https://img-cloud.zhoujie218.top/2024/08/03/66adcbc0acef1.png)

如果以上两个网站测试均通过，即为 IPv6 已经完美分流

**至此，你的 OpenWrt 上已经拥有了绝对完美、秒杀全网大部分教程贴的 OpenClash 完美设置，且所有的细节设置都已经尽力为性能、安全和效率而优化，尽情享受吧！**

