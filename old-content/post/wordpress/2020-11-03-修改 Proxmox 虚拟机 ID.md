---
title: "修改 Proxmox 虚拟机 ID"
date: "2020-11-03"
categories: 
  - "luanqibazhao"
  - "diannaowangruo"
tags: 
  - "pve"
url: "/archives/1886.html"
---

在安装虚拟机时，我们往往会对虚拟机 ID 做一些规划，比如 100~199 为服务器，200-299 为客户端。当你安装好系统，部署完服务后却发现忘记设置虚拟机 ID 时，作为一名强迫症患者，此时会选择删除重装？还是就此妥协？

1. 关闭需要更改 ID 的虚拟机
2. 进入 `/etc/pve/nodes/` 目录
3. 进入该目录下的节点目录，名称即为你的 Proxmox 服务器名称
4. KVM 虚拟机进入 `qemu-server` 目录，LXC 容器进入 `lxc` 目录
5. 重命名原 ID 配置文件为目标 ID
6. 编辑该配置文件，修改硬盘存放目录 (共 2 处)
7. 进入 `/var/lib/vz/images` 目录
8. 重命名原 ID 目录后进入该目录
9. 重命名磁盘文件(/dev/pve/)
10. 刷新 Web 控制台，并启动虚拟机
