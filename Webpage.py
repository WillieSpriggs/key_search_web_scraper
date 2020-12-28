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
        sentence_idx = []
        key_sentences = []

        missing_leading = False
        missing_trailing = False

        for i in range(len(sentences)):
            for key in keywords:
                if (key.upper() in sentences[i].upper()):
                    if (i > 0):
                        # If key sentence is not the first, add leading supporting sentences
                        for j in range(num_supporting):
                            target_idx = i - (num_supporting - j)
                            if ((target_idx >= 0) and (target_idx not in sentence_idx)):
                                sentence_idx.append(target_idx)
                                key_sentences.append(sentences[target_idx])
                            elif (target_idx < 0):
                                missing_leading = True

                    # Adding key sentences
                    sentence_idx.append(i)
                    key_sentences.append(sentences[i])

                    if (i < len(sentences) - 1):
                        # If key sentence is not the last, add following supporting sentences
                        for k in range(num_supporting):
                            target_idx = i + (k + 1)
                            if ((target_idx < len(sentences)) and (target_idx not in sentence_idx)):
                                sentence_idx.append(target_idx)
                                key_sentences.append(sentences[target_idx])
                            elif (target_idx >= len(sentences)):
                                missing_trailing = True

                    break

        return [key_sentences, missing_leading, missing_trailing]

    def keysearch(self, paragraph : str, keywords : list, num_supporting : int, search_incomplete : bool):
        return_list = [None, None, None, None]

        sentences = [paragraph]
        for delimeter in self.__delimeters:
            sentences = self.splitSentences(sentences, delimeter)
        
        # If previous search was incomplete, complete the search
        if (search_incomplete == True):
            completion_sentences = []
            for i in range(num_supporting):
                if (i < len(sentences)):
                    completion_sentences.append(sentences[i])
            
            for sentence in completion_sentences:
                self.pushToDataFile("POSTTEXT" + sentence + "\n")
            self.pushToDataFile("<p>\n")

            # Update sentences
            sentences = sentences[len(completion_sentences):]
            
        
        # Buffer sentences: used in the case where next keysearch is incomplete.
        buffer_front = []
        for i in range(num_supporting):
            target_idx = len(sentences) - num_supporting + i
            if (target_idx >= 0 and target_idx < len(sentences)):
                buffer_front.append(sentences[target_idx])
        return_list[0] = buffer_front

        # Check if a key exists within 
        foundKeys = []
        for key in keywords:
            if (key.upper() in paragraph.upper()):
                foundKeys.append(key)
        if (len(foundKeys) < 1):
            return return_list
        
        # Find key sentences.
        key_data = self.findKeySentences(sentences, foundKeys, num_supporting)
        return_list[1] = key_data[0]
        return_list[2] = key_data[1]
        return_list[3] = key_data[2]

        # return [buffer_front, key_sentences, missing_front, missing_back]
        return return_list

    def addPretext(self, pretext_sentences : list, key_sentences : list):
        return_sentences = key_sentences

        if (pretext_sentences != None and key_sentences != None):
            # Insert 
            for i in range(len(pretext_sentences)):
                if (pretext_sentences[i] not in key_sentences):
                    return_sentences.insert(i, "PRETEXT" + pretext_sentences[i])

        return return_sentences
        
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
        buffer_front = []
        search_incomplete = None

        for p in paragraphs:
            if (p.getText() != ""):
                push_data = self.keysearch(p.getText(), keywords, num_supporting, search_incomplete)
                push_sentences = push_data[1]
                search_incomplete = push_data[3]

                if (push_sentences != None and len(push_sentences) > 0):
                    if (push_data[2] == True):
                        # Search is missing key sentences.
                        push_sentences = self.addPretext(buffer_front, push_sentences)

                    self.pushToDataFile("<p>\n")
                    for sentence in push_sentences:
                        self.pushToDataFile(sentence + "\n")
                    if (search_incomplete == False):
                        self.pushToDataFile("<p>\n")
                
                buffer_front = push_data[0]
        
        return 1


# Test function
def test():
    w = Webpage("https://www.whitehouse.gov/about-the-white-house/presidents/barack-obama/", "Q9B4PUDIrln317rLxPqr")

    # print("ID: ", w.getPageId())
    # print("URL: ", w.getPageURL())
    # print("Empty: ", w.isEmpty())

    # w.parseWebpage(["obama"], 2)

    t1 = "Hello my name is Willie. I am from Navasota, Texas. I like to play basketball! I have played basketball for the majority of my life. Do you like to code? I do, and I study computer science at Texas A&M University! Gig em, Aggies!"
    keys = ["life", "code"]
    print(w.keysearch(t1, keys, 1))

if (__name__ == "__main__"):
    test() 