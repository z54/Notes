# 多屏设置
	xrandr --output HDMI-2 --same-as eDP-1
	Xrandr命令查看当前了了连接的所有显示器
	看到如下输出
		DVI-I-0 disconnected
		VGA-0 connected
		DVI-I-1 connected
		HDMI-0 disconnected
	选择状态为connected的
		1. 关闭指定显示器：xrandr --output VGA-0 --off
		2. 设置指定显示器的分辨率：xrandr --output DVI-I-1 --mode 1680x1050
		3. 让指定显示器自动选择分辨率与屏幕位置：xrandr --output DVI-I-1 --auto
		4. 使用扩展模式
			1. 设置指定显示器为主屏幕：xrandr --output DVI-I-1 --primary
			2. 设置多个显示器之间的相对位置：xrandr --output DVI-I-1 --left-of VGA-0
		5. 使用同步显示模式：xrandr --output DVI-I-1 --same-as VGA-0
	如何用Linux外接显示器或投影仪 - 皮波迪 - 博客园
	
# 快捷键

## 自定义快捷键方法

