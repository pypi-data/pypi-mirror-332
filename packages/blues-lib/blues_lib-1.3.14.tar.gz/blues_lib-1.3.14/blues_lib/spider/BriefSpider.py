import sys,re,os,json
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.Spider  import Spider  
from spider.brief.BriefCrawlerChain  import BriefCrawlerChain  

class BriefSpider(Spider):

  def get_chain(self):
    return BriefCrawlerChain()

  def get_items(self):
    return self.request.get('briefs')