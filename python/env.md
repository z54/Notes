# env

## PATH

`C:\Users\sun\.windows-build-tools\python27\`
`C:\Users\sun\AppData\Local\Programs\Python\Python36-32`

## env

- Debian

系统自带python2.7，配置环境以安装扩展模块

`sudo apt-get install python-pip python-dev`

- Windows

[Download Python | Python.org](https://www.python.org/downloads/)

下载版本2.7，安装完成点选`pip`和`Add python.exe to Path`

## Extra

### usage

1. usage 1

    1. 下载包，解压，进入文件夹

    2. `python setup.py install`

2. usage 2

    - `pip install package_name`

### package

- bs4 ( beautifulsoup ) : 从HTML或XML文件中提取数据

    - install

        [Beautiful Soup: We called him Tortoise because he taught us.](https://www.crummy.com/software/BeautifulSoup/)

        `python setup.py install`

        或

        `pip install bs4`

    - check

    `from bs4 import BeautifulSoup`

- request

    - install

        [Requests: HTTP for Humans — Requests 2.19.0 documentation](http://docs.python-requests.org/en/latest/)

        `python setup.py install`

        或

        `pip install requests`

    - check

        `import requests`

- tools

    2to3.py
