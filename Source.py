from Webpage import Webpage

import string
import random

class Source:
    
    __active_pages = []
    __MAX_ID_LENGTH = 10

    def __init__(self, source_type: str):
        self.__source_type = source_type
        self.__source_id = self.__generateId(self.__MAX_ID_LENGTH)
        self.__num_pages = 0
        self.__page_list = []


    # Getters/Setters
    def getSourceId(self):
        return self.__source_id

    def getSourceType(self):
        return self.__source_type

    def getNumPages(self):
        return self.__num_pages
    
    def getPages(self):
        return self.__active_pages


    # Methods
    def addPage(self, page_reference : str):
        if (page_reference == ""):
            print("ERROR: could not add page [no page reference given]")
            return

        if (self.__source_type == "Website"):
            for webpage in self.__active_pages:
                if (webpage.getURL() == page_reference):
                    print("ERROR: could not add page [duplicate page found with reference: ", page_reference, "]")
                    return

            # Generate page ID for new page
            page_id = self.__generateId(self.__MAX_ID_LENGTH)

            # Check if ID is available
            valid_id = False
            while (valid_id == False):
                valid_id = True
                for Page in self.__active_pages:
                    if (Page.getPageId() == page_id):
                        valid_id = False

                if (valid_id == False):        
                    page_id = self.__generateId(self.__MAX_ID_LENGTH)

            new_page = Webpage(page_reference, page_id)
            self.__active_pages.append(new_page)
            self.__num_pages += 1
    
    def deletePage(self, page_reference : str):
        if (self.__num_pages < 1):
            print("ERROR: could not delete page [no pages found]")
            return

        if (page_reference == ""):
            print("ERROR: could not delete page [no page reference given]")
            return

        for i in range(self.__num_pages):
            if (self.__active_pages[i].getURL() == page_reference):
                self.__active_pages[i].destroyPage()
                self.__num_pages -= 1
                print("disposing ", self.__active_pages[i].getURL())
                self.__active_pages.pop(i)
                return

        print("ERROR: could not delete page [page ", page_reference, " not found]")

    def destroySource(self):
        while (self.__num_pages > 0):
            self.deletePage(self.__active_pages[0].getURL())

    def __generateId(self, id_length : int):
        valid_characters = string.ascii_letters + string.digits
        return (''.join((random.choice(valid_characters) for i in range(id_length))))
    
    def idReshuffle(self):
        new_id = self.__generateId(self.__MAX_ID_LENGTH)
        self.__source_id = new_id
        return new_id



# Test function
def test():
    s = Source("Website")

    # General Tests
    print("ID: ", s.getSourceId())
    print("Type: ", s.getSourceType())
    print("Num Pages: ", s.getNumPages())

    print("testing adding pages...")
    s.addPage("howdyaggie.com/home")
    s.addPage("howdyaggie.com/about")
    s.addPage("howdyaggie.com/contacts")
    active_pages = s.getPages()
    for Page in active_pages:
        print(Page.getURL())
        print(Page.getPageId())
        print("-----")
    print("completed...")
    print("Num Pages: ", s.getNumPages())

    print()
    print("testing deleting: howdyaggie.com/about")
    s.deletePage("howdyaggie.com/about")

    print("printing page list...")
    active_pages = s.getPages()
    for Page in active_pages:
        print(Page.getURL())
        print(Page.getPageId())
        print("-----")
    print("completed...")
    print("Num Pages: ", s.getNumPages())

    print("\ntesting destroying source...")
    s.destroySource()
    print("completed...")
    print("Num Pages: ", s.getNumPages())

if (__name__ == "__main__"):
    test()