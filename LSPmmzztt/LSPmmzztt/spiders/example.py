import scrapy
import time


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["mmzztt.com"]
    start_urls = ["https://mmzztt.com/photo/"]

    def start_requests(self):
        # 发起请求时使用自定义的User-Agent
        for index in range(1, 2):
            yield scrapy.Request(url='https://mmzztt.com/photo/page/{0}/'.format(index), callback=self.parse)
        # yield scrapy.Request(url='https://mmzztt.com/photo/', callback=self.parse)

    def parse(self, response):
        print(1)
        time.sleep(1)
        urls = response.xpath('/html/body/section/div/div/main/ul/li/div/div[2]/a/@href').extract()
        print(urls)
        for url in urls:
            yield scrapy.Request(url, self.one)
        # yield scrapy.Request(urls[0], self.one)

    def one(self, response):

        try:
            num = response.xpath('/html/head/link[1]/@href').extract()[0][-5:]
            url = response.xpath('/html/body/section[1]/div/div/main/article/figure/img/@src').extract()[0][:28]
            print(1)
            time.sleep(1)
            print(num, url)

            yield scrapy.Request('https://mmzztt.com/app/post/p?id={0}'.format(num), self.two, meta={'url': url, 'num': num})
        except:
            print('error')

    def two(self, response):
        try:
            print(response.status_code)
        except:
            print('errortwo')
        time.sleep(1)
        data = {}
        data['num'] = response.meta.get('num')
        data['url'] = response.meta.get('url')
        data['data'] = response.json()['data']
        print(data)
        yield data

