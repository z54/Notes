# I/O 编程

## 文件

### 打开文件

- 读

`open(name[.mode[.buffering]])`
默认模式是读模式，默认缓冲区是无

``` python
>>> f = open(r'c:\text\qiye.txt')
```

### 文件模式

值 | 功能
-|-
r | 读
w | 写
a | 追加
b | 二进制
+ | 读/写

### 文件读取

`read（）`、`readlines（）`、`close（）`

- `read()`、`close()`

如果成功打开文本文件，接下来调用read（）方法则可以一次性将文件内容全部读到内存中，最后返回的是str类型的对象

```python
>>> f = open(r'c:\text\qiye.txt')
>>> f.read()
     "qiye"
>>> f.close()
```

- `readlines`
对于大文件，可以反复调用read（size）方法，一次最多读取size个字节

###　文件写入

```python
f = open(r'c:\text\qiye.txt','w')
f.write('qiye')
f.close()
```
