import numpy as np
import pandas as pd

df = pd.read_spss("BAM Working Dataset, SOC2155 Version-1.sav")
print(df.describe())