# config
- 排除文件干扰
    - `AppMenu > Preferences > Workspace Settings`
```
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
# usage
- 显示所有快捷键
`C-K C-S`
- 全部保存
`C-K S`
- 多行同时修改
`Ctrl-Alt-<up/down>`
- 选中所有行末尾出现光标
`Shift-Alt-i`
- 页面中出现这个词的不同地方都出现光标
`ctrl+shift+L或者ctrl+f2`
- 竖直的列光标，同时可以选中多列
`shift+alt，再使用鼠标拖动`

- [Visual Studio Code 如何同时编辑多处_百度经验](https://jingyan.baidu.com/article/3052f5a1066eb597f31f86db.html)

# fatal
# Reference
- [【VisualStudioCode】VSCode隐藏文件夹ignore folder - CSDN博客](https://blog.csdn.net/teng_ontheway/article/details/51697778)