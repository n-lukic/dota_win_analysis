from utils.db_ops import create_db, insert_match
from utils.api_ops import get_match

create_db()

df = pd.read_csv('data.csv')
match_ids = df['match_id'].values.tolist()

for id in match_ids:

    r = get_match(id)
    insert_match(r)

    with open(f'data/matches_out/{id}.json', 'w') as outfile:
        json.dump(r, outfile)
    time.sleep(1.1)
