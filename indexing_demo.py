import json
from pprint import pprint

with open('data/matches_out/4227823549.json') as f:
    data = json.load(f)

data['chat']

pprint(data)
