from .source import Source
from .webpage import Webpage

class Website(Source):

  def __init__(self, site_url):
    super().__init__("website")
    self.__site_url = site_url

  def getSiteURL(self):
    return self.__site_url

  def addPage(self, page_url: str):
    self._Source__pages.append(Webpage(page_url, self.generatePageId()))
  
  def parseWebsite(self, keywords: list, num_supporting_sentences: int):
    for page in self._Source__pages:
      page.parseWebpage(keywords, num_supporting_sentences)

    self.generateJson()
  
  def generateJson(self):
    webpages = []
    for page in self._Source__pages:
      webpages.append(page.getJson())

    json = {
      "source_type": self._Source__source_type,
      "site_url": self.__site_url,
      "pages": webpages
    }
    
    self._Source__json = json

