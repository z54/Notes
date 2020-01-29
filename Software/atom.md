# Initial

## 基础扩展

- 汉化 **Atom Simplified Chinese Menu Master**

## Atom & gcc

1. 下载Atom并安装
2. 配置gcc编译环境
    1. 安装MinGW
    2. 添加系统变量PATH
3. 配置Atom编译环境-插件
    / |/
    -|-
    linter-gcc <br> linter <br> gcc-make-run | c语言环境

  > F6 运行

## Atom & python

1. 安装python
2. 插件 **atom-python-run**
> F5 运行

## Atom & markdown

1. **markdown-preview-enhanced**

# Usage
- 格式化
  `Edit -> Lines -> Auto Indent`
  ctrl-shift-C

# fatal
1. [Atom本地安装插件右上角出现红色报错解决方案 - 阮文明 - 博客园](https://www.cnblogs.com/ruanwenming/p/7702309.html)

在github上搜索你相中的插件(Package)，并下载ZIP包或直接克隆项目到本地。然后将该包直接复制到C盘中的用户下的 `.atom\packages\` 文件夹下，注意 atom前面有一个点。

然后重启Atom后发现右上角会有红色报错，大概是 `cannot find module ‘lodash.random’` 之类的，缺少关键项。然后用管理员权限打开`cmd`，将目录切入到该插件文件夹里，缺少什么就用`npm`命令安装什么，键入以下命令：

`npm install lodash.random`

安装完毕后重启，会发现缺少新的关键项，继续使用npm安装，如此往复，我安装时大约重复了五六次。打开后终于不报错了，插件好用了。

如果插件还不好用，就从UI界面的插件列表中光明正大的卸载了该插件，再重新UI界面安装。不缺少关键项后通常就不会因为环境问题报错安装不上了。

# 参考
- [Atom安装并配置C/C++开发环境](https://blog.csdn.net/qq_36731677/article/details/54609583)
- [Atom安装并配置C/C++开发环境 - CSDN博客](https://blog.csdn.net/qq_36731677/article/details/54609583)
