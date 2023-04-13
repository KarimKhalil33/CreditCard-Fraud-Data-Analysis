import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

def filter_data(file_path,df):
    df = (
        pd.read_csv(file_path)
        .dropna(subset=['distance_from_home'])
        .iloc[:len(df) // 65]
        .query('(distance_from_home < 15000) & (used_pin_number == 1) | (used_chip == 1)')
        .dropna(axis=1, how='any')
    )
    return df