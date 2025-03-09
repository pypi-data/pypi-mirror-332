import sys,os,re
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.material.MaterialCrawlerChain import MaterialCrawlerChain  
from spider.deco.BriefMaterialDeco import BriefMaterialDeco
from spider.crawler.CrawlerHandler import CrawlerHandler
from pool.BluesMaterialIO import BluesMaterialIO  
from util.BluesConsole import BluesConsole 

class BriefMaterialCrawler(CrawlerHandler):
  '''
  Linke the brief chain to the material chain
  '''
  kind = 'handler'
  
  @BriefMaterialDeco()
  def resolve(self,request):
    '''
    Parameter:
      request {dict} : the brief hander's request: schema,count,briefs,materials
    '''
    if not request or not request.get('schema') or not request.get('browser') or not request.get('briefs'):
      return

    materials = self.__crawl(request)
    request['materials'] = materials
  
  def __crawl(self,request):
    schema = request.get('schema')
    briefs = request.get('briefs')
    size = request.get('max_material_count')

    mateirals = []

    for brief in briefs:
      material = self.__crawl_one(request,brief)
      if material:
        mateirals.append(material)
      if len(mateirals) >= size:
        break
    return mateirals
  
  def __crawl_one(self,request,brief):
    req = request.copy()
    del req['briefs']
    del req['materials']
    req['brief'] = brief
    req['material'] = None

    handler = MaterialCrawlerChain()
    handler.handle(req)
    return req.get('material')

