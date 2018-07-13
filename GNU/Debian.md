# Debian Install

**disconnect the network**

1. Debian GNU/Linux installer boot menu
    - `Install`
2. Select a language
    - Language: `English`
3. Select your location
    - Country, territory or area: `other` -> `Asia` -> `China`
4. Configure locales
    - Country to base default locale settings on: `United States - en_US.UTF-8`
5. Configure the keyboard
    - Keymap to use: `American English`
6. configure the network
    - Hostname: `debian`
    - Domain name: `<null>`
7. Set up users and passwords
    - Root password: `1`
    - Re-enter password to verify: `1`
    - Full name for the new user: `zach`
    - Username for your account: `zach`
    - Choose a password for the new user: `1`
    - Re-enter password to verify: `1`
8. Parition disks
    - Partitioning method: `Guided - use entire disk and set up LVM`
    - Select disk to parition:
    `SCSI1 (0,0,0) (sda) - 21.5 GB VMware, VMware Virtual S`
    - Partitioning scheme: `Separate /home partition`
    - Write the changes to disk s and configure LVM? `Yes`
    - `Finish patitioning and write changes to disk`
    - Write the changes to disks? `Yes`
9. Configure the package manager
    - Scan another CD or DVD? `No`
    - Debian archive mirror country: `<tab>` `<Go Back>`
    - Continue without a network mirror? `Yes`
10. Configuring popularity-contest
    - Participate in the package usage survey? `No`
11. Software selection
    - Choose software to install: `Null`
12. Install the GRUB boot loader on a hard disk
    - Install the GRUB loader to the mastaer boot record? `Yes`
    - Device for boot loader installation: `/dev/sda`
13. Finish the installation
    - `Continue`

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

## Component

**main** consists of DFSG-compliant packages, which do not rely on software outside this area to operate. These are the only packages considered part of the Debian distribution.

**contrib** packages contain DFSG-compliant software, but have dependencies not in main (possibly packaged for Debian in non-free).

**non-free** contains software that does not comply with the DFSG.

# Initial Config 2017

``` bash
NormalUser=`cat /etc/group | grep 1000 | cut -d ":" -f 1`
if[`whoami` -eq $NormalUser]
then
echo command 'su' and enter your root password
 mount `fdisk -l | grep FAT16 | cut -d " " -f 1` /mnt && cp /mnt/Debian/* /home/$NormalUser && ./start
 echo 'deb http://mirrors.ustc.edu.cn/debian sid main non-free contrib
deb http://mirrors.163.com/debian sid main non-free contrib' > /etc/apt
apt-get update
apt-get install aptitude
wget --http-user=jkxjxxz --http-password=secret http://cs2.swfu.edu.cn/pub/resources/tools/apt-mark-showmanual.wx672laptop
aptitude -R install `cat apt-mark-showmanual.wx672laptop`
echo -e User_Alias NORMAL = $NormalUser"\n"NORMAL  ALL = NOPASSWD: ALL > /etc/sudoers.d/$NormalUser && chmod 0440 /etc/sudoers.d/$NormalUser
su $NormalUser
for f in dotfile/dot.*; do ln -sf $f; done
ln -sf dotfile/help/dot.* .
rm -f .bash*
rename 's/dot//' dot.*
wget -O .keys.png http://cs2.swfu.edu.cn/~wx672/tex-fun/keys/keys.png
sudo cp ~/dotfile/etc/systemd/system/autologin@.service /etc/systemd/system/
sudo ln -s /etc/systemd/system/autologin@.service /etc/systemd/system/getty.target.wants/getty@tty8.service
 tty=`cat /etc/systemd/system/getty.target.wants/getty@tty8.service`
echo ${tty/wx672/$NormalUser} > /etc/systemd/system/getty.target.wants/getty@tty8.service
log_in=`cat /etc/systemd/logind.conf`
echo ${log_in/#NAutoVTs=6/NAutoVTs=8}
sudo cp ~/dotfile/etc/default/locale /etc/default
sudo cp ~/dotfile/etc/default/keyboard /etc/default
sudo dpkg-reconfigure locales
sudo reboot
```
# Software configure

## xterm: ~/Xresources
xterm*fullscreen: true

```
xterm字体设置
home目录下建.Xresources，内容如下，之后运行xrdb -merge ~/.Xresources，重启xterm
! -*- mode: Conf[Xdefaults];-*-
!!! https://wiki.archlinux.org/index.php/X_resources
!!! run 'xrdb -merge .Xresources' after change

xpdf.paperColor: #f7f4ef
xpdf.matteColor: #f7f4ef
xpdf*background: #f7f4ef

xterm*loginShell: true

!!!font and locale
!xterm*faceName: DejaVu Sans Mono:antialias=True:pixelsize=22
!xterm*boldFont: DejaVu Sans Mono:style=Bold:pixelsize=22
xterm*faceName: Monospace:pixelsize=20
xterm*boldFont: Monospace:pixelsize=20
!xterm*faceNameDoublesize: WenQuanYi Micro Hei Mono
xterm*faceNameDoublesize: Noto Sans Mono CJK SC

! set 'cjkWidth' to true makes aptitude window messy.
!xterm*cjkWidth: true
xterm*locale: true
xterm*utf8: true
!xterm*utf8Title: true
xterm*fontMenu*fontdefault*Label: Default
xterm*xftAntialias: true
xterm*selectToClipboard: true

!!! make url selection better (seems not working)
! http://www.debian-administration.org/article/66/Customizing_your_xterm
xterm*charClass: 33:48,36-47:48,58-59:48,61:48,63-64:48,95:48,126:48

!!!look and feel
xterm*termName: xterm-256color
xterm*ScrollBar: false
xterm*visualBell: false
xterm*fullscreen: never
xterm*borderLess: true
xterm*internalBorder: 0
xterm*externalBorder: 0
xterm*borderWidth: 0


xterm*omitTranslation: fullscreen
! disable alt-enter in xterm, and enable it in emacs.
xterm*metaSendsEscape: true

xterm*allowSendEvents: True
xterm*allowTitleOps: True
xterm*sessionMgt: false

!!! http://sunaku.github.io/zenburn-terminal-color-scheme.html
XTerm*color0: #000d18
XTerm*color1: #e89393
XTerm*color2: #9ece9e
XTerm*color3: #f0dfaf
XTerm*color4: #1f1f1f
! #8cd0d3
XTerm*color5: #c0bed1
XTerm*color6: #dfaf8f
XTerm*color7: #efefef
XTerm*color8: #000d18
XTerm*color9: #e89393
XTerm*color10: #9ece9e
XTerm*color11: #f0dfaf
XTerm*color12: #8cd0d3
XTerm*color13: #c0bed1
XTerm*color14: #dfaf8f
XTerm*color15: #efefef
XTerm*colorBD: #ffcfaf
XTerm*colorIT: #80d4aa
XTerm*colorUL: #ccdc90
XTerm*foreground: #dcdccc
XTerm*background: black
!#1f1f1f
XTerm*cursorColor: #8faf9f

```
# Tip

## 无法启动，进入救援rescue模式

``` bash
ls (hd0,gpt8)
set root=(hd0,gpt8)
set prefix=(hdq,gpt8)/boot/grub
insmod normal
Normal
sudo update-grub
sudo grub-install /dev/sda
```

## 虚拟机全屏（未测试成功）

- Check your current System Resolution (Host System)
- Edit /etc/default/grub (as root)
- Uncomment the line GRUB_GFXMODE=800x600 (Your screen resolution here mine was 1920x1080)
- Save the file
- Execute the command update-grub (as root)
- Reboot (shutdown -r now)
