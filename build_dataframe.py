import pandas as pd
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import LabelBinarizer

heroes = pd.read_csv('data/heroes_data.csv')

pd.get_dummies(heroes['localized_name'], prefix = 'radiant')

pd.get_dummies(heroes['localized_name'], prefix = 'dire')
