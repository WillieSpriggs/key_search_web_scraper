from .page import Page
from .web import web_scrape as scrape
from .key_search import key_search as search

class Webpage(Page):

  def __init__(self, page_url: str, page_id: str):
    super().__init__(page_id)
    self.__page_url = page_url
    self.__page_title = ""

  def getPageURL(self):
      return self.__page_url

  def parseWebpage(self, keywords: list, num_supporting_sentences: int):
    soup = scrape.buildSoup(self.__page_url)
    self.__page_title = scrape.getTitle(soup)

    key_sentences = search.keySearch(scrape.getParagraphs(soup), keywords, num_supporting_sentences)
    self.generateJson(key_sentences)

  def generateJson(self, key_sentences: list):
    json = {
      "page_url": self.__page_url,
      "page_title": self.__page_title,
      "key_sentences": key_sentences,
    }

    self._Page__json = json

