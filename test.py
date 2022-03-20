import requests as requests

import runner
from app.search.search import Searcher
from pprint import pprint


queries = ['Поездка в ДГТУ']
url = 'http://localhost:5000/search'
get_postfix = '?query={query}'

for query in queries:

    r = requests.get(url + get_postfix.format(query=query))
    print(r.json())



