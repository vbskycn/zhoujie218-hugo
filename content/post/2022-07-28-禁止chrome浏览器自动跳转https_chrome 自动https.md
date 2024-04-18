---
title: "禁止chrome浏览器自动跳转https_chrome 自动https"
date: "2022-07-28"
categories: 
  - "diannaowangruo"
tags: 
  - "chrome"
  - "https"
url: "/archives/2455.html"
---

**现在浏览器为了安全，只要是访问过 https 的域名的，如果使用 http 请求，就会自动跳 https，在一些特殊场景下，我们在 https 和 http 部署了不同的两套系统，这种方式就会影响我们系统正常演示。**

**针对 chrome 内核浏览器，如 360 浏览器、edge 等，都通用。**

**在浏览器地址栏输入：chrome://net-internals/#hsts**

**进入如下界面**

![img](https://img-cloud.zhoujie218.top/piggo/202207282053830.png)

**在 1 框中，录入你的 http 的域名，如果查询有记录，那就是这个问题导致了自动跳转。**

**这时到 2 框中，录入域名，点击删除，在上 1 框中确认删除成功后。**

**重新打开浏览器，录入 http 域名，就不会自动跳转了。**

**注意，如果你手残，又手动跳转了 https，那就得重来一次。**

**以上。**
