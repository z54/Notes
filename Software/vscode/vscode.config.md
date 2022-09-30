## setting

```tinymind
vscode <br>setting
    默认使用tab缩进
    排除文件干扰
    显示80字符分割线
    智能提示
        Markdown
    Tex配置
    C配置
    双击文本选择间断
    工作区配置
```

## 配置路径

```bat
@REM 打开用户配置文件

F1 -> sej
@REM or
AppMenu > Preferences > Workspace Settings
@REM or
start code %homepath%\AppData\Roaming\Code\User\settings.json 
```

- [【VisualStudioCode】VSCode隐藏文件夹ignore folder - CSDN博客](https://blog.csdn.net/teng_ontheway/article/details/51697778)
- [第一次使用VS Code时你应该知道的一切配置](https://juejin.cn/post/6844903826063884296)

## 配置项

```json

    // 默认使用tab缩进

    "editor.detectIndentation": true, 
    "editor.insertSpaces": false,
    "editor.tabSize": 4

    // 关闭认证

    "security.workspace.trust.enabled": false,

    // 显示80字符分割线

    "editor.rulers": [ 
        80
    ],

    // [高亮当前行](https://csjiabin.github.io/2020/04/24/VSCode%E7%9A%84%E4%BD%BF%E7%94%A8/)

    "workbench.colorCustomizations": {
    "editor.lineHighlightBackground": "#00000020",
    "editor.lineHighlightBorder": "#00000000"
    }

    // 排除文件干扰

    //-------- Search configuration --------  

    "search.exclude": {  
        "**/node_modules": true,  
        "**/bower_components": true  
    },  
  
    //-------- Files configuration --------  
    
    "files.exclude": {  
        "**/.git": true,  
        "**/.svn": true,  
        "**/.DS_Store": true,  
        "**/node_modules": true,  
        "**/iOS": true  
    }  

    // 双击选择文本
    
    "editor.wordSeparators": "`~!@#$%^&*()=+[{]}\\|;:'\",<>/?、，。", // 去除了-.，添加了、
    
    // Markdown 提示

    "[markdown]": { 
        "editor.wordWrap": "on",
        "editor.quickSuggestions": true,
        "editor.defaultFormatter": "cipchk.vscode-markdown-compact-table-formatter",
    },
```
