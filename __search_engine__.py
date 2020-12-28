import sys, getopt
import json
from googlesearch import search

from Website import Website

__SEARCH_DELAY = 5
__websites = {} # {URL : Website}

def googleSearch(query : str, result_cnt : int):
    sites = []

    try:
        for result in search(query, tld = "co.in", num = result_cnt, stop = result_cnt, pause =__SEARCH_DELAY):
            sites.insert(-1, result)
    except:
        print("Error: search terminated [issue performing google search]")

    return sites
    

def createWebsite(url : str, keywords : list, num_supporting : int):
    new_site = Website(url)
    new_site.constructPages(keywords, num_supporting)

    # If the site is not empty, add it to list of sites.
    if (new_site.getNumPages() > 0):
        __websites.update({url :new_site})

def destroyWebsite(url : str):
    target_site = __websites[url]

    target_site.destroySource()
    __websites.pop(url)

def createJSON():
    json_string = "["

    for website in __websites:
        json_string += __websites[website].generateJSONString()
    
    # Removing final comma and capping string.
    json_string = json_string[:-1] + "]"

    # Creating the JSON file.
    with open("__search_engine__.json", "w") as json_file:
        json.dump(json_string, json_file)


def main(argv : str):
    query = None
    num_results = None
    keywords = None
    num_supporting = None

    # Read in command line arguments.
    try:
        opts, args = getopt.getopt(argv, "q:r:k:s:")
    except getopt.GetoptError:
        print("ERROR: error reading command line arguments [__search_engine__.py -q <\"query\">] -r <num_results> -k <keywords> -s <num_supporting>")
        return
    
    for opt, arg in opts:
        if (opt == '-q'):
            query = arg
        elif (opt == '-r'):
            num_results = int(arg)
        elif (opt == '-k'):
            keywords = arg
        elif (opt == '-s'):
            num_supporting = int(arg)
        else:
            print("ERROR: opt argument " + opt + " was not recognized")
            return
    
    # Preparing arguments for program use.
    keywords = keywords.split(',')

    # Beginning key search.
    urls = googleSearch(query, num_results)
    for url in urls:
        createWebsite(url, keywords, num_supporting)

    # Creating JSON file.
    if (len(__websites) > 0):
        createJSON()
    else: 
        print("ERROR: No results found for keywords ", keywords)
        
    

if (__name__ == "__main__"):
    main(sys.argv[1:])