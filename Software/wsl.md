---
id: DXIiJmT28Q6aEh8bCWSkc
title: Wsl
desc: ''
updated: 1639423509837
created: 1639423509837
---

[Windows](Windows.md)<!-- [[Windows]] --> 

## env

- [在 Windows 10 上安装 WSL | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)
- [旧版 WSL 的手动安装步骤 | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual)
- [Manually download Windows Subsystem for Linux (WSL) Distros | Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install-manual)
- [Run Linux GUI apps with WSL | Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)

---

- [WSL 的基本命令 | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/wsl/basic-commands)

```cmd
@REM 安装wsl
wsl --install

列出可用的 Linux 发行版
wsl --list --online 

安装特定的 Linux 发行版
wsl --install -d Ubuntu
wsl --install -d Debian

列出已安装的 Linux 发行版
wsl --list --verbose
wsl -l -v

将 WSL 版本设置为 1 或 2
wsl --set-default-version 2

设置默认 Linux 发行版
wsl -s debian
wsl -s ubuntu
wsl --set-default-version <Version#>
wsl cat /etc/issue
wsl --list --verbose

检查 WSL 状态
wsl --status

更新 WSL
wsl --update

终止指定的发行版
wsl --terminate <Distribution Name>

注销或卸载 Linux 发行版
wsl --unregister <DistributionName>

立即终止所有正在运行的发行版和 WSL 2 轻量级实用工具虚拟机
wsl --shutdown

net stop lxssmanager
net start lxssmanager
```

[WSL与Windows交互实践 - 蘑菇先生 - 博客园](https://www.cnblogs.com/mushroom/p/8969338.html)

## fatal

### %LOCALAPPDATA%/Docker/wsl/data/ext4.vhdx 文件太大

tasklist | find "docker" && taskkill /f /im "docker.exe"
wsl --shutdown

迁移

[win10使用WSL 2运行Docker Desktop，运行文件从C盘迁移到其他目录 - xhznl - 博客园](https://www.cnblogs.com/xhznl/p/13184398.html#4634011)
[【Docker】win10上修改docker的镜像文件存储位置（九）- 通过WSL2修改_2021 真实-CSDN博客_docker wsl2 镜像位置](https://blog.csdn.net/u013948858/article/details/111464534)

%localappdata%\Docker\wsl\data\ext4.vhdx

set datadir=D:\Docker\wsl\data
set bakdir=D:\Docker\wsl\data\bak
mkdir %bakdir%

wsl --export docker-desktop-data %bakdir%\docker-desktop-data.tar
wsl --unregister docker-desktop-data
wsl --import docker-desktop-data %datadir% %bakdir%\docker-desktop-data.tar --version 2

空间优化

[适用于 linux 的 windows 子系统 - Docker Desktop WSL ext4.vhdx 太大 - 代码日志](https://stackoverflow.com/questions/70946140/docker-desktop-wsl-ext4-vhdx-too-large)

Optimize-VHD -Path "%localappdata%\Docker\wsl\data\ext4.vhdx" -Mode Full
