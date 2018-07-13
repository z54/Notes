<!-- TOC -->

- [Markdown](#markdown)
  - [Headers](#headers)
  - [link](#link)
  - [image](#image)
  - [highlighting](#highlighting)
  - [Task Lists](#task-lists)
  - [Tables](#tables)
  - [toc](#toc)
- [fatal](#fatal)
- [参考](#)

<!-- /TOC -->

# Markdown

## Headers
```
# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag
```
Emphasis
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

As Kanye West said:

> We're living the future so
> the present is our past.
Inline code
I think you should use an
`<addr>` element here instead.

## link
It's very easy to make some words **bold** and other words *italic* with Markdown. You can even [link to Google!](http://google.com)

## image
![Alt text](/figs/cover.jpg)

![Alt text](/figs/cover.jpg "Optional title")

![Image of Yaktocat](https://www.baidu.com/img/superlogo_c4d7df0a003d3db9b65e9ef0fe6da1ec.png)

## highlighting

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

## Task Lists
* Item 1
* Item 2
  * Item 2a
  * Item 2b
Ordered
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> ~~supported~~
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

## Tables

First Header | Second Header | ThirdHeaderHeader
:- | :-: | -:
Content from cell 1 | Content from cell 2 | Content from cell 3
Content in the first column | Content in the second column | Content in the third column

## toc
**Markdown Preview Enhanced**
- [Atom markdown 目录组件支持（插件）](https://jingyan.baidu.com/article/6181c3e0be9473152ff1536c.html)

# fatal
- 竖线用 `&#124;` 或者 `&#x7C;` 来代替
- 行内换行 `<br>`

# 参考
- [Mastering Markdown · GitHub Guides](https://guides.github.com/features/mastering-markdown/)
