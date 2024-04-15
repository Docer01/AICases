"""
author：道客儿
V：Docer01
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('../../data/boston/boston.csv', header=None, sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

plt.figure(figsize=(10, 10))
# 把所有字段之间的相关性，通过矩阵以热力图的形式展示
cm = np.corrcoef(df[df.columns].values.T)
hm = sns.heatmap(cm, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size': 10}, yticklabels=df.columns,
                 xticklabels=df.columns)

plt.show()
