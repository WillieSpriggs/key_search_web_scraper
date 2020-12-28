import os

class Page:

    def __init__(self, page_id : str):
        self.__page_id = page_id
        self.__is_empty = True


    # Getters/Setters
    def getPageId(self):
        return self.__page_id
    
    # Object methods
    def isEmpty(self):
        return self.__is_empty

    def pushToDataFile(self, text : str):
        if (text == ""):
            return

        try:
            data_file = open(self.__page_id + ".txt", "a+")
            data_file.write(text)
            data_file.close()
            
            if (text[0 : 5] != "<url>" and text[0 : 7] != "<title>"):
                if (self.__is_empty == True):
                    self.__is_empty = False
            
            return 1
        except:
            print("ERROR: could not push data to file: ", self.__page_id)
            return 0
        
    def destroyPage(self):
        file_name = "" + self.__page_id + ".txt"

        if (os.path.exists(file_name)):
            os.remove(file_name)
            self.__is_empty == True
        else: 
            print("WARNING: page deleted, but ", file_name, " does not exist")


# Test function
def test():
    p = Page("Q9B4PUDIrln317rLxPqr")

    print("ID: ", p.getPageId())
    print("Empty: ", p.isEmpty())

if (__name__ == "__main__"):
    test() 