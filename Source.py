from Webpage import Webpage

import string
import random

class Source:

    __MAX_ID_LENGTH = 10

    def __init__(self, source_type: str):
        self.__source_type = source_type
        self.__num_pages = 0
        self.__active_pages = {} # {page_reference : Page}


    # Getters/Setters
    def getSourceType(self):
        return self.__source_type

    def getNumPages(self):
        return self.__num_pages


    # Methods
    def addPage(self, page_reference : str):
        if (page_reference == ""):
            print("ERROR: could not add page [no page reference given]")
            return

        if (self.__source_type == "Website"):
            for webpage in self.__active_pages:
                if (self.__active_pages[webpage].getPageURL() == page_reference):
                    print("ERROR: could not add page [duplicate page found with reference: ", page_reference, "]")
                    return

            # Generate page ID for new page
            page_id = self.__generateId(self.__MAX_ID_LENGTH)

            # Check if ID is available
            valid_id = False
            while (valid_id == False):
                valid_id = True
                for webpage in self.__active_pages:
                    if (self.__active_pages[webpage].getPageId() == page_id):
                        valid_id = False

                if (valid_id == False):        
                    page_id = self.__generateId(self.__MAX_ID_LENGTH)

            new_page = Webpage(page_reference, page_id)
            self.__active_pages.update({page_reference : new_page})
            self.__num_pages += 1
    
    def deletePage(self, page_reference : str):
        if (self.__num_pages < 1):
            print("ERROR: could not delete page [no pages found]")
            return

        if (page_reference == ""):
            print("ERROR: could not delete page [no page reference given]")
            return

        if (page_reference in self.__active_pages.keys()):
            self.__active_pages[page_reference].destroyPage()
            self.__num_pages -= 1
            print("disposing ", page_reference)
            self.__active_pages.pop(page_reference)

    def constructPages(self, keywords : list, num_supporting : int):
        if (len(self.__active_pages) < 1):
            return

        if (self.__source_type == "Website"):
            for page in self.__active_pages:
                self.__active_pages[page].parseWebpage(keywords, num_supporting)

        # If page is empty, remove it from list of pages. 
        delete_pages = []
        for page in self.__active_pages.keys():
            if (self.__active_pages[page].isEmpty()):
                delete_pages.append(page)
        for page in delete_pages:
            self.deletePage(page)
    
    def destroySource(self):
        # Create a list of all keys in __active_pages dict
        keys = []
        for page_reference in self.__active_pages:
            keys.append(page_reference)

        for page_reference in keys:
            self.deletePage(page_reference)

    def __generateId(self, id_length : int):
        valid_characters = string.ascii_letters + string.digits
        return (''.join((random.choice(valid_characters) for i in range(id_length))))



# Test function
def test():
    s = Source("Website")

    # General Tests
    print("Type: ", s.getSourceType())
    print("Num Pages: ", s.getNumPages())

    print("testing adding pages...")
    s.addPage("howdyaggie.com/home")
    s.addPage("howdyaggie.com/about")
    s.addPage("howdyaggie.com/contacts")
    print("completed...")
    print("Num Pages: ", s.getNumPages())

    print()
    print("writing to howdyaggie.com/home...")

    print()
    print("testing deleting: howdyaggie.com/about")
    s.deletePage("howdyaggie.com/about")
    print("Num Pages: ", s.getNumPages())

    print("\ntesting destroying source...")
    s.destroySource()
    print("completed...")
    print("Num Pages: ", s.getNumPages())

if (__name__ == "__main__"):
    test()