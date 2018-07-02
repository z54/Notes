# 文件
- 读
`open(name[.mode[.buffering]])`
默认模式是读模式，默认缓冲区是无
``` python
>>> f = open(r'c:\text\qiye.txt')
```
值 | 功能
-- | -
r | 读
w | 写
a | 追加
b | 二进制
+ | 读/写

#
read（）、readlines（）、close（）
