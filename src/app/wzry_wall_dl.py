# -*- coding: utf-8 -*-

"""
created by：2018-1-14 11:38:2
modify by: 2018-1-31 18:27:47

功能：王者荣耀壁纸下载
"""

import sys
import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

from src.comm.app_config import *
from src.comm.utils import Utils
from src.comm.logging_util import LoggingFileHandler

class WzrzWallDL:
    """
    王者荣耀壁纸下载
    """

    def __init__(self):
        self.conf_path = os.path.join(os.getcwd(), "res/conf/config.json")

        if os.path.isfile(self.conf_path):
            conf_json_info = Utils.load_json_file(self.conf_path)
            print("OK: The config file is %s !!!" % (self.conf_path))
            self.url = conf_json_info["config"]["url"]
            self.max_page_number = conf_json_info["config"]["max_page_number"]
            self.download_path = conf_json_info["config"]["download_path"]
            self.images_resolution = conf_json_info["config"]["images_resolution"]
            logfile_path = conf_json_info["config"]["logfile_path"]
            program_name = conf_json_info["config"]["program_name"]
        else:
            print("Unkown: The config file %s is not exit!!!" % (self.conf_path))
            sys.exit(1)

        self.logger_handle = LoggingFileHandler.timed_rotating_file_handler(logfile_path,
                            program_name, log_encoding="utf-8")

    def wzrz_wall_dl(self):
        # 获得浏览器的session，浏览器用Firefox、Chrome、IE等都可以
        # driver = webdriver.Chrome()
        driver = webdriver.PhantomJS()
        # 浏览器全屏显示
        driver.maximize_window()
        # 加载页面
        driver.get(self.url)
        """
        # 获得了session对象后，要定位元素，webdriver提供了一系列的元素定位方法，常用的有以下几种方式:
        # id, name, class-name, link, text, partial, link, text, tag, name, xpath, cssselector
        """
        move_element = driver.find_element_by_xpath('//a[@title="游戏资料"]')

        """
        # 当你调用ActionChains的方法时，不会立即执行，而是会将所有的操作按顺序存放在一个队列里，当你调用perform()方法时，队列中的时间会依次执行。
        # move_to_element(to_element) —— 鼠标移动到某个元素
        # click(on_element=None) —— 单击鼠标左键
        """
        ActionChains(driver).move_to_element(move_element).perform()

        driver.find_element_by_xpath('//a[@title="游戏壁纸"]').click()
        # 获取所有的窗口
        all_handles = driver.window_handles
        # 跳入窗口
        driver.switch_to.window(all_handles[1])
        time.sleep(3)

        if os.path.isdir(self.download_path):
            os.chdir(self.download_path)
        else:
            os.mkdir(self.download_path)
            os.chdir(self.download_path)

        # 初始页数
        page_num = 0

        if self.images_resolution in images_resolution_list:
            dl_images_resolution = images_resolution_list[self.images_resolution]
        else:
            self.logger_handle.error("The images_size: %s is not exits!!!", self.images_resolution)
            driver.close()
            sys.exit(1)

        while page_num <= self.max_page_number:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            newhero_item_lists = soup.find_all('div', {'class': 'p_newhero_item'})

            title_lists = []
            href_lists = []
            span_size_list = []

            for item in newhero_item_lists:
                sub_soup = BeautifulSoup(str(item), 'html.parser')
                title_list = sub_soup.find('h4')
                title_lists.append(title_list.text)
                link_list = sub_soup.find('li', {'class': dl_images_resolution})
                soup = BeautifulSoup(str(link_list), 'html.parser')
                a = soup.find('a')
                href_lists.append(a['href'])
                span_size_list.append(soup.span.string)

            for (i, x) in enumerate(title_lists):
                url = href_lists[i]
                rep = requests.get(url).content
                path = title_lists[i] + "_" + span_size_list[i] + '.jpg'
                try:
                    with open(path, 'wb') as imgage_file:
                        imgage_file.write(rep)
                except IOError as err:
                    self.logger_handle.error('保存失败 : %s', err)
                    self.logger_handle.error("The download url: %s , The filename: %s ", url, path)
                else:
                    self.logger_handle.info('保存成功 %s.jpg', title_lists[i])
                    self.logger_handle.info("The download url: %s , The filename: %s ", url, path)

            driver.find_element_by_xpath('//a[@class="downpage"]').click()
            time.sleep(3)
            page_num = page_num + 1

        # 当执行完抓取操作后，必须关闭session，不然让它一直占内存会影响机器其他进程的运行
        driver.close()
        print("OK: 运行完成，程序已经关闭!!!")
