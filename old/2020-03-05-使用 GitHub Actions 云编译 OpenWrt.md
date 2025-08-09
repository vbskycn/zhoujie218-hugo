---
title: "使用 GitHub Actions 云编译 OpenWrt"
date: "2020-03-05"
categories: 
  - "diannaowangruo"
tags: 
  - "actions"
  - "github"
  - "openwrt"
url: "/archives/1356.html"
---

## 前言

Github Ac­tions 是 GitHub 推出的持续集成 (Con­tin­u­ous in­te­gra­tion，简称 CI) 服务，它提供了配置非常不错的虚拟服务器环境（E5 2vCPU/​7G RAM），基于它可以进行构建、测试、打包、部署项目。对于公共仓库可免费无时间限制的使用（指累积时间），不过要使用它首先需要知道如何编写 workflow 文件。但这篇文章并不是教你如何枯燥的去编写 work­flow 文件，而是教你如何去使用博主已经编写好的 Open­Wrt 编译方案。

## 教程更新

- 2020-02-01 新图文教程
- 2019-12-10 新增 **macOS 编译方案**使用说明
- 2019-12-06 添加 tmate 网页终端链接说明
- 2019-12-05 优化基础使用教程，添加 @lietxia 大佬的图文教程链接
- 2019-12-04 新增**云menuconfig**使用方法
- 2019-12-03 新增**并发编译**使用方法
- 2019-11-30 新增**自定义源码编译**使用方法
- 2019-11-14 全网独家首发

## 方案特点

- 免费
- 一键快速编译
- 定时自动编译
- 客制化编译
- 并发编译（可同时进行20+5个编译任务）
- 无需搭建编译环境（在线`make menuconfig`生成配置文件)
- 无需消耗自己的计算机与服务器的计算资源（性感E5在线编译）
- 无需担心磁盘空间不足（近60G磁盘空间）
- 无需使用清理文件（内核更新不怕 boom ）
- 编译速度快（编译时间1-2小时）
- 编译成功率提升200%（万兆自由网络环境）
- 全新环境（杜绝编译环境不干净导致编译失败）

> 本解决方案是一个开放平台，任何人都可以基于此打造自己专属的编译方案。

## 项目地址

