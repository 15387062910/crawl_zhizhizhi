# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
from selenium import webdriver


def driver_init():
    """
    初始化browser对象
    :return: browser对象
    """
    driver = webdriver.Chrome()
    return driver


