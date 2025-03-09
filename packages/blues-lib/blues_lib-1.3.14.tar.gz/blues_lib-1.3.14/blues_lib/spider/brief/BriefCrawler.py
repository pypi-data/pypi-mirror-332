import sys,os,re,time
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.crawler.CrawlerHandler import CrawlerHandler
from spider.deco.BriefDeco import BriefDeco
from sele.behavior.BehaviorChain import BehaviorChain
from pool.BluesMaterialIO import BluesMaterialIO  
from util.BluesConsole import BluesConsole 

class BriefCrawler(CrawlerHandler):
  '''
  Replace the schema's placeholder by data
  '''
  kind = 'handler'
  
  @BriefDeco()
  def resolve(self,request):
    '''
    Parameter:
      request {dict} : schema,count,briefs,materials
    '''
    if not request or not request.get('schema') or not request.get('browser'):
      return

    if not request.get('schema').brief_atom:
      return

    briefs = self.__crawl(request)
    self.__console(briefs)
    request['briefs'] = briefs
  
  def __before_crawl(self,browser,schema):
    before_brief_atom = schema.before_brief_atom
    if before_brief_atom:
      handler = BehaviorChain(browser,before_brief_atom)
      handler.handle()
  
  def __crawl(self,request):
    browser = request.get('browser')
    schema = request.get('schema')
    url = schema.brief_url_atom.get_value()

    browser.open(url)

    self.__before_crawl(browser,schema)
    return self.__crawl_brief(browser,schema)

  def __crawl_brief(self,browser,schema):
    brief_atom = schema.brief_atom
    if brief_atom:
      handler = BehaviorChain(browser,brief_atom)
      outcome = handler.handle()
      return outcome.data
    else:
      return None

  def __console(self,briefs):
    if not briefs:
      BluesConsole.error('No available briefs')
    else:
      count = str(len(briefs))
      BluesConsole.success('%s initial briefs were obtained' % count)
