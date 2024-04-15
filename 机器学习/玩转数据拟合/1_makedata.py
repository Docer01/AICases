from sklearn import datasets  # 引入数据集
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

# 利用make_regression函数生成回归样本数据
# 参数：
# n_samples：返回的样本数量
# n_features：自变量个数，n_features
# n_informative：参与建模特征数
# n_targets：因变量个数
# noise：噪音，可以修改为1.6试试看
# bias：偏差(截距)
# coef：是否输出coef标识
# random_state：随机状态若为固定值则每次产生的数据都一样
X, y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1.1)

print(X.shape)
print(y.shape)
print(X)
print(y)

# 绘制构造的数据
plt.figure()
plt.scatter(X, y)
plt.show()
