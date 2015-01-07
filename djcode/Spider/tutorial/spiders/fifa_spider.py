import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import FIFAItem

class FIFASpider(CrawlSpider):
    name = "FIFA"
    allowed_domains = ["fifa.com"]
    start_urls = [
        "http://www.fifa.com/worldcup/news/all-news.html"
    ]

    rules = (
        #news
        Rule(SgmlLinkExtractor(allow = (r"/worldcup/news/library/edition2014/all-news,page=[0-9]+.htmx"), attrs = "data-attr")),
        Rule(SgmlLinkExtractor(allow = (r"/worldcup/news/", ), deny = (r"worldcup/news/all-news(?!page)", r"http://www.fifa.com/worldcup/news/index.html")), callback = "parse_newsV1"),
        Rule(SgmlLinkExtractor(allow = (r"/worldranking/news/", )), callback = "parse_newsV2"),
        Rule(SgmlLinkExtractor(allow = (r"/world-match-centre/news/", )), callback = "parse_newsV2"),

        #player
    )

    def parse_newsV1(self, response):
        article = Selector(response)
        item = FIFAItem()
        item["title"] = article.xpath("//h1[@class='dcm-articletitle']/text()").extract()
        item["content"] = article.xpath("//div[@class='article-body']//p/text()").extract()
        item["link"] = response.url
        yield item

    def parse_newsV2(self, response):
        article = Selector(response)
        item = FIFAItem()
        item["title"] = article.xpath("//h1[@class='mC']/h1/text()").extract()
        item["content"] = article.xpath("//div[@class=' articleBody  landscapePh ']//p/text()").extract()
        item["link"] = response.url
        yield item
