try:
  from googlesearch import search
except ImportError:
  print("No module named 'google' found.")

SEARCH_DELAY = 5

def getSearchResults(query: str, result_cnt: int):
  urls = []

  try:
      for result in search(
        query, 
        tld = "com", 
        num = result_cnt, 
        start = 0, 
        stop = result_cnt, 
        pause = SEARCH_DELAY
        ):
        urls.append(result)
  except:
      print("Error: could not perform google search.")

  return urls