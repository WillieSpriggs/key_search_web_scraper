from  Page import Page

class Webpage(Page):

    def __init__(self, page_url : str, page_id : str):
        super().__init__(page_id)
        self.__page_url = page_url


    # Getters/Setters
    def getURL(self):
        return self.__page_url


# Test function
def test():
    w = Webpage("helloworld.com/about", "Q9B4PUDIrln317rLxPqr")

    print("ID: ", w.getPageId())
    print("URL: ", w.getPageURL())
    print("Empty: ", w.isEmpty())

if (__name__ == "__main__"):
    test() 