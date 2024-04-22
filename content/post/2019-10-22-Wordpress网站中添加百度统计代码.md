---
title: "Wordpress网站中添加百度统计代码"
date: "2019-10-22"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
url: "/archives/837.html"
---

百度统计是流量分析平台，帮助收集网站访问数据，提供流量趋势、来源分析、转化跟踪、页面热力图、访问流等多种统计分析服务，同时与百度搜索、百度推广、云服务无缝结合，为网站的精细化运营决策提供数据支持，进而有效提高企业的投资回报率。

一、百度统计添加网站

* * *

登录百度统计： [](https://tongji.baidu.com/)[https://tongji.baidu.com](https://tongji.baidu.com)

管理->新增网站

![](/images/2019/10/ea978d616dd82580eddb3e73b4c5b357.png) ![](/images/2019/10/644fa5c2a67c0b3dbee34c1980e9c2ad.png)

复制以上代码到个人站点中

二、Wordpress添加百度统计代码

* * *

登录到wordpress管理后台->外观->编辑

![](/images/2019/10/f77114b35c0eaa44d8c37ad1880d9d54.png)

选择要编辑的主题->主题文件->主题页眉(header.php)

![](/images/2019/10/bdbd36301b33269560a922561f004aad.png)

此时看到文档并不能保存

![](/images/2019/10/52a4da52b16b3a78b211666466485b71.png)

需要设置可写权限：

登录到服务器后找到文件夹/wordpress/wp-content/themes

chmod -R 777 themes/

修改权限后，即可看到更新文件按钮，将百度统计代码插入到以下位置：

![](/images/2019/10/facd10cd60526a528c6e4717b49c42be.png)

三、检验

登录到百度统计后台->管理->代码检查

![](/images/2019/10/09c53d23010acd872337e61224f4f848.png)

- 提示：代码安装正确
- 百度统计有时间周期，过一段时间刷新报告即可看到今日流量
