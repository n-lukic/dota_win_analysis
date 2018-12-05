import requests
import json
import pandas as pd
import time
import logging

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



"""takes the name of a csv containing Dota 2 match ids (under a column
"match_id") and returns the matches as json objects.

"""
logging.basicConfig(level=logging.DEBUG)

df = pd.read_csv('top_ids_patch_719.csv')
match_ids = df['match_id'].values.tolist()

s = requests.Session()
retries = Retry(total=None, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
s.mount('http://', HTTPAdapter(max_retries=retries))

for id in match_ids:
    r = s.get(f"https://api.opendota.com/api/matches/{id}")
    r = r.json()

    with open(f'data/patch_719_scrape/{id}.json', 'w') as outfile:
        json.dump(r, outfile)
    time.sleep(1.1)
