# -*- coding: utf-8 -*-

"""
created by：2017-05-10 20:11:31
modify by: 2018-1-16 10:39:45

功能：各种常用的方法函数的封装。
"""

import os
import json


class Utils:
    """util, 工具类

    Attributes:

    """

    @staticmethod
    def rename_file(oldfile, newfile):
        """文件重命名

        参数:

            oldfile：旧文件名；string。
            newfile：新文件名;string。
        """
        if not os.path.isfile(newfile):
            os.rename(oldfile, newfile)

    @classmethod
    def get_path_of_file(cls, dir_path):
        """遍历文件夹, 返回所有文件list(不含有文件夹)"""
        if os.path.exists(dir_path):
            file_path_list = []
            for root, dirs, files in os.walk(dir_path):
                file_path_list.extend(os.path.join(root, file) for file in files)
            return file_path_list
        else:
            print("This path %s does not exist!" % (dir_path))

    @classmethod
    def get_listdir(cls, dir_path):
        """遍历文件夹,单层"""
        if os.path.exists(dir_path):
            value_list = os.listdir(dir_path)
            return value_list
        else:
            print("This path %s does not exist!" % (dir_path))

    @staticmethod
    def load_json_file(json_file):
        """加载json文件"""
        with open(json_file, "r", encoding="utf8")  as frs:
            res = json.load(frs)
        return res

    @classmethod
    def dump_json_file(cls, data, json_file, ensure_ascii=False):
        """写入数据json文件"""
        if data is not None:
            res = json.dumps(data, ensure_ascii=ensure_ascii)
            with open(json_file, "w", encoding="utf8")  as fws:
                fws.write(res)
        else:
            print("This json data is None")

    @staticmethod
    def get_json_value(json_file, key):
        """根据key获取json文件中的value"""
        with open(json_file, "r", encoding="utf8")  as frs:
            res = json.load(frs)
        if key in res:
            return res[key]

    @staticmethod
    def set_json_value(json_file, key, value):
        """根据key设置json文件中的value"""
        with open(json_file, "r", encoding="utf8")  as frs:
            res = json.load(frs)
        res[key] = value
        result = json.dumps(res, indent=4, sort_keys=True, ensure_ascii=False).replace("'", "\"")
        with open(json_file, "r", encoding="utf8")  as fws:
            fws.write(result)
