# encoding: utf-8
# __author__ = "wyb"
# date: 2018/9/7
# 项目的配置文件


# 设置路径
cached_path = "cached"
img_path = "img"
data_path = "data"


# 设置爬取的链接
# 热门特价、最新特价、今日热榜、国内优惠
crawl_url = {
    "hot_special": "https://zhizhizhi.com/",
    "new_special": "https://zhizhizhi.com/new/",
    "today_hot": "https://zhizhizhi.com/hot/today/",
    "domestic_discount": "https://zhizhizhi.com/d/cn/",
}

# for url_name in crawl_url:
#     print(url_name, crawl_url[url_name])


# 设置请求头
headers = {
    'user-agent': '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
}

