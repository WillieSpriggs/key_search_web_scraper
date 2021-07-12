import os

class Page:

  def __init__(self, page_id):
    self.__page_id = page_id
    self.__json = {}

  def getPageId(self):
    return self.__page_id
  
  def getJson(self):
    return self.__json

