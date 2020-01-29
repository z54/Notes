# sublime

# 激活

Sublime Text 3 (Build 3143)激活码
—– BEGIN LICENSE —–
TwitterInc
200 User License
EA7E-890007
1D77F72E 390CDD93 4DCBA022 FAF60790
61AA12C0 A37081C5 D0316412 4584D136
94D7F7D4 95BC8C1C 527DA828 560BB037
D1EDDD8C AE7B379F 50C9D69D B35179EF
2FE898C4 8E4277A8 555CE714 E1FB0E43
D5D52613 C3D12E98 BC49967F 7652EED2
9D2D2E61 67610860 6D338B72 5CF95C69
E36B85CC 84991F19 7575D828 470A92AB
—— END LICENSE ——

# env

## 将Sublime Text 3 打造成 C/C++ 编译器 - 简书
已剪辑自: http://www.jianshu.com/p/86c0822cc89b
本文介绍Sublime Text 3的C/C++开发环境搭建，包括MinGW的安装，gcc运行c语言，g++运行c++语言，在sublime中运行以及在cmd中运行的方法。
安装MinGW
MinGW是Minimalist GNU on Windows的首字母缩写，安装后就可以使用很多的GNU工具。GNU（GNU’s Not Unix）是linux中的一个著名的项目，包含了gcc\g++\gdb等工具。也就是说，安装MinGw后，我们就可以使用gcc和g++命令了。
首先去官网下载MinGW。网站为 http://www.mingw.org/


MinGW
安装截图：


安装截图
选中截图中的4项，点击 Installation > Apply Changes ，等待安装完成。


选项
安装完成后，测试是否安装成功。
先配置C/C++环境变量：
- 变量名              变量值
 - C_INCLUDEDE_PATH   C:\MinGW\include
 - LIBRARY_PATH          C:\MinGW\lib
 - Path               C:\MinGW\bin


环境变量
注意：Windows环境变量的修改不会立即生效，需要重启Windows。
开始测试，我的测试代码 test.c：

```c
#include
int main(int argc, char const *argv[])
{
    printf("hello\n");
    return 0;
}
```

在cmd中调用gcc：
gcc test.c -o test


测试
出现如图，安装和环境变量配置成功了。
Sublime Text 3配置
实现 使SublimeText 3调用系统cmd窗口输出


新建编译环境


文件内容
配置新的编译文件 C.sublime-build
内容为：
`"cmd": ["g++", "${file}", "-o","${file_path}/${file_base_name}"],`  //此命令导致编译错误，修正如下
```bash
{
"cmd": "gcc -Wall \"$file_name\"-o \"$file_base_name\"",  
"file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:?(.*)$",
"working_dir": "${file_path}",
"encoding":"cp936",
"selector": "source.c",
"variants":
[
{
"name": "Run",
"cmd": ["cmd","/C","start","cmd","/c", "${file_path}/${file_base_name}.exe &pause"]
}
]
}
```
修改版：输出为a.exe
E:\Tools\SublimeTextBuild3126x64\Data\Packages\User\C.sublime-build

```bash
{  
    "working_dir": "$file_path",  
    "cmd": "gcc -Wall \"$file_name\"",  
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",  
    "encoding":"cp936",
    "selector": "source.c",  
    "variants": [{  
        "name": "Run",  
        "cmd": ["cmd","/C","start","cmd","/c", "${file_path}/a.exe &pause"]
    }]  
}
```

保存。
测试是否搭建成功
先将 Build System 选为 C
按住 Sublime Text 快捷键 编译和运行
Ctrl + Shift + B
测试结果如下：


完成测试
至此，Sublime Text 3 已经被成功地打造成 C编译器。
C++的 Build System 文件类似，自行配置。多练练搜索技能。

