# -*- coding: utf-8 -*-
import scrapy
from ku137.items import Ku137Item


class Ku137netSpider(scrapy.Spider):
    name = 'ku137net'
    allowed_domains = ['ku137.net']

    def start_requests(self):
        '''首页遍历爬取所有页,间接获取总页数'''
        start_urls = ['https://www.ku137.net/b/1']
        # for i in range(1, 2):
        #     url1 = start_urls[0] + str(i)
        #     yield scrapy.Request(url=url1, callback=self.parse)
        yield scrapy.Request(url=start_urls[0], callback=self.start_requests2)
        # callback=self.parse 可以调用 start_requests2 或者 start_requests3
        # start_requests2 是组装页面 start_requests3 是按照下一页走的


    def start_requests2(self,response):
        url2 = 'https://www.ku137.net/b/1/list_1_'
        getnumber = response.css('body  div.list  div.w1200  div.page  span.pageinfo  strong::text').get()
        for i in range(1, int(getnumber)+1):
            url1 = url2 + str(i) + '.html'
            self.log('url is %s' % url1)
            yield scrapy.Request(url=url1, callback=self.parse)

    # def start_requests3(self,response):
    #     url2 = response.url
    #     self.log('url is %s' % url2)
    #     yield scrapy.Request(url=url2, callback=self.parse)
    #
    #     next_page =response.css('body  div.list  div.w1200  div.page  a::attr(href)')[-2].get() # get()
    #     #self.log('url is %s' % response.url)
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         # self.log('url is %s' % next_page)
    #         yield response.follow(next_page, self.start_requests3)


    def parse(self, response):
        '''进入到具体页面'''
        urltemp = response.css('body  div.list  div.w1200  div.l-pub  div  ul  li  a::attr(href)').getall()
        for i in urltemp:
            yield scrapy.Request(url=i, callback=self.parse2)

    def parse2(self, response):
        '''爬取当前页面的具体图片'''
        item = Ku137Item()
        item['imgtitle'] = response.css('head  title::text').get()
        item['page'] = response.url
        imgurltemp = response.css('body  div.content  img::attr(src)').getall()
        for i in imgurltemp:
            item['imgurl'] = [i]
            item['imgname'] = i.split('/')[-1]
            yield item

        next_page =response.css('body   div.page  a::attr(href)')[-1].get() # get()
        # self.log('url is %s' % response.url)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            # self.log('url is %s' % next_page)
            yield response.follow(next_page, self.parse2)
