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


# Test function
def test():
    w = Website("helloworld.com")

    print("ID: ", w.getSourceId())
    print("Type: ", w.getSourceType())
    print("Pages: ", w.getNumPages())
    print("URL: ", w.getSiteURL())


if (__name__ == "__main__"):
    test()