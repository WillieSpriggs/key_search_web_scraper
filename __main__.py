import Source
import Page
import Keyword

def main():
    print('hello world')

    
    # Keyword tests
    print("----- Keyword class tests -----")
    key1 = Keyword("Hello")
    print("Current key: " + key1.getKeyword())
    print("Changing key to: \"Howdy\".")
    print(key1.setKeyword("Howdy"))
    print("Print new keyword: " + key1.getKeyword())
    print("Creating new key... Keyword: \"Aggie\"")
    key2 = Keyword("Aggie")
    print("Total number of keys: " + key2.getNumKeys())
    

    print("-------------------------------")

    # Page tests
    print("----- Page class tests -----")
    print("----------------------------")

    # Webpage tests
    print("----- Webpage class tests -----")
    print("-------------------------------")

    # Source tests
    print("----- Source class tests -----")
    print("-------------------------------")

    # Website tests
    print("----- Website class tests -----")
    print("-------------------------------")


if __name__ == "__main__":
    main() 