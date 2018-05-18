<!-- TOC -->

- [Mode](#mode)
- [常用命令 usual](#usual)
- [正常流程 normal](#normal)
  - [主机名管理 hostname](#hostname)
  - [旗标 banner](#banner)
  - [接口配置 interface](#interface)
  - [密码配置 password](#password)
  - [config manage](#config-manage)
- [VTP](#vtp)
- [TRUNK](#trunk)
- [STP](#stp)
- [HSRP](#hsrp)
- [VRRP](#vrrp)
- [GLBP](#glbp)

<!-- /TOC -->
# Mode
| command            | mode                                   | prompt 提示符        |
| ------------------ | -------------------------------------- | -------------------- |
|                    | User mode <br> 用户模式                | Switch>              |
| enable             | Privileged mode <br> 特权模式          | Switch#              |
| conf t             | Global configuration <br> 全局配置模式 | Switch(config)#      |
| exit               | 返回上一级                             |                      |
| C-Z                | 返回特权模式                           | Switch#              |
# 常用命令 usual
| 命令                                               | 解释                    |
| -------------------------------------------------- | ----------------------- |
| `switch(config)#host SW1` <br> `sw1(config)#`      | 配置主机名              |
| `Switch#show version`                              | 显示IOS名称以及版本信息 |
| `Switch#show mac-address-table`                    | 查看交换的mac地址表     |
| `Switch(config-if)#duplex {full / half / auto}`    | 指定接口的双工模式      |
| `Switch(config-if)#speed {10 / 100 / 1000 / auto}` | 指定接口的通信速率      |

# 正常流程 normal
```
Switch>en
Switch#conf t
Switch(config)#int f0/1
Switch(config-if)#
```
## 主机名管理 hostname
```
Switch(config)#host SW1
SW1(config)#
```
## 旗标 banner
> 提示语
  ```
  Switch(config)#banner ?
  motd  Set Message of the Day banner
  ```

  ```
  SW1(config)#banner motd #
  Enter TEXT message.  End with the character '#'.
  Internal network, then you must disconnect immediately.
  #

  SW1(config)#^Z
  SW1#
  %SYS-5-CONFIG_I: Configured from console by console

  SW1#exit

  SW1 con0 is now available

  Press RETURN to get started.

  Internal network, then you must disconnect immediately.

  SW1>

  ```
## 接口配置 interface
```
Switch(config)#int ?
  Ethernet         IEEE 802.3
  FastEthernet     FastEthernet IEEE 802.3
  GigabitEthernet  GigabitEthernet IEEE 802.3z
  Port-channel     Ethernet Channel of interfaces
  Vlan             Catalyst Vlans
  range            interface range command
```

## 密码配置 password
```
Switch(config)#line ?
  <0-16>   First Line number
  console  Primary terminal line
  vty      Virtual terminal
```
```

```
## config manage
- 删除现有配置
```
Switch> enable
Switch# erase start-config
Switch# reload
```


# VTP
# TRUNK
# STP
# HSRP
# VRRP
# GLBP
