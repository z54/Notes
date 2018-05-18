# Install

## Download

- [JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
- [Android Studio](https://developer.android.com/studio/)

# config

## JDK

1. install，默认安装位置 `C:\Program Files\Java\jdk-*.*.*`
2. path 
    - `此电脑-属性-高级系统设置-环境变量`
        \ | \   
        - | -
        新建JAVA_HOME | `C:\Program Files\Java\jdk-9.0.4`
        追加PATH      | `;%JAVA_HOME%\bin`
    -  
    ```
    set PATH=C:\jdk1.6.0_15\bin;%PATH%
    set JAVA_HOME=C:\jdk1.6.0_15
    ```
    
## SDK

- 打开Android Studio后并新建项目，完成后直接点击运行，软件自动下载需求的插件**不需要设置代理**
- ~~代理设置方式为http，地址127.0.0.1，端口1080；~~
- ~~若下载过慢则复制下载链接到浏览器，下载完毕根据Sdk内同名文件夹位置复制入。~~

## AVD

- 打开AVD-选择机型-下载系统版本-启动

# run

1. 启动AVD
2. 启动项目并选择虚拟机