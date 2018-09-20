# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
import os
from settings import cached_path


def cached_url(url, driver, cached_name):
    """
    缓存, 避免重复下载网页浪费时间
    :param url: 商品列表页中一页的url
    :param driver: 浏览器驱动
    :param cached_name: 缓存页面的文件夹名
    """
    filename = url.rsplit('/')[-2] + '.html'
    folder = os.path.join(cached_path, cached_name)
    path = os.path.join(cached_path, cached_name, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        # 建立 cached 文件夹
        if not os.path.exists(folder):
            os.makedirs(folder)

        driver.get(url)
        # print(driver.page_source)
        with open(path, 'wb') as f:
            f.write(driver.page_source.encode())
        content = driver.page_source
        return content


