# Programming

## 界面

- 应用的res\layout目录下编写XML布局文件
    - activity_main主要负责的是包含toolbar的整个页面布局，其中，使用了一个`<include/>`标签把content_main放进activity_main布局中
- 在Activity中使用以下Java代码显示XML文件中布局的内容。
    - `setContentView(R.layout.main);`

#

##