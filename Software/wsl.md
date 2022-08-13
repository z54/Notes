---
id: DXIiJmT28Q6aEh8bCWSkc
title: Wsl
desc: ''
updated: 1639423509837
created: 1639423509837
---

## env

- [在 Windows 10 上安装 WSL | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)
- [旧版 WSL 的手动安装步骤 | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual)
- [Manually download Windows Subsystem for Linux (WSL) Distros | Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install-manual)
- [Run Linux GUI apps with WSL | Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)

---

- [WSL 的基本命令 | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/wsl/basic-commands)

```ps
安装
wsl --install

列出可用的 Linux 发行版
wsl --list --online 

安装特定的 Linux 发行版
wsl --install --distribution <Distribution Name>
wsl --install -d Ubuntu
wsl --install -d Debian

列出已安装的 Linux 发行版
wsl --list --verbose

将 WSL 版本设置为 1 或 2
wsl --set-default-version 2

设置默认 Linux 发行版
wsl --set-default <Distribution Name>

检查 WSL 状态
wsl --status

更新 WSL
wsl --update

wsl --terminate <Distribution Name>
wsl --unregister <DistributionName>

wsl --shutdown

net stop lxssmanager
net start lxssmanager
```

## fatal

### %LOCALAPPDATA%/Docker/wsl/data/ext4.vhdx 文件太大

[win10使用WSL 2运行Docker Desktop，运行文件从C盘迁移到其他目录 - xhznl - 博客园](https://www.cnblogs.com/xhznl/p/13184398.html#4634011)
[【Docker】win10上修改docker的镜像文件存储位置（九）- 通过WSL2修改_2021 真实-CSDN博客_docker wsl2 镜像位置](https://blog.csdn.net/u013948858/article/details/111464534)

关闭docker
wsl --shutdown
set mydir=E:\DockerData\wsl\docker-desktop-data\
mkdir %mydir%
wsl --export docker-desktop-data %mydir%docker-desktop-data.tar
wsl --unregister docker-desktop-data
wsl --import docker-desktop-data %mydir% %mydir%docker-desktop-data.tar --version 2
