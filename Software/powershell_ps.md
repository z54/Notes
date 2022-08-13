# powershell

```tinymind
powershell
    基础语法（获取各类信息）
    修改组策略
```

- [PowerShell 命令是什么？ - PowerShell | Microsoft Docs](https://docs.microsoft.com/zh-cn/powershell/scripting/powershell-commands?view=powershell-7.1)
- [GroupPolicy Module | Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/grouppolicy/?view=windowsserver2019-ps)
- [Powershell 开启远程桌面_weixin_30713953的博客-CSDN博客](https://blog.csdn.net/weixin_30713953/article/details/94952286)
- [Powershell执行文件和脚本_xiaoxiao的博客-CSDN博客_powershell执行bat文件](https://blog.csdn.net/weixin_43871760/article/details/89173872)
- [PowerShell中查看当前版本、Windows版本、.NET版本信息的代码_PowerShell_脚本之家](https://www.jb51.net/article/53150.htm)

```tinymind
version
    <#PowerShell 的版本号#> 
        $host
    <#PowerShell 中各组件的版本号#>
        $PSVersionTable.PSVersion
    <#查看当前 PowerShell的.Net运行版本#>
        [environment]::Version
        $PSVersionTable.CLRVersion
    <#查看所有安装的.Net 版本#> 
        dir 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' | sort-object name -Descending | select-object -ExpandProperty PSChildName 
    <#查看机器是否安装.Net 4.5#> 
        (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Client' -Name Version).Version
    <#查询PowerShell当前版本#>
        $psversiontable.BuildVersion.Major
    <#查询Windows当前版本#>
        [System.Environment]::OSVersion.Version.Major
        ([string]::concat((cmd /c "ver"))).split(" ")[3].split(".")[0]
```

## Create a Virtual Machine with PowerShell

[Create a Virtual Machine with Hyper-V | Microsoft Docs](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/create-virtual-machine)

```powershell
# Set VM Name, Switch Name, and Installation Media Path.
$VMName = 'TESTVM'
$Switch = 'External VM Switch'
$InstallMedia = 'C:\Users\Administrator\Desktop\en_windows_10_enterprise_x64_dvd_6851151.iso'

# Create New Virtual Machine
New-VM -Name $VMName -MemoryStartupBytes 2147483648 -Generation 2 -NewVHDPath "D:\Virtual Machines\$VMName\$VMName.vhdx" -NewVHDSizeBytes 53687091200 -Path "D:\Virtual Machines\$VMName" -SwitchName $Switch

# Add DVD Drive to Virtual Machine
Add-VMScsiController -VMName $VMName
Add-VMDvdDrive -VMName $VMName -ControllerNumber 1 -ControllerLocation 0 -Path $InstallMedia

# Mount Installation Media
$DVDDrive = Get-VMDvdDrive -VMName $VMName

# Configure Virtual Machine to Boot from DVD
Set-VMFirmware -VMName $VMName -FirstBootDevice $DVDDrive
```

## config computer

[Windows 10/11 上的预配包概述 - 配置 Windows | 微软文档](https://docs.microsoft.com/en-us/windows/configuration/provisioning-packages/provisioning-packages)

[Use a script to install a desktop app in provisioning packages (Windows 10/11) - Configure Windows | Microsoft Docs](https://docs.microsoft.com/en-us/windows/configuration/provisioning-packages/provisioning-script-to-install-app)

[Windows Configuration Designer command-line interface (Windows 10/11) - Configure Windows | Microsoft Docs](https://docs.microsoft.com/en-us/windows/configuration/provisioning-packages/provisioning-command-line)

[PowerShell cmdlets for provisioning Windows 10/11 (Windows 10/11) - Configure Windows | Microsoft Docs](https://docs.microsoft.com/en-us/windows/configuration/provisioning-packages/provisioning-powershell)

## Apply

```powershell
获取系统信息

Get-WindowsUpdateLog    # 升级日志
Get-NetIPAddress        # 获取IP
Get-NetIPAddress -AddressFamily IPv4 # 获取地址为IPv4的IP

# 打开管理员terminal
start-process powershell -verb runas
start-process cmd -verb runas
```

```powershell
设置

Get-command -verb set
```

### 隐藏任务栏搜索栏

[Hiding TaskBar Search with PowerShell • The Lonely Administrator](https://jdhitsolutions.com/blog/powershell/8424/hiding-taskbar-search-with-powershell/)

Set-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Search -Name SearchBoxTaskbarMode -Value 0 -Type DWord -Force

.\SearchBarTools.ps1

```powershell
# SearchBarTools.ps1

Disable-TaskBarSearch
# Enable-TaskBarSearch

Restart-Explorer
```

### 配置ip

- [Powershell命令修改本机IP为固定地址_AKSPD的技术博客_51CTO博客](https://blog.51cto.com/u_12078224/2432278)
- [PowerShell设置IP地址_insist100的博客-CSDN博客_powershell修改ip地址](https://blog.csdn.net/insist100/article/details/80573866)

```powershell

Get-NetIPAddress -InterfaceIndex 12 -AddressFamily IPv4 # 获取指定网卡信息

Start-Process "$psHome\powershell.exe" -ArgumentList "$currentFile $fullPara"   -verb runas # 管理员启动powershell
New-NetIPAddress -InterfaceIndex 12 -IpAddress 172.28.96.2 -PrefixLength 24 # 配置ip，不生效

Remove-NetIPAddress -InterfaceIndex 12 -IpAddress 172.28.96.2 -PrefixLength 24 # 删除配置
0
---

New-NetIPAddress -InterfaceIndex 12 -IPAddress 192.168.80.83 -PrefixLength 24  
Set-DNSClientServerAddress -InterfaceIndex 12 -ServerAddresses 211.111.111.1,211.111.111.12

---

Import-Module NetTCPIP
Import-Module DnsClient

New-NetIPAddress -InterfaceIndex 8 -IpAddress 192.168.1.2 -PrefixLength 24 -DefalutGateway 192.168.1.1
Set-DNSClientServerAddress -InterfaceIndex 8 -ServerAddress ("192.168.1.3","192.168.1.4")
```

```powershell
变量

set var abc
echo $var

# path

$env:Path += ";c:\users\xiaomin\go\bin"
setx /M PATH "%PATH%;c:\users\xiaomin\go\bin"

$PSVersionTable.PSVersion # Powershell版本

Major  Minor  Build  Revision
-----  -----  -----  --------
5      1      19041  906
```

## Get

```powershell

Get-Verb    # 返回大多数命令遵循的谓词的列表。
Get-Command # 检索计算机上安装的所有命令的列表。

---

Get-Member  # 它在基于对象的输出上运行，并且能够发现可用于命令的对象、属性和方法。
Select-Object -First 3 # 它在基于对象的输出上运行，只显示前三个

---

Get-Help    # 以命令名称为参数调用此命令，将显示一个帮助页面，其中说明了命令的各个部分。

```

## Get-Command

```powershell

Get-Command -Verb 'Get' | Select-Object -First 5 # 获取以Get为动词开头的命令

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           Get-AppPackage                                     2.0.1.0    Appx
Alias           Get-AppPackageDefaultVolume                        2.0.1.0    Appx
Alias           Get-AppPackageLastError                            2.0.1.0    Appx
Alias           Get-AppPackageLog                                  2.0.1.0    Appx
Alias           Get-AppPackageManifest                             2.0.1.0    Appx

Get-Command -Noun U*  | Select-Object -First 5   # 获取以U为名字开头的命令

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Clear-UevAppxPackage                               2.1.639.0  UEV
Cmdlet          Clear-UevConfiguration                             2.1.639.0  UEV
Cmdlet          Disable-Uev                                        2.1.639.0  UEV
Cmdlet          Disable-UevAppxPackage                             2.1.639.0  UEV
Cmdlet          Disable-UevTemplate                                2.1.639.0  UEV

Get-Command -Verb Get -Noun U* # 获取以Get为动词开头，以U为名字开头的命令

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Get-UevAppxPackage                                 2.1.639.0  UEV
Cmdlet          Get-UevConfiguration                               2.1.639.0  UEV
Cmdlet          Get-UevStatus                                      2.1.639.0  UEV
Cmdlet          Get-UevTemplate                                    2.1.639.0  UEV
Cmdlet          Get-UevTemplateProgram                             2.1.639.0  UEV
Cmdlet          Get-UICulture                                      3.1.0.0    Microsoft.PowerShell.Utility
Cmdlet          Get-Unique                                         3.1.0.0    Microsoft.PowerShell.Utility

Get-Command -ParameterType Process # 获取

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Debug-Process                                      3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Enter-PSHostProcess                                3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Get-Process                                        3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Get-PSHostProcessInfo                              3.0.0.0    Microsoft.PowerShell.Core
Cmdlet          Stop-Process                                       3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Wait-Process                                       3.1.0.0    Microsoft.PowerShell.Management

Get-Command -Name 'Get-Net*' | Select-Object -First 5 # 获取名称以Get-Net开头的命令

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        Get-Net6to4Configuration                           1.0.0.0    NetworkTransition
Function        Get-NetAdapter                                     2.0.0.0    NetAdapter
Function        Get-NetAdapterAdvancedProperty                     2.0.0.0    NetAdapter
Function        Get-NetAdapterBinding                              2.0.0.0    NetAdapter
Function        Get-NetAdapterChecksumOffload                      2.0.0.0    NetAdapter

Get-Process | Where-Object {$_.ProcessName -Like "p*"} # 获取名称以p开头的进程

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    116      16    14132      21100             16180   0 pacjsworker
    217      19    13636       6044       4.95   7288   1 PopBlock
    557      28   120332     127424       1.88   2864   1 powershell
    934      49   184968     209992      29.31  14052   1 powershell
    583      29    96028     107096       0.80  15204   1 powershell
    167      11     2444      10960       0.05   1504   1 prevhost
    162      11     2360      15752       0.64   2672   1 prevhost

```

## Get-process

```powershell
Get-Process | Select-Object -First 5 # 获取进程

Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    497      28    20408      34480       0.30  11768   1 ApplicationFrameHost
    123       9     1592       6024              4972   0 armsvc
    383      19    58860      78028       1.58   1300   1 chrome
    247      17    55164      77540       2.81   1592   1 chrome
    235      15    80760      98988       7.47   2124   1 chrome

Get-Process | Get-Member | Select-Object -First 5 # 获取进程列头

Name    MemberType    Definition
----    ----------    ----------
Handles AliasProperty Handles = Handlecount
Name    AliasProperty Name = ProcessName
NPM     AliasProperty NPM = NonpagedSystemMemorySize64
PM      AliasProperty PM = PagedMemorySize64
SI      AliasProperty SI = SessionId

Get-Process | Get-Member -MemberType Method | Select-Object -First 5 # 筛选类型为Method的进程

Name                MemberType Definition
----                ---------- ----------
BeginErrorReadLine  Method     void BeginErrorReadLine()
BeginOutputReadLine Method     void BeginOutputReadLine()
CancelErrorRead     Method     void CancelErrorRead()
CancelOutputRead    Method     void CancelOutputRead()
Close               Method     void Close()

Get-Process | Get-Member | Select-Object Name, Definition | Select-Object -First 5 # 获取进程中Name列和Definition列，没看懂

Name    Definition
----    ----------
Handles Handles = Handlecount
Name    Name = ProcessName
NPM     NPM = NonpagedSystemMemorySize64
PM      PM = PagedMemorySize64
SI      SI = SessionId
```

## Get-help

```powershell
若要查看示例，请键入: "get-help Get-Verb -examples".
有关详细信息，请键入: "get-help Get-Verb -detailed".
若要获取技术信息，请键入: "get-help Get-Verb -full".
有关在线帮助，请键入: "get-help Get-Verb -online"
```

Update-Help

## 参考：Powershell远程机多跳问题

[Powershell远程机多跳问题_咕咕鸡的博客-CSDN博客](https://blog.csdn.net/baidu_35407267/article/details/79648010)

[Powershell如何修改组策略（group policy）_咕咕鸡的博客-CSDN博客](https://blog.csdn.net/baidu_35407267/article/details/79700790)

## 参考：PowerShell修改IP地址

[PowerShell修改IP地址_缘随心愿的技术博客_51CTO博客](https://blog.51cto.com/281816327/1841304)
