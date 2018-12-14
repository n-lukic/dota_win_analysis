import utils.db_ops as db
import utils.api_ops as api
import pandas as pd
import json
import time

db.create_db()

df = pd.read_csv('data.csv')
match_ids = df['match_id'].values.tolist()

for id in match_ids:

    r = api.get_match(id)
    db.insert_match(r)

    with open(f'data/matches_out/{id}.json', 'w') as outfile:
        json.dump(r, outfile)
    time.sleep(0.1)

    r
