

import pyecharts.options as opts
from pyecharts.charts import Surface3D
import pandas as pd




def surface3d_data():
    df = pd.read_excel('fualt1.xlsx',sheet_name='Sheet3')
    df.columns = ['x','y','z']
    for index,row in df.iterrows():
        print([row['x'],row['y'],row['z']])
        yield [row['x'],row['y'],row['z']]



