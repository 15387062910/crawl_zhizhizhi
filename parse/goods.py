# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
import re
from pyquery import PyQuery as pq
from models.goods import RecommendItem, DetailInfo
from spider.basic_crawl import cached_url


def html_from_url(url, driver, cached_name):
    """
    从 url 中下载网页(已经缓存的不用再下载)
    :param url: 页面链接
    :param driver: 浏览器驱动
    :param cached_name: 缓存页面的文件夹名
    :return:
    """
    page = cached_url(url, driver, cached_name)
    return page


def item_from_div(div):
    """
    从一个 div 里面获取到一个商品信息
    :param div: 商品item的div
    :return:
    """
    e = pq(div)
    """
        title -> 商品标题
        detail_url -> 商品详情页链接
        money -> 商品价格
        abstract -> 描述信息
    """
    # 小作用域变量用单字符
    m = RecommendItem()
    m.title = e(".title_box").text().split(sep="\n")[0]
    m.money = e('.dprice').text()
    m.abstract = e(".excerpt_text").text()
    # 获取详情页链接:
    try:
        m.detail_url = re.findall('href="(.*?)"', e(".title_box").html())[0]
    except Exception as e:
        pass
    m.save()
    return m


def item_from_url(url, driver, cached_name):
    """
    从 url 中下载网页并解析出页面内所有的商品item
    :param url: 商品列表页中一页的url
    :param driver: 浏览器驱动
    :param cached_name: 缓存页面的文件夹名
    :return:
    """
    page = html_from_url(url, driver, cached_name)
    e = pq(page)
    items = e(".post_item")
    return [item_from_div(i) for i in items]


def detail_from_html(url, driver, cached_name):
    """
    从商品详情页中获取商品详细信息
    :param url: 商品详情页的hurl
    :param driver: 浏览器驱动
    :param cached_name: 缓存页面的文件夹名
    :return:
    """
    # todo: 待完成商品详细信息的解析工作
    html = html_from_url(url, driver, cached_name)
    e = pq(html)
    """
    title -> 商品标题
    money -> 商品价格
    buy_url -> 商品购买链接
    post_list -> 相关商品推荐
    """
    d = DetailInfo()

    d.classification = ''
    d.special_link = ''
    d.title = ''
    d.money = ''
    d.description = ''
    d.img_url = ''
    d.buy_url = ''
    d.post_list = e(".postlist").html()
    # d.save()

    return d