[将Sublime Text 3 打造成 C/C++ 编译器 - 简书](https://www.jianshu.com/p/86c0822cc89b)

## Sublime Text+MinGW实现轻量级C语言开发环境 - Lorain_Lynies的博客 - CSDN博客

十分喜欢sublime text这个文本编辑器，主要是小巧强大，插件丰富。
必备插件package control插件管理器,codeintel代码补全插件,emmet快速编码神器（html/css）,coolformat代码格式化工具，jsformat脚本格式化工具。
配置sublime text的C语言编译器。
1、下载安装MinGW。
添加路径C:\MinGW\bin到系统变量PATH。
2、配置sublime text。
a、Tool>Build System>New Build System输入如下代码：

```bash
{  
    "working_dir": "$file_path",  
    "cmd": "gcc -Wall \"$file_name\"-o \"$file_base_name\"",  
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",  
    "selector": "source.c",  
    "variants": [{  
        "name": "Run",  
        "shell":true,  
        "cmd": ["start", "${file_path}/${file_base_name}"]  
    }]  
}
```

[Sublime Text+MinGW实现轻量级C语言开发环境 - CSDN博客](https://blog.csdn.net/lorain_lynies/article/details/52028831)

## vim

1、安装Sublime Text 3 
     下载安装：http://www.sublimetext.com/3
Package Control安装：https://sublime.wbond.net/installation
 
2、如何安装插件
在第1步中安装好后 按 Ctrl+Shift+P ，输入insta 在下拉菜单选择 Install Package 按回车键，在接着弹出的输入框中输入插件名字，回车选择即可安装该插件：

3、常用插件
    1、ConvertToUTF8　　　　     支持多种编码，解决中文乱码问题。
    2、Bracket Highlighter　　      用于高亮匹配括号、引号、html标签。
    3、DocBlockr　　　　　　　    可以自动生成PHPDoc风格的注释。
    4、Emmet 　　　　　　　　 　 快速编写HTML，原 Zen Coding。
    5、SideBar Enhancements　　这个插件改进了侧边栏，增加了许多功能
    6、evernote　　　　　　　　　这个是 evernote 的插件，支持 markdown 语法
    7、markdown preview　　　　markdown 预览插件
 
4、主题
主题在 Sublime Text 中其实也属于插件，因此安装主题的方法与安装插件一致，输入主题名字 Brogrammer 即可完成安装。
接着进入设置：在菜单栏中  Preferences -> Setting - User ，在打开的配置文件中添加下面两行选项（注意如果前后有其他选项请添加对应的逗号进行分隔）：
"theme": "Brogrammer.sublime-theme",
"color_scheme": "Packages/Theme - Brogrammer/brogrammer.tmTheme"
 
主题详细信息：https://packagecontrol.io/packages/Theme%20-%20Brogrammer
 
5、启用 Vim 模式
      在菜单栏中： Preferences -> Setting - User ，即可打开配置文件进行编辑，将 ignored_packages 项的[]里面内容清空：
 "ignored_packages":
[
]
这样就启用了 Vim 模式，按 Esc 退出编辑模式，即进入了 Vim 模式。
     vim 模式快捷键说明请查看 http://feliving.github.io/Sublime-Text-3-Documentation/vintage.html
 
6、启用 Ctrl 功能键及自定义功能键
 　　Preference->Setting User 添加如下内容:
 
 "vintage_ctrl_keys": true
   这样就支持以下命令了：
    ○ Ctrl+[ : Esc键的别名
    ○ Ctrl+R : Redo
    ○ Ctrl+Y : 向下滚动一行
    ○ Ctrl+E : 向上滚动一行
    ○ Ctrl+F : 下一页
    ○ Ctrl+B : 上一页
如果觉得以上按键太复杂，可以自定义按键，找到 Vintage.sublime-package这个文件，其实是一个压缩包，改名zip后缀后解压得出文件，使用记事本打开 Default.sublime-keymap 文件，找到需要修改的快捷键进行修改即可。
例如我需要将 ctrl+f 下一页修改成 f+f 下一页：
搜索 “ctrl+f”，找到以下代码：

```bash
{ "keys": ["ctrl+f"], "command": "set_motion", "args": {
"motion": "move",
"motion_args": {"by": "pages", "forward": true, "extend": true }},
"context": [{"key": "setting.command_mode"}, {"key": "setting.vintage_ctrl_keys"}]
},
```
 
修改成

```bash
{ "keys": ["f","f"], "command": "set_motion", "args": {
"motion": "move",
"motion_args": {"by": "pages", "forward": true, "extend": true }},
"context": [{"key": "setting.command_mode"}, {"key": "setting.vintage_ctrl_keys"}]
},
```

这样，你 按esc退出编辑模式，按两下f键，即可实现向下翻页了，大家可以尝试下将 ctrl+b 向上翻页修改成 b+b 。

[Sublime Text 3 插件安装及Vim 模式设置 - zuike - 博客园](http://www.cnblogs.com/zuike/p/4402022.html)

## sublime 格式化

平时在使用sublime时，在代码凌乱的时候看得挺烦，又懒得去装啥插件，后来发现sublime其实已经自带了代码格式化的功能，多数人都没发现罢了
功能名为reindent，如果使用了SublimeText汉化包，它的名称为“再次缩进”

路径：`Edit - Line - Reindent`（中文路径则是：`编辑 - 行 - 再次缩进`）

网上有文章提到该功能不需要选中代码之后才能执行格式化功能，默认是格式化整个文件里的代码；个人进行测试后，并不是这样的，光标停在哪一行，使用该功能后，它执行的仅为向右缩进的简单功能，与当前代码结构无关，它仅执行缩进。而只有全选所有代码时，执行该功能，才会对代码进行格式化

reindent功能默认sublime并没有分配快捷键，可执行以下操作进行设置快捷键

1、打开设置快捷键的界面（分左右两块区域，左边为编辑器默认，通常为了保证不影响正常功能，左边的默认设置不作修改，而修改右边的User区域）：

Preferences → Key Bindings – User

2、在其中添加代码，快捷键组合可按需设置：

```bash
{"keys": ["ctrl+shift+r"], "command": "reindent" , "args":
{"single_line": false}}
```

[Sublime Text 3 自带的格式化代码功能（reindent） - TerryZ的个人空间 - 开源中国](https://my.oschina.net/u/171860/blog/754867)

## 跳转

sublime text如何显示函数列表，如何实现编辑区域随意跳转？
函数列表，函数跳转
CTRL+R
跳到上一个编辑处
alt+-
跳到下一个编辑处
alt+shift+-

[(9 条消息)sublime text如何显示函数列表，如何实现编辑区域随意跳转？ - 知乎](https://www.zhihu.com/question/29615755)
