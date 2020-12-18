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
        try:
            source = requests.get(self.__page_url)
        except:
            print("ERROR: could not parse website [could not request site]")
            return 0

        soup = BeautifulSoup(source.text, "lxml")

        try:
            paragraphs = soup.find_all("p")
        except:
            print("ERROR: issue finding paragraph tags")
            return 0
        
        # Push file header
        try:
            title = soup.find("title").getText()
        except:
            title = None
            print("WARNING: could not find title for source: ", self.__page_url)

        self.pushToDataFile("URL: " + self.__page_url + "\n")
        if (title != None):
            self.pushToDataFile("Title: " + title + "\n")
        
        # Push data to file
        for p in paragraphs:
            if (p.getText() != ""):
                self.pushToDataFile(p.getText() + "\n")
        
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