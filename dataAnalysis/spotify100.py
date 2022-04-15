#%%
import pandas as pd
df = pd.read_csv('spotify.csv')
df.describe
#%%
df.isnull().sum().sum()
#%%
pd.df.dropna(axis = 0, how ='any', thresh = None, subset = None, inplace=False)

# %%
