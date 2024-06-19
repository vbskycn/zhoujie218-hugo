---
title: "BT(宝塔面板)-Panel service startup failed"
date: "2020-02-05"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "bt"
url: "/archives/1180.html"
---

今天bt reload面板的时候遇到了Panel service startup failed这个错误，**init**.py这种错误提示有好几处。这完全就是升级不当造成的，应该是大鸟从5.9升级到6.X的时候没有升级好。遗留了这种错误。

大鸟升级的时候用的：BT(宝塔面板)5.9升级6.X-最牛叉的升级方案  这个升级方案，当时也是为了写这个教程，所以用了这个方法去升级，升级好了之后没什么大问题，但是遇到了两个错误，一个是宝塔终端不能用还有个就是 Panel service startup failed 这两个错误。

\[caption id="attachment\_1183" align="alignnone" width="1024"\]![BT(宝塔面板)-Panel service startup failed](http://img-cloud.zhoujie218.top/wp-content/uploads/2020/02/bt宝塔面板-panel-service-startup-failed20200205-1024x465.jpg) BT(宝塔面板)-Panel service startup failed\[/caption\]

今天大鸟准备解决宝塔终端不能用的问题，却发现了 Panel service startup failed 想来也是用计划任务那个方式升级的时候一些底层的代码没有更新，造成了这种兼容性的问题。这个问题如何解决：

#### 第一、修复重启面板

点击面板右上角修复，或者重启面板，这样有可能解决问题，如图：

\[caption id="attachment\_1184" align="alignnone" width="1024"\]![BT(宝塔面板)-Panel service startup failed](http://img-cloud.zhoujie218.top/wp-content/uploads/2020/02/bt宝塔面板-panel-service-startup-failed20200205-1-1024x128.jpg) BT(宝塔面板)-Panel service startup failed\[/caption\]

看着大鸟的提示的错误，修复面板肯定不行，这是很严重的兼容性的问题，升级不恰当造成的。我们看下一种方法。

#### 第二、重装面板

这个有点暴力了，但是大鸟只能用这个方法，我们可以ssh工具连接服务器，在命令行方式下面执行重装面板的命令。

这里是6.X的面板所以大鸟这里贴下命令：

1. yum install \-y wget && wget \-O install.sh http://download.bt.cn/install/install\_6.0.sh && bash install.sh

因为大鸟的面板环境都已经配置好，所以这个安装命令只是重新安装了面板，不会影响网站数据，当然，我们最好已经备份好了网站数据，让后来执行这个操作。

安装好之后，所有的web环境都不会改变，不过面板登录密码会被重置，我们需要自己修改或者记下新的密码。

到这里大鸟的问题解决了，连带宝塔终端不能用的问题都解决了，看来是升级不当造成的。

#### 第三、python错误

遇到这种错误解决起来容易点，错误代码如下：

1. Starting Bt\-Panel… failed
2. ——————————————————
3. Traceback (most recent call last):
4. File “main.py”, line 101, in <module>
5. if not os.path.exists(templatesConf): public.writeFile(templatesConf,’default’);
6. AttributeError: ‘module’ object has no attribute ‘writeFile’
7. ——————————————————
8. Error: BT\-Panel service startup failed.

错误原因：

python public包 跟面板冲突。如何解决呢？可以尝试使用下面的两条命令：

1. pip uninstall public
2. bt restart

第四、总结

额，大鸟在分享 ‘BT(宝塔面板)5.9升级6.X-最牛叉的升级方案’这篇文章的时候，没想到这种方式升级的不完全，造成很多底层代码的不更新不执行，所以导致了大鸟这些错误。当然大鸟在重装了面板之后宝塔终端不能用和Panel service startup failed这两个错误都解决了。

当然在解决问题之前我们需要备份网站数据，这个只是大鸟自己遇到的这个问题，问题不尽相同，所以不能解决也不能怨我啊。

以上问题都是基于宝塔面板6.8.7 Centos 7，所以解决问题之前要注意自己服务器环境。
