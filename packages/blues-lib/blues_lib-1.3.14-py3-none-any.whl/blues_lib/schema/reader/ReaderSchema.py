import sys,os,re
from abc import ABC,abstractmethod
sys.path.append(re.sub('test.*','blues_lib',os.path.realpath(__file__)))
from atom.AtomFactory import AtomFactory     


class ReaderSchema(ABC):
  def __init__(self):
    
    # protected field
    self._atom_factory = AtomFactory()

    # the schema's type
    self.category = 'reader'

    # the schema class's name
    self.type = ''

    # the source site
    self.site = ''

    # { URLAtom } the list page url [required]
    self.brief_url_atom = None

    # { ArrayAtom } The actions that need to be performed before crawling the brief
    self.before_brief_atom = None

    # { BriefAtom } the brief atom [required]
    self.brief_atom = None

    # { ArrayAtom } the events before fetch material
    self.before_material_atom = None

    # { ArticleAtom } the article atom
    self.material_atom = None
