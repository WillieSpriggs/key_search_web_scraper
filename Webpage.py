from bs4 import BeautifulSoup
import requests

from  Page import Page

class Webpage(Page):

    def __init__(self, page_url : str, page_id : str):
        super().__init__(page_id)
        self.__page_url = page_url


    # Getters/Setters
    def getPageURL(self):
        return self.__page_url

    # Methods
    def parseWebpage(self):
        self.pushToDataFile("URL: " + self.__page_url + "\n")
        
        try:
            source = requests.get(self.__page_url)
        except:
            print("ERROR: could not parse website [could not request site]")
            return 0

        soup = BeautifulSoup(source.text, "lxml")
        try:
            title = soup.find("title").getText()
            self.pushToDataFile("Title: " + title + "\n")
        except:
            print("WARNING: could not find title for source: ", self.__page_url)

        try:
            for paragraph in soup.find_all("p"):
                if (paragraph.getText() != ""):
                    self.pushToDataFile(paragraph.getText() + "\n")
    
        except:
            print("ERROR: issue finding paragraph tags")
            return 0
        
        return 1


# Test function
def test():
    w = Webpage("https://www.hillspet.com/dog-care/dog-breeds/doberman", "Q9B4PUDIrln317rLxPqr")

    print("ID: ", w.getPageId())
    print("URL: ", w.getPageURL())
    print("Empty: ", w.isEmpty())

    w.parseWebpage()

if (__name__ == "__main__"):
    test() 