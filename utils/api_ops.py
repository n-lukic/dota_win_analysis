import requests
import json
import pandas as pd
import time
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_match(match_id):
    """
    Takes a Dota2 match id and returns a json file from the Open Dota API
    """
    s = requests.Session()
    retries = Retry(total=None, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
    s.mount('http://', HTTPAdapter(max_retries=retries))

    r = s.get(f"https://api.opendota.com/api/matches/{match_id}")
    r = r.json()

    return r

def get_heroes():
    """
    Returns OpenDota's data on all heroes in the game, including names, types etc.
    anda saves it as a csv.
    """
    r = requests.get('https://api.opendota.com/api/heroes')
    r = r.json()

    df = pd.DataFrame(r)
    df.to_csv('data/heroes_data.csv')

def get_radiant_heroes(r):
    radiant_heroes = []
    for player in r['players']:
        hero_id = player['hero_id']

        if 0 <= player['player_slot'] <= 127:
            radiant_heroes.append(str(hero_id))
    radiant_heroes = '|'.join(radiant_heroes)
    return radiant_heroes

def get_dire_heroes(r):
    dire_heroes = []
    for player in r['players']:
        hero_id = player['hero_id']

        if 128 <= player['player_slot'] <= 255:
            dire_heroes.append(str(hero_id))
    dire_heroes = '|'.join(dire_heroes)
    return dire_heroes
