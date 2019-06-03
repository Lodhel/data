import numpy as np
import pandas as pd

df = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
full_df = len(df.index)
df = df.loc[df.lunch == 'free/reduced']

print(df)