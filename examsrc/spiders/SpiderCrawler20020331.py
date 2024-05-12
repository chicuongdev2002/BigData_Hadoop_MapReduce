import scrapy
from examsrc.items import examsrcItem

class Spider20020331(scrapy.Spider):
    name = "20020331AppCrawler"
    allowed_domains = ["books.toscrape.com"]

    fromPage = 5
    toPage = 15

    def start_requests(self):
        # Mã nguồn này đang cào dữ liệu từ trang 1 đến trang 10
        for page in range(self.fromPage,self.toPage+1):
            yield scrapy.Request(url='https://books.toscrape.com/catalogue/page-{page_num}.html'.format(page_num=page), callback=self.getBookURL20020331)

    # Lấy danh sách các URL của các quyển sách   
    def getBookURL20020331(self, response):
        bookURLs =  response.xpath('//div[@class="image_container"]//a/@href').getall()
        for bookUrl in bookURLs:
            request = scrapy.Request(url = response.urljoin(bookUrl), callback=self.getBookDetail20020331)
            yield request
    
    # Lấy thông tin từng quyển sách
    def getBookDetail20020331(self, response):
        item = examsrcItem()
        item['title20020331'] = response.xpath('normalize-space(string(/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]))').get()
        item['genre20020331'] = response.xpath('//table//tr[1]/td/text()').get()
        item['type20020331'] = response.xpath('//table//tr[2]/td/text()').get()
        item['priceex20020331'] = response.xpath('//table//tr[3]/td/text()').get().replace('£','')
        item['pricein20020331'] = response.xpath('//table//tr[4]/td/text()').get().replace('£','')
        item['tax20020331'] = response.xpath('//table//tr[5]/td/text()').get()
        item['ava20020331'] = response.xpath('//table//tr[6]/td/text()').get()
        item['review20020331'] = response.xpath('//table//tr[7]/td/text()').get() 
        yield item