[](https://github.com/P3TERX/Actions-OpenWrt)[https://github.com/P3TERX/Actions-OpenWrt](https://github.com/P3TERX/Actions-OpenWrt)

支持项目请随手点个 `star`，让更多的人发现、使用并受益。

## 准备工作

- 注册 GitHub 账号
- 搭建编译环境，用于生成`.config`文件。(可选)

> **TIPS:** 关于编译环境的搭建，推荐去看我之前写的相关文章，Win­dows 10 可以使用 WSL ，ma­cOS、Linux 可以使用 Docker 。

## 基础使用

首先你必须要熟悉整个 Open­Wrt 的编译过程，这会让你非常容易的理解如何使用 GitHub Ac­tions 进行编译，即使你没有成功过。因为实际上本地编译近 90% 失败的原因是因为网络问题导致的，中国大陆特色，咱也不敢多说。而使用 GitHub Ac­tions 编译成功率至少提升 200% ，为什么这样说呢？因为 Ac­tions 服务器由 Mi­crosoft Azure 提供，在自由的美利坚，拥有万兆带宽。

### 首次编译

- 在自己搭建编译环境中使用 [Lean's OpenWrt](https://p3terx.com/go/aHR0cHM6Ly9naXRodWIuY29tL2Nvb2xzbm93d29sZi9sZWRl) 源码生成`.config`文件。（或使用后面进阶玩法中的**云menuconfig**，直接 SSH 到 Actions 进行操作）

> **TIPS:** 方案默认引用 Lean 的源码，因为他的 README 影响了我开始学习编译，也就有了这个项目，而且他的源码非常的优秀。有其它需求可自行修改 work­flow 文件，方法后面的进阶使用中有说明。

- 进入 [P3TERX/Actions-OpenWrt](https://p3terx.com/go/aHR0cHM6Ly9naXRodWIuY29tL1AzVEVSWC9BY3Rpb25zLU9wZW5XcnQ=) 项目页面，点击页面中的 [Use this template](https://p3terx.com/go/aHR0cHM6Ly9naXRodWIuY29tL1AzVEVSWC9BY3Rpb25zLU9wZW5XcnQvZ2VuZXJhdGU=) （使用这个模版）按钮。

\[caption id="attachment\_1575" align="alignnone" width="1024"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-1024x489.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file.png) \[/caption\]

- 填写仓库名称，然后点击`Create repository from template`（从模版创建储存库）按钮。

\[caption id="attachment\_1576" align="alignnone" width="814"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-1.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-1.png) \[/caption\]

- 经过几秒钟的等待，页面会跳转到新建的仓库，内容和我的项目是相同的。然后点击`Create new file`（创建新文件）按钮。

\[caption id="attachment\_1577" align="alignnone" width="1024"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-2-1024x499.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-2.png) \[/caption\]

- 文件名填写为`.config`，把生成的`.config` 文件的内容复制粘贴到下面的文本框中。

\[caption id="attachment\_1578" align="alignnone" width="1024"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-3-1024x419.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-3.png) \[/caption\]

- 翻到页面最下方，点击`Commit new file`（提交新文件）按钮即可。后续编译工作会自动开始，你可以在 Actions 页面进行查看。

\[caption id="attachment\_1579" align="alignnone" width="1024"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-4-1024x369.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-4.png) \[/caption\]

- 在等待编译完成的过程中，你可以进入[这个页面](https://p3terx.com/go/aHR0cHM6Ly9naXRodWIuY29tL1AzVEVSWC9BY3Rpb25zLU9wZW5XcnQ=)点击右上角的`star`，这是对博主最大的支持，而且还可以加快编译速度哦（雾
- 最后经过一两个小时的等待，不出意外你就可以在 Actions 页面看到已经打包好的固件目录压缩包。

\[caption id="attachment\_1580" align="alignnone" width="828"\][![](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-5.png)](https://img-cloud.zhoujie218.top/wp-content/uploads/2020/04/unnamed-file-5.png) \[/caption\]

> **TIPS:** 如需 ipk 文件可以在**进阶使用**章节找到方法。因为大多数人只需要固件，而且总是有萌新问固件在哪，所以现在默认只上传固件。

### 再次编译

默认情况下触发编译有两种方式：

1. 发布 release
2. 修改`.config`文件

他们分别对应以下使用场景：

- 在编译配置没有修改的情况下，若源码有更新，那么在 releases 页面发布一个 release 将直接使用最新源码进行编译。
- 如果你想修改配置，则生成船新的`.config`文件 push 到仓库来触发编译的工作流程。

其它触发方式你可以在后面的进阶使用中看到。

## 进阶使用

### 自定义环境变量与功能

点击查看打开 work­flow 文件（`.github/workflows/build-openwrt.yml`），你会看到有如下一些环境变量，可按照自己的需求对这些变量进行定义。

```none
env:
  REPO_URL: https://github.com/coolsnowwolf/lede
  REPO_BRANCH: master
  CONFIG_FILE: .config
  DIY_SH: diy.sh
  SSH_ACTIONS: false
  UPLOAD_BIN_DIR: false
  UPLOAD_FIRMWARE: true
  TZ: Asia/Shanghai
```

> **TIPS:** 修改时需要注意`:`(冒号)后面有空格。

| 环境变量 | 功能 |
| --- | --- |
| `REPO_URL` | 源码仓库地址 |
| `REPO_BRANCH` | 源码分支 |
| `CONFIG_FILE` | `.config`文件名 |
| `DIY_SH` | DIY 脚本文件名 |
| `SSH_ACTIONS` | SSH 连接 Actions 功能。默认`false` |
| `UPLOAD_BIN_DIR` | 上传 bin 目录。即包含所有 ipk 文件和固件的目录。默认`false` |
| `UPLOAD_FIRMWARE` | 上传固件目录。默认`true` |
| `TZ` | 时区设置 |

### DIY 脚本

仓库内有一个 `diy.sh` 文件，你可以把对源码修改的指令写到这个文件中，比如修改默认 IP、主机名、主题、添加 / 删除软件包等操作。但不仅限于这些操作，发挥你强大的想象力，可做出更强大的功能。

> **TIPS:** 脚本工作目录在源码目录，内附一个修改默认 IP 的例子供参考使用。

### 添加软件包

在 DIY 脚本中加入对指定软件包的远程仓库的克隆指令。就像下面这样：

```none
git clone https://github.com/P3TERX/xxx package/xxx
```

这样做的好处是每一次编译都会拉取最新的源码。

> **TIPS:** 生成`.config`文件时记得选中相应的软件。如果添加的软件包与 Open­Wrt 中已有的软件包同名的情况，则需要把源码中的同名软件包删除，否则会优先编译 Open­Wrt 中的软件包。这同样可以利用到的 DIY 脚本。

最后不要忘了添加更新 feeds 的命令

```none
./scripts/feeds update -a
./scripts/feeds install -a
```

### Custom files（自定义文件）

俗称 “files 大法”，在仓库根目录下新建 `files` 目录，把文件放入即可。

### 定时自动编译

点击查看编辑 work­flow 文件（`.github/workflows/build-openwrt.yml`）取消注释下面两行。

```none
#  schedule:
#    - cron: 0 8 * * 5
```

例子是北京时间每周五下午 4 点钟开始编译（周末下班回家直接下载最新固件开始折腾）。如需自定义则按照 cron 格式修改即可，Ac­tions 虚拟环境中的时区是 UTC ，注意按照自己所在地时区进行转换。

### 真·一键编译（点击 star 开始编译）

点击自己仓库页面上的 Star 开始编译，为了防止被滥用，这个功能默认没有开启。开启后如果被恶意点击轻则封号，严重可能会导致中美关系恶化、原子弹爆炸、第三次世界大战等后果。（大雾

点击查看编辑 work­flow 文件（`.github/workflows/build-openwrt.yml`）取消注释下面两行，后续点击自己仓库上的 star 即可开始编译。

```none
#  watch:
#    types: [started]
```

> **TIPS:** 字段`started`并不是“开始了”的意思，而是“已经点击 Star”。 **吐槽:** 官方并没有提供一个开始按钮，通过搜索找到过很多奇怪的一键触发方式，但都是通过 Web­hook 来实现的。机智的我发现了可以通过点击 Star 来触发，这样就相当于把 Star 当成开始按钮。这个`started`有种一句双关的意思了。

有个小技巧可以防止恶意点击，在 `runs-on: ubuntu-latest` 下面加上 `if: github.event.repository.owner.id == github.event.sender.id`。这样只有你自己点 `star` 才会触发编译。

```none
jobs:
  build:
    runs-on: ubuntu-latest
    if: github.event.repository.owner.id == github.event.sender.id
```

### 自定义源码编译

此方案默认引用的是 L 大的源码，如果你觉得不好用或者有编译其它源码的需求可以进行替换，自由是本解决方案最大的特点。

点击查看编辑 work­flow 文件（`.github/workflows/build-openwrt.yml`），修改下面的相关环境变量字段。

```none
REPO_URL: https://github.com/coolsnowwolf/lede
REPO_BRANCH: master
```

比如修改为 Open­Wrt 官方源码 19.07 分支

```none
REPO_URL: https://github.com/openwrt/openwrt
REPO_BRANCH: openwrt-19.07
```

> **TIPS:** 注意冒号后面有空格

### 并发编译（同时编译多个固件）

#### 多 repository 方案

通过 [P3TERX/Actions-OpenWrt](https://p3terx.com/go/aHR0cHM6Ly9naXRodWIuY29tL1AzVEVSWC9BY3Rpb25zLU9wZW5XcnQ=) 项目创建多个仓库来编译不同架构机型的 Open­Wrt 固件。

#### 多 workflow 方案

基于 GitHub Ac­tions 可同时运行多个工作流程的特性，最多可以同时进行至少 20 个编译任务。也可以单独选择其中一个进行编译，这充分的利用到了 GitHub Ac­tions 为每个账户免费提供的 20 个 Ubuntu 虚拟服务器环境。此外你还可以额外再使用 5 个 macOS 虚拟服务器环境进行编译，开启方法在后面有说明。

点击查看

### 云 menuconfig（SSH 连接到 Actions）

通过 tmate 连接到 GitHub Ac­tions 虚拟服务器环境，可直接进行 `make menuconfig` 操作生成编译配置，或者任意的客制化操作。也就是说，你不需要再自己搭建编译环境了。这可能改变之前所有使用 GitHub Ac­tions 的编译 Open­Wrt 方式。

点击查看

### macOS 编译方案

GitHub Ac­tions 的 ma­cOS 虚拟机性能要高于 Ubuntu 虚拟机，所以使用它编译 Open­Wrt 理论上速度会更快。博主经过几天时间的研究已经总结出了 macOS 下的 OpenWrt 编译环境的搭建方法，并编写出了适用于 ma­cOS 虚拟环境的 Open­Wrt 编译方案的 work­flow 文件。

由于并不是每个开发者都会按照规范去写代码，所以使用 ma­cOS 编译 Open­Wrt 不可避免的会遇到非常多的问题，而且后续测试发现 ma­cOS 虚拟机性能已大幅下降，故相关 work­flow 文件已经移除。也不建议任何人使用 ma­cOS 编译 Open­Wrt 。

## 尾巴

希望大家不要滥用免费的开发资源，需要时再编译，让开发者来充分利用才能产生更多更好的软件，这样大家才能受益。

* * *

相关 TG 群组：[GitHub Actions Group](https://p3terx.com/go/aHR0cHM6Ly90Lm1lL0dpdEh1Yl9BY3Rpb25z)

相关 TG 频道：[GitHub Actions Channel](https://p3terx.com/go/aHR0cHM6Ly90Lm1lL0dpdEh1Yl9BY3Rpb25zX0NoYW5uZWw=)

本博客已开设 [Telegram 频道](https://p3terx.com/go/aHR0cHM6Ly90Lm1lL1AzVEVSWF9aT05F)，欢迎小伙伴们订阅关注。

> **本文作者：**[P3TERX](https://p3terx.com/)
> 
> **本文链接：**[https://p3terx.com/archives/build-openwrt-with-github-actions.html](https://p3terx.com/archives/build-openwrt-with-github-actions.html)
> 
> **版权声明：**本博客所有文章除特别声明外，均采用 [CC BY-NC-SA 4.0](https://p3terx.com/go/aHR0cHM6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL2xpY2Vuc2VzL2J5LW5jLXNhLzQuMC9kZWVkLnpo) 许可协议。非商业转载及引用请注明出处（作者、原文链接），商业转载请联系作者获得授权。
