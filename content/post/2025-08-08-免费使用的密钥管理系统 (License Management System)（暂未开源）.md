---
title: "免费使用的密钥管理系统 (License Management System)（暂未开源）"
date: "2025-08-08"
categories: 
  - "diannaowangruo"
  - "wangyesheji"
tags: 
  - "license"
  - "密钥"
  - "开源"
  - "许可证"
url: "/archives/2677.html"
---

# 密钥管理系统 (License Management System)

> 现代化License管理系统，支持密钥生成、验证、设备管理等功能

![系统截图1](https://img-cloud.zhoujie218.top/2025/08/08/6895620ddd447.png)

![系统截图2](https://img-cloud.zhoujie218.top/2025/08/08/6895621d7c746.png)

![系统截图3](https://img-cloud.zhoujie218.top/2025/08/08/689562205aa4f.png)

## 系统特性

![系统截图4](https://img-cloud.zhoujie218.top/2025/08/08/68956233c2cdf.png)

![系统截图5](https://img-cloud.zhoujie218.top/2025/08/08/6895622d2aa60.png)

## 📚 文档导航

本系统提供完整的技术文档，按照不同用户角色进行分类：

### 📖 用户指南

面向最终用户的使用文档：

- [用户指南](https://license.zhoujie8.cn/user-guide) - 完整的安装、部署、使用指南

### 🔧 开发者指南

面向开发者的技术文档：

- [开发者指南](https://license.zhoujie8.cn/developer-guide) - 技术架构、API接口、集成指南

### ⚙️ 管理员指南

面向系统管理员的运维文档：

- [管理员指南](https://license.zhoujie8.cn/admin-guide) - 系统配置、备份恢复、故障排除

## 根据您的需求，快速选择相应的文档：

### 👤 我是最终用户

**想要安装和使用系统**

- [📖 用户指南](https://license.zhoujie8.cn/user-guide/) - 完整的安装、部署、使用指南
    - [🚀 快速开始](https://license.zhoujie8.cn/user-guide/#_1) - 环境要求和基本安装
    - [📦 安装指南](https://license.zhoujie8.cn/user-guide/#_6) - 详细的安装步骤
    - [🐳 Docker部署](https://license.zhoujie8.cn/user-guide/#docker) - 容器化部署方案
    - [📖 使用指南](https://license.zhoujie8.cn/user-guide/#_12) - 系统操作说明
    - [⚙️ 配置说明](https://license.zhoujie8.cn/user-guide/#_21) - 环境变量配置
    - [🔧 故障排除](https://license.zhoujie8.cn/user-guide/#_27) - 常见问题解决

### 👨‍💻 我是开发者

**想要集成API或了解技术细节**

- [🔧 开发者指南](https://license.zhoujie8.cn/developer-guide/) - 技术架构、API接口、集成指南
    - [🏗️ 技术架构](https://license.zhoujie8.cn/developer-guide/#_1) - 系统架构设计
    - [🔐 密钥验证逻辑](https://license.zhoujie8.cn/developer-guide/#_6) - 验证机制详解
    - [📡 API接口](https://license.zhoujie8.cn/developer-guide/#api) - 完整的API文档
    - [🔗 客户端集成](https://license.zhoujie8.cn/developer-guide/#_34) - 集成示例和SDK
    - [🛡️ 安全机制](https://license.zhoujie8.cn/developer-guide/#_40) - 安全设计和防护
    - [🧪 测试指南](https://license.zhoujie8.cn/developer-guide/#_42) - 测试方法和工具

### 👨‍💼 我是系统管理员

**想要配置和维护系统**

- [⚙️ 管理员指南](https://license.zhoujie8.cn/admin-guide/) - 系统配置、备份恢复、故障排除
    - [⚙️ 系统配置](https://license.zhoujie8.cn/admin-guide/#_1) - 环境变量和高级配置
    - [💾 备份恢复](https://license.zhoujie8.cn/admin-guide/#_15) - 数据备份和恢复策略
    - [🔧 故障排除](https://license.zhoujie8.cn/admin-guide/#_28) - 系统问题诊断和解决
    - [📊 监控维护](https://license.zhoujie8.cn/admin-guide/#_36) - 系统监控和维护
    - [🛡️ 安全加固](https://license.zhoujie8.cn/admin-guide/#_46) - 安全配置和加固措施

## 🚀 快速开始

### 🐳 Docker部署

#### 最新版本部署

```bash
# 创建数据目录（持久化）
mkdir -p ${PWD}/license-data

# 设置目录权限（Linux/macOS）
sudo chown -R 1000:1000 ${PWD}/license-data
sudo chmod -R 755 ${PWD}/license-data

# 停止并删除旧容器
docker stop license-management-system
docker rm license-management-system

# 启动容器
docker run -d \
  --name license-management-system \
  --restart unless-stopped \
  -p 3005:3005 \
  -v ${PWD}/license-data:/app/data \
  -e JWT_SECRET="your-super-secret-jwt-key-change-this-in-production" \
  -e LICENSE_SECRET_KEY="your-super-secret-license-key-change-this-in-production" \
  -e PORT="3005" \
  -e NODE_ENV="production" \
  -e DEBUG_MODE="false" \
  -e LOG_LEVEL="warn" \
  zhoujie218/license-management-system:latest
```

#### 可选环境变量

```bash
# 全局请求速率限制：每分钟最多允许 2000 个请求
-e RATE_LIMIT_MAX_REQUESTS="2000" \

# API 接口的请求限制：每分钟最多允许 5000 个 API 请求
-e API_RATE_LIMIT_MAX_REQUESTS="5000" \

# 登录尝试限制：最多允许 20 次失败的登录尝试
-e LOGIN_RATE_LIMIT_MAX_ATTEMPTS="20" \

# 允许的访问来源域名（多个使用英文逗号分隔，无空格）
-e ALLOWED_DOMAINS="https://yourdomain.com,https://www.yourdomain.com" \

# 允许加载的 CDN 链接（多个使用英文逗号分隔）
-e ALLOWED_CDNS="https://cdn.bootcdn.net,https://static.cloudflareinsights.com,https://*.cloudflare.com" \
```

#### 验证部署

```bash
# 使用Docker Compose
docker-compose up -d

# 或使用Docker Hub镜像
docker run -d -p 3005:3005 zhoujie218/license-management-system:latest
```

### 访问系统

打开浏览器访问：`http://localhost:3005`

### 默认账户

- **用户名**: admin
- **密码**: admin123

### 🌐 域名配置（重要）

如果您需要部署到自己的域名，请配置以下环境变量：

```bash
# 在 .env 文件中添加
ALLOWED_DOMAINS=https://yourdomain.com
ALLOWED_CDNS=https://cdn.bootcdn.net,https://cdn.jsdelivr.net

# 默认cos允许所有域名和cdn
```

**详细配置说明**: 请参考[用户指南](user-guide.md)中的部署配置章节。

> **注意**: 如果看到CSP错误（如Cloudflare Insights被阻止），这是正常的。如果系统功能正常，可以忽略这些错误。

## 🏗️ 技术架构

本系统采用**应用-密钥类型**架构，已废弃旧的产品-套餐模型：

- **应用 (Application)**: 每个密钥必须属于一个应用
- **密钥类型 (License Type)**: 每个应用下有多个密钥类型
- **密钥 (License)**: 基于应用和密钥类型生成

### 核心特性

- ✅ 应用-密钥类型架构
- ✅ 设备管理策略（宽松期/严格期）
- ✅ 密钥激活逻辑（首次验证激活）
- ✅ 批量管理功能（导出、删除、复制）
- ✅ 用户管理功能
- ✅ IP地址记录
- ✅ 速率限制
- ✅ 暂停/恢复功能
- ✅ 搜索和过滤功能
- ✅ 在线备份还原功能
- ✅ 备份文件管理

## 📞 支持与反馈

如有问题或建议，请：

1. 查看对应分类的文档
2. 提交Issue描述问题
3. 联系技术支持

### 相关链接

- 🌐 [项目主页](https://github.com/vbskycn/License)
- 📚 [在线文档](https://license.zhoujie8.cn/)
- 🐛 [问题反馈](https://github.com/vbskycn/License/issues)
- 🐳 [Docker镜像](https://hub.docker.com/r/zhoujie218/license-management-system)

* * *

**密钥管理系统** - 让License管理更简单、更高效！
