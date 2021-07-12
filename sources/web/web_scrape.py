from bs4 import BeautifulSoup
import requests

def buildSoup(url: str):
  try:
    webpage = requests.get(url)
  except:
    print("ERROR: could not parse website: " + url)

  return BeautifulSoup(webpage.text, "lxml")

def getTitle(soup: object):
  try:
    title = soup.find("title").get_text()
  except:
    print("ERROR: could not find title.")
  
  return title

def getParagraphs(soup: object):
  try:
    paragraphs = soup.find_all("p")
  except:
    print("ERROR: could not find paragraphs.")

  return tagsListToStringsList(paragraphs)

def tagsListToStringsList(tags_list: list):
  strings_list = []

  for paragraph in tags_list:
    strings_list.append(paragraph.get_text())

  return strings_list

# def crawl(self):
#   # Returns a list of supporting pages to parse
#   supporting_pages = []

#   try:
#     source = requests.get(self.__site_url)
#   except:
#     print("ERROR: could not parse website [could not request site]")
#     return 0

#   soup = BeautifulSoup(source.text, "lxml")

#   try:
#     links = soup.find_all("a", attrs={'href': re.compile("^https://")})
#   except:
#     try:
#       links = soup.find_all("a", attrs={'href': re.compile("^http://")})
#     except:
#       print("ERROR: issue finding paragraph tags")
#       return supporting_pages

#   print("short: \"" + self.__short_url + "\"")
#   for link in links:
#     if (self.__short_url in link):
#       supporting_pages.append(link.get("href"))
  
#   return supporting_pages


# Test script
def main():
  soup = buildSoup("https://en.wikipedia.org/wiki/%22Hello,_World!%22_program")
  title = getTitle(soup)
  paragraphs = getParagraphs(soup)

  print(paragraphs)

if (__name__ == "__main__"):
    main()



  

