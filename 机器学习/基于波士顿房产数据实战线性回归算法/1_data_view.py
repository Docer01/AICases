"""
author：道客儿
V：Docer01
"""

import pandas as pd
import seaborn as sns
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv('../../data/boston/boston.csv', header=None, sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# 遍历所有字段，并与标签字段MEDV组成x、y展示散点图
for col in df.columns:
    sns.jointplot(x=col, y='MEDV', data=df)

plt.tight_layout()
plt.show()
