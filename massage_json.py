import json
import pandas as pd

match = open('ti8_data.json', 'r')

type(match)

match = json.load(match)

type(match)

print(json.dumps(match, sort_keys=True, indent=4))

print(json.dumps(match['picks_bans'], sort_keys=True, indent=4))

len(match['players'])
print(json.dumps(match['players'][0], sort_keys=True, indent=4))
