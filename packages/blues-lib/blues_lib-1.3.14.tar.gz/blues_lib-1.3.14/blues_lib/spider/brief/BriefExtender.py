import sys,os,re
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.crawler.CrawlerHandler import CrawlerHandler
from spider.deco.BriefDeco import BriefDeco
from util.BluesURL import BluesURL 
from util.BluesAlgorithm import BluesAlgorithm 

class BriefExtender(CrawlerHandler):
  '''
  Extend the required fields by existed fields
  '''
  kind = 'handler'
  
  @BriefDeco()
  def resolve(self,request):
    if not request or not request.get('briefs'):
      return
    
    self.__extend(request)

  def __extend(self,request):
    schema = request.get('schema')
    briefs = request.get('briefs')
    for brief in briefs:
      brief['material_type'] = schema.type # news gallery shortvideo qa
      brief['material_site'] = schema.site # ifeng bbc
      brief['material_id'] = schema.site+'_'+BluesAlgorithm.md5(brief['material_url'])
      