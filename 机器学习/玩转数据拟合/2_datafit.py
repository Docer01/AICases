"""
author：道客儿
V：Docer01
"""

from sklearn import datasets  # 引入数据集
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

# 利用make_regression函数生成回归样本数据
X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1.1)

# 用polyfit拟合数据，deg=1代表用一次函数
z1 = np.polyfit(x=X.reshape(100), y=y, deg=1)
p1 = np.poly1d(z1)
print(z1)
print(p1)

# 绘制构造的数据
plt.figure()
plt.scatter(X, y)
y = z1[0] * X + z1[1]
plt.plot(X, y, c='red')
plt.show()
