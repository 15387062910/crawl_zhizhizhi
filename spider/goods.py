# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
from webdriver import driver_init
from parse.goods import item_from_url, detail_from_html
from settings import crawl_url
import time


def crawl_item(name, link, driver_singleton):
    """
    爬取单项商品的基础信息和详细信息
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
        print(items)
        for item in items:
            # 爬取商品的详细信息
            # todo - 待完成: 爬取商品的详细信息
            item_url = item.detail_url
            if item_url:
                details = detail_from_html(item_url, driver_singleton, name + "_details")
                print(details)
    driver_singleton.close()


def crawl_goods():
    """
    循环遍历爬取链接爬取商品的基础信息和详细信息
    :return:
    """
    for url_name in crawl_url:
        driver = driver_init()
        try:
            crawl_item(url_name, crawl_url[url_name], driver)
        except Exception as e:
            print(e)
            print("something error happen!")