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

![](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/10/1530265-20190121165727396-177376463120191022.png) ![](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/10/1530265-20190121165801616-185022132620191022.png)

复制以上代码到个人站点中

二、Wordpress添加百度统计代码

* * *

登录到wordpress管理后台->外观->编辑

![](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/10/1530265-20190121170320219-212710812820191022.png)

选择要编辑的主题->主题文件->主题页眉(header.php)

![](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/10/1530265-20190121170500663-117297433520191022.png)

此时看到文档并不能保存

![](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/10/1530265-20190121170534396-59572044120191022.png)

需要设置可写权限：

登录到服务器后找到文件夹/wordpress/wp-content/themes

chmod -R 777 themes/

修改权限后，即可看到更新文件按钮，将百度统计代码插入到以下位置：

![](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/10/1530265-20190121171633798-173606584020191022.png)

三、检验

登录到百度统计后台->管理->代码检查

![](http://img-cloud.zhoujie218.top/wp-content/uploads/2019/10/1530265-20190121172106350-184197065020191022.png)

- 提示：代码安装正确
- 百度统计有时间周期，过一段时间刷新报告即可看到今日流量
