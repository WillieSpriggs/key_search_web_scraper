import string
import random

class Source:

  __ID_SIZE = 7

  def __init__(self, source_type: str):
    self.__source_type = source_type
    self.__pages = []
    self.__json = {}

  def getSourceType(self):
    return self.__source_type
  
  def getJson(self):
    return self.__json
  
  def generatePageId(self):
    valid_characters = string.ascii_letters + string.digits
    
    new_id = ''.join((random.choice(valid_characters) for i in range(self.__ID_SIZE)))
    while (not self.isUniqueId(new_id)):
      new_id = ''.join((random.choice(valid_characters) for i in range(self.__ID_SIZE)))

    return new_id

  def isUniqueId(self, new_page_id: str):
    for page in self.__pages:
      if new_page_id == page.getPageId():
        return False

    return True
