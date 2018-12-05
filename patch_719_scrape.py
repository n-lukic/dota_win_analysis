import requests
import json
import pandas as pd
import time

df = pd.read_csv('top_ids_patch_719.csv')

match_ids = df['match_id'].values.tolist()

matches = []

for id in match_ids:
    r = requests.get(f"https://api.opendota.com/api/matches/{id}")
    r = r.json()

    with open(f'data/patch_719_scrape/{id}.json', 'w') as outfile:
        json.dump(r, outfile)
    time.sleep(1.1)
