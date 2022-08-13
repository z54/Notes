# GDB

## Usage

```bash
gcc -g test.c -o test
gdb test
```

```bash
b 20 // 设置第20行为断点
b func // 设置func函数为断点

info break // 查看所有断点
info watchpoints // 查看所有观察点

delete // 删除断点

watch i //

run // 执行

n // next，下一行
s // step，下一步
c // continue，继续

p i // print，输出变量的值

<enter> // 反复执行上一次的命令

q // quit，退出
```

