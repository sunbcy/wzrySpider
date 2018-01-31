# **Readme**

## **Basic Requirements**

### ***Install PhantomJS***

PhantomJS安装方法有两种，一种是下载源码之后自己来编译，另一种是直接下载编译好的二进制文件。然而自己编译需要的时间太长，而且需要挺多的磁盘空间。官方推荐直接下载二进制文件然后安装。

大家可以依照自己的开发平台选择不同的包进行下载

[下载地址](http://phantomjs.org/download.html)

当然如果你不嫌麻烦，可以选择

[下载源码](http://phantomjs.org/build.html)

### ***Install webdriver(可选)***

PhantomJS是一个无头浏览器，没有UI界面，所以我推荐可以再下一个火狐驱动或者谷歌驱动，这样你可以看到页面的跳转等具体是一个什么样子。

- Firefox的驱动geckodriver 下载地址：

    <https://github.com/mozilla/geckodriver/releases/>

- chromium的驱动chromedriver 下载地址:

    <https://sites.google.com/a/chromium.org/chromedriver/downloads>

### ***Using Python module:***

- [selenium](www.seleniumhq.org)

        $ pip install selenium

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

        $ pip install beautifulsoup4

- [requests](www.python-requests.org)

        $ pip install requests

## **Run program**

    $ python3 main.py

## **BUGS**

- 有四张照片会被爬取很多遍，这是网页决定的，可以选择链接去重，因为相同名字的图片会被覆盖，所以这里就没有去管