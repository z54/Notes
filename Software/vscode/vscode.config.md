## setting

```tinymind
vscode <br>setting
    排除文件干扰
    智能提示
        Markdown
    Tex配置
    C配置
    双击文本选择间断
    默认使用tab缩进
    工作区配置
```

```bat
: 打开用户配置文件

F1 -> sej
: or
start code %homepath%\AppData\Roaming\Code\User\settings.json 
: or
- `AppMenu > Preferences > Workspace Settings`
```

- [【VisualStudioCode】VSCode隐藏文件夹ignore folder - CSDN博客](https://blog.csdn.net/teng_ontheway/article/details/51697778)
- [第一次使用VS Code时你应该知道的一切配置](https://juejin.cn/post/6844903826063884296)

### 默认使用tab缩进

```json
    "editor.detectIndentation": true, 
    "editor.insertSpaces": false,
    "editor.tabSize": 4
```

### 关闭认证

```json
"security.workspace.trust.enabled": false,
```

### 高亮当前行

[高亮当前行](https://csjiabin.github.io/2020/04/24/VSCode%E7%9A%84%E4%BD%BF%E7%94%A8/)

```json
"workbench.colorCustomizations": {
"editor.lineHighlightBackground": "#00000090",
"editor.lineHighlightBorder": "#00000000"
}
```

### 排除文件干扰

```json
// Place your settings in this file to overwrite default and user settings.  
{  
     //-------- Search configuration --------  
  
    // Configure glob patterns for excluding files and folders in searches. Inherits all glob patterns from the files.exclude setting.  
    "search.exclude": {  
        "**/node_modules": true,  
        "**/bower_components": true  
    },  
  
    //-------- Files configuration --------  
  
    // Configure glob patterns for excluding files and folders.  
    "files.exclude": {  
        "**/.git": true,  
        "**/.svn": true,  
        "**/.DS_Store": true,  
        "**/node_modules": true,  
        "**/iOS": true  
    }  
}  
```

### 双击选择文本

```json
    "editor.wordSeparators": "`~!@#$%^&*()=+[{]}\\|;:'\",<>/?、，。",
    // 去除了-.，添加了、
```

### Markdown 提示

```json
    "[markdown]": {
        "editor.wordWrap": "on",
        "editor.quickSuggestions": true,
        "editor.defaultFormatter": "cipchk.vscode-markdown-compact-table-formatter",
    },
```

### 多行标签显示

math
todo:
- [VSCode多行显示tabs，将新打开Tab的放到最后_langwang122的博客-CSDN博客](https://blog.csdn.net/langwang122/article/details/107943991)
- [vscode 文件标签栏多行显示 - GongKiro - 博客园](http://cncc.bingj.com/cache.aspx?q=vscode+%e5%a4%9a%e8%a1%8c%e6%a0%87%e7%ad%be&d=4546085639497069&mkt=zh-CN&setlang=zh-CN&w=IYnly1ve7_8TUnLzfvnEE8Zp81ja0tZO)
