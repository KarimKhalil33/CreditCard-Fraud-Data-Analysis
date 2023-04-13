import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def filter_dataset(file_path,mydata):
    mydata = (pd.read_csv(file_path)
              .dropna(subset=['distance_from_home'])
              .dropna(axis=1, how='any')
              .query('distance_from_home < 15000 & ((used_pin_number == 1) | (used_chip == 1))')
              .iloc[:len(mydata) // 65])
    return mydata
