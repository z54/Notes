# example
- 抓取百度首页
    ``` python
    # python 2.x
    import urllib2

    response = urllib2.urlopen("http://www.baidu.com")
    print response.read()
    ```

    ``` python
    # python 2.x
    import urllib2

    request = urllib2.Request("http://www.baidu.com")
    response = urllib2.urlopen(request)
    print response.read()
    ```

- 抓取京东金融一级目录名称
    ``` python
    # python 3.x
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen('http://jr.jd.com')
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    text_list = bs_obj.find_all("a", "nav-item-primary")
    for text in text_list:
        print(text.get_text())
    html.close()
    ```
