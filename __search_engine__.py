try:
    from googlesearch import search
except ImportError:
    print("No Module named 'google' found.")

from Website import Website
from Webpage import Webpage

__PAUSE_TIME = 5
websites = []

def googleSearch(query: str, result_cnt: int):
    for result in search(query, tld = "co.in", num = result_cnt, stop = result_cnt, pause =__PAUSE_TIME):
        site = Website(result)


def main():
    googleSearch("All about dobermans", 20)
    

if (__name__ == "__main__"):
    main()