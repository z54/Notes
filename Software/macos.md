# MACOS

- [MACOS](#macos)
  - [shortcut](#shortcut)
  - [change hostname](#change-hostname)
  - [参考](#参考)
  - [homebrew](#homebrew)
  - [Shortcut](#shortcut-1)
  - [Software](#software)
  - [Config](#config)
  - [FATAL](#fatal)

## shortcut

command-space: spotlight
option-space: launchpad
control-space: change input method

Control–Command–Power button: force Restart

## change hostname

`sudo hostname mbp`

## 参考

- [强制退出Mac程序的六种方法 - 丿灬安之若死 - CSDN博客](https://blog.csdn.net/mp624183768/article/details/80599064)

## homebrew

[Homebrew Documentation](https://docs.brew.sh/Manpage)

```
brew -v # brew版本

brew list  # 列出所有已安装formula（软件包）和cask（应用包）
brew list --versions # 所有已安装软件版本

brew search docker
brew install wget
brew install --cask firefox
brew install --cask docker

brew update  # 更新列表
brew upgrade # 更新软件

brew uninstall docker # 卸载
brew autoremove # 卸载没有依赖条件的软件
```

## Shortcut

| Chrome | - |
|--------|---|
| 下载 | Shift+Command+J |

| system | - |
|--------|---|
| 全屏 | Ctrl+Command+F |
| 锁屏 | Ctrl+Command+Q |
| 注销 | Shfit+Command+Q |
| force Restart | Control–Command–Power button |

- [强制退出Mac程序的六种方法](https://blog.csdn.net/mp624183768/article/details/80599064)

| 退出程序 | - |
|------|---|
| 正常退出 | Command+Q |
| 强制退出程序 | Command+Option+Shift+Esc |
| 打开强制退出窗口 | Command+Option+Esc |
| 命令行 | killall [程序名称] |

| opt | - |
|-----|--|
| 删除文件 | Command + Del |

| space | - |
|-------|---|
| 切换输入法 | Control + Space |
| spotlight | command + space |
| launchpad | option + space |
| input method | control + space |

| Safari | - |
|--------|---|
| 页顶 | Command + top |
| 页底 | Command + bottom |

- [在 Mac 上拍摄截屏](https://support.apple.com/zh-cn/HT201361)
- [Mac如何正确的截屏？ - 知乎](https://zhuanlan.zhihu.com/p/52619446)

| 截图 | - |
|----|---|
| 全屏 | Shift + Command + 3 |
| 选中范围 | Shift + Command + 4 |
| 捕捉窗口或菜单 | Shift + Command + 4 + Space |

| 截图到剪切板 | - |
|--------|---|
| 全屏 | cmd+Ctrl+shift+3 |
| 范围 | cmd+Ctrl+shift+4 |
| 活动窗口 | cmd+Ctrl+shift+4+space |

## Software

- homebrew，CLI库
- Cinch，窗口切分：将窗口拖到边沿
- parallels, 虚拟化软件
- alfred
- CheatSheet
- IINA, video player

## Config

[Mac终端ls命令区分文件夹和文件的颜色](https://www.jianshu.com/p/488869d76447)

- change hostname

`sudo hostname mbp`

## FATAL

- Q：Chrome 浏览器被劫持
- A：系统偏好设置，删除不认识的描述文件
