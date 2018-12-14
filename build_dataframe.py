import pandas as pd
from utils.api_ops import get_heroes
from utils.db_ops import Base, Matches
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np



heroes = pd.read_csv('data/heroes_data.csv')

radiant_hero = pd.get_dummies(heroes['id'], prefix = 'radiant')
dire_hero = pd.get_dummies(heroes['id'], prefix = 'dire')

hero_table = pd.concat([radiant_hero, dire_hero], axis=1)
hero_table[:] = 0

engine = create_engine('sqlite:///data\\dota_analysis.db', echo=True)
Session = sessionmaker(bind=engine)
session= Session()

match_id = []
radiant_win = []
radiant_heroes = []
dire_heroes = []
for row in session.query(Matches).all():
    match_id.append(row.match_id)
    radiant_win.append(row.radiant_win)
    radiant_heroes.append(row.radiant_heroes)
    dire_heroes.append(row.dire_heroes)
df = pd.DataFrame({'match_id': match_id, 'radiant_win': radiant_win, 'radiant_heroes': radiant_heroes, 'dire_heroes': dire_heroes})

df = df.join(hero_table, how='left')

df.fillna(0, inplace=True)
df.iloc[:,4:] = df.iloc[:,4:].astype(int)

for idx, row in enumerate(df['radiant_heroes']):
    rads = list(map(int, row.split('|')))
    for id in rads:
        for ix, val in enumerate(list(df.columns)):
            if ('radiant' in val and str(id) in val):
                df.iloc[idx ,ix] = 1

for idx, row in enumerate(df['dire_heroes']):
    dirs = list(map(int, row.split('|')))
    for id in dirs:
        for ix, val in enumerate(list(df.columns)):
            if ('dire' in val and str(id) in val):
                df.iloc[idx ,ix] = 1

lr=LogisticRegression()
target = df['radiant_win']
features = df.iloc[:,4:]

params = {'penalty':('l1', 'l2'), 'C' : np.logspace(-3, 4, 10)}

gs = GridSearchCV(lr, params)
gs.fit(features, target)

model = gs.best_estimator_
model.fit(features, target)

zero_data = np.zeros(shape=(1,232))
comp = pd.DataFrame(zero_data, columns=list(features.columns))
comp = comp.astype(int)

comp.iloc[:,0] = 1
comp.iloc[:,1] = 1
comp.iloc[:,2] = 1
comp.iloc[:,3] = 1

comp.iloc[:,200] = 1
comp.iloc[:,190] = 1
comp.iloc[:,220] = 1
comp.iloc[:,213] = 1
comp.iloc[:,215] = 1


choices = []
for i in range(4, 121):
    predict_comp = comp
    tuple = []
    predict_comp.iloc[0,i] = 1
    win = model.predict(predict_comp)
    if win==1:
        tuple = [i, float(model.predict_proba(predict_comp)[:,1])]
        choices.append(tuple)
        continue

max(choices, key=lambda item: item[1])
