import sys,os,re
sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from spider.GridMaterialListSpider import GridMaterialListSpider    
from schema.reader.ifeng.IFengSchemaFactory import IFengSchemaFactory     
from schema.reader.chinadaily.ChinaDailySchemaFactory import ChinaDailySchemaFactory     

class GridSpiderFactory():
  
  def create_ifeng_spider(self,max_material_count=1): 
    factory = IFengSchemaFactory()
    schemas = factory.create_news_schemas()
    return GridMaterialListSpider({
      'schemas':schemas,
      'max_material_count':max_material_count,
    })
    
  def create_chinadaily_spider(self,max_material_count=1):
    factory = ChinaDailySchemaFactory()
    schemas = factory.create_news_schemas()
    return GridMaterialListSpider({
      'schemas':schemas,
      'max_material_count':max_material_count,
    })