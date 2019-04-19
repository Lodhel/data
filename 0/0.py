import numpy as np
import pandas as pd

df = pd.read_csv('https://stepik.org/media/attachments/course/4852/titanic.csv')

print(df.index)
print(df.shape)
print(df.size)
print(df.columns)
print(df.dtypes)
print(df.get_dtype_counts())

print(len(df.index))