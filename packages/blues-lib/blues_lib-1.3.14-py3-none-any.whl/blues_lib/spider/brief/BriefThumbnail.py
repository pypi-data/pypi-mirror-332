import sys,os,re
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.deco.MaterialDeco import MaterialDeco
from spider.crawler.CrawlerHandler import CrawlerHandler
from pool.BluesMaterialIO import BluesMaterialIO

class BriefThumbnail(CrawlerHandler):
  '''
  Extend the required fields by existed fields
  '''
  kind = 'handler'

  @MaterialDeco()
  def resolve(self,request):
    if not request or not request.get('briefs'):
      return
    
    self.__download(request)

  def __download(self,request):
    briefs = request.get('briefs')
    for brief in briefs:
      # convert online image to local image
      brief['material_thumbnail'] = BluesMaterialIO.get_download_thumbnail(brief)
