import pandas as pd

def csvExcel(df):
    pd.ExcelWriter(df)

my_list = [1,2,3].to_list