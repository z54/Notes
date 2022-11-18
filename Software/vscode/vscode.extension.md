# extension

```tinymind
vscode <br>extension
    Markdown <br>(buildin support)
        联系图
            graphviz markdown preview
        思维导图
            tinymind
        双向链接
            Markdown Notes
        改名或移动后自动修改索引
            Markdown Link Updater
        粘贴excel表格
            Excel to Markdown table
        格式化表格样式为紧凑
            Markdown Compact Table Formatter
        一键贴图
            Paste Image
        生成项目Markdown 引力图
            Markdown Links
        修改图片显示尺寸(如需)
            Markdown Image size
        快捷键支持(如需)
            Markdown All in One
        化学公式支持(如需)
            Mathpix Markdown
    Git
        Git Graph
        GitLens
    Graph
        Draw.io
    DB
        Mysql
        ERD Editor
    Tex
    Python
    Tools
        使用系统默认设备打开文件
            Open
        文件对比
            Diff
    所见即所得 vditor
        vscode all markdown
        Office Viewer(Markdown Editor), 支持codeblock (graphviz)
```

# Extension

配置文件
start "" vscode %homepath%\AppData\Roaming\Code\User\settings.json

| Extension | recommendations in Workshop | scene | 备注 |
|-----------|-----------------------------|-------|----|
| Terminal | - | CLI | 直接在终端运行当前行或当前文件，`run active file in active terminal`, F4 |
| open | - | - | 可选择系统默认打开方式打开pdf,xls等文件 |
| Project Dashboard | - | - | - |
| Markdown all in one | - | Markdown | - |
| TinyMind for Markdown | 除chemistry, math | Markdown | tinymind |
| Markdown link updater | - | Markdown | - |
| Excel to Markdown table | - | Markdown | 外部表格直接粘贴成markdown格式 |
| Markdown Compact Table Formatter | - | Markdown | 以紧凑的方式格式化 Markdown 表格 |
| Markdown Preview Mermaid Support | x | Markdown | mermaid |
| Vscode Markdown Notes | - | Markdown | 支持`[[]]`双向链接和backlinks |
| paste image | - | Markdown | 直接粘贴图片，Ctrl Alt v |
| todo Hightlight | - | todo | - |
| mathpix markdown | chemistry, math | smiles, tex | - |
| Math Snippets | math | math | - |
| LaTeX Workshop | tex | tex | 在保存时自动编译 tex 文件到 pdf |
| mssql | sql | sql | 智能提示 |
| SQLTools | SQL | SQL | - |
| Import Cost | python | python | - |
| Jupyter | python | python | python依赖 |
| LiveCode for python | python | python | - |
| Python | python | python | - |
| Python Preview | python | python | - |
| C/C++ | C | C | - |
| Markdown Image Size | 需要时开启 | Markdown | `![](img =100x200)` |
| markdownlint | 需要时开启 | Markdown | - |
| images preview | 需要时开启 | Markdown | 编辑界面即时预览图片 |
| VSCode Markdown Mind Map Preview | 需要时开启 | Markdown | 根据 md 文件自动画出脑图，F1 `View Mind Map`，纯内容（无前缀）不出现在脑图中 |
| Git Graph | 需要时开启 | git | 图形化查看提交合并记录，使用时打开 |
| GitLens | 需要时开启 | git | 查看每一行的编辑历史，使用时打开 |
| Auto Close Tag | 需要时开启 | html | - |
| Auto Rename Tag | 需要时开启 | html | - |
| Diff | 需要时开启 | file | 文件比较 |
| Partial Diff | 需要时开启 | text | 段落文字对比 |
| Color Highlight | 需要时开启 | - | 直接显示颜色 |
| docs-markdown | - | - | - |
| docs-preview | - | - | - |
| Draw.io Integration | 需要时开启 | - | `filename.dio.png`，规范化作图 |
| Markdown Links | 需要时开启 | - | F1 `show graph` |
| Markdown Preview Enhanced | 需要时开启 | - | 支持浏览器预览markdown |
| Preview | - | - | - |
| Remote - SSH | 需要时开启 | - | - |
| Remote - WSL | 需要时开启 | - | - |
| Select Line Status Bar | 需要时开启 | - | - |
| SFTP | 需要时开启 | - | - |
| Tab Jumper | - | - | 使用Ctrl num跳转到对应tab |
| Visual Studio IntelliCode | - | - | - |

