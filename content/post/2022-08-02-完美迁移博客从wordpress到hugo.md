---
title: "完美迁移博客从wordpress到hugo"
date: "2022-08-02"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "hugo"
  - "wordpress"
url: "/archives/2461.html"
---

## 前言

博客写了很多年，都没有写出什么有技术含量的文章。网络互联，你抄我也抄：） 这篇文章也是借鉴网友的 下面有他的链接完美从wordpress转到hugo

## 网站情况简介

开始介绍迁移过程之前，我先简单说一下我网站的基本情况供大家参考。如果大家网站情况和我一样，那完全可以采用跟我相同的迁移方案。 笔者从 06 年开始学做网站，那个时候还是im286 的时代。以前一直转战于各种免费空间，各种程序，体验的是那种安装折腾的过程，现在年纪大了，折腾不动了，就想越简单越好。本人没有什么技术，只是出于业余爱好，喜欢捣鼓一些网页程序之类的东东。3年前入手阿里云ESC，域名也备案了，也就绑在阿里了，也不想天天给网站搬家，真的是一件累人的事！

前几天看到一个博客特别漂亮，折腾之火熊熊燃烧。一路baidu过来，发现是静态博客hexo 。现在还可以结合cloudfare pages,netlifi,vercel ，github，这些国外大厂提供网站托管，cdn,免费，速度也不错。 最终我选的是cloudfare pages + github +hugo 因为cf不支持hexo集成,后面又研究hugo，有集成的更简单，鼠标键盘点点点，几分钟就建好了一个网站，更新也方便，写好文章，用github推上去，网站就自动更新了。

## 建一个网站的流程

- fork好喜欢的主题仓库
- 设置好网站信息，设置好cloudfare pages
- github推送，OK

原来我用的程序是wordpress,虽然没有写出什么技术文章，但是也有100多篇，也算是回忆吧。丢是不能丢的，转格式吧 baiduing..... 找了很多方法，下面这个是最完美的。 我们要迁移文章，还有图片。图床迁移实际上并不是一件容易的事情，因为目前所有的迁移工具都是只能**识别 markdown 语法**的图片链接而不是**html 标签**里面的链接。这就导致我们必须将 Wordpress 中的所有文章全部转成**markdown 语法**。 最后一个问题就是保证文章的链接迁移前后没有变化，这样就可以保证拥有旧链接的人们可以正常访问。 综上，我们需要解决三个问题：

1. 解析 Wordpress 备份的 "XML" 为拥有 markdown 语法的 ".md" 文件；
2. 图床迁移；
3. 固定链接。

## 方案对比

