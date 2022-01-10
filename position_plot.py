import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import math
import random

col1 = 'Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)'
col2 = 'Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)'
idx = "Entity"

data = pd.read_csv('annual-death.csv')

data = data[[idx, col1, col2]]

cardi = Counter()
drug = Counter()
names = set([])
for i, row in data.iterrows():
	if(math.isnan(row[col1]) or math.isnan(row[col2])) : continue
	cardi[row[idx]] += row[col1]
	drug[row[idx]] += row[col2]
	names.add(row[idx])

for name in names:
	plt.scatter(drug[name], cardi[name])

plt.xlabel("Drug Death")
plt.ylabel("Cardiovascular Death")
plt.show()