from abc import ABC,abstractmethod
from .ReaderSchema import ReaderSchema

class NewsReaderSchema(ReaderSchema,ABC):

  def __init__(self):
    super().__init__()
    
    # the schema class's name
    self.type = 'news'
