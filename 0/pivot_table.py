import pandas as pd

data = "https://stepik.org/media/attachments/course/4852/accountancy.csv"
df = pd.read_csv(data)

print(df.head)
print("##############\r\n")
print(df.dtypes)

print(df.groupby("Executor").mean())
print("########\r\n")

table = df.pivot_table("Salary", columns="Executor", index="Type")
print(table)