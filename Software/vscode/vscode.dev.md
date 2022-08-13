# vscode dev

```tinymind
plug
    [[node.js]]语法
        [菜鸟教程](https://www.runoob.com/nodejs/nodejs-tutorial.html)
    plus教程
        开发文档，[Extension API | Visual Studio Code Extension API](https://code.visualstudio.com/api)
        开发指导，[Extension Guides](https://code.visualstudio.com/api/extension-guides/overview)
        插件示例，[vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)
        界面介绍，[Extension Guidelines](https://code.visualstudio.com/api/references/extension-guidelines)
    需求
        插件冲突，同时开启时，mermaid语法失效
        markdown preview mermaid support，mathpix markdown
        两个插件同时调用了代码块，需要融合成一个
```

struct

```sh
.
├── .vscode
│   ├── launch.json     // 用于启动和调试扩展的配置
│   └── tasks.json      // 编译TypeScript的生成任务的配置
├── .gitignore          // 忽略生成输出和节点输出模块
├── README.md           // 扩展功能的可读描述
├── src
│   └── extension.ts    // 扩展源代码
├── package.json        // 扩展清单
├── tsconfig.json       // TypeScript配置
```

## 准备

- 环境
  - npm install -g yo generator-code
  - [VSCode插件开发全攻略（一）概览 - 我是小茗同学 - 博客园](https://www.cnblogs.com/liuxianan/p/vscode-plugin-overview.html)
  - [microsoft/vscode-extension-samples: Sample code illustrating the VS Code extension API.](https://github.com/microsoft/vscode-extension-samples)

```tinymind
sample
    helloworld*
```

## 扩展

- [Managing Extensions in Visual Studio Code](https://code.visualstudio.com/docs/editor/extension-marketplace)
- [The Visual Studio Code command-line options](https://code.visualstudio.com/docs/editor/command-line)

f1 `Reload Window`

```bat
@ext:py
@category:"programming languages" @sort:installs 

code --list-extensions
code --install-extension ms-vscode.cpptools
code --uninstall-extension ms-vscode.csharp
code --enable-extension tomoki1207.selectline-statusbar
code --disable-extension sandcastle.vscode-open

code --extensions-dir <dir>
    Set the root path for extensions.
code --list-extensions
    List the installed extensions.
code --show-versions
    Show versions of installed extensions, when using --list-extension.
code --install-extension (<extension-id> | <extension-vsix-path>)
    Installs an extension.
code --uninstall-extension (<extension-id> | <extension-vsix-path>)
    Uninstalls an extension.
code --enable-proposed-api (<extension-id>)
    Enables proposed API features for extensions. Can receive one or more extension IDs to enable individually.
```

| Argument | Description |
|----------|-------------|
| --install-extension <ext> | Install an extension. Provide the full extension name publisher.extension as an argument. Use --force argument to avoid prompts. |
| --uninstall-extension <ext> | Uninstall an extension. Provide the full extension name publisher.extension as an argument. |
| --disable-extensions | Disable all installed extensions. Extensions will still be visible in the Disabled section of the Extensions view but they will never be activated. |
| --list-extensions | List the installed extensions. |
| --show-versions | Show versions of installed extensions, when using --list-extensions |
| --enable-proposed-api <ext> | Enables proposed api features for an extension. Provide the full extension name publisher.extension as an argument. |


## 需求

- [x] 下载并融合markdown preview mermaid support，mathpix markdown， tinymind
  - %userprofile%\Documents\DEV\vscode_plug
  - [mjbvz/vscode-markdown-mermaid: Adds Mermaid diagram and flowchart support to VS Code's builtin markdown preview](https://github.com/mjbvz/vscode-markdown-mermaid)
  - [Mathpix/vscode-mathpix-markdown: Enable rendering Mathpix Markdown with latex and chemistry support.](https://github.com/mathpix/vscode-mathpix-markdown)
  - [ArcticLampyrid/vscode-markdown-tinymind](https://github.com/ArcticLampyrid/vscode-markdown-tinymind)