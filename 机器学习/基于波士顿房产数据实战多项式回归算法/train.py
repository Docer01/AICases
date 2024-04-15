"""
author：道客儿
V：Docer01
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# 数据加载：加载波士顿房屋数据集
df = pd.read_csv('../../data/boston/boston.txt', sep="\s+", skiprows=22, header=None)

# 数据准备：分割数据集，横向分为特征（X）和目标变量（y），纵向分为训练集和测试集
X = np.hstack([df.values[::2, :], df.values[1::2, :2]])
y = df.values[1::2, 2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 将特征向量转换为多项式特征
# 使用PolynomialFeatures类将原始特征向量X转换为多项式特征向量X_poly。
# 在这个案例中，选择了二次多项式特征。
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)

# 使用多项式回归模型进行拟合
model = LinearRegression()
model.fit(X_train_poly, y_train)

# 模型预测：利用训练好的模型对测试集进行预测
X_test_poly = poly.transform(X_test)
y_test_pred = model.predict(X_test_poly)

# 计算模型的性能指标
mse = mean_squared_error(y_test, y_test_pred)
print("均方误差：", mse)
