---
title: "WordPress SEO指南"
date: "2021-11-01"
categories: 
  - "it-related"
tags: 
  - "wordpress"
url: "/archives/2355.html"
---

# WordPress SEO指南

WordPress应该是被使用最多的CMS系统，记得以前看到过报道，全世界20%以上的网站用的是WP。虽然最初是作为博客写作CMS发布的，但现在不仅博客使用，新闻、杂志、门户类网站也用，简单的电子商务网站也能用WP，最近越来越多企业网站也开始使用WordPress。

WordPress的优势太多了：

- 开源、免费但功能强大
- 内容层和展现层分离，因而模板极为丰富，又可以用于各种类型网站
- 简单、灵活、开放、标准化，有强大的插件库，实现各种功能
- 安装简单，使用也很简单
- 版本更新频繁，但升级十分简单
- 开发者社群规模够大，某项功能即使不会做又找不到插件，也能找到开发者帮你写

虽然WordPress并不能说是完美搜索引擎友好的，但至少是友好度非常高的CMS之一，在各种插件帮助下和适当设置后， WordPress搭建的网站是可以做到比较完美SEO的。

这篇WordPress SEO指南就简单讨论一下优化WordPress网站的几个要素。相同的考虑也适用于其它博客系统。这里只谈技术性优化，关于博客的运营、市场研究、文章写作等问题，可以参考以前翻译的[博客SEO指南](https://www.seozac.com/seo-tips/blog-seo/)。

## 标题标签和描述标签

老版WordPress的缺省帖子标题标签是这个格式的：

> 博客名称 – 帖子标题

需要改为：

> 帖子标题 – 博客名称

这个修改通常是由下面推荐安装的SEO插件自动实现的，几个流行的WP SEO插件都一定有这个功能。不安装插件的话，也可以在模板文件中自己修改，以前我刚刚开始用WordPress写博客时还没有现在这些插件，都是自己修改模板，在所用模板的header.php文件中，wp\_title（帖子标题）和bloginfo(‘name’) （博客名称）两个顺序调换一下就行了：

> < title >< ? php wp\_title(); ? > – < ? php bloginfo(‘name’); ? > < /title>

或者bloginfo(‘name’)也可以直接硬编码，写上博客名称，少一次php执行，还能写成与设置的博客名称不一样的。

描述标签就是写帖子时摘要（Excerpt）中填写的内容，这个摘要内容也就是首页、栏目页帖子标题下面的简短介绍文字。通常我会从帖子前两段文字中摘一两句话，并在文字上稍微改动一下，尽量避免首页、栏目页和实际帖子页面的重复内容。

如果安装了SEO插件，可以单独写不同于摘要的描述标签，一般我不使用，没有太大必要。

关键词标签可以直接删除，不管对用户还是对搜索引擎，目前都没用，以后也看不出变得有用的可能性。

## 文章内部链接

两种情况，一是文章结尾处或侧栏中显示的相关帖子，这个肯定是插件实现，比如我用的是[Related Post](https://wordpress.org/plugins/wordpress-23-related-posts-plugin/)。相关文章对用户和搜索引擎都有好处，几乎是必须的设置。通常设定显示5-10篇相关文章。

二是贴子正文中链接到其它相关帖子，是[站内链接优化](https://www.seozac.com/seo-tips/internal-links/)的重要部分。我博客里用的比较多，有很多读者也问过我是怎么加的帖子内链接，看到网上有人说我肯定是用插件，其实不是，我就是人工加的。也有插件可以实现，自动在指定关键词加上指定链接， 如[SEO Smart Links](https://wordpress.org/plugins/seo-automatic-links/)，不过我并不建议，虽然插件可以设置一组关键词，可以限制生成链接的次数，但还是不可能像人工那样灵活、自然。人工加基本上是随机的，所以也是最自然的。

人工加内部链接时重要的规则就是别给自己设定规则，不要脑子里有一根弦：“遇到这个关键词，我要链接到这里，每篇帖子只加一次。”我的做法就是随便加，想起来觉得合适就加，没想起来就不加。

## 网站地图

XML版网站地图是必须要有的，也有插件可以实现，如我用的 [Google XMLSitemaps](https://wordpress.org/plugins/google-sitemap-generator/)，虽然名字里带Google，但生成的sitemaps是所有搜索引擎通用的。Sitemap插件很多，基本上都一样。

网页版网站地图没有太大必要，可放可不放。其它类型网站也同样，网站结构没问题的话，是否放页面版网站地图，视用户体验而定，不用考虑SEO。

## 模板的选择和修改

WP官网有大量模板可以下载，搜索“wordpress模板”，也有很多免费、付费的模板网站。选择模板时建议考虑几个方面：

- 好看，设计风格符合行业。我个人喜欢简单的视觉设计，如读者所见，所有图片我都给删了
- 必须是响应式设计
- 必须有面包屑导航
- 功能尽量简单，代码简洁，打开速度快
- 页面代码如H1、H2标签等使用正确，如帖子标题应该是H1

选择好模板后通常还得修修补补，所以懂点编程，虽然不是SEO一定要会的，但是有很大帮助，对个人站长是必不可缺的，一点不懂PHP，想改模板都无法下手。

比如，我用的都是英文模板，一些比较重要的地方还是得中文化，有的在模板文件中可以很容易找到并修改，如右侧栏文字，有的还需要修改核心文件，如留言部分的“留言”、“提交”按钮之类的。

SEO每天一贴到目前为止用的都是免费模板，修改的地方还挺多。比如我把帖子页面的By Zac作者链接删了，原因见下面各类存档部分。

帖子页面的发布日期也删了一段时间，因为一些帖子在搜索结果中显示居然是2006年之类时间写的，用户体验实在不怎么样。但后来又加回去了，因为贴子里说“前几天”之类的话时，如果没有发布日期，有时候会显得莫名其妙，读者可能以为是前不久，其实是10多年前的事了。

再比如首页最下面加了一段关于本博客的说明文字，趁机加点关键词，能稳定显示在首页上，不然首页内容都是帖子摘要，不停变化，无法控制。这段文字只显示在首页，需要在模板或核心文件相应地方（视模板调用方法）加一个简单判断条件：

> <?php if( is\_home() && !is\_paged() ) : ?>

## 栏目及URL设计

栏目规划可以参考以前写的[网站结构优化](https://www.seozac.com/seo-tips/site-structure/)和[多关键词优化](https://www.seozac.com/keywords/multiple-keywords/)帖子，原理和所有网站一样，根据关键词研究结果规划栏目，把次级关键词分配到栏目首页上。

为了使网站结构更扁平一点，可以多规划些栏目，但不要学我这个博客，栏目有点过多了，我现在后悔已经来不及了。

栏目URL我建议还是使用英文单词比较好，中文容易在搜索结果中表现为乱码，拼音URL其实并不易读，尤其是稍长时，比如两三个字的拼音连起来。

WP栏目页面URL缺省设置是：

域名/category/栏目名

中间多了个完全没必要的/category/，可以使用[WP No Category Base插件](https://wordpress.org/plugins/no-category-base-wpml/)删除这层目录。

帖子URL在WP后台Permalink部分有很多格式可以选：

![WordPress SEO优化指南](https://cdn.jsdelivr.net/gh/vbskycn/pipitu/img/202111012041415.jpeg)

有用编号的，有带日期的。建议使用自定义的：

/%category%/%postname%/

也就是 /栏目名/帖子标题/ 的格式，是网站结构的标准格式。

如果不是新闻类网站，不建议URL中带日期。

这种静态化的URL是需要服务器支持mod\_rewrite的，有不止一个站长问过我虚拟主机是否支持mod\_rewrite，说他们主机服务商说的，虚拟主机不能支持mod\_rewrite。没这回事，虚拟主机一样可以支持mod\_rewrite，不支持的只是服务商不愿意给你打开而已。

## 留言系统设置及管理

正常留言多当然是好事，但垃圾留言多了就不是好事了。我的多次经验说明，垃圾留言多了，网站质量评分会明显下降，排名下滑。所以对留言还是需要设置一定门槛。很多链接群发软件或服务就是利用一些博客之类的CMS系统对所有留言来者不拒，既不审核、也不过滤的漏洞实现的。

首先是安装启用[Akismet插件](https://wordpress.org/plugins/akismet/)，他们的垃圾留言数据库会挡住大部分垃圾留言。

每条留言人工审核工作量有点大，可以在WP后台设置第一次留言不马上显示，必须等待审核，有了至少一次人工审核通过的读者的留言才会自动显示。

留言中有两个以上链接的不会显示，等待审核。

设置关键词黑名单，把常见的医疗、赌博等垃圾词列进去。除非你就是做这个行业的。

这样垃圾留言绝大部分会被挡住了。

## 版权及转载声明

我在每篇帖子结尾都加了版权声明及转载要求。通常在模板里的single.php这个文件中加，不用每篇帖子人工加。

虽然SEO热度大不如前，但我的几乎每篇帖子还是有不少转载的，大部分没留原始出处，也没留原作者，甚至有的干脆说是他写的，但还是有正规网站会尊重版权，至少标明原作者的。即使比例不高，积少成多，长期坚持还是会有效果的。

## Tag系统的使用

除了正常的分类系统，博客还经常使用tag系统，在其它网站和CMS也很流行。

Tag页面有很多好处，能覆盖更多关键词，页面相关度高，生成又简单。但也有潜在问题，网站内容不够多的话，tag页面质量会降低，tag词设置不合理的话，和分类页面会有重复。

所以建议使用tag的同学要注意，内容不够丰富时谨慎启用tag系统，设置tag的词时尽量不要与现有分类名称重复。

读者可以参考[Tag页面的优化贴子](https://www.seozac.com/seo-tips/how-to-optimize-tag-page/)。

## 转向处理

[网址规范化](https://www.seozac.com/seo/url-canonicalization/)是几乎每个网站都存在，所以都要考虑的问题。

前面提到的URL的各种形式，选定了一种格式显示在网站上，其它格式还是可以访问的，需要做301转向到选择的规范化格式，这个工作下面介绍的Dean’s Permalinks Migration插件会自动处理。SEO插件会在帖子页面加上canonical标签，各种格式的URL即使都能访问并没有做301转向，也会通过 canonial标签规范化到选择的格式。

全站不带www的URL需要做301转向到带www的URL（或者反过来，有的网站选择不带www的版本为规范化版本），http版的URL也要做301转向到https版本。LAMP（Linux+Apache+MySQL+PHP）服务器，这个可以通过.htaccess 文件里的rewrite规则实现，如SEO每天一贴实际用的转向规则是：

> RewriteCond %{SERVER\_PORT} 80 RewriteRule ^(._)$ [https://www.seozac.com/$1](https://www.seozac.com/$1) \[R=301,L\] RewriteCond %{HTTP\_HOST} ^seozac.com \[NC\] RewriteRule ^(._)$ [https://www.seozac.com/$1](https://www.seozac.com/$1) \[L,R=301\]

这只是个例子，别照抄。同样的功能，可以用不太相同的正则表达式和规则实现，不同服务器写法要求也可能不同。比如只做不带www转向到带www可以写成：

> RewriteCond %{HTTP\_HOST} ^seozac.com \[NC\] RewriteRule ^(.\*)$ [http://www.seozac.com/$1](http://www.seozac.com/$1) \[L,R=301,NC\]

贵网站具体怎么写，问程序员。

## 提速设置

缓存还是要设置一下的，可以将页面生成纯静态的，不需要每次有人访问都PHP从数据库调用内容，比较明显地提高速度。有不少插件，我用的是[WP Super Cache](https://wordpress.org/plugins/wp-super-cache/)。

服务器开启gzip.。

可能的话，考虑CDN。这个我没有使用。

图片建议压缩后再上传，不要把照相机、手机里几M的文件直接拿来用。

## 各类存档

WP缺省有多种存档页面，包括按分类、按发布日期、按作者。这些存档页面大部分是没有用的，反倒有副作用，可能造成复制内容。

按分类存档当然要使用，这是正常的导航系统。

按日期、按作者存档，通常可以去掉，这两个存档内容和按分类是一样的，并没有实质价值。要去掉这两个存档，需要在模板中删除相应的显示代码，有的模板现在已经没有这两个存档了，或者通过widgets控制显示与否。

当然在模板中去掉代码，直接访问存档页面还是能访问的，为保险起见，可以在这两个存档页面全部加上noindex标签，确保搜索引擎不索引收录，或者用[robots文件禁止抓取](https://www.seozac.com/seo-tips/robots-support/)。

## 推荐插件

除了上面提到的插件，我还装了这几个插件：

[All In One SEO Pack](https://wordpress.org/plugins/all-in-one-seo-pack/) – SEO专用插件是必须的，我装的是All in One SEO Pack，会自动或手动设置很多SEO功能，如：

- 帖子页面标题、说明标签的客制化，加noindex 或nofollow标签（通常不加，但给了这个选项的自由）
- 加上canonical标签
- 首页标题、说明标签客制化
- 设置各类页面标题标签的格式，如前面提到的帖子标题顺序
- 各类页面是否加noindex或nofollow的缺省设置，写帖子时还可以覆盖这个缺省设置

另一个很有名的SEO插件是[Yoast SEO](https://wordpress.org/plugins/wordpress-seo/)，功能比All in One SEO更多更复杂一些，但大致是一样的，现在也更流行。之所以选择All in One SEO是最早写博客时先找到的它，习惯了而已。

[AMP](https://wordpress.org/plugins/amp/) – 这个不用解释了， [Google AMP](https://www.seozac.com/gg/google-amp/)实现最简单的方式。

[Autoptimise](https://wordpress.org/plugins/autoptimize/) – 把WordPress零散的CSS和JS文件集合到一个文件中，减少调用文件数，提高速度。试用了一下，没卸载，但目前并没有启用，觉得效果不大。

[Broken Link Checker](https://wordpress.org/plugins/broken-link-checker/) – 检查帖子连到其他网站的链接是否还有效。[上次检查清理链接](https://www.seozac.com/content/404-cleanup/)时发现很多当年连出去的链接已经无效了。

[Dean’s Permalinks Migration](http://www.deanlee.cn/wordpress/permalinks-migration-plugin/) – 帖子URL有任何变动时，这个插件自动设置301转向。

[WP-Optimise](https://wordpress.org/plugins/wp-optimize/) – 清理数据库中的备份等不需要的东西。

WP还有很多其它插件，能实现你能想到的各种各样的功能，常见但和SEO不直接相关的如两步认证登录、流量统计、图片处理等。在各种插件帮助下和适当设置后， 但要注意，启用的插件越多，插件越复杂，WP速度将越慢，所以，不是必须的功能，就不要安装了。

读者现在没时间看这么长帖子，或者想留着以后参考，可以下载[《WordPress SEO指南》PDF文件](https://www.seozac.com/wordpress-seo-guide.pdf)。
