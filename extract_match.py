import requests
import json
import pandas as pd

match_ids = pd.read_csv


r = requests.get('https://api.opendota.com/api/matches/4120320008')
r = r.json()
with open('ti8_data.json', 'w') as outfile:
    json.dump(r, outfile)
