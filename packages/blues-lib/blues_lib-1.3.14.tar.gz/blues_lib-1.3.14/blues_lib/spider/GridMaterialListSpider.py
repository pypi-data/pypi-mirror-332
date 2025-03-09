import sys,re,os,json
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from sele.browser.BluesStandardChrome import BluesStandardChrome
from sele.browser.BluesHeadlessChrome import BluesHeadlessChrome
from spider.MaterialListSpider import MaterialListSpider
from pool.BluesMaterialIO import BluesMaterialIO
from util.BluesConsole import BluesConsole 

class GridMaterialListSpider():

  def __init__(self,request):
    '''
    Crawl the total count materials from the schemas
    Param {Dict} request
      - schemas {List<Schema>} : multi platform or channels' schema
      - max_material_count {int} : the total excepted crawled count
    '''
    self.request = self._get_request(request)    

  def _get_request(self,request):
    req = request.copy()
    req['browser'] = self._get_browser(req)
    req['max_material_count'] = request.get('max_material_count',1)
    return req
    
  def _get_browser(self,request):
    if request.get('browser'):
      return request.get('browser')

    if request.get('headful'):
      return BluesStandardChrome()
    else:
      return BluesHeadlessChrome()
  
  def spide(self):
    materials = self.crawl()
    self.__save(materials)

  def crawl(self):
    '''
    Quantity allocation strategy:
      style 1: Single platform preferred
      style 2: Average distribution of platform
    '''
    total_count = self.request['max_material_count']
    crawled_count = 0
    missing_count = total_count
    material_list = []

    for schema in self.request['schemas']:

      # use style 1
      materials = self.__crawl_once(schema,missing_count)
      count = len(materials) if materials else 0
      if count:
        material_list.extend(materials)

      crawled_count += count
      missing_count -= count

      if crawled_count >= total_count:
        break

    self.request['browser'].quit()
    values = (len(material_list),total_count)
    BluesConsole.success('Crawled All/Total = %s/%s' % values)
    return material_list

  def __crawl_once(self,schema,missing_count):
    '''
    Crawl one or multi materials from the same schema
    '''
    req = {
      'browser':self.request['browser'],
      'schema':schema,
      'max_material_count':missing_count,
    }

    spider = MaterialListSpider(req)
    # crawl but don't save
    spider.handle()
    return spider.get_items()

  def __save(self,materials):
    if not materials:
      return 0

    result = BluesMaterialIO.insert(materials)
    if result['code'] == 200:
      BluesConsole.success('Inserted %s materials successfully' % result['count'])
    else:
      BluesConsole.error('Failed to insert, %s' % result.get('message'))

    return result['count']
