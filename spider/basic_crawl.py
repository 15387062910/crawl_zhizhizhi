# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
import os
import requests
from settings import cached_path, img_path, headers


def download_image(url, floder_name, img_name):
    """
    下载图片到指定的文件夹下
    :param url: 图片网址
    :param floder_name: 图片存储的子文件夹名
    :param img_name: 图片名字
    :return:
    """
    # folder_path: 图片存储路径   img_name: 图片存储文件名   img_path_detail: 图片存储具体地址
    folder_path = os.path.join(img_path, floder_name)
    img_name = img_name + ".jpg"
    img_path_detail = os.path.join(img_path, floder_name, img_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if os.path.exists(img_path_detail):
        return

    # 如果url不为None发送网络请求, 把结果写入到文件夹中
    if url:
        r = requests.get(url, headers)
        # print(img_path)
        with open(img_path_detail, 'wb') as f:
            f.write(r.content)


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


