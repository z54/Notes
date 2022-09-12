# everything

> 依赖于NTFS格式，仅可用于windows

## 配置

Tool ->  option ->  General ->  check Show Search Everything folder context menu item
Tool ->  option ->  General -> Keyboard ->  Show window Hotkey: Alt+E

[[everything-cli.help]]

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
# 搜索路径为 D盘 且搜索 .pdf
.pdf D: 
# 搜索路径为 C盘 或 D盘 且搜索 .pdf  
.pdf C: | D:
# 搜索路径为 非C盘 且搜索 .pdf
.pdf !C:
```

### cmd调用

```cmd
rem 直接调用（可以放入cmd文件作为快捷操作）
"C:\Program Files\Everything\Everything.exe" -s "c:\ .pdf"

rem path调用
path="C:\Program Files\Everything\";%path%;
everything -s .pdf
everything -s regex:.*.pdf
```

### cli

[下载 - voidtools](https://www.voidtools.com/zh-cn/downloads/)
下载 Everything 命令行接口

```cmd
es -s keyword
```