---
title: "通过 Docker 自建 Lsky Pro 图片审核接口"
date: "2023-09-01"
categories: 
  - "diannaowangruo"
tags: 
  - "docker"
  - "nsfwjs"
  - "鉴黄"
url: "/archives/2557.html"
---

## NSFW 是什么

NSFW 是一个英文网络用语，是 Not Safe For Work 或者 Not Suitable For Work 的缩写，意思是某个网络内容不适合上班时间浏览。

它通常被用于标记那些带有淫秽色情、暴力血腥、极端另类等内容的邮件、视频、博客、论坛帖子里等，以免读者不恰当的点击浏览。常见的用法是，在链接的后面，加上一对括号，括号中标记 NSFW。

## 部署方法

使用如下命令部署，其中`-p 3000:3000` 是端口映射，`--restart=always` 是自动重启：

```
COPYdocker run -p 3000:3000 --restart=always penndu/nsfw-api:latest
```

如 Docker Hub 下载较慢，也可使用下面阿里云镜像源：

```
COPYdocker run -p 3000:3000 --restart=always registry.cn-beijing.aliyuncs.com/dusays/nsfw-api:latest
```

## 食用方法

**POST /classify**

**请求示例**

```
COPYPOST /classify HTTP/1.1
Content-Type: multipart/form-data
```

在 `image` 字段中提供图像。

**响应示例**

```
COPYHTTP/1.1 200 OK
Content-Type: application/json
COPY{
    "porn": 0.59248286485672,
    "sexy": 0.39802199602127075,
    "hentai": 0.006243097595870495,
    "neutral": 0.0031403270550072193,
    "drawing": 0.00011181648733327165
}
```

## 图床演示

管理员进入后台角色组设置，选择指定的角色组点击编辑，进入图片审核标签，开启图片审核，设置审核动作，驱动调整为 NsfwJs，接口地址设置为 `http://127.0.0.1:3000/classify`，属性为 `image`，阈值为 `60`「以上参数根据实际情况调整」

![image-20230901145352560](/images/2023/09/725e062165bd19158ac4b6c24b750c5b.webp)

## 效果

![image-20230901145124825](/images/2023/09/05fabed514d9ee49acebcc0192f1033a.webp)

## 已开启api，轻量使用

[https://img-up.zhoujie218.top/](https://img-up.zhoujie218.top/)
