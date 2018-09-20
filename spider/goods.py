# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
from webdriver import driver_init
from parse.goods import item_from_url
from settings import crawl_url
import time


def crawl_item(name, link, driver_singleton):
    """
    爬取单项商品
    :param name: 商品列表的名字
    :param link: 商品列表的首页url
    :param driver_singleton: browser对象实例
    :return:
    """
    if link == "https://zhizhizhi.com/":
        time.sleep(13)
    for i in range(1, 33):
        # link: https://zhizhizhi.com/new/  ->  https://zhizhizhi.com/new/page/i
        items = item_from_url("{}page/{}/".format(link, i), driver_singleton, name)
        if items is not []:
            print(items)
    driver_singleton.close()


def crawl_goods():
    """
    循环遍历爬取链接爬取商品
    :return:
    """
    for url_name in crawl_url:
        driver = driver_init()
        crawl_item(url_name, crawl_url[url_name], driver)
