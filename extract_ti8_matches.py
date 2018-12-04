import requests
import json
import pandas as pd
import time

df = pd.read_csv('matches_ti8.csv')

match_ids = df['match_id'].values.tolist()

matches = []

for id in match_ids:
    r = requests.get(f"https://api.opendota.com/api/matches/{id}")
    r = r.json()

    matches.append(r)
    time.sleep(1.5)

with open('ti8_data.json', 'w') as outfile:
    json.dump(matches, outfile)
