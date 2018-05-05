[toc]

# Syntax guide

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
Lists
Unordered
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
Images
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
Links
http://github.com - automatic!
[GitHub](http://github.com)
Blockquotes
As Kanye West said:

> We're living the future so
> the present is our past.
Inline code
I think you should use an
`<addr>` element here instead.

# Examples
It's very easy to make some words **bold** and other words *italic* with Markdown. You can even [link to Google!](http://google.com)

Sometimes you want numbered lists:

1. One
1. Two
1. Three

Sometimes you want bullet points:

* Start a line with a star
* Profit!

Alternatively,

- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this

  If you want to embed images, this is how you do it:

  ![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

  # Structured documents

Sometimes it's useful to have different levels of headings to structure your documents. Start lines with a `#` to create headings. Multiple `##` in a row denote smaller heading sizes.

### This is a third-tier heading

You can use one `#` all the way up to `######` six for different heading sizes.

If you'd like to quote someone, use the > character before the line:

> Coffee. The finest organic suspension ever devised... I beat the Borg with it.
> - Captain Janeway

And, of course emoji! :sparkles: :camel: :boom:

## Syntax highlighting

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

## Task Lists
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
If you include a task list in the first comment of an Issue, you will get a handy progress indicator in your issue list. It also works in Pull Requests!

## Tables

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

## toc
**Markdown Preview Enhanced**
[Atom markdown 目录组件支持（插件）](https://jingyan.baidu.com/article/6181c3e0be9473152ff1536c.html)

# 参考
- [Mastering Markdown · GitHub Guides](https://guides.github.com/features/mastering-markdown/)
