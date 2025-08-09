---
title: "开源工具：Cloudflare Pages 部署记录清理，给我们的大善人节约一点资源吧（原创）"
date: "2025-01-07"
categories: 
  - "diannaowangruo"
tags: 
  - "cloudflare"
  - "github"
url: "/archives/2651.html"
---

# Cloudflare Pages 部署记录清理工具

你是否遇到过Cloudflare Pages项目删除失败，workes项目记录太多，网页不能删除？

这个工具就是解决 Cloudflare Pages 部署记录过多，导致无法创建新部署，无法删除项目的问题。

强烈推荐大家都用上，给我们的大善人节约一点硬盘空间：）

这是一个利用GitHub Actions 自动化运行的工具。该工具会保留每个项目最新的 10 个部署记录，删除更早的部署以节省空间。

![image-20250107154422056](https://img-cloud.zhoujie218.top/2025/01/07/677cdb5eca982.png)

## 功能特点

- 自动获取账号下所有的 Cloudflare Pages 项目（一次运行获取最活跃的10个）
- 对每个项目只保留最新的 10 个部署记录
- 自动删除较早的部署记录
- 支持批量处理多个项目
- 循环处理直到清理完所有旧记录
- 支持通过 GitHub Actions 自动运行

* * *

## 使用方法（推荐 GitHub Actions 自动运行）

### 1\. Fork 本项目

\#### 点击下方链接一键 Fork

https://github.com/vbskycn/delete-cloudflare-deployments/fork

### 2\. 获取必要信息

首先需要获取以下信息：

- Cloudflare Account ID
- Cloudflare API Token（需要有 Pages 的编辑权限）

#### 获取 API Token

1. 登录 Cloudflare 控制台：[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)
2. 点击 "Create Token" 按钮
3. 选择 "Create Custom Token"
4. 设置以下权限：
    - Account - Cloudflare Pages - Edit
    - Zone - DNS - Edit（如果需要）
5. 在 "Account Resources" 中选择你的账号
6. 设置 Token 名称（例如：pages-deployment-cleanup）
7. 点击 "Continue to summary" 然后创建 Token
8. 保存显示的 Token 值（这个值只会显示一次）

重要提示： API Token 只会显示一次，请务必立即保存。

#### 获取 Account ID

1. 登录 Cloudflare 控制台
2. 在右侧边栏找到 "Account ID"
3. 或者从浏览器地址栏中复制，格式类似：[https://dash.cloudflare.com/your-account-id](https://dash.cloudflare.com/your-account-id)

### 3\. 设置仓库变量

在 Fork 后的仓库中配置以下变量：

```
CF_API_TOKEN=your_cloudflare_api_token
CF_ACCOUNT_ID=your_cloudflare_account_id
```

![image-20250107154744260](https://img-cloud.zhoujie218.top/2025/01/07/677cdc2709a95.png)

* * *

## GitHub Actions 配置

要设置自动运行，需要在 GitHub 仓库中配置以下 Secrets：

1. 打开仓库的 Settings
2. 进入 Secrets and variables → Actions
3. 添加以下 secrets：
    - CF\_API\_TOKEN
    - CF\_ACCOUNT\_ID

* * *

## 常见问题

### 1\. API 返回 403 错误

检查 API Token 是否具有正确的权限，确保包含了 Pages 的编辑权限。

### 2\. 部署记录未完全清理

由于 API 限制，每次只能获取 25 个记录。脚本会自动循环处理，多运行几次即可。

如果你的部署记录太多，每一次运行可能需要比较长的时间。

* * *

如有问题，请访问 [GitHub Issues](https://github.com/vbskycn/delete-cloudflare-deployments/issues)

Cloudflare Pages 官方脚本：[删除部署记录脚本](https://pub-505c82ba1c844ba788b97b1ed9415e75.r2.dev/delete-all-deployments.zip)
