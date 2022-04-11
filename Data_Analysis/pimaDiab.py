import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport as ProfileReport
from csvToExcel import csvExcel
df = pd.read_csv('titanic.csv')
csvExcel(df)