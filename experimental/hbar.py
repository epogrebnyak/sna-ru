import pandas as pd

import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("data/sna.csv", index_col=0)
t = df.loc[2018,].divide(1000).round(1)
performance = (t.C, t.I, t.IM, t.EX, t.desc)
varnames = ("C", "I", "IM", "EX", "df.desc")


fig, ax = plt.subplots()

# Example data

y_pos = np.arange(len(performance))


ax.barh(y_pos, performance, align="center")
ax.set_yticks(y_pos)
ax.set_yticklabels(varnames)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("mln rub")
ax.set_title("How fast do you want to go today?")

plt.show()

df = pd.DataFrame({"lab": ["A", "B", "C"], "val": [10, 30, 20], "vam": [12, 13, 12]})

df["white"] = df.val.cumsum().shift(1, fill_value=0)
ax = df.plot.barh(x="lab", y=["white", "val"], stacked=True)
plt.show()

# Can try sankey
# - https://plot.ly/python/sankey-diagram/
# - https://matplotlib.org/3.1.1/api/sankey_api.html