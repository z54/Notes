# vscode

[Documentation for Visual Studio Code](https://code.visualstudio.com/docs)

- github支持的markdown语法
	- [Basic writing and formatting syntax - GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
	- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [VS Code built-in markdown extension's Textmate grammar](https://github.com/microsoft/vscode-markdown-tm-grammar)

- [viatsko/awesome-vscode: 🎨 A curated list of delightful VS Code packages and resources.](https://github.com/viatsko/awesome-vscode#readme)

```tinymind
vscode
    env
    usage
    config
        snippets
        workspace
    extension
```

## install

winget install Microsoft.VisualStudioCode

## usage

| 名字 | 快捷键 |
|----|-----|
| 显示所有快捷键 | `C-K C-S` |
| 全部保存 | `C-K S` |
| 多行同时修改 | `Ctrl-Alt-<up/down>` |
| 选中所有行末尾出现光标 | `Shift-Alt-i` |
| 页面中出现这个词的不同地方都出现光标 | `ctrl+shift+L或者ctrl+f2` |
| 竖直的列光标，同时可以选中多列 | `shift+alt，再使用鼠标拖动` |
| 手动选择多列 | `Ctrl Shift ↑/↓` |

### 替换

> 开启正则 alt+r

| - | 查找 | 替换 |
|---|----|----|
| 单条件查找 | `\n\n` | `\n` |
| 多条件查找 | `\n\n\|\t` | `\n` |
| 带原值替换 | `　　(\d)` | `$1` |

- [Visual Studio Code 如何同时编辑多处_百度经验](https://jingyan.baidu.com/article/3052f5a1066eb597f31f86db.html)

## config

- [vscode.config](vscode.config.md)<!-- [[vscode.config]] -->

### workspace

- [vscode.workspace](vscode.workspace.md)<!-- [[vscode.workspace]] -->

### env

- [vscode.env](vscode.env.md)<!-- [[vscode.env]] -->

### snippets

- [vscode.snippets](vscode.snippets.md)<!-- [[vscode.snippets]] -->

## extension

- [vscode.extension](vscode.extension.md)<!-- [[vscode.extension]] -->

start explorer %userprofile%\.vscode

- c
- python
- tex
- markdown
