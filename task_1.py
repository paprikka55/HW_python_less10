import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['cyborg'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)

columns = []
for item in data.values:
    columns.append(item[0])
columns = set(columns)
for item in columns:
    data.loc[data['whoAmI'] == item, item] = True
    data.loc[data['whoAmI'] != item, item] = False
del data['whoAmI']
print(data)
