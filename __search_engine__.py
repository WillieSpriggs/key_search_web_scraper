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
    

def createWebsite(url : str):
    new_site = Website(url)
    new_site.constructPages()
    __websites.update({url :new_site})

def destroyWebsite(url : str):
    target_site = __websites[url]

    target_site.destroySource()
    __websites.pop(url)


def main():
    urls = googleSearch("all about dobermans", 3)

    for url in urls:
        createWebsite(url)
    
    for url in urls:
        destroyWebsite(url)
        
    

if (__name__ == "__main__"):
    main()