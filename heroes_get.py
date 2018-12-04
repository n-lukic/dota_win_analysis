import requests
import pandas as pd
import json

r = requests.get('https://api.opendota.com/api/heroes')
r = r.json()

df = pd.DataFrame(r)

df.to_csv('heroes_data.csv')
