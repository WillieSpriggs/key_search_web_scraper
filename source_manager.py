from sources.website import Website
import json

class SourceManager:

  def __init__(self):
    self.__sources = []

  def createWebsites(self, site_urls: list):
    for site_url in site_urls:
      new_website = Website(site_url)
      new_website.addPage(site_url)
      self.__sources.append(new_website)
  
  def parseAllSources(self, keywords: list, num_supporting_sentences: int):
    for source in self.__sources:
      if (source.getSourceType() == "website"):
        source.parseWebsite(keywords, num_supporting_sentences)

  def generateJson(self):
    sources = []
    for source in self.__sources:
      sources.append(source.getJson())
    
    with open ("search_results.json", "w") as json_file:
      json_file.write(json.dumps({ "sources": sources }))

    

  