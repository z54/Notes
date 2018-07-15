# 6.1.3 fatal

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
