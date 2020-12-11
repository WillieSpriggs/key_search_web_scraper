import os

class Page:

    def __init__(self, page_id : str):
        self.__page_id = page_id
        self.__is_empty = True

        # Creating data file
        file_name = "" + page_id + ".txt"
        data_file = open(file_name, "a+")
        data_file.close()


    # Getters/Setters
    def getPageId(self):
        return self.__page_id
    
    # Object methods
    def isEmpty(self):
        return self.__is_empty

    def pushToFile(self, text : str):
        if (text == ""):
            return

        data_file = open(self.__page_id, "a+")
        data_file.write(text)
        data_file.close()

        if (self.__is_empty == True):
            self.__is_empty == False
        
    def destroyPage(self):
        file_name = "" + self.__page_id + ".txt"

        print("destroying page... ")
        if (os.path.exists(file_name)):
            os.remove(file_name)
            self.__is_empty == True
            print("successful")
        else: 
            print(file_name, "does not exist.")


# Test function
def test():
    p = Page("Q9B4PUDIrln317rLxPqr")

    print("ID: ", p.getPageId())
    print("Empty: ", p.isEmpty())

if (__name__ == "__main__"):
    test() 