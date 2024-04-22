---
title: "解决宝塔php8 不能安装fileinfo模块的问题"
date: "2023-08-27"
categories: 
  - "diannaowangruo"
tags: 
  - "fileinfo"
  - "php8"
  - "宝塔"
url: "/archives/2551.html"
---

## 解决宝塔php8 不能安装fileinfo模块的问题

阿里云服务器系统 Alibaba Cloud (Aliyun ) 2.1903 LTS (Hunting Beagle) x86\_64(Py3.7.9) 或者类似系统

因照顾小机器的安装宝塔默认使用了禁用fileinfo参数，可能是检测到了禁用参数所以提示的不支持 可以使用以下命令重装默认开启 fileinfo的php

![image-20230827192340694](https://img-cloud.zhoujie218.top/2023/08/3545df842e35f4917583d946c78ab2b2.webp)

命令行执行

# 下载php编译安装脚本

```
wget http://download.bt.cn/install/0/php.sh
```

#替换禁用fileinfo参数改为开启

```
sed -i "s/--disable-fileinfo/--enable--fileinfo/g" php.sh
```

#安装php-8.2

```
bash php.sh install 8.2
```

![image-20230827192416306](https://img-cloud.zhoujie218.top/2023/08/7efe971de6987b7b67352d82fd7e09ec.webp)

官方论坛提几次都说不支持阿里云系统，还是自己动手