当然，我们可以直接选择官网给出的方案[Migrate to Hugo](https://gohugo.io/tools/migrations/)。对于 wordpress，主要有以下几种。 ![image.png](https://img-cloud.zhoujie218.top/piggo/202208011522171.png)

这几种方案我都尝试过，各有优势却都不完美。以下是详细说明

1. [wordpress-to-hugo-exporter](https://github.com/SchumacherFM/wordpress-to-hugo-exporter)： 可以导出，且文件名称就是带有日期和中文的标题名称。但是不是原生 markdown 格式。而是如下图所示的结构。不满足需求 1，2，所以**排除**。
2. exitwp-for-hugo: 原始仓库是用 python2.x 写的，但是有人完善了 python3.x 的版本。这个程序可以将 Wordpress 的 xml 文件转成 markdown 语法的 md 文件，但是文件名太乱。（因为标题中包含了中文，所以这个程序会自动将中文转成 unicode 编码然后用它作为文件名储存在电脑中）![image.png](https://img-cloud.zhoujie218.top/2024/04/22/6626037f5b5f3.png)
3. [exitwp-for-hugo](https://github.com/wooni005/exitwp-for-hugo): 原始仓库是用 python2.x 写的，但是有人完善了 python3.x 的版本。这个程序可以将 Wordpress 的 xml 文件转成 markdown 语法的 md 文件，但是文件名太乱。（因为标题中包含了中文，所以这个程序会自动将中文转成 unicode 编码然后用它作为文件名储存在电脑中）![image.png](https://img-cloud.zhoujie218.top/2024/04/22/6626037fa9c14.png)
4. [blog2md](https://github.com/palaniraja/blog2md): 与[exitwp-for-hugo](https://github.com/wooni005/exitwp-for-hugo)类似，文件名太乱且不包含日期。![image.png](https://img-cloud.zhoujie218.top/2024/04/22/6626037fa20bd.png)
5. [wordhugopress](https://github.com/nantipov/wordhugopress): java 写的程序，对于新手不太友好，但是也可以基于 Wordpress 博客中的文章生成 markdown 语法的 md 文件。需要配置数据库用户名和密码，而且最后生成的目录结构很乱。![image.png](https://img-cloud.zhoujie218.top/2024/04/22/6626037f54bc2.png)

然后突然发现一个仓库[wordpress-export-to-markdow\_L 版](https://github.com/AvantaR/wordpress-export-to-markdown)，这个只需要自己在电脑上安装 node.js 环境，然后就可以直接运行了。它可以解决除**固定链接**以外的所有问题，是一个近乎完美的方案。基于 L 版，[AvantaR](https://github.com/AvantaR)，在 markdown 的 yaml 头文件中添加了**slug**参数，详细实现见该仓库[wordpress-export-to-markdow\_A 版](https://github.com/AvantaR/wordpress-export-to-markdown)。 实际上**slug**和**url**还是有区别的。以下面这个 yaml 头和网站https://img-cloud.zhoujie218.top/archives/1018.html为例：

```yaml
title: "Drcom下如何优雅地使用路由器上网"
date: "2016-12-23"
categories: 
- "other"
tags: 
- "路由器"
url: "/archives/1018"
```

上面的配置文件中使用了**url**，所以该文章最后的链接是[https://img-cloud.zhoujie218.top/archives/1018](https://img-cloud.zhoujie218.top/archives/1018.html)/如果将**url**改为**slug**，如下所示。

```yaml
title: "Drcom下如何优雅地使用路由器上网"
date: "2016-12-23"
categories: 
  - "other"
tags: 
  - "路由器"
slug: "/archives/1018"
```

两者的区别就是**slug**指的是文章的缩写名，在最后生成的文章链接中，会在前面加上文章所在的目录名（根域名 + 目录名 + slug 参数对应的值）（上面的例子中，目录名是 post），而**url**后面的参数就是直接添加到根域名下的参数。因为我网站的固定连接下没有 post 路径，所以我在 L 版的基础上进行了修改得到了 M 版[wordpress-export-to-markdown\_M](https://github.com/MLZC/wordpress-export-to-markdown)以达到我自己的需求。

## 最终方案使用说明

### 转换 Wordpress xml 以及保持文章链接不变

使用方法就是直接 clone 该仓库，然后将 Wordpress 的 xml 文件放到该程序的根目录下并改名为_export.xml_, 然后执行下面的命令。因为我修改了一些默认参数，所以可以设置--wizard=false， 当然，如果你们像自己更改默认值，可以去掉--wizard=false。

```basic
npm install && node index.js --wizard=false
```

### 图床迁移

这部分实际上没有什么好说的，主要使用这两个软件，都是图形化界面，配置一下图床信息，选择一下 markdown 文件或者文件夹地址就可以自动迁移了。后者是免费的，前者虽然收费但是有免费体验期，对于只使用一次的用户来说就是免费。

![image.png](https://img-cloud.zhoujie218.top/2024/04/22/6626037f4e87e.png)

~ 实际上还有[PicGo](https://github.com/Molunerfinn/PicGo)和[picgo-plugin-pic-migrater](https://github.com/PicGo/picgo-plugin-pic-migrater)，可以使用。~ 之前可能有用，但是程序很久都没有更新过了，一堆 bug，根本不能正常迁移。还是推荐大家使用 iPic 和 iPic Mover。

### 来个更简单的图片转移方法

我写了一个python程序，自动下载所有md文件中的图片到images文件夹，并且会修改md文章中的相对链接。把图片全部静态托管到hugo所在的服务就OK了,下面是下载链接。如果有解压密码的话就是本站域名。

py程序下载地址：

\[login\_email\] https://www.zhoujie218.top/wp-content/uploads/file/wp-img\_to\_hugo.rar \[/login\_email\]
