"""
author：道客儿
V：Docer01
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. 数据加载：加载波士顿房屋数据集
df = pd.read_csv('../../data/boston/boston.csv', header=None, sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

# 2. 数据准备：分割数据集，横向分为特征（X）和目标变量（y），纵向分为训练集和测试集
X = df['RM'].values.reshape(-1, 1)
y = df['MEDV'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=16)

# 3. 模型训练：使用线性回归模型训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 4. 模型预测：利用训练好的模型对测试集进行预测
y_pred = model.predict(X_test)

# 5. 模型评估：计算模型拟合的性能指标（均方误差）
mse = np.mean((y_pred - y_test) ** 2)
print("均方误差：", mse)

# 6. 结果可视化：绘制拟合曲线和真实值的散点图
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predict Price')
plt.title('Linear Regression')
plt.show()
