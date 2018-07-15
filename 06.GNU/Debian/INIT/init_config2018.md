# Initial Config 2018

## 检查联网
`ping 123.125.115.110`
`ping 220.181.57.216`

## config
```bash
NormalUser=`cat /etc/group | grep 1000 | cut -d ":" -f 1`

# sources.list & system update
echo 'deb http://mirrors.ustc.edu.cn/debian stable main contrib non-free' > /etc/apt/sources.list
apt-get update
apt-get dist-upgrade

# x-window & chromium: startx成功
apt-get install x-window-system-core chromium

# startx成功，中键可以打开菜单，可打开xterm，打开chromium失败
apt-get install sawfish

# 虚拟机切换全屏
open-vm-tools-desktop

# vmware tools
mkdir /mnt/cdrom
mount /dev/cdrom /mnt/cdrom
cd
tar zxpf /mnt/cdrom/VMwareTools-x.x.x-yyyy.tar.gz
cd vmware-tools-distrib
sudo ./vmware-install.pl

# no sudo password
echo "$NormalUser ALL = NOPASSWD: ALL" > /etc/sudoers.d/$NormalUser && chmod 0440 /etc/sudoers.d/$NormalUser

# 中文环境
fonts-wqy-microhei
sudo dpkg-reconfigure locales
```
