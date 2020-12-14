try:
    from googlesearch import search
except ImportError:
    print("No Module named 'google' found.")

from Website import Website
from Webpage import Webpage

__SEARCH_DELAY = 5
websites = []

def googleSearch(query: str, result_cnt: int):
    sites = []

    try:
        for result in search(query, tld = "co.in", num = result_cnt, stop = result_cnt, pause =__SEARCH_DELAY):
            sites.insert(-1, result)
    except:
        print("Error: search terminated. [Issue performing google search]")

    return sites

def createWebsite():
    pass
    # Create site.
    # Check if ID is unique (idResuffle)


def main():
    sites = googleSearch("All about dobermans", 5)
    print(sites)
    

if (__name__ == "__main__"):
    main()