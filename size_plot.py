import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import math
import random

col1 = 'Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)'
idx = "Entity"
year = "Year"

data = pd.read_csv('annual-death.csv')

data = data[[idx, year, col1]]

drug = {}
names = set([])
for i, row in data.iterrows():
	if(math.isnan(row[col1])) : continue
	if(row[idx] != "United States") : continue
	drug[int(row[year])] = row[col1]

drug_t = []
drug_n = []
for i in range(2007,2018):
	drug_t.append(drug[i]/2)
	drug_n.append(-drug[i]/2)

plt.fill_between(list(range(2007,2018)), drug_n, drug_t)
plt.xlabel("years")
plt.ylabel("annual deaths by drug")

ax = plt.gca()
ax.axes.yaxis.set_ticks([])

plt.grid(True)

plt.show()