> tinymind, mathpix, mermaid 同为codeblock类扩展，导致冲突，只能选其一

1. [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight), `TODO：`, `FIXME：`, F1 `List highlighted annotations` 显示工作区全部 tudo 列表

    ```json
    // @ext:wayou.vscode-todo-highlight
    "todohighlight.isCaseSensitive": false,
    "todohighlight.isEnable": true,
    "todohighlight.include": [
            "**/*.md",
    ],
    "todohighlight.keywords": [
        "DEBUG:",
        "REVIEW:",
        {
            "text": "NOTE:",
            "color": "#ff0000",
            "backgroundColor": "yellow",
            "overviewRulerColor": "grey"
        },
    ],
    ```
2. Select LineStatus Bar, 在状态栏左侧显示选中了多少行
3. Markdown All in one，支持代码块，支持 tex 语法，支持数学
   - Alt s，删除线
   - Ctrl b，加粗
   - Ctrl i，斜体
   - Ctrl Shift [，标题升一级
   - Ctrl Shift ]，标题降一级
   - Alt C, 打勾/去勾
   - Ctrl M，公式
   - Alt Shift F，格式化
4. [paste image](https://github.com/mushanshitiancai/vscode-paste-image), Markdown 直接粘贴图片，Ctrl Alt v
    ```bash
    # @ext:mushan.vscode-paste-image
    Default name: HHmmss
    File path confirm input box mode: only name
    path: ${currentFileDir}/img
    show file path confirm input box: checked
    ```
5. Markdownlint, 写的时候不开，避免提前陷入格式陷阱（纠结格式耽误正事） 
   1. [enable inline HTML elements](https://github.com/DavidAnson/markdownlint/issues/105)

    ```json
    // @ext:davidanson.vscode-markdownlint
    "markdownlint.config": {
            "MD033": {
                "allowed_elements": ["br",],
            }
        },  
    ```
6. [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/), 支持PlantUML, [code chunk](https://shd101wyy.github.io/markdown-preview-enhanced/#/zh-cn/code-chunk)

## NotUse 

1. ~~[vscode-mindmap](https://github.com/souche/vscode-mindmap)~~, 自有.km 格式，可以导出.png，脑图，纯图形界面，快捷键 tab 生成子节点，主要问题：只有父子节点之间连线，**不可自定义连接线**
2. ~~[js mindmap](https://github.com/borsh/jsmm)~~,自有.jsmm 格式，纯图形化，**无快捷键**
3. ~~Mermaid~~, 支持Markdown，细节不可控
4. ~~[PlantUML](https://plantuml.com/)~~, Graphviz 的封装，依赖java，支持`*.wsd, *.pu, *.puml, *.plantuml, *.iuml`，支持Markdown(enhance preview)
5. ~~graphviz~~，支持Markdown(原生preview)
6. ~~Draw.io~~ integration: mermaid plugin，dio 的 mermaid 插件
7. ~~Foam for VSCode (Wikilinks to Markdown)~~，链接不支持中文

## config

### markdown

```json
    "extensions": {
        "recommendations": [
			"cipchk.vscode-markdown-compact-table-formatter",
			"tchayen.markdown-links",
			"shd101wyy.markdown-preview-enhanced",
			"geeklearningio.graphviz-markdown-preview",
			"dendron.dendron",
			"gurumukhi.selected-lines-count",
			"qiqiworld.vscode-markdown-tinymind",
			"yzhang.markdown-all-in-one",
			"csholmq.excel-to-markdown-table"
		]
    }
```

## 配置

参见 [[vscode.workspace]], 将extension 配置为工作区建议项

