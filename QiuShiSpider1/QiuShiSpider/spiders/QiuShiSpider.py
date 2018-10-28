#coding:utf-8

import scrapy
from QiuShiSpider.items import QiushispiderItem
import time
from scrapy_redis.spiders import RedisSpider

class QiuShi(RedisSpider):
    name = "qiushi"

    allowed_domains = [
        "qiushibaike.com"
    ]

    # start_urls = [
    #     "https://www.qiushibaike.com/pic/"
    # ]

    def parse(self,response):
        """
        获取页面链接
        :param response:
        :return:
        """
        page_list = response.xpath('//ul[@class="pagination"]/li/a/@href')
        last_num = page_list[-2].extract()
        num = int(last_num.rsplit("?",1)[0].rsplit("/",1)[1])
        pRange = range(1,num+1)
        for page in pRange:
            page_url = "https://www.qiushibaike.com"+last_num.replace(str(num),str(page))
            yield scrapy.Request(page_url,callback=self.get_img,dont_filter=True)
            #这里用scrapy请求得到的地址，我们将地址以回调函数的形式传递给了self.get_img，
            # 在这里dont_filter 代表对重复的url不进行过滤
            time.sleep(2)
    def get_img(self,response):
        """
        获取指定页面的所有图片链接
        :param response:
        :return:
        """
        img_src_list = response.xpath('//div[@id="content-left"]//img/@src')
        for img_src in img_src_list:
            src = img_src.extract()
            qiushi = QiushispiderItem()
            qiushi["src"] = src
            yield qiushi


