# everything

> 依赖于NTFS格式，仅可用于windows

## 配置

Tool ->  option ->  General ->  check Show Search Everything folder context menu item
Tool ->  option ->  General -> Keyboard ->  Show window Hotkey: Alt+E

- [everything-cli.help](everything-cli.help)<!-- [[everything-cli.help]] --> 

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



### cmd调用

```cmd
@echo off
@REM 可以放入cmd文件作为快捷操作

@REM 路径调用
"C:\Program Files\Everything\Everything.exe" -s "c:\ .pdf"

@REM path调用
path="C:\Program Files\Everything\";%path%;
everything -s .pdf
everything -s regex:.*.pdf
```

### cli

[下载 Everything 命令行接口](https://www.voidtools.com/zh-cn/downloads/)

```cmd
es -s keyword
```