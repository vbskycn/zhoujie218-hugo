---
title: 安装虚拟环境
slug: install-the-virtual-environment-z1ut2dg
url: /post/install-the-virtual-environment-z1ut2dg.html
date: '2024-06-25 14:17:58+08:00'
lastmod: '2024-07-16 10:50:25+08:00'
toc: true
isCJKLanguage: true
---

# 安装虚拟环境

## 如何安装

你可以按照以下步骤来解决问题：

1. **使用虚拟环境安装 pipenv**： 建议在项目目录中使用虚拟环境来安装和管理 pipenv。首先确保你的系统安装了 `python3-venv`​ 包（如果没有安装可以通过 `apt install python3-venv`​ 安装）。
2. **创建并激活虚拟环境**： 在你的项目目录中执行以下命令来创建虚拟环境并激活它：

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate


    python3 -m venv mkdocs

    ```

    这里 `myenv`​ 是你给虚拟环境取的名字，可以根据需要自定义。
3. **在虚拟环境中安装 pipenv**： 在激活的虚拟环境中，使用 pip 安装 pipenv：

    ```bash
    pip install pipenv
    ```

    这样就能确保 pipenv 被安装在你的虚拟环境中，而不会影响到系统的 Python 环境。
4. **使用 pipenv 管理项目依赖**： 在虚拟环境中使用 pipenv 来管理项目依赖，例如：

    ```bash
    pipenv install requests
    ```

    这会在当前项目的 pipenv 环境中安装 requests 包。

通过以上步骤，你可以避免直接在系统范围内安装 pipenv 或其他 Python 包时出现的问题，同时也能更好地管理项目的依赖关系。

‍

## 如何使用

在创建成功一个虚拟环境后，激活和进入该虚拟环境的步骤取决于你使用的操作系统。以下是不同操作系统上的激活方法：

### 1. **Windows**

在 Windows 上，虚拟环境的激活脚本位于 `Scripts`​ 目录中。你可以使用以下命令激活虚拟环境：

```sh
.\mkdocs\Scripts\activate
```

激活成功后，你会看到命令提示符前面有虚拟环境的名称，例如：

```sh
(mkdocs) C:\path\to\your\project>
```

### 2. **Linux 和 macOS**

在 Linux 和 macOS 上，虚拟环境的激活脚本位于 `bin`​ 目录中。你可以使用以下命令激活虚拟环境：

```sh
source mkdocs/bin/activate
```

激活成功后，你会看到命令提示符前面有虚拟环境的名称，例如：

```sh
(mkdocs) user@hostname:~/path/to/your/project$
```

### 3. **退出虚拟环境**

当你完成工作并想要退出虚拟环境时，可以使用以下命令（适用于所有操作系统）：

```sh
deactivate
```

退出后，命令提示符将恢复为激活虚拟环境之前的状态。

### 例子

假设你在当前目录下创建了一个名为 `mkdocs`​ 的虚拟环境：

#### Windows

```sh
python -m venv mkdocs
.\mkdocs\Scripts\activate
```

#### Linux 和 macOS

```sh
python -m venv mkdocs
source mkdocs/bin/activate
```

### 额外提示

1. **查看激活状态**：你可以使用 `which python`​ 或 `where python`​ 命令来确认当前使用的 Python 解释器是否来自虚拟环境。
2. **安装包**：在激活虚拟环境后，你可以使用 `pip`​ 来安装需要的包，这些包将仅在虚拟环境中可用，不会影响全局 Python 环境。

    ```sh
    pip install mkdocs
    ```

通过这些步骤，你就可以成功激活并进入虚拟环境，开始在隔离的环境中进行开发工作了。
