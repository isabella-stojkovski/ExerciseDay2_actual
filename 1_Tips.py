import seaborn as sn
import pandas as pd

## 1a

df = sn.load_dataset("tips")
df.head()
df.shape
df.info
df.info()
df.describe()
df.columns
df.size
print(df)

## 1b

df["day"].replace({"Sun":"Sunday", "Mon":"Monday", "Tue":"Tuesday", "Wed":"Wednesday", "Thur":"Thursday", "Fri":"Friday", "Sat":"Saturday"}, inplace=True)
print(df)

df.value_counts("day")

## 1c

import matplotlib.pyplot as plt

df_male=df[df['sex']=='Male']
df_female=df[df['sex']=='Female']

fig, ax = plt.subplots()
colors = {"Sunday": "red", "Monday": "yellow", "Tuesday":"green", "Wednesday":"blue", "Thursday":"pink", "Friday":"orange", "Saturday":"purple"}
plt.scatter(df["total_bill"], df["tip"], c=df["day"].map(colors))
ax.set(ylabel="Tip", xlabel="Total bill", title="Tip paid by total bill amount")
ax.plt.legend()


fig, axes = plt.subplots(1,2,sharex=True,sharey=True)
df_male.plot.scatter(x="total_bill", y="tip", c=df_male["day"].map(colors),ax=axes[0], ylabel="Tip", xlabel="Total bill", title="Male_Tip paid by total bill amount")
df_female.plot.scatter(x="total_bill", y="tip", c=df_female["day"].map(colors),ax=axes[1], ylabel="Tip", xlabel="Total bill", title="Female_Tip paid by total bill amount")
df_male.legend()
df_female.legend()























