---
title: "最近docker很难访问了,教你白嫖Cloudflare Workers 搭建 Docker Hub镜像加速服务"
date: "2024-06-18"
categories: 
  - "it-related"
  - "diannaowangruo"
tags: 
  - "docker"
  - "hub"
  - "加速"
  - "镜像"
url: "/archives/2626.html"
---

## 简介

**最近docker很难访问了，很多镜像都关了，自己动免费辱一个专用镜像**

## 请不要使用我的地址，随时可能关闭，建议花5分钟时间自己搭一个

基于Cloudflare Workers 搭建 Docker Hub镜像加速服务。

1. 首先要注册一个Cloudflare账号。
2. Cloudflare账号下域名的一级域名，推荐万网注册个top域名，再转移到Cloudflare，很便宜的。
3. 注意 Worker 每天每免费账号有次数限制，为10万次。每分钟为1000次。

## 步骤

登录到CF的仪表盘 [https://dash.cloudflare.com/](https://dash.cloudflare.com/)

点击 workers-and-pages > 创建应用程序 > 创建 Worker > 点击保存 >点击完成 > 编辑代码

![img](https://img-cloud.zhoujie218.top/2024/06/18/667157ca0b354.png)

### 编辑代码

#### 编辑 worker.js 文件

编辑覆盖后，ctrl + s 即可保存。

```javascript
import HTML from './docker.html';
export default {
    async fetch(request) {
        const url = new URL(request.url);
        const path = url.pathname;
        const originalHost = request.headers.get("host");
        const registryHost = "registry-1.docker.io";
        if (path.startsWith("/v2/")) {
        const headers = new Headers(request.headers);
        headers.set("host", registryHost);
        const registryUrl = `https://${registryHost}${path}`;
        const registryRequest = new Request(registryUrl, {
            method: request.method,
            headers: headers,
            body: request.body,
            // redirect: "manual",
            redirect: "follow",
        });
        const registryResponse = await fetch(registryRequest);
        console.log(registryResponse.status);
        const responseHeaders = new Headers(registryResponse.headers);
        responseHeaders.set("access-control-allow-origin", originalHost);
        responseHeaders.set("access-control-allow-headers", "Authorization");
        return new Response(registryResponse.body, {
            status: registryResponse.status,
            statusText: registryResponse.statusText,
            headers: responseHeaders,
        });
        } else {
        return new Response(HTML.replace(/{{host}}/g, originalHost), {
            status: 200,
            headers: {
            "content-type": "text/html"
            }
        });
        }
    }
}
1234567891011121314151617181920212223242526272829303132333435363738
```

#### 编辑 docker.html 文件

点击新建文件，创建此文件。ctrl + s 即可保存。

![img](https://img-cloud.zhoujie218.top/2024/06/18/667157d7b30a3.png)

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>镜像使用说明</title>
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .header {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: #fff;
            padding: 20px 0;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        .content {
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            padding: 20px 0;
            background-color: #333;
            color: #fff;
        }
        pre {
            background-color: #272822;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: 'Source Code Pro', monospace;
        }
        a {
            color: #4CAF50;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        @media (max-width: 600px) {
            .container {
                margin: 20px;
                padding: 15px;
            }
            .header {
                padding: 15px 0;
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Source+Code+Pro:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="header">
        <h1>镜像使用说明</h1>
    </div>
    <div class="container">
        <div class="content">
            <p>为了加速镜像拉取，你可以使用以下命令设置镜像加速 registry mirror:+</p>
            <pre><code>sudo tee /etc/docker/daemon.json <<EOF
{
    "registry-mirrors": ["https://{{host}}"]
}
EOF</code></pre>

<pre><code>sudo systemctl restart docker #请务必重启docker服务</code></pre>
<p>本镜像站点只是为了演示，随时关闭，建议花5分钟自己搭建一个
    <a href="https://www.zhoujie218.top/archives/2626.html" target="_blank">https://www.zhoujie218.top/archives/2626.html</a> #这是详细教程</p>
<br>

            <p>为了避免 Worker 用量耗尽，你可以手动 pull 镜像然后 re-tag 之后 push 至本地镜像仓库:</p>
            <pre><code>docker pull {{host}}/library/alpine:latest # 拉取 library 镜像
docker pull {{host}}/coredns/coredns:latest # 拉取 coredns 镜像</code></pre>
        </div>
    </div>
    <div class="footer">
        <p>Powered by Cloudflare Workers</p>
        <p><a href="https://zhoujie218.top" target="_blank">访问博客 zhoujie218.top</a></p>
    </div>
</body>
</html>
```

### 保存部署并配置触发器

上述两个文件的代码保存后，选择部署 > 保存并部署

点击左上角的项目连接，配置触发器。（自定义域名访问）

### 自定义域名访问

![image-20240618175524964](https://img-cloud.zhoujie218.top/2024/06/18/6671599019d4d.png)

## 访问界面和配置docker如下

![](https://img-cloud.zhoujie218.top/2024/06/18/667167040eaad.png)

# 请不要使用上面的地址，随时可能关闭，建议花5分钟时间自己搭一个
