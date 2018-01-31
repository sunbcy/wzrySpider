########################################################
#        Program to Download Wallpapers from           #
#     http://pvp.qq.com/web201605/wallpaper.shtml      #
#                                                      #
#                 Author - CQ                          #
#                                                      #
#                 dated - 2018-1-8 14:28:52            #
#                 Update - 2018-1-8 14:28:57           #
########################################################

import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests

driver = webdriver.PhantomJS()
driver.maximize_window()

url = 'http://pvp.qq.com/'
driver.get(url)
moveElement = driver.find_element_by_xpath('//a[@title="游戏资料"]')
ActionChains(driver).move_to_element(moveElement).perform()
driver.find_element_by_xpath('//a[@title="游戏壁纸"]').click()
all_h = driver.window_handles
print(all_h)
driver.switch_to.window(all_h[1])
time.sleep(3)

if os.path.isdir("D://王者荣耀"):
    os.chdir("D://王者荣耀")
else:
    os.mkdir("D://王者荣耀")
    os.chdir("D://王者荣耀")

page_num = 0

while page_num < 12:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    Lists = soup.find_all('div', {'class': 'p_newhero_item'})
    titleLists = []
    hrefLists = []
    for item in Lists:
        subSoup = BeautifulSoup(str(item), 'html.parser')
        titleList = subSoup.find('h4')
        titleLists.append(titleList.text)
        linkList = subSoup.find('li', {'class': 'sProdImgL6'})
        soup = BeautifulSoup(str(linkList), 'html.parser')
        a = soup.find('a')
        hrefLists.append(a['href'])

    for i in range(len(titleLists)):
        url = hrefLists[i]
        r = requests.get(url).content
        path = titleLists[i] + '.jpg'
        try:
            with open(path, 'wb') as f:
                f.write(r)
                print('保存成功 %s.jpg' % titleLists[i])
        except BaseException:
            print('保存失败')

    driver.find_element_by_xpath('//a[@class="downpage"]').click()
    time.sleep(3)
    page_num = page_num + 1
    print(page_num)
driver.close()
