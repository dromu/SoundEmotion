import pandas as pd

df = pd.read_csv("Input\data_completa.csv")

df.loc[df['selected'] == 0, 'selected'] = 1
df.to_csv("Input\data_completa.csv", index=None)