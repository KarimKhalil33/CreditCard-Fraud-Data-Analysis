import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def filter_data(file_path, df):
    mydata = (pd.read_csv(file_path)
              .dropna(subset=['distance_from_home'])
              .dropna(axis=1, how='any')
              .query('distance_from_last_transaction < 75 & ratio_to_median_purchase_price < 30 & distance_from_home < 400')
              .iloc[:len(df) // 170])
    return df

