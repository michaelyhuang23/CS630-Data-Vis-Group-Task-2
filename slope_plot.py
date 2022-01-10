import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import math
import random

cols = []
cols.append('Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)')
cols.append('Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)')
cols.append('Deaths - Lower respiratory infections - Sex: Both - Age: All Ages (Number)')
cols.append('Deaths - Chronic respiratory diseases - Sex: Both - Age: All Ages (Number)')

idx = "Entity"
year = "Year"

data = pd.read_csv('annual-death.csv')

data = data[[idx, year, *cols]]

table = {col : {} for col in cols}
names = set([])
for i, row in data.iterrows():
	suc = True
	for col in cols:
		if math.isnan(row[col]) : suc = False
	if not suc : continue
	names.add(row[idx])
	if len(names) >= 21 :
		names.remove(row[idx])
		break
	for col in cols:
		if row[idx] not in table[col] : table[col][row[idx]] = []
		table[col][row[idx]].append((row[year],row[col]))

slope = {col : {} for col in cols}
for col in cols:
	for ck in table[col].keys():
		table[col][ck].sort()
		yre, vale = table[col][ck][-1]
		yrs, vals = table[col][ck][0]
		if yre == yrs : slope[col][ck]=0
		else : slope[col][ck] = (vale - vals)/(yre - yrs)

names = list(names)

colsS = ['Drug', 'Cardiovascular', 'Lower respiratory infections', 'Chronic respiratory infections']

dx = []
dy = []
for i in range(len(names)): dx.append([])
for i in range(len(names)): dy.append([])

for i,n in enumerate(names):
	for col in cols:
		dx[i].append(1)
		dy[i].append(slope[col][n]/200)

dx = np.array(dx)
dy = np.array(dy)
X = np.arange(0, len(names))
Y = np.arange(0, len(colsS))
print(names)
print(colsS)
print(X)
print(Y)
print(dx)
plt.quiver(Y,X,dx, dy,scale = 20)

plt.xticks(Y, colsS)
plt.yticks(X, names)
plt.grid(True)
plt.show()