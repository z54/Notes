# Windows

```tinymind
windows
    tools
    vitrual
        wsl
        Hyper-V
    remote
        ssh
        remote control
    CLI
        cmd
        powershell
    System
        Port
        service
        Activate
        administration program
        application program
        system variable 
    config
        regedit
        gpedit
    Fatal
```

- [在 Windows 10 上创建开发环境 | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/dev-environment/overview)
- [5 款 Windows 任务栏增强工具推荐 - 知乎](https://zhuanlan.zhihu.com/p/46685515)
- [Awesome/README-cn.md at master · Awesome-Windows/Awesome](https://github.com/Awesome-Windows/Awesome/blob/master/README-cn.md)
- [README - Windows Apps That Amaze Us](https://amazing-apps.gitbook.io/windows-apps-that-amaze-us/zh-cn)
- [stackia/best-windows-apps: 推荐好用、优秀的 Windows 应用](https://github.com/stackia/best-windows-apps)
- [我最喜欢的软件 Windows 版 - 小众软件](https://love.appinn.com/)
- [Disassembler0/Win10-Initial-Setup-Script: PowerShell script for automation of routine tasks done after fresh installations of Windows 10 / Server 2016 / Server 2019](https://github.com/Disassembler0/Win10-Initial-Setup-Script)

## Tools

Msconfig.exe：系统配置实用程序
regedit.exe：注册表

| Tools | detail |
-|-
Zenmap | 端口扫描
Free Port Scanner | 端口扫描
ScanPort | 端口扫描
X-Scan | 安全漏洞检测
Shadow Security Scaner | 系统漏洞扫描
ProtectX | 端口监视
Iris | 抓包
EffeTach HEEP Sniffer |  HTTP 协议的网络嗅探器
Winpcap | 在线视频地址
Real Spy Monitor | 键盘敲击、网页站点、视窗开关、程序执行、屏幕扫描以及文件的出入等都是其监控的对象
geek | 软件卸载器

## vitrual

[wsl](wsl.md)<!-- [[wsl]] --> 

wsl --install

- [[Hyper-V]]

```cmd
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
```

## remote

### 开启远程ssh

[如何使用 SSH 远程控制一台 Windows 服务器 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1420930)

1. 改IP - 远程机和网关
2. 开启远程开关 - 远程机
3. 关闭防火墙 - 远程机
4. 安装ssh服务 - 远程机

```ps1
# 开启ssh
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# 防火墙
Get-NetFirewallRule -Name *ssh*
# 如果是放开的，那么结果会提示 OpenSSH-Server-In-TCP状态是 enabled

set-ExecutionPolicy RemoteSigned 执行策略更改 y 开启 n 关闭

Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name 'fDenyTSConnections' -Value 0 :: 开启远程开关
Write-Host 正在重启 Remote Desktop Services ... -ForegroundColor DarkYellow
Set-Service TermService -StartupType Automatic -Status Running -PassThru
```

### 开启远程桌面

```cmd
@rem 开启远程桌面
wmic RDTOGGLE WHERE ServerName='%COMPUTERNAME%' call SetAllowTSConnections 1
 
@rem 检查端口状态
netstat -ano | findstr 3389
 
@rem 关闭远程桌面
wmic RDTOGGLE WHERE ServerName='%COMPUTERNAME%' call SetAllowTSConnections 0
```

## system

### 端口

- 协议端口，TCP/IP 0-65535
- 服务端口，如网页80端口，FTP 21端口

[windows系统不常用命令01-taskkill](https://blog.csdn.net/matrixbbs/article/details/122064612)
```cmd
::端口占用

netstat -ano | findstr 8000
tasklist | findstr 8124

taskkill /pid 8124 /F
taskkill /im java.exe /F

tasklist | find "Everything" || start "" "%PROGRAMFILES%\Everything\Everything.exe"
tasklist | find "Everything" && taskkill /f /im "Everything.exe"
```

### 服务

```cmd
net start [service]
net stop [service]

启动hyperv
net start vmms
```

### 激活

```cmd
slmgr.vbs /upk
slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX
slmgr /skms zh.us.to
slmgr /ato
```

### 管理程序

- regedit.exe----注册表
- rsop.msc-------组策略结果集
- regedt32-------注册表编辑器
- rononce -p ----15秒关机
- regsvr32 /u *.dll----停止dll文件运行
- regsvr32 /u zipfldr.dll------取消ZIP支持
- cmd.exe--------CMD命令提示符
- chkdsk.exe-----Chkdsk磁盘检查
- certmgr.msc----证书管理实用程序
- calc-----------启动计算器
- charmap--------启动字符映射表
- cliconfg-------SQL SERVER 客户端网络实用程序
- Clipbrd--------剪贴板查看器
- conf-----------启动netmeeting
- compmgmt.msc---计算机管理
- cleanmgr-------垃圾整理
- ciadv.msc------索引服务程序
- osk------------打开屏幕键盘
- odbcad32-------ODBC数据源管理器
- oobe/msoobe /a----检查XP是否激活
- lusrmgr.msc----本机用户和组
- logoff---------注销命令
- iexpress-------木马捆绑工具，系统自带
- Nslookup-------IP地址侦测器
- fsmgmt.msc-----共享文件夹管理器
- utilman--------辅助工具管理器
- gpedit.msc-----组策略1

### 内置程序

1. calc：启动计算器
2. appwiz.cpl：程序和功能
3. certmgr.msc：证书管理实用程序
4. charmap：启动字符映射表
5. chkdsk.exe：Chkdsk磁盘检查(管理员身份运行命令提示符)
6. cleanmgr: 打开磁盘清理工具
7. cliconfg：SQL SERVER 客户端网络实用工具
8. cmstp：连接管理器配置文件安装程序
9. cmd.exe：CMD命令提示符
10. 自动关机命令
    Shutdown -s -t 600：表示600秒后自动关机
    shutdown -a ：可取消定时关机
    Shutdown -r -t 600：表示600秒后自动重启
    rundll32 user32.dll,LockWorkStation：表示锁定计算机
11. colorcpl：颜色管理，配置显示器和打印机等中的色彩
12. CompMgmtLauncher：计算机管理
13. compmgmt.msc：计算机管理
14. credwiz：备份或还原储存的用户名和密码
15. comexp.msc：打开系统组件服务
16. control：控制面版
17. dcomcnfg：打开系统组件服务
18. Dccw：显示颜色校准
19. devmgmt.msc：设备管理器
20. desk.cpl：屏幕分辨率
21. dfrgui：优化驱动器 Windows 7→dfrg.msc：磁盘碎片整理程序
22. dialer：电话拨号程序
23. diskmgmt.msc：磁盘管理
24. dvdplay：DVD播放器
25. dxdiag：检查DirectX信息
26. eudcedit：造字程序
27. eventvwr：事件查看器
28. explorer：打开资源管理器
29. Firewall.cpl：Windows防火墙
30. FXSCOVER：传真封面编辑器
31. fsmgmt.msc：共享文件夹管理器
32. gpedit.msc：组策略
33. hdwwiz.cpl：设备管理器
34. inetcpl.cpl：Internet属性
35. intl.cpl：区域
36. iexpress：木马捆绑工具，系统自带
37. joy.cpl：游戏控制器
38. logoff：注销命令
39. lusrmgr.msc：本地用户和组
40. lpksetup：语言包安装/删除向导，安装向导会提示下载语言包
41. lusrmgr.msc：本机用户和组
42. main.cpl：鼠标属性
43. mmsys.cpl：声音
44. magnify：放大镜实用程序
45. mem.exe：显示内存使用情况(如果直接运行无效，可以先管理员身份运行命令提示符，在命令提示符里输入mem.exe>d:a.txt 即可打开d盘查看a.txt，里面的就是内存使用情况了。当然什么盘什么文件名可自己决定。)
46. MdSched:Windows内存诊断程序
47. mmc：打开控制台
48. mobsync：同步命令
49. mplayer2：简易widnows media player
50. Msconfig.exe：系统配置实用程序
51. msdt：微软支持诊断工具
52. msinfo32：系统信息
53. mspaint：画图
54. Msra：Windows远程协助
55. mstsc：远程桌面连接
56. NAPCLCFG.MSC：客户端配置
57. ncpa.cpl：网络连接
58. narrator：屏幕“讲述人”
59. Netplwiz：高级用户帐户控制面板，设置登陆安全相关的选项
60. netstat : an(TC)命令检查接口
61. notepad：打开记事本
62. Nslookup：IP地址侦测器
63. odbcad32：ODBC数据源管理器
64. OptionalFeatures：打开“打开或关闭Windows功能”对话框
65. osk：打开屏幕键盘
66. perfmon.msc：计算机性能监测器
67. perfmon：计算机性能监测器
68. PowerShell：提供强大远程处理能力
69. printmanagement.msc：打印管理
70. powercfg.cpl：电源选项
71. psr：问题步骤记录器
72. Rasphone：网络连接
73. Recdisc：创建系统修复光盘
74. Resmon：资源监视器
75. Rstrui：系统还原
76. regedit.exe：注册表
77. regedt32：注册表编辑器
78. rsop.msc：组策略结果集
79. sdclt：备份状态与配置，就是查看系统是否已备份
80. secpol.msc：本地安全策略
81. services.msc：本地服务设置
82. sfc /scannow：扫描错误并复原/windows文件保护
83. sfc.exe：系统文件检查器
84. shrpubw：创建共享文件夹
85. sigverif：文件签名验证程序
86. slui：Windows激活，查看系统激活信息
87. slmgr.vbs -dlv ：显示详细的许可证信息
88. snippingtool：截图工具，支持无规则截图
89. soundrecorder：录音机，没有录音时间的限制
90. StikyNot：便笺
91. sysdm.cpl：系统属性
92. sysedit：系统配置编辑器
93. syskey：系统加密，一旦加密就不能解开，保护系统的双重密码
94. taskmgr：任务管理器(旧版)
95. TM任务管理器(新版)
96. taskschd.msc：任务计划程序
97. timedate.cpl：日期和时间
98. UserAccountControlSettings用户账户控制设置
99. utilman：辅助工具管理器
100. wf.msc：高级安全Windows防火墙
101. WFS：Windows传真和扫描
102. wiaacmgr：扫描仪和照相机向导
103. winver：关于Windows
104. wmimgmt.msc：打开windows管理体系结构(WMI)
105. write：写字板
106. wscui.cpl：操作中心
107. wuapp：Windows更新
108. wscript：windows脚本宿主设置

### 系统变量

[Windows 10 环境变量 (用户变量与系统变量)_Yongqiang Cheng的博客-CSDN博客_用户变量](https://blog.csdn.net/chengyq116/article/details/105900122/)
[Windows 系统变量大全「建议收藏」-Java架构师必看](https://javajgs.com/archives/61389)

```
%path%
%COMMONPROGRAMFILES% - C:\Program Files\Common Files
%COMMONPROGRAMFILES(x86)% - C:\Program Files (x86)\Common Files
%COMSPEC% - C:\Windows\System32\cmd.exe
%HOMEDRIVE% - C:
%HOMEPATH% - C:\Users\<username>
%SYSTEMROOT% - C:\Windows
%WINDIR% - C:\Windows
%TMP% - C:\Users\<username>\AppData\Local\Temp
%TEMP% - C:\Users\<username>\AppData\Local\Temp
%APPDATA% - C:\Users\<username>\AppData\Roaming
%ALLUSERSPROFILE% - C:\ProgramData
%CD% - Typing in this command will give you the current directory you are working in.
%CMDEXTVERSION% - This variable expands to the version of the command-line extensions.
%DATE% - This variable will give you the current date according to date format preferences.
%ERRORLEVEL% - Determines the error level set by last executing command.
%LOCALAPPDATA% - C:\Users\<username>\AppData\Local
%LOGONSERVER% - \\<domain_logon_server>
%PATH% - C:\Windows\system32;C:\Windows;
%PATHEXT% - .com;.exe;.bat;.cmd;.vbs;.vbe;.js;.jse;.wsf;.wsh;.msc
%PROGRAMDATA% - C:\ProgramData
%PROGRAMFILES% - C:\Program Files
%PROGRAMW6432% - C:\Program Files
%PROGRAMFILES(X86)% - C:\Program Files (x86)
%PROMPT% - $P$G
%SYSTEMDRIVE% - C:
%TIME% - Similarly, it gives you current time according to the time format preferences.
%USERNAME% - <username>
%USERPROFILE% - C:\Users\<username>
%USERDOMAIN% - Userdomain associated with current user.
%USERDOMAIN_ROAMINGPROFILE% - Userdomain associated with roaming profile.
%PUBLIC% - C:\Users\Public
%PSMODULEPATH% - %SystemRoot%\system32\WindowsPowerShell\v1.0\Modules\
%ONEDRIVE% - C:\Users\<username>\OneDrive
%CMDCMDLINE% - Outputs command line used to launch the current Command Prompt session.
%COMPUTERNAME% -Outputs the system name.
%PROCESSOR_REVISION% - Outputs processor revision.
%PROCESSOR_IDENTIFIER% - Outputs processor identifier.
%PROCESSOR_LEVEL% - Outputs processor level.
%RANDOM% - This variable prints a random number from 0 through 32767
%NUMBER_OF_PROCESSORS% - Outputs the number of physical and virtual cores.
%OS% - Windows_NT
```

## config

### regedit

[批处理操作注册表完全攻略(读取注册表/写入注册表等)_DOS/BAT_脚本之家](https://www.jb51.net/article/30077.htm)

```ps
<!-- 创建或修改项 -->
Windows Registry Editor Version 5.00
    [HKEY_LOCAL_MACHINE\SOFTWARE\TTT]
    "Name"="TTT BLOG"

<!-- 删除项 -->
Windows Registry Editor Version 5.00
    [HKEY_LOCAL_MACHINE\SOFTWARE\TTT]
    "EMail"=-

Windows Registry Editor Version 5.00
    [-HKEY_LOCAL_MACHINE\SOFTWARE\TTT]
    [-HKEY_LOCAL_MACHINE\SOFTWARE\DDD]
```

### 图片打开方式恢复默认照片查看器

[Win10正式版怎么把图片打开方式恢复默认照片查看器？_windows10_Windows系列_操作系统_脚本之家](https://www.jb51.net/os/win10/365765.html)

```ps
Windows Registry Editor Version 5.00
 
 ; Change Extension's File Type
 [HKEY_CURRENT_USER\Software\Classes\.jpg]
 @="PhotoViewer.FileAssoc.Tiff"
 
 ; Change Extension's File Type
 [HKEY_CURRENT_USER\Software\Classes\.jpeg]
 @="PhotoViewer.FileAssoc.Tiff"
 
 ; Change Extension's File Type
 [HKEY_CURRENT_USER\Software\Classes\.gif]
 @="PhotoViewer.FileAssoc.Tiff"
 
 ; Change Extension's File Type
 [HKEY_CURRENT_USER\Software\Classes\.png]
 @="PhotoViewer.FileAssoc.Tiff"
 
 ; Change Extension's File Type
 [HKEY_CURRENT_USER\Software\Classes\.bmp]
 @="PhotoViewer.FileAssoc.Tiff"
 
 ; Change Extension's File Type
 [HKEY_CURRENT_USER\Software\Classes\.tiff]
 @="PhotoViewer.FileAssoc.Tiff"
 
 ; Change Extension's File Type
 [HKEY_CURRENT_USER\Software\Classes\.ico]
 @="PhotoViewer.FileAssoc.Tiff"
```

### win11右键默认显示更多选项

[有没有什么办法可以让win11右键默认显示更多选项？ - 知乎](https://www.zhihu.com/question/480356710)

管理员运行命令：

reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve 重启就恢复win10右键了

reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /va /f 这个是恢复win11右键

### 显示隐藏的文件、文件夹和驱动器

[win10使用注册表源文件添加或修改注册表键项的方法_windows10_Windows系列_操作系统_脚本之家](https://www.jb51.net/os/win10/403291.html)

```ps
Windows Registry Editor Version 5.00   
  
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Folder\Hidden\SHOWALL]   
"CheckedValue"=dword:00000001   
"DefaultValue"=dword:00000002   
"HKeyRoot"=dword:80000001   
"Id"=dword:00000002   
"RegPath"="Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced"  
"Text"="@shell32.dll,-30500"  
"Type"="radio"  
"ValueName"="Hidden"  
```

### 组策略

run - gpedit

[查看window用户登录日志 - Frank_Allen - 博客园](https://www.cnblogs.com/ZeroTensor/p/11495308.html)

[能追踪Windows系统登录时间的三种方法_windows_Windows系列_操作系统_脚本之家](https://www.jb51.net/os/windows/20557.html)

[查看window用户登录日志_耐得住寂寞，才能受得住繁华-CSDN博客_windows查看用户登录日志](https://blog.csdn.net/CSNDRYL/article/details/77194060)

[Windows登录日志详解_zhulinu的专栏 -CSDN博客](https://blog.csdn.net/zhulinu/article/details/52747984)

### 查看window用户登录日志

```bat
一、作用: 

查看是用户登录时间, 机器是否被别人使用

二、具体步骤:

1.命令输入: gpedit.msc  

2.“计算机配置”→“Windows设置”→“安全设置”→“本地策略”→“审核策略”，双击其中的“审核帐户登陆事件”
==>审核登录事件-->勾上成功/失败-->点击应用-->点击确定

3.控制面板-->系统和安全-->查看事件日志-->事件查看器-->windows日志-->安全，便可以看到用户的登录和注销以及账户名等信息
```

[GroupPolicy Module | Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/grouppolicy/?view=windowsserver2019-ps&viewFallbackFrom=win10-ps)

## Fatal

- 内存错误，蓝屏
    1. start up the software `Windows Memory problem`
    2. click the choice `Restart now and check for problems`
    3. then PC will restart and enter to scanning mode, wait
    4. computer will restart and product a Memory Diagnostics Report
        1. run `eventvwr`
        2. `Event Viewer (local)` - `Windows Logs` - `System`
        3. `filter current log`
        4. `Event Sources`: `MemoryDiagnostics-Results`
