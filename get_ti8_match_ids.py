import pandas as pd

match_ids = pd.read_csv('ti8_match_id_query.csv')

df = pd.DataFrame(match_ids)

df_nodupes = df.drop_duplicates()

df_nodupes.to_csv('matches_ti8.csv', index=False)
