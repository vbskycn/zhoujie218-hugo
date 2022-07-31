---
title: "完美迁移博客从wordpress到hugo"
date: "2022-07-31"
categories: 
  - "diannaowangruo"
tags: 
  - "hugo"
url: "wordpress-tu-hugo-wanmei-ok"
---


## 前言

博客写了很多年，都没有写出什么有技术含量的文章。天下互联，你抄我也抄：）
我篇文章也是借鉴网友，下面有他的链接
完美从wordpress转到hugo

## 网站情况简介

开始介绍迁移过程之前，我先简单说一下我网站的基本情况供大家参考。如果大家网站情况和我一样，那完全可以采用跟我相同的迁移方案。

笔者从 16 年开始写博客，很早之前在简书上随便写一写，然后迁移到了 csdn。后来由于在第三方网站上写作不自由，所以就自建博客了。在简书和 csdn 写作期间，都是用的**平台自己的图床**，直到自建博客开始才开始使用七牛云的 OSS 服务，每月免费 10G 但是仅限 http 流量，2020 年我才将图床也全部升级为 https 调用。

图床迁移实际上并不是一件容易的事情，因为目前所有的迁移工具都是只能**识别 markdown 语法**的图片链接而不是**html 标签**里面的链接。这就导致我们必须将 Wordpress 中的所有文章全部转成**markdown 语法**。

最后一个问题就是保证文章的链接迁移前后没有变化，这样就可以保证拥有旧链接的人们可以正常访问。

综上，我们需要解决三个问题：

1. 解析 Wordpress 备份的 "XML" 为拥有 markdown 语法的 ".md" 文件；
2. 图床迁移；
3. 固定链接。

## 方案对比

