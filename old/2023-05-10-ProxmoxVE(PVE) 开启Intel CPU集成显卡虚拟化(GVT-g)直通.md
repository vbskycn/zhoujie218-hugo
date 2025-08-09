---
title: "ProxmoxVE(PVE) 开启Intel CPU集成显卡虚拟化(GVT-g)直通"
date: "2023-05-10"
categories: 
  - "diannaowangruo"
tags: 
  - "pve"
url: "/archives/2532.html"
---

Intel CPU集成显卡虚拟化(GVT-g)直通技术与PCIe显卡直通有一定区别，PCIe显卡直通是直接由VM独占显卡。集成显卡虚拟化(GVT-g)和Nvidia vGPU效果类似，就是一个显卡可以同时分配给多台VM并且同时使用，互不干扰。这个方案也是性价比最高的方案。

intel GVT-g 技术有最大并发限制大约在**1-4数量**之间具体视CPU规格 通过[intel ARK](https://ark.intel.com/content/www/cn/zh/ark.html)来查询。

所谓并发的意思就是，并发多少个就可以在多少个VM同时使用。

PCI/GPU 直通仍然是 Proxmox VE 中的一项实验性功能！无法迁移(热迁移/故障转移)含有直通设备的 VM/VPS AMD CPU的核心显卡没有类似intel GVT-g一样的虚拟化技术，所以只能直接以独占直通的方式给某一VM/VPS

因AMD CPU的核心显卡直通步骤比较复杂，本文内不做记录。将会有单独的一篇文章来记录AMD CPU的核心显卡直通

### 基本要求

**硬件:**

- 准备好支持的硬件
    
- 受支持的核心显卡
    

CPU支持核心集成显卡需要 intel 10代或以前(根据内核版本指导)，如版本太新 不代表不支持，也不代表能一定稳定。可能会有一些奇奇怪怪的问题，还需自己踩坑。

**系统：**

- ProxmoxVE(PVE) 中确保已启用 IOMMU
    
- ProxmoxVE(PVE) 中已为VM安装好系统
    
- VM中的系统如为Windows BOIS引导方式需为UEFI
    

### 必要设置

**1\. 机型设置** 在VM的硬件设置中，为VM的`机型` 设置为`q35` 如VM系统为Windows，BIOS引导方式应为UEFI(需在安装系统前定义) 如VM系统为[Linux](https://www.insilen.com/tags/linux)，BIOS引导方式则无要求均支持

\[ \]025453.png)![img](https://img-cloud.zhoujie218.top/piggo/202305101630403.png)

**2\. 编辑引导文件**

**GRUB引导非常常见**，一般也是ProxmoxVE(PVE)系统的**默认引导**方式

该行可能值内容可能会有所有差异，但如果是新系统且已启用 IOMMU，值内容一般如下：

```plain
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt"
```

还没有启用 IOMMU ？[查看方法](https://www.yuque.com/zhoujie218/net/1926a450-8807-41a6-8542-9f6ada8fdc4d#requirements)

在后面加入`i915.enable_gvt=1`

```plain
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt i915.enable_gvt=1"
```

检查无误后，按 `ctrl`+`x` 并按`y`确认保存更改，并更新 grub 配置：

紧接编辑模块`/etc/modules`：

将`kvmgt`添加到其中，注意检查内容。不能重复也不能少

```plain
# 此处为 手动启动IOMMU时候添加
# Modules required for PCI passthrough
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
# 以下为本次添加
# Modules required for Intel GVT
kvmgt
exngt
vfio-mdev
```

检查无误后，按 `ctrl`+`x` 并按`y`确认保存更改。 更改模块后，需要刷新 initramfs。通过执行以下命令来完成：

```plain
update-initramfs -u -k all
```

重启服务器。

重新启动后检查是否再次使用此命令获得任何输出：

```plain
ls /sys/bus/pci/devices/0000\:00\:02.0/mdev_supported_types/
```

**3\. 为虚拟机分配显卡**

1. 添加 -> PCI设备 \[ \]025703.png)![img](https://img-cloud.zhoujie218.top/piggo/202305101630888.png)
    
2. 选择你的 集成显卡 \[ \]025837.png)![img](https://img-cloud.zhoujie218.top/piggo/202305101630549.png)
    
3. Mdev类型变为可选，点开它 \[ \]025847.png)![img](https://img-cloud.zhoujie218.top/piggo/202305101630412.png)
    
4. 按需求分配显卡给VM即可 \[ \]025856.png)![img](https://img-cloud.zhoujie218.top/piggo/202305101630380.png)
    

上图中，可用代表还有几块虚拟集成显卡可以分配：

- 如选择了可用1，那么该VM就能获得最高512M专用显存且最大输出分辨率为 1920×1200
    
- 如选择了可用2，那么该VM就能获得最高384M专用显存且最大输出分辨率为 1024×768,然后另一台VM就还有一个可用数能获得最高384M专用显存且最大输出分辨率为 1024×768的集成显卡。
    

想加大可用数？ 可以尝试在BIOS中加大分配给核心集成显卡专用显存，也能很大程度提高一些可用数
