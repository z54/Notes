# snippets

[vscode自定义代码提示：用户代码片段 - gbckt - 博客园](https://www.cnblogs.com/gbckt/p/14304796.html)

> 不支持自动联想的字符（需要Ctrl Space)：`+`,`-`,`=`,`;`,`.`,`<`,`>`,`1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`,`0`

file -- preferences -- user snippets -- markdown.json

%USERPROFILE%\AppData\Roaming\Code\User\snippets\markdown.json

代码示例如下，使用 $加数字可以通过制表符控制光标移动，例如 $1 、 $2 、 $3...，数字越大越靠后，生成代码块后，光标会在数字最小的位置如 $1 开始，最小是 $1，$0 控制的是光标最后所在位置，官方给的例子中，光标会在 $1 位置，按下 tab 后，光标会跳到 $2 位置

```json
"Print to console": {
    "prefix": "log",
    "body": [
        "console.log('$1');",
        "$2"
    ],
    "description": "Log output to console"
}
```

```json
"博客配置": {
    "prefix": "setting",
    "body": [
        "---",
        "title: ${1:标题}",
        "date: $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE",
        "categories:",
        " - ${2|使用上下键选择分类,📒笔记,🔧工具|}",
        "tags:",
        " - ${3|使用上下键选择标签,vscode,JS,css,html,Vue,uniapp,微信小程序,React,TypeScript|}",
        "---",
        "",
        ":::tip",
        "${4:输入摘要}",
        ":::",
        "",
        "<!-- more -->",
        "",
        "$5"
    ],
    "description": "博客配置"
}
```