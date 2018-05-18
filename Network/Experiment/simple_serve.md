<link rel="stylesheet" type="text/css" href="../images/auto-number-title.css" />
<!-- TOC -->

- [简单的服务器（网站、邮件、DNS）](#dns)
    - [实验要求](#)
    - [拓扑](#)
    - [配置](#)
        - [R0](#r0)
        - [R1](#r1)
        - [Server0](#server0)
        - [Server1](#server1)
        - [PC0](#pc0)
        - [PC1](#pc1)
    - [实验结果](#)
        - [互发邮件验证](#)
            - [PC0](#pc0)
            - [PC1](#pc1)
        - [互访网站验证](#)
            - [PC0](#pc0)
            - [PC1](#pc1)

<!-- /TOC -->

# 简单的服务器（网站、邮件、DNS）

## 实验要求

双方互相访问服务器网站，互发邮件

## 拓扑

## 配置

### R0

```
en
conf t
int f0/0
ip add 192.168.1.1 255.255.255.0
no sh
int f0/1
ip add 192.168.2.1 255.255.255.0
no sh
```
- 静态路由`ip route 192.168.3.0 255.255.255.0 192.168.1.2`

### R1

```
en
conf t
int f0/0
ip add 192.168.1.2 255.255.255.0
no sh
int f0/1
ip add 192.168.3.1 255.255.255.0
no sh
```
- 静态路由`ip route 192.168.2.0 255.255.255.0 192.168.1.1`
- 
### Server0

![s0_1](/images/s0_1.jpg)
![s0_2](/images/s0_2.jpg)
![s0_3](/images/s0_3.jpg)
![s0_4](/images/s0_4.jpg)

### Server1

![s1_1](/images/s1_1.jpg)
![s1_2](/images/s1_2.jpg)
![s1_3](/images/s1_3.jpg)
![s1_4](/images/s1_4.jpg)

### PC0

![p0_1](/images/p0_1.jpg)
![p0_2](/images/p0_2.jpg)

### PC1

![p1_1](/images/p1_0.jpg)
![p1_2](/images/p1_1.jpg)

## 实验结果

### 互发邮件验证

#### PC0

![r1_p0](/images/r1_p0.jpg)

#### PC1	

![r1_p1](/images/r1_p1.jpg)

### 互访网站验证

#### PC0

![r2_p0](/images/r2_p0.jpg)

#### PC1 

![r2_p1](/images/r2_p1.jpg)