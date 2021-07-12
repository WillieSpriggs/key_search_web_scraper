from sources.web import web_search as search
from source_manager import SourceManager

def main(): 
  urls = ['https://www.humanesociety.org/resources/top-reasons-adopt-pet', 'https://www.hhhstopeka.org/adopt/top-10-reasons-to-adopt-from-an-animal-shelter/', 'https://www.aspca.org/news/10-reasons-adopt-shelter-dog', 'https://petcarehospital.net/blog/adopting-instead-of-buying-a-pet', 'https://www.pedigreefoundation.org/six-reasons-adopt-rescue/'] # search.getSearchResults("why you should adopt from a shelter", 5)
  
  manager = SourceManager()
  manager.createWebsites(urls)
  manager.parseAllSources(["love", "cost", "puppy", "happy"], 1)
  manager.generateJson()
        

if (__name__ == "__main__"):
    main()