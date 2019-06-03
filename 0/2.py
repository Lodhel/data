import pandas as pd

data = "https://stepik.org/media/attachments/course/4852/accountancy.csv"
df = pd.read_csv(data)

print(df.groupby('Type').aggregate('Salary'))

#print(df.columns)