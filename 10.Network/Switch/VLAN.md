# VLAN 
## 配置

- VLAN数据库配置模
```
    Switch#vlan database
    Switch(vlan)#vlan vlan-id [name vlan-name]
    Switch（vlan）# no vlan vlan-id
    Switch(vlan)#exit
```
- 全局配置模式
```    
    Switch(config)#vlan vlan-id
    Switch(config-vlan)#name vlan-name
    Switch（config）# no vlan 20
```
- 端口加入VLAN
```
    Switch(config)# vlan 20
    Switch(config)# interface interface-id
    Switch(config-if)# switchport mode access
    Switch(config-if)# switchport access vlan vlan-id
    Switch(config-if)# no switchport access vlan vlan-id
    
    Switch(config)# interface range f0/1 – 10
    Switch(config-if-range)# switchport access vlan vlan-id
```
- 配置trunk
```
    Switch(config)#interface interface-id
    Switch(config-if)#switchport trunk encapsulation { isl | dot1q | negotiate }
    Switch(config-if)#switchport mode {dynamic {desirable | auto} | trunk | access}
    Switch(config-if)#switchport trunk native vlan vlan-id
```
- 以太网通道（线路逻辑捆绑）
    - 配置PAgP以太网通道
    ```
        Switch(config-if)#interface internet-id
        Switch(config-if)#channel-protocol pagp
        Switch(config-if)#channel-group number mode { on | auto | desirable }
    ```
    - 配置LACP以太网通道
    ```
        Switch(config-if)#interface internet-id
        Switch(config-if)#channel-protocol lacp
        Switch(config-if)#channel-group number mode { on | passive | active }
    ```
    - 查看以太网通道
    ```
    SW1#show etherchannel summary 
    ```