# **wzrySpider**

## **Basic Requirements**

### ***Python versions***

应该安装好Python(v3.4.3或者更高，可以使用Python -V来确认)。

### ***Install PhantomJS***

PhantomJS安装方法有两种，一种是下载源码之后自己来编译，另一种是直接下载编译好的二进制文件。然而自己编译需要的时间太长，而且需要挺多的磁盘空间。官方推荐直接下载二进制文件然后安装。

大家可以依照自己的开发平台选择不同的包进行下载

[下载地址](http://phantomjs.org/download.html)

当然如果你不嫌麻烦，可以选择

[下载源码](http://phantomjs.org/build.html)

### ***Install webdriver(可选)***

PhantomJS是一个无头浏览器，没有UI界面，所以建议再下一个火狐驱动或者谷歌驱动，这样你可以看到页面的跳转等具体是一个什么样子。

- Firefox的驱动geckodriver 下载地址：

    <https://github.com/mozilla/geckodriver/releases/>

- chromium的驱动chromedriver 下载地址:

    <https://sites.google.com/a/chromium.org/chromedriver/downloads>

### ***Using Python module:***

***方法一：***

- [selenium](www.seleniumhq.org)

        $ pip install selenium

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

        $ pip install beautifulsoup4

- [requests](www.python-requests.org)

        $ pip install requests

***方法二：***

如果你已经安装好pipenv,那么可以直接在项目下面执行(可选：

    $ pipenv install
    $ pipenv shell

***方法三：***

项目下有requirements.txt文件，因此可以直接：

    $ pip install -r requirements.txt

## **Run program**

    $ python3 main.py

## **BUGS**

- 有四张照片会被爬取很多遍，这是网页决定的，可以选择链接去重，因为相同名字的图片会被覆盖，所以这里就没有去管