当然，我们可以直接选择官网给出的方案[Migrate to Hugo](https://gohugo.io/tools/migrations/)。对于 wordpress，主要有以下几种。

[
](https://image.i-ll.cc//uPic/20211009/Drxefh.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim)![](https://image.i-ll.cc//uPic/20211009/Drxefh.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim#crop=0&crop=0&crop=1&crop=1&id=eV9wE&originHeight=440&originWidth=662&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

这几种方案我都尝试过，各有优势却都不完美。以下是详细说明

1.  [wordpress-to-hugo-exporter](https://github.com/SchumacherFM/wordpress-to-hugo-exporter)： 可以导出，且文件名称就是带有日期和中文的标题名称。但是不是原生 markdown 格式。而是如下图所示的结构。不满足需求 1，2，所以**排除**。
[
](https://image.i-ll.cc//uPic/20211010/InznCv.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim)![](https://image.i-ll.cc//uPic/20211010/InznCv.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim#crop=0&crop=0&crop=1&crop=1&id=ZzAXD&originHeight=594&originWidth=573&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=) 
2.  [exitwp-for-hugo](https://github.com/wooni005/exitwp-for-hugo): 原始仓库是用 python2.x 写的，但是有人完善了 python3.x 的版本。这个程序可以将 Wordpress 的 xml 文件转成 markdown 语法的 md 文件，但是文件名太乱。（因为标题中包含了中文，所以这个程序会自动将中文转成 unicode 编码然后用它作为文件名储存在电脑中）
[
](https://image.i-ll.cc//uPic/20211010/x3GmFS.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim)![](https://image.i-ll.cc//uPic/20211010/x3GmFS.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim#crop=0&crop=0&crop=1&crop=1&id=bJrMv&originHeight=270&originWidth=1249&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=) 
3.  [blog2md](https://github.com/palaniraja/blog2md): 与[exitwp-for-hugo](https://github.com/wooni005/exitwp-for-hugo)类似，文件名太乱且不包含日期。
[
](https://image.i-ll.cc//uPic/20211010/8JNn1t.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim)![](https://image.i-ll.cc//uPic/20211010/8JNn1t.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim#crop=0&crop=0&crop=1&crop=1&id=JPId0&originHeight=213&originWidth=1244&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=) 
4.  [wordhugopress](https://github.com/nantipov/wordhugopress): java 写的程序，对于新手不太友好，但是也可以基于 Wordpress 博客中的文章生成 markdown 语法的 md 文件。需要配置数据库用户名和密码，而且最后生成的目录结构很乱。
[
](https://image.i-ll.cc//uPic/20211010/By0AxI.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim)![](https://image.i-ll.cc//uPic/20211010/By0AxI.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim#crop=0&crop=0&crop=1&crop=1&id=m150X&originHeight=255&originWidth=1268&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=) 

然后突然发现一个仓库[wordpress-export-to-markdow_L 版](https://github.com/AvantaR/wordpress-export-to-markdown)，这个只需要自己在电脑上安装 node.js 环境，然后就可以直接运行了。它可以解决除**固定链接**以外的所有问题，是一个近乎完美的方案。基于 L 版，[AvantaR](https://github.com/AvantaR)，在 markdown 的 yaml 头文件中添加了**slug**参数，详细实现见该仓库[wordpress-export-to-markdow_A 版](https://github.com/AvantaR/wordpress-export-to-markdown)。

实际上**slug**和**url**还是有区别的。以下面这个 yaml 头和网站[https://blog.i-ll.cc](https://blog.i-ll.cc/)为例：

| ```
1 2 3 4 5 6 7

```

 | ```
title:  "Drcom下如何优雅地使用路由器上网"  date:  "2016-12-23"  categories:   - "other"  tags:   - "路由器"  url:  "/archives/108"
```

|

上面的配置文件中使用了**url**，所以该文章最后的链接是[https://blog.i-ll.cc/archives/108/](https://blog.i-ll.cc/archives/108/)。如果将**url**改为**slug**，如下所示。

| ```
1 2 3 4 5 6 7

```

 | ```
title:  "Drcom下如何优雅地使用路由器上网"  date:  "2016-12-23"  categories:   - "other"  tags:   - "路由器"  slug:  "/archives/108"
```

|

那么该文章最后的链接是[https://blog.i-ll.cc/post/archives/108/](https://blog.i-ll.cc/post/archives/108/)。

两者的区别就是**slug**指的是文章的缩写名，在最后生成的文章链接中，会在前面加上文章所在的目录名（根域名 + 目录名 + slug 参数对应的值）（上面的例子中，目录名是 post），而**url**后面的参数就是直接添加到根域名下的参数。因为我网站的固定连接下没有 post 路径，所以我在 L 版的基础上进行了修改得到了 M 版[wordpress-export-to-markdown_M](https://github.com/MLZC/wordpress-export-to-markdown)以达到我自己的需求。

## 最终方案使用说明

### 转换 Wordpress xml 以及保持文章链接不变

使用方法就是直接 clone 该仓库，然后将 Wordpress 的 xml 文件放到该程序的根目录下并改名为_export.xml_, 然后执行下面的命令。因为我修改了一些默认参数，所以可以设置`--wizard=false`， 当然，如果你们像自己更改默认值，可以去掉`--wizard=false`。

| ```
1

```

 | ```
npm install && node index.js --wizard=false
```

|

### 图床迁移

这部分实际上没有什么好说的，主要使用这两个软件，都是图形化界面，配置一下图床信息，选择一下 markdown 文件或者文件夹地址就可以自动迁移了。后者是免费的，前者虽然收费但是有免费体验期，对于只使用一次的用户来说就是免费。

[
](https://image.i-ll.cc//uPic/20211010/EvkeIl.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim)![](https://image.i-ll.cc//uPic/20211010/EvkeIl.png?imageMogr2/auto-orient/blur/1x0/quality/75%7Cwatermark/2/text/WmhhbyBDaGnigJhzIEJsb2c=/font/dGltZXMgbmV3IHJvbWFu/fontsize/240/fill/IzAwMDAwMA==/dissolve/75/gravity/SouthEast/dx/10/dy/10%7Cimageslim#crop=0&crop=0&crop=1&crop=1&id=plusB&originHeight=187&originWidth=534&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)

~ 实际上还有[PicGo](https://github.com/Molunerfinn/PicGo)和[picgo-plugin-pic-migrater](https://github.com/PicGo/picgo-plugin-pic-migrater)，可以使用。~ 之前可能有用，但是程序很久都没有更新过了，一堆 bug，根本不能正常迁移。还是推荐大家使用 iPic 和 iPic Mover。

## 随便说说

服务器是 2021 年 9 月 27 日到期，由于我学习和工作太忙，一直抽不出时间来弄。就又将服务器续费了 7 天。抽空的时候研究一下怎么迁移最方便。直到 2021 年 10 月 2 号才完全弄好，今天才有一点时间将迁移过程总结一下。这个方案完美适配我自己的网站，不一定适合所有人，在此分享出迁移思路或许对大家有所帮助。(ps. 研究生期间没有怎么更新 blog，PhD 期间争取做到一到两周更一次，内容大概会聚焦在研究方向和大数据相关的知识上。)



