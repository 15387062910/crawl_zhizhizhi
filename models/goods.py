# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
from . import Model


class RecommendItem(Model):
    """
    存储推荐商品的基本信息
    """
    def __init__(self):
        """
        title -> 商品标题
        detail_url -> 商品详情页链接
        money -> 商品价格
        abstract -> 描述信息
        """
        self.title = ''
        self.detail_url = ''
        self.money = ''
        self.abstract = ''


class DetailInfo(Model):
    """
    存储推荐商品的详细信息
    """
    def __init__(self):
        """
        classification -> 商品分类
        special_link -> 特价直达链接
        title -> 商品标题
        money -> 商品价格
        description -> 商品描述
        img_url -> 商品图片链接
        buy_url -> 商品购买链接
        post_list -> 相关商品推荐
        """
        self.classification = ''
        self.special_link = ''
        self.title = ''
        self.money = ''
        self.description = ''
        self.img_url = ''
        self.buy_url = ''
        self.post_list = ''

