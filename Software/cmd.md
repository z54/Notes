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

### net

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
USERPROFILE=C:\Users\zach

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
<JUNCTION>     dir2 [C:\Users\zach\Desktop\dir1]
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
