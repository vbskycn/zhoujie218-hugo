---
title: "GCP 挂载 google drive 网盘，搭建emby的演示"
date: "2020-07-22"
categories: 
  - "diannaowangruo"
url: "/archives/1793.html"
---

### [GCP 挂载 google drive 网盘，搭建emby的演示](https://bbsok.cf/archives/1312)

<iframe title="媲美netflix，emby 搭建 第二期 google云搭建+rclone挂载googledrive，以及服务器首次设置" src="https://www.youtube.com/embed/C6VYVDEAX1o?feature=oembed" width="525" height="295" frameborder="0" allowfullscreen="allowfullscreen" data-mce-fragment="1"></iframe>

建议1.7以上内存，20以上空间 Ubuntu 18.04 LTS 台湾 1、安装rclone curl https://rclone.org/install.sh | sudo bash

2、配置 rclone config 命名：emby

3、挂载 mkdir -p /home/gdrive

/usr/bin/rclone mount emby: /home/gdrive \\ --umask 0000 \\ --default-permissions \\ --allow-non-empty \\ --allow-other \\ --buffer-size 32M \\ --dir-cache-time 12h \\ --vfs-read-chunk-size 64M \\ --vfs-read-chunk-size-limit 1G &

——————————

4、查看挂载 df -h 5、自动挂载 cat > /etc/systemd/system/rclone.service <<EOF \[Unit\] Description=Rclone AssertPathIsDirectory=LocalFolder After=network-online.target

\[Service\] Type=simple ExecStart=/usr/bin/rclone mount emby: /home/gdrive \\ --umask 0000 \\ --default-permissions \\ --allow-non-empty \\ --allow-other \\ --buffer-size 32M \\ --dir-cache-time 12h \\ --vfs-read-chunk-size 64M \\ --vfs-read-chunk-size-limit 1G ExecStop=/bin/fusermount -u LocalFolder Restart=on-abort User=root

\[Install\] WantedBy=default.target EOF

6、设置启动 systemctl start rclone 7、开启启动 systemctl enable rclone 8、安装bbrplus wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-

双倍发包 加速 NetSpeed/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh

9、虚拟内存 wget https://www.moerats.com/usr/shell/swap.sh && bash swap.sh

10，安装emby 新版本是4.4.3 请自行更换下载连接和安装包名称 wget https://github.com/MediaBrowser/Emby.Releases/releases/download/4.4.2.0/emby-server-deb\_4.4.2.0\_amd64.deb dpkg -i emby-server-deb\_4.4.2.0\_amd64.deb

嘎鱼饭 google drive 资源 挂载 搭建后 效果如下：

\[caption id="attachment\_1795" align="alignnone" width="854"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-42-854x1024.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/07/unnamed-file-42.png) \[/caption\]

**Emby免费体验服务器** 地址：emby.gayufan.com 端口：8096 账号：gayufan.com 密码：在嘎鱼饭官网首页获取 [嘎鱼饭官网](https://gayufan.com/)
