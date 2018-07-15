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
