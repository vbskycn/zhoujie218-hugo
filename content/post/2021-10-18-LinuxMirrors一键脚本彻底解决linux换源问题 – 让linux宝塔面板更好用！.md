---
title: "LinuxMirrors一键脚本彻底解决linux换源问题 – 让linux宝塔面板更好用！"
date: "2021-10-18"
categories: 
  - "diannaowangruo"
tags: 
  - "baota"
  - "github"
  - "linux"
  - "源"
url: "/archives/2103.html"
---

国内vps安装好linux系统后（centos，debian，ubuntu等），除了deepin以外，其他Linux发行版从官方源下载东西都很慢，这个时候，我们就需要给自己的系统换一个镜像源了，使用镜像源不仅可以给官方源的服务器减压，还能提供更快的速度。这也是为啥，我们总需要换源的原因！！

当然，换源不麻烦，国内源可供选择的也很多，比如说，阿里云，腾讯云，华为云等等。但是不管如何，还是使用脚本来换源比较省心省力。这篇文章就来推荐一个一键脚本换源的方法！！

#### 1、项目

1）地址：[](https://github.com/SuperManito/LinuxMirrors)[](https://github.com/SuperManito/LinuxMirrors)[](https://github.com/SuperManito/LinuxMirrors)[https://github.com/SuperManito/LinuxMirrors](https://github.com/SuperManito/LinuxMirrors)

2）已适配的 GNU/Linux 发行版

| Debian | 8.0 ~ 11.0 |
| --- | --- |
| Ubuntu | 16.04 ~ 21.04 |
| Kali Linux | 2.0 ~ 2021.2 |
| RHEL | 7.0 ~ 8.4 |
| CentOS | 7.0 ~ 8.4 |
| Fedora | 28 ~ 34 |

目前仅支持上述基于 Debian 与 Redhat 系的发行版和及其部分衍生版本，同样支持上述版本中拥有相同底层核心的其它发行版，例如 [`Armbian`](https://www.armbian.com/) [`Kubuntu`](https://kubuntu.org/) [`Oracle Linux`](https://www.oracle.com/cn/technical-resources) 等

注意，理论支持所有架构的环境，`arm64` 环境已经过测试！！

#### 2、脚本当前使用的开源镜像站

| 序号 | 镜像站名称 | 镜像站地址 | IPv6 | Kali Linux | Fedora | EPEL |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 阿里云 | [mirrors.aliyun.com](https://developer.aliyun.com/special/mirrors/notice) | √ | √ | √ | √ |
| 2 | 腾讯云 | [mirrors.cloud.tencent.com](https://mirrors.cloud.tencent.com/) | √ | √ | √ | √ |
| 3 | 华为云 | [mirrors.huaweicloud.com](https://mirrors.huaweicloud.com/) | √ | √ | √ | √ |
| 4 | 网易 | [mirrors.163.com](https://mirrors.163.com/) |  |  | √ |  |
| 5 | 搜狐 | [mirrors.sohu.com](https://mirrors.sohu.com/) |  |  |  |  |
| 6 | 清华大学 | [mirrors.tuna.tsinghua.edu.cn](https://mirrors.tuna.tsinghua.edu.cn/) | √ | √ | √ | √ |
| 7 | 浙江大学 | [mirrors.zju.edu.cn](https://mirrors.zju.edu.cn/) |  | √ | √ | √ |
| 8 | 南京大学 | [mirrors.nju.edu.cn](https://mirrors.nju.edu.cn/) |  | √ | √ | √ |
| 9 | 重庆大学 | [mirrors.cqu.edu.cn](https://mirrors.cqu.edu.cn/) |  | √ | √ | √ |
| 10 | 兰州大学 | [mirror.lzu.edu.cn](https://mirror.lzu.edu.cn/) | √ |  | √ | √ |
| 11 | 上海交通大学 | [mirror.sjtu.edu.cn](https://mirror.sjtu.edu.cn/) | √ | √ | √ | √ |
| 12 | 哈尔滨工业大学 | [mirrors.hit.edu.cn](https://mirrors.hit.edu.cn/) | √ | √ |  | √ |
| 13 | 中国科学技术大学 | [mirrors.ustc.edu.cn](https://mirrors.ustc.edu.cn/) | √ | √ | √ | √ |

**注意**，所有镜像站均支持 `Debian` `Ubuntu` `CentOS` 软件源，建议优先选择由企业提供的软件源 如果使用过程中脚本不能正常输出中文内容则可对照此列表使用，顺序与脚本一致！

#### 3、脚本部署

1）一键更换国内软件源脚本（请通过 `SSH客户端工具` 使用）

```
bash <(curl -sSL https://gitee.com/SuperManito/LinuxMirrors/raw/main/ChangeMirrors.sh)
```

**注意：**

- _Debian 系 Linux 默认注释了源码仓库和预发布软件源，若需启用可将 list 源文件中相关内容的所在行 `取消注释`。_
- _RedHat 系 Linux 配置了所有可以配置的仓库，但有一些仓库默认没有启用，若需启用可将 repo 源文件中的 `enabled=0`修改成 `enabled=1`。_

2）安装过程，可以选择自己喜欢的源！

\[caption id="attachment\_2127" align="aligncenter" width="954"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101044652846.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2021/11/20211101044652846.png) \[/caption\]

#### 4、Docker 一键安装脚本

1）Docker 一键安装脚本如下：

```
bash <(curl -sSL https://gitee.com/SuperManito/LinuxMirrors/raw/main/DockerInstallation.sh)
```

Docker CE：Docker Community Edition 镜像仓库，用于下载并安装 Docker 相关软件包。

Docker Hub：Docker Hub 镜像仓库，默认为官方提供的公共库，用于切换下载镜像时的来源仓库，简称镜像加速器。

注意：脚本集成安装 `Docker Engine`与 `Docker Compose`，可手动选择安装版本和下载源，还可手动选择镜像加速器，支持国内外服务器环境和 `ARM`架构处理器环境使用。

2）安装截图

#### 5、最后

1）如果提示 `Command 'curl' not found` 则说明当前未安装 `curl` 软件包，安装命令如下：

```
sudo apt install -y curl  或  sudo yum install -y curl
```

2）如果提示 `Command 'wget' not found` 则说明当前未安装 `wget` 软件包，安装命令如下：

```
sudo apt install -y wget  或  sudo yum install -y wget
```

如果提示 `bash: /proc/self/fd/11: No such file or directory`，请切换至 `Root` 用户执行。
