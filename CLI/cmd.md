# cmd

## 变量

```cmd
rem 变量 
set var=1 
echo %var%

set a=1
set /a a += 2
set /a b = a + 3
set /a c = a - 1
set /a d = a * 2
set /a e = a / 2
set /a f = 5 % 2
echo 自增%a% 加%b% 减%c% 乘%d% 除%e% 余%f%

set a=1
set /a b1 = 1 "&" 1 
set /a b2 = 1 "&" 0 
set /a b3 = 0 "&" 0 
set /a c1 = 1 "|" 1 
set /a c2 = 1 "|" 0 
set /a c3 = 0 "|" 0
set /a d0 = !0 
set /a d1 = !1 
set /a m1 = 1 "<<" 1
set /a m2 = 1 ">>" 1
echo 11与=%b1% 10与=%b2% 00与=%b3% 
echo 11或=%c1% 10或=%c2% 00或=%c3%
echo 非0=%d0% 非1=%d1% 
echo 1左移1=%m1% 1右移1=%m2%

set /p var=input
echo %var%

set var = a#b
set str = %var:#=.%
echo #替换为. %str%

set var=0123456789
echo %var:~1,4%
echo %var:~-3%
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
