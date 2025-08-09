---
title: "Frp内网穿透实现 以服务器CentOS+客户端OpenWrt为例"
date: "2022-07-01"
categories: 
  - "diannaowangruo"
tags: 
  - "frp"
  - "openwrt"
url: "/archives/2436.html"
---

要想将自己提供的服务发布到Internet，需要公网IP地址。由于IPv4地址资源紧张，家庭宽带获取IPv4公网地址难度大、代价高。采用内网穿透技术，可通过拥有公网IPv4地址的服务器来访问内网资源。

　　内网穿透可以采用花生壳等软件实现，也可自行搭建服务器完成。本文在CentOS（服务器）+ OpenWrt（客户端）的结构下，介绍利用Frp实现内网穿透的方法。

　　【注意】Frp分为服务器端和客户端，服务器端名为：frps，客户端名为frpc。安装时务必注意区分。

![](https://img-cloud.zhoujie218.top/wp-content/uploads/2022/07/20220701041650268.png)

一、资源获取

1. Frp项目地址 [https://github.com/fatedier/frp](https://github.com/fatedier/frp)
    
2. Frp发行安装包 [https://github.com/fatedier/frp/releases](https://github.com/fatedier/frp/releases)
    
3. Frp文档 [https://gofrp.org/docs/](https://gofrp.org/docs/)
    

二、CentOS服务器配置

1. Frps安装包获取 1）前往 1.2 中的发行安装包地址，寻找适合您的安装包。如x86平台64位的linux机器，应该使用名为 frp\_x.xx.x\_linux\_amd64.tar.gz 的安装包（x.xx.x为版本号）。选中安装包名称，右键复制链接地址。

2）前往服务器执行下列命令，将安装包下载到服务器CentOS系统中。

wget [https://github.com/fatedier/frp/releases/download/v0.32.1/frp\_0.32.1\_linux\_amd64.tar.gz](https://github.com/fatedier/frp/releases/download/v0.32.1/frp_0.32.1_linux_amd64.tar.gz) 3）执行下列命令，解压安装包。

tar -xvf frp\_0.32.1\_linux\_amd64.tar.gz

2. Frps安装 1）执行下列命令，为Frps程序新建一个目录。

mkdir /etc/frps 2）将解压的Frp文件复制到Frps程序目录内。

mv frp\_0.32.1\_linux\_amd64/\* /etc/frps/

3. 注册系统服务 1）新建Frps服务文件

vim /usr/lib/systemd/system/frps.service 2）按键盘 i 键，进入编辑状态。写入如下代码（也可直接按鼠标右键粘贴）。然后按 ESC 按键，输入 :wq 回车后保存并退出。

\[Unit\] Description=The nginx HTTP and reverse proxy server After=network.target remote-fs.target nss-lookup.target

\[Service\] Type=simple ExecStart=/etc/frps/frps -c /etc/frps/frps.ini KillSignal=SIGQUIT TimeoutStopSec=5 KillMode=process PrivateTmp=true StandardOutput=syslog StandardError=inherit

\[Install\] WantedBy=multi-user.target 3）重载配置文件

systemctl daemon-reload 4）启动服务

systemctl start frps 5）添加开机自启

systemctl enable frps

4. 编辑服务器端配置文件 1）打开配置文件

vim /etc/frps/frps.ini 2）写入如下内容后保存。配置文件其他的的选项可前往此地址查看：

[https://gofrp.org/docs/reference/server-configures/](https://gofrp.org/docs/reference/server-configures/)

\[common\] bind\_port = 7000

vhost\_http\_port = 80 vhost\_https\_port = 443

token = abcd1234

# Web

# dashboard\_port = 8080

# dashboard\_user = admin

# dashboard\_pwd = 123

【说明】

　　行2：提供服务的端口。后续Frpc客户端将绑定服务器的该端口，完成与服务器的通信。

　　行4：HTTP端口，可通过客户端绑定的域名（域名需解析至服务器的IP），加上此端口来访问对应的内网HTTP服务。

　　行5：HTTPS端口，可通过客户端绑定的域名，加上此端口来访问对应的内网HTTPS服务。

　　行7：Token认证口令，客户端需使用该口令才能与服务器建立通信。

　　行10：监控Web面板端口。（需使用时可将前面的 # 去掉）。

　　行11：监控Web面板用户名。

　　行12：监控Web面板密码。（此密码易泄露，请勿设置常用密码）

3）重启服务使配置生效

systemctl restart frps

5. 防火墙放通 1）配置CentOS系统防火墙

　　在系统防火墙内，放通上述配置文件的TCP端口。

　　具体方法请自行查阅CentOS系统防火墙配置。根据版本不同，有iptables和firewalld两种防火墙，二者配置方法稍有不同。也可采用管理软件，如宝塔面板、小皮面板等，进行可视化配置。

2）配置服务器安全组

　　前往服务器IDC管理面板（如腾讯云、阿里云等控制中心），配置安全组，放通这些TCP端口。

三、OpenWrt客户端配置 　　在2.1获取的安装包中，已经包含了Frpc客户端软件。可在客户端再次获取该安装包，采用同样的方式安装Frpc客户端即可。

　　在OpenWrt内，也提供了Frpc的可视化软件，可进行安装。本文介绍OpenWrt可视化安装与配置方法。如希望在终端内使用命令安装与配置，可参考Frps的配置方法、Frpc的配置选项。Frpc配置文件的选项见：

[https://gofrp.org/docs/reference/client-configures/](https://gofrp.org/docs/reference/client-configures/)

1. OpenWrt安装Frpc 1）登录OpenWrt管理后台

2）进入：系统->Software。点击 Update lists 更新软件列表后，在Filter处输入 frpc，找到名为 luci-i18n-frpc-zh-cn 的软件，点击右侧安装按钮，将自动安装该软件和 frpc、luci-app-frpc等其他依赖。

2. 配置Frpc 安装完毕后刷新浏览器。进入：服务->frp 客户端。在 “通用设置” 选项卡中，设置服务器地址、端口、令牌及其他可选项。

　　1）服务器地址：填写安装有Frps的服务器IP地址。

　　2）服务器端口：填写Frps配置文件 bind\_port 选项设置的端口，本文的示例配置文件对应的此处为7000。

　　3）令牌：填写Frps配置文件 token 选项设置的令牌。

　　配置完毕后，点击页面右下角的 保存并应用 按钮。并前往 系统->启动项 中重启frpc服务。

　　至此，Frp服务器和客户端搭建完毕，可在OpenWrt内的Frp客户端页面，查看frp客户端是否在运行状态。也可在服务器的Frp监控面板（前提是配置文件配置了监控面板的参数），查看是否有客户端建立了连接。后续，在客户端内添加代理服务，即可在Internet上访问到局域网内的服务。

四、添加代理服务

1. 代理服务设置 在 服务->frp 客户端 页面的最下方，输入新增的服务名，点击 “新增” 按钮。设置 代理类型、本地IP、监听端口、远程端口和其他可选项。

　　1）代理类型：根据使用的服务不同，有不同的代理类型。如：希望将网页服务发布到公网，则选择HTTP或HTTPS类型。希望使用SSH远程管理、Windows远程桌面，则选择TCP类型。希望使用即时通讯服务，则选择UDP类型。选择什么类型，需明确自己要提供什么服务到公网。

　　2）本地IP：提供服务的局域网设备IP。如局域网内IP为192.168.1.10的主机作为Web服务器向公网提供服务，则在此输入192.168.1.10

　　3）监听端口：局域网设备向公网提供服务的服务端口。

　　4）远程端口：外网用户在Internet上访问您提供的服务所使用的端口。设定该端口后，外网用户可通过 “Frps服务器IP:远程端口” 的方式，访问到局域网内 “本地IP:监听端口” 所对应的服务。

　　【注意】代理类型为HTTP或HTTPS时，没有该选项，远程端口为Frps服务器配置文件内，配置选项为 vhost\_http\_port、vhost\_https\_port 设置的端口。本文的示例配置文件内，这两个端口为 80、443。

　　配置完毕后，点击弹出内的 “保存” 按钮，并再次点击网页内的 “保存并应用” 按钮。然后前往 系统->启动项 中重启frpc服务。

　　【注意】如果代理类型为HTTP或HTTPS类型，经测试必须在新增的 “HTTP设置” 选项卡内，绑定一个域名。域名需指向Frps主机的IP地址或别名地址。否则开启Frpc服务将失败。

　　访问HTTP或HTTPS服务时，采用 “域名:Frps配置文件指定的端口” 方式访问，服务器将根据域名的不同，解析至不同的局域网HTTP或HTTPS服务。

2. 防火墙放通 1）局域网内提供服务的设备，需放通其提供的服务所使用的入站端口（Frpc内设置的监听端口）。

2）如果代理类型不是HTTP或HTTPS，则还需在服务器CentOS系统内放通向Internet用户提供服务的端口（Frpc内设置的远程端口）。

3）如果代理类型不是HTTP或HTTPS，则还需在服务器IDC管理面板内的安全组中，放通向Internet用户提供服务的端口（Frpc内设置的远程端口）。

五、解决OpenWrt的Frpc掉线问题 　　如果Frpc安装在OpenWrt内，当OpenWrt刚启动完毕时，必然无法立即建立到Internet的连接。而是需要经历PPPoE拨号 或 等待DHCP服务器派发地址 的过程。在未建立到Internet连接时，Frpc服务的开机自启将启动失败，而后需要手动启动Frpc。通过模拟守护进程定时监测Frpc服务的状态，即可解决该问题。

```
   进入OpenWrt管理Web面板，前往 系统->计划任务 页面。在计划任务中另起一行，添加如下代码即可解决该问题。
```

_/1_ \* if \[ $(/etc/init.d/frpc status) != "running" \]; then /etc/init.d/frpc restart; fi 【说明】

1）定时时间

　　① 从左到右依次为：分 时 日 月 年。\*代表通配符，也可输入具体数字。

　　　　例如：0 7 表示每天7时0分执行计划任务。

- - - - - - 表示每分钟执行计划任务。

　　② _/1_ _中的_/1表示每。如在分钟上，设置\*/5，表示每5分钟。

2）任务代码

　　/etc/init.d/frpc status 可获取到frpc服务的状态，通过$()取得返回值，与 “running” 进行比较，如果不在 “running” 状态，则使用 /etc/init.d/frpc restart 重启服务。
