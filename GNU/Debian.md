# Install

1. Debian GNU/Linux installer boot menu
    - `Installer`
2. Select a language
    - English
3. Select your location
    - other -> Asia -> China
4. Configure locales
    - United States - en_US.UTF-8
5. Configure the keyboard
    - American English

	**disconnect the network**

6. configure the network
    - Hostname: debian
7. Set up users and passwords
    - Root password: 1
    - Re-enter password to verify: 1
    - Full name for the new user: zach
    - Username for your account: zach
    - Choose a password for the new user: 1
    - Re-enter password to verify: 1
8. Parition disks
    - Partitioning method: Guided - use entire disk and set up lvm
    - Select disk to parition: SCSI1 (0,0,0) (sda) - 21.5 GB VMware, VMware Virtual S
    - Partitioning scheme: Separate /home partition
    - Write the changes to disk s and configure LVM? Yes
    - Finish patitioning and write changes to disk
    - Write the changes to disks? Yes
9. Configure the package manager
    - No
    - Continue without a network mirror? Yes
10.  Configuring popularity-contest
    - No
11.  Software selection
    - Null
12.  Install the GRUB boot loader on a hard disk
    - Install the GRUB loader to the mastaer boot record? Yes
    - Device for boot loader installation: /dev/sda
13.  Finish the installation
    - Continue

# Initial Config

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
 echo -e User_Alias      NORMAL = $NormalUser"\n"NORMAL  ALL = NOPASSWD: ALL > /etc/sudoers.d/$NormalUser && chmod 0440 /etc/sudoers.d/$NormalUser
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

# Tip

- 无法启动，进入救援rescue模式

``` bash
ls (hd0,gpt8)
set root=(hd0,gpt8)
set prefix=(hdq,gpt8)/boot/grub
insmod normal
Normal
sudo update-grub
sudo grub-install /dev/sda
```
