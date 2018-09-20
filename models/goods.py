# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
from . import Model


class RecommendItem(Model):
    """
    存储推荐商品信息
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



