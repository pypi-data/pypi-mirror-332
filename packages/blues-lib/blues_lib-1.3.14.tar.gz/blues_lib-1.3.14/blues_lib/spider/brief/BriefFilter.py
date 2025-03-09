import sys,os,re
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.crawler.CrawlerHandler import CrawlerHandler
from spider.deco.BriefDeco import BriefDeco
from pool.BluesMaterialIO import BluesMaterialIO  
from util.BluesURL import BluesURL 
from util.BluesConsole import BluesConsole 

class BriefFilter(CrawlerHandler):
  '''
  Remove the unavailable breifs
  '''
  kind = 'handler'
  
  @BriefDeco()
  def resolve(self,request):
    if not request or not request.get('briefs'):
      return
    
    request['briefs'] = self.__filter(request)

  def __filter(self,request):
    briefs = request.get('briefs')
    avail_briefs = [] 
    
    for brief in briefs:

      title = brief['material_title']

      if not BluesMaterialIO.is_legal_brief(brief):
        BluesConsole.error('Unavial biref [Not Legal] : %s' % title)
        continue

      if BluesMaterialIO.exist(brief):
        BluesConsole.error('Unavial biref [Exist] : %s' % title)
        continue

      avail_briefs.append(brief)

    return avail_briefs if avail_briefs else None
