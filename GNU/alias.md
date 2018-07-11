# location

`/home/username/.bashrc`

# alias

```bash
#thesis
alias src='cd /home/sunforx/mount/f/Documents/OS/Graduation/ZOS/src'
alias tssmake='cd /home/sunforx/thesis && make'
alias tssbk='cp /home/sunforx/thesis/zach.tex /home/sunforx/mount/f/Documents/OS/Graduation/Thesis && cp /home/sunforx/thesis/thesis.bib /home/sunforx/mount/f/Documents/OS/Graduation/Thesis'
alias tssre='cp /home/sunforx/mount/f/Documents/OS/Graduation/Thesis/zach.tex /home/sunforx/thesis && cp /home/sunforx/mount/f/Documents/OS/Graduation/Thesis/thesis.bib /home/sunforx/thesis'
#self
alias gw='gcc -Wall'
alias sss='ss-local -v -c /etc/shadowsocks/config.json'
alias ess='sudo vi /etc/shadowsocks/config.json'
alias sn='sudo poweroff'
alias upup='sudo apt-get update && sudo apt-get upgrade'
#alias dh='sudo dhclient eth0'
alias os='cd /home/sunforx/Documents/os'
#alias os4='cd /usr/src/linux-source-4.5'
#alias os2='cd /usr/src/linux-2.6.17'
alias al='vi /home/sunforx/.bash_aliases && source /home/sunforx/.bash_aliases'
alias re='reboot'
alias to='synclient touchpadoff=1'
alias tl='synclient touchpadoff=0'
alias lo='xbacklight +10'
alias ld='xbacklight -10'
alias ve='. ~/venv/bin/activate'
alias gc='git checkout'
#alias flasky='cd /home/sunforx/Documents/flasky'
alias em='emacsclient -nc'
alias usb='sudo mount /dev/sdb1 /home/sunforx/mount/usb && cd ~/mount/usb'
alias wdc='sudo mount /dev/sda4 /home/sunforx/mount/c && cd ~/mount/c'
alias wdd='sudo mount /dev/sda5 /home/sunforx/mount/d && cd ~/mount/d'
alias wde='sudo mount /dev/sda6 /home/sunforx/mount/e && cd ~/mount/e'
alias wdf='sudo mount /dev/sda7 /home/sunforx/mount/f && cd ~/mount/f'
alias wifi='sudo nmtui'
alias st='sudo hwclock --hctosys'
alias li='sudo tee /sys/class/backlight/intel_backlight/brightness <<< 1000'
alias pb='ping baidu.com'
alias power='`acpi -b | grep -P -o "[0-9]+(?=%)" | head -n 1'
#

alias ls='/bin/ls --color=auto -F'
alias rm='/bin/rm -i'
alias cp='/bin/cp -i'
alias mv='/bin/mv -i'
alias zathura='zathura --fork 2>/dev/null'
alias sm='sm -n Purisa'
alias toilet='toilet --gay --font future'
alias blame='systemd-analyze blame | head'
alias cs2='xterm -e mosh cs2 &'
alias cs2ssh='xterm -e ssh -XC cs2 &'
alias cs3='xterm -e mosh cs3 &'
alias cs3ssh='xterm -e ssh -XC cs3 &'
alias wget='wget -c --no-check-certificate'
alias espeak='espeak -s 120 -v mb-us1'
#alias screencapture='avconv -f x11grab -s 1366x768 -i :0.0+0,0 -vf scale=w=1280:h=720 -vcodec libx264 -pre lossless_ultrafast -threads 0 /tmp/screen.mkv'
alias screencapture='ffmpeg -video_size 1366x768 -framerate 25 -f x11grab -i :0.0+0,0 screen.mp4'
alias grep='grep --color=auto'
alias Date='date +%Y%m%d%H%M'
alias impressive='/usr/bin/impressive --windowed -c memory --clock -M --nologo'
alias xcompmgr='xcompmgr -CcfF -I-.02 -O-.04 -D0001 -t-5 -l-5 -r4.2 -o.82'
#docs
alias sdf='ssh tty.sdf.org'
```