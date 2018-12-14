import pandas as pd
from utils.api_ops import get_heroes

get_heroes()
heroes = pd.read_csv('data/heroes_data.csv')

radiant_hero = pd.get_dummies(heroes['id'], prefix = 'radiant')
dire_hero = pd.get_dummies(heroes['id'], prefix = 'dire')

hero_table = pd.concat([radiant_hero, dire_hero], axis=1)

hero_table.columns.values
