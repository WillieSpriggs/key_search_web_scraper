from googlesearch import search

from Website import Website

__SEARCH_DELAY = 5
__websites = {} # {URL : Website}
# keywords = []
# num_supporting = 0

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


def main():
    urls = googleSearch("joe biden policies", 5)
    keywords = ["coronavirus", "health care", "millitary", "security", "foreign policy"]
    num_supporting = 3

    for url in urls:
        createWebsite(url, keywords, num_supporting)

    if (len(__websites) > 0):
        pass
        # Create and return JSON file.
    else: 
        print("ERROR: No results found for keywords ", keywords)
    
    # for url in urls:
    #     destroyWebsite(url)
        
    

if (__name__ == "__main__"):
    main()