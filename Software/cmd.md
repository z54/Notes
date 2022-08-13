# cmd

[CMD有哪些有趣的命令？ - 知乎](https://www.zhihu.com/question/29930842?sort=created)
[Windows 命令 | Microsoft Docs](https://docs.microsoft.com/zh-cn/windows-server/administration/windows-commands/windows-commands#s)
[Windows CMD命令大全(值得收藏)_DOS/BAT_脚本之家](https://www.jb51.net/article/141568.htm)

```cmd
ping 127.0.0.1
ping 127.0.0.1 -t

rem arp缓存
arp -a

rem 查看本机开启的端口
netstat -a -n

netstat -ano | findstr "1080"
tasklist|findstr "4568"

rem 查看所有用户
net user
```

## 注释

[cmd的注释符号是什么？_Zola的博客-CSDN博客_cmd 注释](https://blog.csdn.net/weixin_42596182/article/details/93783388)

1. ::，注释内容（第一个冒号后也可以跟任何一个非字母数字的字符）
2. rem，注释内容（不能出现重定向符号和管道符号）
3. %注释内容%（可以用作行间注释，不能出现重定向符号和管道符号）
4. :标签，注释内容（可以用作标签下方段的执行内容）

date - b

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
echo %ERRORLEVEL% - 扩展到当前 ERRORLEVEL 数值。
echo %CMDEXTVERSION% - 扩展到当前命令处理器扩展版本号。
echo %CMDCMDLINE% - 扩展到调用命令处理器的原始命令行。
echo %HIGHESTNUMANODENUMBER% - 扩展到此计算机上的最高 NUMA 节点号。

echo %CD% - 扩展到当前目录字符串。
echo %DATE% - 用跟 DATE 命令同样的格式扩展到当前日期。
echo %TIME% - 用跟 TIME 命令同样的格式扩展到当前时间。
echo %RANDOM% - 扩展到 0 和 32767 之间的任意十进制数字。
echo %ERRORLEVEL% - 扩展到当前 ERRORLEVEL 数值。
echo %CMDEXTVERSION% - 扩展到当前命令处理器扩展名版本号。
echo %CMDCMDLINE% - 扩展到调用命令处理器的原始命令行。

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

tasklist|find /i "abc.exe"
if %errorlevel% == 0 (taskkill /IM abc.exe)

[CMD 一条命令 执行 多条命令_夏华东的博客的博客-CSDN博客_cmd一行多条命令](https://blog.csdn.net/weixin_44493841/article/details/107140526)

如果想一次运行多条命令可能用到的连接符个人了解到的有三个：&&，|| 和 &。

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

硬链接:修改1.txt后，2.txt做出同样修改，删除1.txt不影响2.txt正常使用
mklink /H 2.txt 1.txt

C:>fsutil hardlink list 1.txt
Desktop\1.txt
Desktop\2.txt

目录链接（类似于快捷方式），显示为dir2，删除dir1后dir2无法使用

mklink /J dir2 dir1

C:>dir /a
<DIR>          dir1
<JUNCTION>     dir2 [C:\Users\zach\Desktop\dir1]
```

## loop

[cmd for 用法 - bug_x - 博客园](https://www.cnblogs.com/cbugs/p/8992059.html)

- `FOR %variable IN (set) DO command [command-parameters]`

```cmd
for 

[cmd for 用法 - bug_x - 博客园](https://www.cnblogs.com/cbugs/p/8992059.html)

- `FOR %variable IN (set) DO command [command-parameters]`

rem 输出1 2 3 4 5
for /l %i in (1,1,5) do @echo %i
rem 枚举了c盘所有目录
for /r c:\ %i in (boot.ini) do echo %i 

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
rem if

if "abc"=="xyz" (echo 字符串abc等于字符串xyz) else (echo 字符串abc不等于字符串xyz)

if 1 equ 2 (echo 1等于2) else (echo 1不等于2)

if defined str (echo 变量str已经被赋值，其值为%str%) else (echo 变量str的值为空)

if exist d:\test.txt (echo D盘下有test.txt存在) else (echo D盘下不存在test.txt)

set varA=B
if "%varA%"=="A" (echo %varA% is A) else if "%varA%"=="B" (echo %varA% is B) else (echo %varA% is C)

rem choice

choice /C YNC /M "确认请按 Y，否请按 N，或者取消请按 C。

与或非（与或没有）

if not %a%=="" echo a不为空
```

## find

`ipconfig | find /n "IPv4"`

## string

`ipconfig | find /n "IPv4"`

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
