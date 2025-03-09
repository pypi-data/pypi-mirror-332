import sys,re,os,json
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.Spider  import Spider  
from spider.material.MaterialCrawlerChain  import MaterialCrawlerChain  
from util.BluesAlgorithm import BluesAlgorithm 

class MaterialSpider(Spider):

  def get_chain(self):
    return MaterialCrawlerChain()

  def get_items(self):
    material = self.request.get('material')
    return [material] if material else None

  def _get_request(self,request):
    req = super()._get_request(request)
    del req['briefs']
    del req['materials']
    req['brief'] = self.__get_brief(request)
    req['material'] = None
    return req
  
  def __get_brief(self,request):
    schema = request.get('schema')
    url = request['material_url']
    return {
      'material_url':url,
      'material_type':schema.type,
      'material_site':schema.site,
      'material_id':schema.site+'_'+BluesAlgorithm.md5(url)
    }

      