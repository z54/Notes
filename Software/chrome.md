# chrome

[browser](browser.md)<!-- [[browser]] --> 

[Chrome 键盘快捷键 - 计算机 - Google Chrome帮助](https://support.google.com/chrome/answer/157179)

## chrome默认的书签位置,json格式保存

explorer %homepath%"\AppData\Local\Google\Chrome\User Data\Default\Bookmarks

## 命令

about:about
chrome://about/

chrome://bookmarks/
chrome://sync/
chrome://flags/
chrome://dino/
chrome://version
chrome://settings/
chrome://extensions/shortcuts
chrome://downloads/
chrome://extensions/
chrome://history
chrome://cache/

about:
about:dns
about:memory
view-source:[URL]
about:cache

## 特性

多线程下载（将默认的 Default 改为 Enabled）
chrome://flags/#enable-parallel-downloading

## search engine

chrome://settings/search

```s
https://search.douban.com/movie/subject_search?search_text=%s
https://search.bilibili.com/all?keyword=%s
http://cn.bing.com/search?q=%s
https://duckduckgo.com/?q=%s
https://github.com/search?q=%s
https://greasyfork.org/zh-CN/scripts?q=%s
https://steamdb.info/instantsearch/?query=%s
https://store.steampowered.com/search/?term=%s
https://www.zhihu.com/search?type=content&q=%s
https://www.baidu.com/s?wd=%s
http://v.qq.com/x/search?opensearch=1&q=%s
```

以下是从Chrome调用CMD的几种方式：

使用Chrome插件：例如“Shell Command”插件，可以直接在Chrome中运行CMD命令。

使用“chrome://net-internals/#q=proxy”命令：在Chrome地址栏中输入该命令，可以打开Chrome的网络内部工具，其中有一项叫做“Sockets”可以使用CMD命令。
 
使用“chrome://flags/#enable-experimental-web-platform-features”命令：在Chrome地址栏中输入该命令，可以打开Chrome的实验性功能选项，其中有一项可以在Chrome中运行CMD命令。

使用JavaScript代码：在Chrome的开发者工具中使用JavaScript代码可以调用CMD命令，并将结果显示在控制台中。

