

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
