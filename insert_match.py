from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import requests
import json
import time
from create_db import Matches

engine = create_engine('sqlite:///data\\dota_analysis.db', echo=True)
Session = sessionmaker(bind=engine)
session= Session()

r = requests.get('https://api.opendota.com/api/matches/4120320008')
r = r.json()

match = Matches(
    match_id = r['match_id'],
    barracks_status_dire = r['barracks_status_dire']

)

session.add(match)
session.commit()
