# crawl_js

### 项目目的
    爬取https://zhizhizhi.com/这个网站的热门特价、最新特价、今日热榜、国内优惠

### 项目基本原理
    请求库: 模拟浏览器 -> Chrome+selenium
    解析库: pyquery
        
    项目逻辑结构如下:
    1. crawl: Downloader 下载页面 or 图片   Chromr+selenium      
    2. parse: HTMLParser 解析页面           pyquery     lxml   (注: pyquery的用法类似前端中的CSS选择器)
    3. model: DataModel 字段 - element     业务逻辑 (自己做一个model)
    
    www.zhizhi.com的api是/page/{} -> 获取数据

### 项目结构
* cached 缓存页面
* models 数据类定义
* parse  项目数据解析
* spider 下载页面以及爬取逻辑
* webdriver 模拟浏览器
* run.py 项目入口文件
* settings.py 项目配置文件

### 项目说明
    该项目的爬取本质:
        https://zhizhizhi.com/这个网站页码都是由js生成的，所以爬取这个网站实际上是在爬取js生成的页面
    安装相关包及插件:
        安装selenium: pip3 install selenium
        安装chrome 并安装相应插件: https://blog.csdn.net/qq_15158911/article/details/72403832
        注: 当然你也可以把selenium改成用firefox浏览器启动(听说简单方便，不需要额外去安装driver驱动)
        安装pyquery: pip3 install pyquery
    运行:
        直接运行项目根目录下的run.py即可