# linux

# command
## aptitude

- 命令行
/ |/
-|-
更新可用的包列表 | `aptitude update`
升级可用的包 | `aptitude upgrade`
将系统升级到新的发行版 | `aptitude dist-upgrade`
安装包 | `aptitude install pkgname`
删除包 | `aptitude remove pkgname`
删除包及其配置文件 | `aptitude purge pkgname`
搜索包 | `aptitude search string`
显示包的详细信息 | `aptitude show pkgname`
删除下载的包文件 | `aptitude clean`
仅删除过期的包文件 | `aptitude autoclean`

- 图形(ing)
/ |/
-|-

## find

## 压缩

- 解压
`tar -xvf file.tar`
解压 tar包

- 压缩
`tar -cvf jpg.tar *.jpg`
将目录里所有jpg文件打包成tar.jpg

Linux下的tar压缩解压缩命令详解 - 码农一只 - 博客园
https://www.cnblogs.com/manong--/p/8012324.html

# Reference
[linux下用aptitude管理软件包 - CSDN博客](https://blog.csdn.net/hongkangwl/article/details/16113505)
