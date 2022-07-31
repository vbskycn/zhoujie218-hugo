---
title: "怎么使用永久免费的VPS服务器 Google Cloud Shell"
date: "2020-02-29"
categories: 
  - "diannaowangruo"
tags: 
  - "google-cloud"
  - "ssh"
url: "/archives/1341.html"
---

启动地址： **[https://ssh.cloud.google.com/](https://ssh.cloud.google.com/)**

CLOUD SHELL 在任意浏览器中通过命令行管理您的基础架构和应用

Google Cloud Shell 让您可以直接在浏览器中通过命令行访问云端资源。您可以轻松管理项目和资源，而无需在系统上安装 [Google Cloud SDK](https://cloud.google.com/sdk) 或其他工具。Cloud Shell 让您可以根据自己的需要，随时使用最新且经过全面身份验证的 Cloud SDK [gcloud](https://cloud.google.com/sdk/gcloud) 命令行以及其他必要的实用工具。

官方文档： [https://cloud.google.com/shell/docs](https://cloud.google.com/shell/docs)

![](https://cloud.google.com/shell/docs/images/cloud-shell-activate.gif)

已登录的用户在网络浏览器中从 GOOGLE CLOUD CONSOLE 启动 CLOUD SHELL 实例，并检查 GOOGLE CLOUD 组件的版本。

![](https://cloud.google.com/images/products/cloud-shell/full-power-access.png)

## 安全可靠且默认经过全面身份验证

Cloud Shell 提供内置授权，方便您访问 Google Cloud Platform 上托管的项目和资源。

![](https://cloud.google.com/images/products/cloud-shell/secure-fully-authenticated.png)

## 您喜爱的工具已预先装好，并且是最新版本

Cloud Shell 预装了许多您喜爱的命令行工具，包括 bash 和 sh，以及 emacs 和 vim，并且均为最新版本。MySQL 客户端、Docker 和 Kubernetes 等管理工具已配置完毕并准备就绪，因此您无需费神思考如何安装最新版本工具及其所有依赖项，只要连接到 Cloud Shell 即可使用！

![](https://cloud.google.com/images/products/cloud-shell/pre-installed-tools.png)

## 方便开发者使用

开发者可以轻松使用所有自己喜欢的且预先配置好的开发工具，包括 Java、Go、Python、Node.js、PHP 及 Ruby 开发和部署工具。您可以在 Cloud Shell 实例中运行 Web 应用，并通过浏览器进行预览，然后使用预先配置的 Git 和 Mercurial 客户端将其提交回代码库。

![](https://cloud.google.com/images/products/cloud-shell/developer-ready.png)

## 5GB 永久性磁盘存储空间

Cloud Shell 提供 5GB 的永久性磁盘存储空间，作为您在 Cloud Shell 实例上的 $HOME 目录。您存储在主目录中的所有文件（包括脚本以及 .bashrc 和 .vimrc 等用户配置文件）在不同会话之间保持不变。

方案

下载安装官方SDK： [https://cloud.google.com/sdk/docs/downloads-versioned-archives](https://cloud.google.com/sdk/docs/downloads-versioned-archives)

地址获取： [点击下载](https://codekon.xyz/tools/codecommand)

也可以用 ：MobaXterm\_Personal\_12.3     FinalShell：[点击下载](https://codekon.xyz/tools/finalshell)

#### CodeCommand 来干点什么吧

先安装sdk 下载64位版，右键管理员安装

添加系统变量  sdk\\bin\\ 

获取到地址就登入吧 

ssh -p 6000 root@devshell-vm-38591f26-0c1a-4990-8066-eef88a294bd1.cloudshell.dev

在用户\\.ssh  文件夹下面  google\_compute\_engine 是私钥

远程centos密钥ssh登入

ssh-keygen -t rsa 一路回车生成密钥

文件600权限  .ssh700权限

id\_rsa       authorized\_keys      改成google\_compute\_engine 里面的私钥

ssh -p 6000 root@devshell-vm-38591f26-0c1a-4990-8066-eef88a294bd1.cloudshell.dev

命令 

初始化： gcloud init

启动：gcloud alpha cloud-shell ssh

选择区域：`gcloud config set compute/region us-east1`

目前 可用计划任务，防止掉线。配额还在测试！

防掉线

- 可以用Shell 或 PHP 做个计划任务，30分钟主动连接一下SSH，目前稳定，不重置不关机！

翻墙

目前还没有 好方法，但是可以用ssh隧道代理

![](https://1.bp.blogspot.com/-VdjgoaiBqaU/XlPCBNCROjI/AAAAAAAAB2g/YG5n4Rj6IhEMnGBoGWN6XNIptgpUt04ZACLcBGAsYHQ/s1600/20200224202948.png)

注意

Cloud Shell 会话的后端虚拟机实例并非永久分配给该会话，当会话处于非活跃状态一小时后，相关虚拟机即会终止。实例终止后，您在 `$HOME` 之外对其所做的任何修改都将丢失。

不推荐搭建什么翻墙，做做爬虫、转存等发挥更大价值

 

 

 

 

## ssh 登录服务器的两种方式

如果是一个比较喜欢折腾的人，在某个云平台购买了一台云主机，除了通过云平台提供的 web 页面上的命令行工具，其实也可以在本地电脑上面通过 ssh 进行登录。具体地又可以分成两种：

1. ssh 用户名密码登录
2. ssh 证书（免密码）登录

需要说明一下，后者的安全性高于前者，因此一般会默认不启用第一种登录方式，只允许第二种登录方式。

SSH 为 Secure Shell 的缩写，是建立在应用层基础上的安全协议，利用 SSH 协议可以有效防止远程管理过程中的信息泄露问题。ssh 分成服务端与客户端，其中服务端运行在被登录的机器上面，客户端运行在操作的机器上面。

### 用户名密码登录

通常 openssh-server 默认允许用户名密码登录，但是不排除为了安全考虑云上的服务器上禁止开启 ssh 的这种登录方式，毕竟用户名加密码的方式很容易被爆力破解。如果大家理解其中的厉害关系，可以检查修改 /etc/ssh/sshd\_config（sshd 的配置文件）中 PasswordAuthentication 这一项配置为 yes（一般默认是 yes ）。修改完配置重启 sshd 服务就可以使用用户名和密码登录了。

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span></pre></td><td class="code"><pre><span class="line"><span class="comment"># -l 指定用户名为 wangao</span></span>
<span class="line"><span class="comment"># -p 指定端口为 2222，默认为 22</span></span>
<span class="line"><span class="comment"># 输入下面的命令后根据提示输入密码就可以登录到对应的服务器了 </span></span>
<span class="line">ssh -l wangao -p 2222 192.168.56.101</span></pre></td></tr></tbody></table>

### ssh 免密登录

所谓免密登录，也就是说不需要人工再输入用户名和密码了，但这并不意味着没有了鉴权的动作，服务器毕竟是自己的，不能随便允许别人登录到上面去搞破坏。ssh 免密登录通过证书进行鉴权。

这里的证书分为公钥与私钥，我们可以简单地理解为：公钥 = 锁；私钥 = 钥匙。

流程基本是这样的：如果我们想要从 A 免密登录到 B，就需要把公钥（锁）放到 B 的特定位置，而 A 拥有私钥（钥匙）的完整副本。当 A 拿着私钥去访问 B 的时候，B 发现自己身上有一把锁（B 可能有很多公钥）可以被 A 的私钥打开，于是给 A 放行，A 就成功登录到 B 了。

> 如何得到证书（公钥与私钥） 上面提到的证书可以通过两种方式获取得到。 第一种是向服务器管理员索取，一般索取得到的是私钥，这样就可以免密登录到任何存放了公钥的服务器了。 第二种是自己生成证书（比如使用 ssh-keygen），然后把公钥放到对应的服务器的特定位置，就可以免密登录到对应的服务器了。

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span>
<span class="line">5</span></pre></td><td class="code"><pre><span class="line"><span class="comment"># 通过 ssh-keygen 可以生成需要的证书 </span></span>
<span class="line"><span class="comment"># 根据提示一路按 RETURN(ENTER) 即可 </span></span>
<span class="line"><span class="comment"># 默认情况下会生成 id_rsa 和 id_rsa.pub </span></span>
<span class="line"><span class="comment"># id_rsa 为私钥，id_rsa.pub 为公钥 </span></span>
<span class="line">ssh-keygen</span></pre></td></tr></tbody></table>

> 公钥放置位置

linux 系统允许多用户登录同一台服务器，一般情况下 /home 目录会有非常多的用户目录。可以把公钥放置在任何一个用户目录的 $HOME/.ssh/authorized\_keys 文件中，比如 cat id\_rsa.pub >> /home/wangao/.ssh/authorized\_keys ，这样就可以使用私钥以 wangao 的名义登录对应的服务器了。

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span>
<span class="line">5</span>
<span class="line">6</span>
<span class="line">7</span></pre></td><td class="code"><pre><span class="line"><span class="comment"># -i 指定私钥，默认条件下使用 ~/.ssh/id_rsa</span></span>
<span class="line"><span class="comment"># -l 指定用户名 </span></span>
<span class="line"><span class="comment"># -p 指定端口，默认为 22</span></span>
<span class="line">ssh -i ~/.ssh/id_rsa -p 2222 -l wangao 192.168.56.101</span>
<div></div>
<span class="line"><span class="comment"># 上面的命令等同于 </span></span>
<span class="line">ssh -p 2222 wangao@192.168.56.101</span></pre></td></tr></tbody></table>

## ssh 免密码登录一般流程

### 生成 PublicKey

> 建议设置并牢记 passphrase 密码短语，以 Linux 生成为例

Linux：ssh-keygen -t rsa \[私钥 (id\_rsa) 与公钥 (id\_rsa.pub)\] Windows：SecurCRT/Xshell/PuTTY \[SSH-2 RSA 2048\]

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span>
<span class="line">5</span>
<span class="line">6</span>
<span class="line">7</span>
<span class="line">8</span>
<span class="line">9</span>
<span class="line">10</span>
<span class="line">11</span>
<span class="line">12</span>
<span class="line">13</span>
<span class="line">14</span>
<span class="line">15</span>
<span class="line">16</span>
<span class="line">17</span>
<span class="line">18</span>
<span class="line">19</span>
<span class="line">20</span>
<span class="line">21</span>
<span class="line">22</span>
<span class="line">23</span>
<span class="line">24</span>
<span class="line">25</span>
<span class="line">26</span>
<span class="line">27</span></pre></td><td class="code"><pre><span class="line"><span class="comment"># 生成 SSH 密钥对 </span></span>
<span class="line">ssh-keygen -t rsa</span>
<div></div>
<span class="line">Generating public/private rsa key pair.</span>
<span class="line"><span class="comment"># 建议直接回车使用默认路径 </span></span>
<span class="line">Enter file <span class="keyword">in</span> <span class="built_in">which</span> to save the key (/root/.ssh/id_rsa): </span>
<span class="line"><span class="comment"># 输入密码短语（留空则直接回车）</span></span>
<span class="line">Enter passphrase (empty <span class="keyword">for</span> no passphrase): </span>
<span class="line"><span class="comment"># 重复密码短语 </span></span>
<span class="line">Enter same passphrase again: </span>
<span class="line">Your identification has been saved <span class="keyword">in</span> /root/.ssh/id_rsa.</span>
<span class="line">Your public key has been saved <span class="keyword">in</span> /root/.ssh/id_rsa.pub.</span>
<span class="line">The key fingerprint is:</span>
<span class="line">aa:8b:61:13:38:ad:b5:49:ca:51:45:b9:77:e1:97:e1 root@localhost.localdomain</span>
<span class="line">The key<span class="string">'s randomart image is:</span></span>
<span class="line"><span class="string">+--[ RSA 2048]----+</span></span>
<span class="line"><span class="string">|    .o.          |</span></span>
<span class="line"><span class="string">|    ..   . .     |</span></span>
<span class="line"><span class="string">|   .  . . o o    |</span></span>
<span class="line"><span class="string">| o.  . . o E     |</span></span>
<span class="line"><span class="string">|o.=   . S .      |</span></span>
<span class="line"><span class="string">|.*.+   .         |</span></span>
<span class="line"><span class="string">|o.*   .          |</span></span>
<span class="line"><span class="string">| . + .           |</span></span>
<span class="line"><span class="string">|  . o.           |</span></span>
<span class="line"><span class="string">+-----------------+</span></span></pre></td></tr></tbody></table>

### 复制密钥对

> 也可以手动在客户端建立目录和 authorized\_keys，注意修改权限

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span></pre></td><td class="code"><pre><span class="line"><span class="comment"># 复制公钥到无密码登录的服务器上, 22 端口改变可以使用下面的命令 </span></span>
<span class="line"><span class="comment">#ssh-copy-id -i ~/.ssh/id_rsa.pub "-p 10022 user@server"</span></span>
<span class="line">ssh-copy-id -i ~/.ssh/id_rsa.pub root@192.168.15.241</span></pre></td></tr></tbody></table>

### 修改 SSH 配置文件

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span>
<span class="line">5</span>
<span class="line">6</span>
<span class="line">7</span>
<span class="line">8</span>
<span class="line">9</span>
<span class="line">10</span>
<span class="line">11</span>
<span class="line">12</span>
<span class="line">13</span>
<span class="line">14</span>
<span class="line">15</span></pre></td><td class="code"><pre><span class="line"><span class="comment"># 编辑 sshd_config 文件 </span></span>
<span class="line">vi /etc/ssh/sshd_config</span>
<div></div>
<span class="line"><span class="comment"># 禁用密码验证 </span></span>
<span class="line">PasswordAuthentication no</span>
<span class="line"><span class="comment"># 启用密钥验证 </span></span>
<span class="line">RSAAuthentication yes</span>
<span class="line">PubkeyAuthentication yes</span>
<span class="line"><span class="comment"># 指定公钥数据库文件 </span></span>
<span class="line">AuthorsizedKeysFile .ssh/authorized_keys</span>
<div></div>
<span class="line">sed -i <span class="string">"s/^PasswordAuthentication.*/PasswordAuthentication no/g"</span> /etc/ssh/sshd_config</span>
<span class="line">sed -i <span class="string">"s/^#RSAAuthentication.*/RSAAuthentication yes/g"</span> /etc/ssh/sshd_config</span>
<span class="line">sed -i <span class="string">"s/^#PubkeyAuthentication.*/PubkeyAuthentication yes/g"</span> /etc/ssh/sshd_config</span>
<span class="line">sed -i <span class="string">"s/^#AuthorizedKeysFile.*/AuthorizedKeysFile .ssh\/authorized_keys/g"</span> /etc/ssh/sshd_config</span></pre></td></tr></tbody></table>

> 重启 SSH 服务前建议多保留一个会话以防不测

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span>
<span class="line">5</span>
<span class="line">6</span></pre></td><td class="code"><pre><span class="line"><span class="comment"># RHEL/CentOS 系统 </span></span>
<span class="line">service sshd restart</span>
<span class="line"><span class="comment"># Ubuntu 系统 </span></span>
<span class="line">service ssh restart</span>
<span class="line"><span class="comment"># Debian 系统 </span></span>
<span class="line">/etc/init.d/ssh restart</span></pre></td></tr></tbody></table>

### 手动增加管理用户

> 可以在 == 后加入用户注释标识方便管理

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span></pre></td><td class="code"><pre><span class="line"><span class="built_in">echo</span> <span class="string">'ssh-rsa XXXX'</span> &gt;&gt;/root/.ssh/authorized_keys</span>
<div></div>
<span class="line"><span class="comment"># 复查 </span></span>
<span class="line">cat /root/.ssh/authorized_keys</span></pre></td></tr></tbody></table>

## 使用 Ansible 添加 ssh 信任关系

> 使用 ansible authorized\_key module 即可

<table><tbody><tr><td class="gutter"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span>
<span class="line">5</span>
<span class="line">6</span>
<span class="line">7</span>
<span class="line">8</span>
<span class="line">9</span>
<span class="line">10</span>
<span class="line">11</span>
<span class="line">12</span>
<span class="line">13</span>
<span class="line">14</span>
<span class="line">15</span></pre></td><td class="code"><pre><span class="line">---</span>
<span class="line">- hosts: all</span>
<span class="line">  remote_user: root</span>
<span class="line">  gather_facts: <span class="literal">false</span></span>
<div></div>
<span class="line">  tasks:</span>
<span class="line">    - name: authadd root</span>
<span class="line">      authorized_key:</span>
<span class="line">        user: root</span>
<span class="line">        state: present</span>
<span class="line">        key: <span class="string">"{{ lookup('file','/root/.ssh/id_rsa.pub') }}"</span></span>
<span class="line">        path: /root/.ssh/authorized_keys</span>
<span class="line">        manage_dir: no</span>
<span class="line">      tags:</span>
<span class="line">        - root</span></pre></td></tr></tbody></table>
