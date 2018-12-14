import requests
import json
import pandas as pd
import time

def get_match(match_id):
    """
    Takes a Dota2 match id and returns a json file from the Open Dota API
    """
    s = requests.Session()
    retries = Retry(total=None, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])
    s.mount('http://', HTTPAdapter(max_retries=retries))

    r = s.get(f"https://api.opendota.com/api/matches/{id}")
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
    df.to_csv('heroes_data.csv')

def get_radiant_heroes(r):
    radiant_heroes = []
        for player in r['players']:
            hero_id = r['players'][player]['hero_id']

            if 0 <= r['players'][player]['player_slot'] <= 127:
                radiant_heroes.append(hero_id)
    radiant_heroes = '|'.join(radiant_heroes)
    return radiant_heroes

 def get_dire_heroes(r):
     dire_heroes = []
         for player in r['players']:
             hero_id = r['players'][player]['hero_id']

             if 128 <= r['players'][player]['player_slot'] <= 255:
                 dire_heroes.append(hero_id)
    dire_heroes = '|'.join(dire_heroes)
    return dire_heroes
