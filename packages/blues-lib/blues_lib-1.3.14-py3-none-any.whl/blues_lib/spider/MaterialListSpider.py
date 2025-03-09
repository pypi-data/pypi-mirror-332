import sys,re,os,json
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.Spider  import Spider  
from spider.crawler.CrawlerChain  import CrawlerChain  

class MaterialListSpider(Spider):

  def get_chain(self):
    return CrawlerChain()

  def get_items(self):
    return self.request.get('materials')