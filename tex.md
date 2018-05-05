# install
## linux
- 下载软件列表并安装
```bash
wget http://cs2.swfu.edu.cn/~wx672/debian-install/list.texlive
sudo apt install `cat list.texlive`
```
- 下载latexmk
编译命令 `latexmk filename.tex`
清空命令 `latexmk -c`
# Method
- 指定坐标
```tex
\node (node_name) at (0, 0) {Display_text};
\node (b) at +(0: 1.5) {B};
```

- foreach
```tex
\foreach \from/\to in {a/b, b/c, c/a}
  \draw [->] (\from) -- (\to);
```


# Example
##

```tex
\begin{tikzpicture}[scale=.9, transform shape]
  \tikzstyle{every node} = [circle, fill=gray!30]
    \node (a) at (0, 0) {A};
    \node (b) at +(0: 1.5) {B};
    \node (c) at +(60: 1.5) {C};
    \foreach \from/\to in {a/b, b/c, c/a}
      \draw [->] (\from) -- (\to);
\end{tikzpicture}
```

## windows
- [下载ISO文件](https://ctan.org/tex-archive/systems/texlive/Images/)
- 打开ISO并启动`install-tl-advanced.bat`安装 texlive
  - 耗时约90min，默认路径在`C:\texlive`

### Reference
- [Windows下打造Sublime Text + Tex Live环境 - 冰原狼 - 博客园](https://www.cnblogs.com/dezheng/p/3895249.html)
- [windows下用Atom编辑Latex时环境配置_行歌行_新浪博客](http://blog.sina.com.cn/s/blog_12cb78c440102wh6q.html)
- [官方下载网站 TEX Live ISO Images](https://ctan.org/tex-archive/systems/texlive/Images/)
- [在 MS Windows 作業系統平台裝設 TeXLive 2011](http://exciton.eo.yzu.edu.tw/~lab/latex/install_latex_cjk_ms_windows.html)
