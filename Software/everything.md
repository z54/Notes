# everything

> 依赖于NTFS格式，仅可用于windows

## 配置

Tool ->  option ->  General ->  check Show Search Everything folder context menu item
Tool ->  option ->  General -> Keyboard ->  Show window Hotkey: Alt+E

- [everything-cli.help](everything.cli.help)<!-- [[everything-cli.help]] --> 

## base

```sh
# 文件或目录
file:
folder:
# 类型
audio:	
zip:	
doc:	
exe:	
pic:	
video:	
# 大小
size[kb|mb|gb]
empty
tiny	0 KB < 大小 <= 10 KB
small	10 KB < 大小 <= 100 KB
medium	100 KB < 大小 <= 1 MB
large	1 MB < 大小 <= 16 MB
huge	16 MB < 大小 <= 128 MB
gigantic	大小 > 128 MB
# 日期
*.pdf dc:2021/1/1
*.pdf dm:2021/1/1
```

## 使用

### 批量修改文件名：选中所需文件，F2重命名

三国演义-罗贯中.pdf
%1-%2.pdf
^(.*?)-(.*?)\.pdf$

### 批量删除文件（数量超过1万）：

1. 选中需要删除的所有文件
2. 编辑-高级-高级复制
3. 新表达式前增加删除指令
   - 文件：`del "`
   - 空文件夹：`rmdir "`
   - 文件夹：`rmdir /s/q "`
4. 全选复制新文件名到cmd执行，关闭everything"复制到"窗口

### 操作符使用

```sh
# 搜索 *.pdf且搜索路径为 D盘
*.pdf D: 
# 搜索 *.pdf且搜索路径为 C盘 或 D盘
*.pdf C: | D:
# 搜索 *.pdf且搜索路径为 非C盘
*.pdf !C:
```

### 分组

<.pdf> | <.mobi>

### dupe

```sh
# 本机上所有重复文件 
dupe: 
# 本机上所有重复的pdf文件
dupe: *.pdf
# 本机上所有重复的pdf文件中在D盘下的部分
dupe: *.pdf d:
# D盘下重复的pdf文件（未解决）
```

### cmd调用

```cmd
@echo off
@REM 可以放入cmd文件作为快捷操作

@REM 路径调用
"C:\Program Files\Everything\Everything.exe" -s "c:\ .pdf"

@REM path调用
path="C:\Program Files\Everything\";%path%;
path="C:\Tools\Everything-1.4.1.1022.x64";%path%;
everything.exe -s .pdf
everything.exe -s regex:.*.pdf
```

### cli

[下载 Everything 命令行接口](https://www.voidtools.com/zh-cn/downloads/)

```cmd
es -s keyword
```