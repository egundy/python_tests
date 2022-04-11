import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport as ProfileReport

df = pd.read_csv('titanic.csv')

df.describe(include='all')

profile = ProfileReport(df)
profile.to_file