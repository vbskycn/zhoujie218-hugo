---
title: "修改Hosts临时解决GitHub的raw.githubusercontent.com无法链接的问题"
date: "2020-02-18"
categories: 
  - "it-related"
  - "diannaowangruo"
url: "/archives/1300.html"
---

前言

正值双11,各大云服务商的活动非常给力,正好给公司添置一台项目服务器,在配置相关环境时,发现GitHub的`raw.githubusercontent.com`域名解析竟然因某些你懂的原因给临时污染了.终于通过修改hosts解决掉此问题,可以正常部署环境了.

* * *

## 解决方法

使用cloudflare代理吧

![image-20240620114348301](https://img-cloud.zhoujie218.top/2024/06/20/6673a5790c0ab.png)

### 查询真实IP

通过[`IPAddress.com`](https://www.ipaddress.com/)首页,输入`raw.githubusercontent.com`查询到真实IP地址

### 修改hosts

CentOS及macOS直接在终端输入 \`\`\` sudo vi /etc/hosts~~

```
添加以下内容保存即可 ```
199<span class="hljs-selector-class">.232</span><span class="hljs-selector-class">.4</span><span class="hljs-selector-class">.133</span> <span class="hljs-selector-tag">raw</span><span class="hljs-selector-class">.githubusercontent</span><span class="hljs-selector-class">.com

</span>
```

* * *
