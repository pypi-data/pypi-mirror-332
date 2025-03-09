import sys,re,os,json
from abc import ABC,abstractmethod
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from sele.browser.BluesStandardChrome import BluesStandardChrome
from sele.browser.BluesHeadlessChrome import BluesHeadlessChrome
from pool.BluesMaterialIO import BluesMaterialIO
from util.BluesConsole import BluesConsole 

class Spider(ABC):

  def __init__(self,request):
    '''
    @param {dict} request
      - {ReaderSchema} schema [required]
      - {Browser} ChromeBrowser [optional]
      - {bool} headfull [optional] : default value : False
      - {int} max_material_count [optional] : defualt value: 1
      - {int} max_material_image_count [optional] : defualt value: 9
    '''
    self.request = self._get_request(request)    
    
  def _get_request(self,request):
    req = request.copy()
    req.update({
      'briefs':None,
      'materials':None,
    })
    req['browser'] = self._get_browser(req)
    req['max_material_count'] = request.get('max_material_count',1)
    req['max_material_image_count'] = request.get('max_material_image_count',9)
    req['min_content_length'] = request.get('min_content_length',200)
    req['max_content_length'] = request.get('max_content_length',10000)
    return req
    
  def _get_browser(self,request):
    if request.get('browser'):
      return request.get('browser')

    if request.get('headful'):
      return BluesStandardChrome()
    else:
      return BluesHeadlessChrome()

  def spide(self):
    '''
    Crawl and Quit and Save
    '''
    self.crawl()
    self.__save()
    
  def handle(self):
    '''
    Just crawl
    '''
    crawl_chain = self.get_chain()
    crawl_chain.handle(self.request)
    self.__console()

  def crawl(self):
    '''
    Crawl and Quit
    '''
    self.handle()
    self.request['browser'].quit()
    
  @abstractmethod
  def get_chain(self):
    pass

  @abstractmethod
  def get_items(self):
    pass

  def __save(self):
    items = self.get_items()
    if not items:
      return 0

    result = BluesMaterialIO.insert(items)
    if result['code'] == 200:
      BluesConsole.success('Inserted %s items successfully' % result['count'])
      return result['count']
    else:
      BluesConsole.error('Failed to insert, %s' % result.get('message'))
      return 0

  def __console(self):
    site = self.request['schema'].site
    items = self.get_items()
    if not items:
      BluesConsole.error('Crawled 0 items from %s' % site)
    else:
      values = (len(items),site)
      BluesConsole.success('Crawled %s items from  %s' % values)
      self.__console_title(items)

  def __console_title(self,items):
    i = 1
    for item in items:
      values = (i,item.get('material_title'))
      BluesConsole.success('%s. %s' % values)
      i+=1

