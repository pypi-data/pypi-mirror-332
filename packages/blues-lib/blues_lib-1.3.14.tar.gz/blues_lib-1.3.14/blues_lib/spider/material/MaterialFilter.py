import sys,os,re,json
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.deco.MaterialDeco import MaterialDeco
from spider.crawler.CrawlerHandler import CrawlerHandler
from pool.BluesMaterialIO import BluesMaterialIO  
from util.BluesConsole import BluesConsole    

class MaterialFilter(CrawlerHandler):
  '''
  Remove the unavailable breifs
  '''
  kind = 'handler'

  @MaterialDeco()
  def resolve(self,request):
    if not request or not request.get('material'):
      return
    
    self.__filter(request)

  def __filter(self,request):
    material = request.get('material')
    if not BluesMaterialIO.is_legal_material(material):
      BluesConsole.error('Illegal material')
      request['material'] = None

    elif not self.__is_limit_valid(request):
      BluesConsole.error('Illegal material of text length')
      request['material'] = None

  def __is_limit_valid(self,request):
    schema = request.get('schema')
    material = request.get('material')
    min_content_length = request.get('min_content_length')
    max_content_length = request.get('max_content_length')

    text_len = len(material.get('material_body_text',''))

    if text_len < min_content_length or text_len > max_content_length:
      return False
    else:
      return True


