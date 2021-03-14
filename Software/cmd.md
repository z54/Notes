# cmd

[CMD有哪些有趣的命令？ - 知乎](https://www.zhihu.com/question/29930842?sort=created)

- `mode`
查看console 口编号

## 变量

```cmd
rem 系统变量
%homedrive% # C
%homepath% # C:\Users\user

: 变量
set var=1
echo $var
set /var var=%var%+1
echo $var
set /p var=input
echo $var
```

## ip

[route Cmd详解 - binsite - 博客园](https://www.cnblogs.com/bingle/p/4243988.html)

```bat
arp -a
ipconfig
ping -I source_ip destination_ip -c 5
telnet ip portnumber
route print
route ADD destination_network MASK subnet_mask gateway_ip
route -p add 192.168.0.0 mask 255.255.0.0 192.168.3.1
route delete 10.41.0.0 mask 255.255.0.0
route delete 10.
route delete 192.0.0.0 mask 0.0.0.0  192.168.3.1 `
```
## loop

[cmd for 用法 - bug_x - 博客园](https://www.cnblogs.com/cbugs/p/8992059.html)

- `FOR %variable IN (set) DO command [command-parameters]`

## find

`ipconfig | find /n "IPv4"`

