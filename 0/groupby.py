import pandas as pd

data = "https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv"
heroes = pd.read_csv(data)

print(heroes.groupby('legs').count())
