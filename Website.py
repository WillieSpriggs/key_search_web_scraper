from Source import Source

class Website(Source):

    def __init__(self, site_url):
        super().__init__("Website")
        self.__site_url = site_url

        # Initialize with homepage
        self.addPage(site_url)


    # Getters/Setters
    def getSiteURL(self):
        return self.__site_url
    
    def generateJSONString(self):
        return_string = ""

        for page in self._Source__active_pages:
            return_string += "{\"website_url\": \"" + self.__site_url + "\",\
             \"page_url\": \"" + self._Source__active_pages[page].getPageURL() + "\",\
              \"file_name\": \"" + self._Source__active_pages[page].getPageId() + ".txt\"},"

        return return_string


# Test function
def test():
    w = Website("helloworld.com")

    print("Type: ", w.getSourceType())
    print("Pages: ", w.getNumPages())
    print("URL: ", w.getSiteURL())


if (__name__ == "__main__"):
    test()