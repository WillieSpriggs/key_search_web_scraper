from bs4 import BeautifulSoup
import requests

from  Page import Page

class Webpage(Page):

    __delimeters = ['.', '!', '?']

    def __init__(self, page_url : str, page_id : str):
        super().__init__(page_id)
        self.__page_url = page_url


    # Getters/Setters
    def getPageURL(self):
        return self.__page_url

    # Methods
    def splitSentences(self, sentences : list, delimeter : str):
        # Splits a list of sentences by a given delimeter.
        return_list = []
    
        for sentence in sentences:
            split_sentences = sentence.split(delimeter)
            for split_sentence in split_sentences:
                if (split_sentence != ""): # If string is empty, don't append.
                    if (split_sentence[-1] not in self.__delimeters):
                        return_list.append(split_sentence + delimeter)
                    else: return_list.append(split_sentence)
        
        return return_list
    
    def findKeySentences(self, sentences : list, keywords : list, num_supporting : int):
        # Returns only the sentences intended to be pushed to data file.
        key_sentences = {}

        for i in range(len(sentences)):
            for key in keywords:
                if (key.upper() in sentences[i].upper()):
                    if (i > 0):
                        # If key sentence is not the first, add leading supporting sentences
                        for j in range(num_supporting):
                            target_idx = i - (num_supporting - j)
                            if ((target_idx >= 0) and (target_idx not in key_sentences.keys())):
                                key_sentences.update({target_idx : sentences[target_idx]})

                    # Adding key sentences
                    key_sentences.update({i : sentences[i]})

                    if (i < len(sentences) - 1):
                        # If key sentence is not the last, add following supporting sentences
                        for k in range(num_supporting):
                            target_idx = i + (k + 1)
                            if ((target_idx < len(sentences)) and (target_idx not in key_sentences.keys())):
                                key_sentences.update({target_idx : sentences[target_idx]})

                    break

        return key_sentences

    def keysearch(self, paragraph : str, keywords : list, num_supporting : int):
        returnString = ""

        if (paragraph == ""):
            return returnString

        foundKeys = []
        for key in keywords:
            if (key.upper() in paragraph.upper()):
                foundKeys.append(key)
        if (len(foundKeys) < 1):
            return returnString

        sentences = [paragraph]
        for delimeter in self.__delimeters:
            sentences = self.splitSentences(sentences, delimeter)
        
        # Find return sentences.
        key_sentences = self.findKeySentences(sentences, foundKeys, num_supporting)

        return key_sentences
        
    def parseWebpage(self, keywords : list, num_supporting : int):
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

        self.pushToDataFile("<url>\n" + self.__page_url + "\n<url>\n")
        if (title != None):
            self.pushToDataFile("<title>\n" + title + "\n<title>\n")
        
        # Push data to file
        for p in paragraphs:
            if (p.getText() != ""):
                push_sentences = self.keysearch(p.getText(), keywords, num_supporting)
                if (len(push_sentences) > 0):
                    self.pushToDataFile("<p>\n")
                    for sentence_key in push_sentences:
                        self.pushToDataFile(push_sentences[sentence_key] + "\n")
                    self.pushToDataFile("<p>\n")
        
        return 1


# Test function
def test():
    w = Webpage("https://www.whitehouse.gov/about-the-white-house/presidents/barack-obama/", "Q9B4PUDIrln317rLxPqr")

    # print("ID: ", w.getPageId())
    # print("URL: ", w.getPageURL())
    # print("Empty: ", w.isEmpty())

    w.parseWebpage(["obama"], 2)

    # t1 = "Hello my name is Willie. I am from Navasota, Texas. I like to play basketball! I have played basketball for the majority of my life. Do you like to code? I do, and I study computer science at Texas A&M University! Gig em, Aggies!"
    # keys = ["life", "code"]
    # print(w.keysearch(t1, keys, 1))

if (__name__ == "__main__"):
    test() 