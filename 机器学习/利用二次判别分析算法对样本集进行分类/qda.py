"""
sklearn的QuadraticDiscriminantAnalysis分类算法
author：道客儿
V：Docer01
"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from make_classifier_data import make_classifier_data
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

# 获取样本数据
datasets = make_classifier_data(200)

# 画图大小
figure = plt.figure(figsize=(8, 9))

# 定义分类方法
classifier_method = QuadraticDiscriminantAnalysis()

# 循环处理三个数据样本
i = 1
for ds_index, dataset in enumerate(datasets):
    # 数据预处理，把数据分为训练集和测试集
    X, y = dataset

    # 先计算X的均值和方差，并据此对数据进行标准化
    X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=6)

    # 计算最大最小，用于计算网格
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    x_, y_ = np.meshgrid(np.arange(x_min, x_max, .1), np.arange(y_min, y_max, .1))

    # 画点的颜色列表
    cm_bright = ListedColormap(['#F10000', '#0000F1'])
    plot_data = plt.subplot(len(datasets), 2, i)

    if ds_index == 0:
        plot_data.set_title("Example Data")
    # 画出样本集分布
    # cmap与c配合使用，cmap是颜色序列，c制定颜色序列的序号，通过这种方式区分两种分类
    # 利用透明度区分训练集和测试集
    plot_data.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
    plot_data.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6)
    plot_data.set_xlim(x_.min(), x_.max())
    plot_data.set_ylim(y_.min(), y_.max())
    plot_data.set_xticks(())
    plot_data.set_yticks(())
    i += 1

    # 数据分类，训练模型
    classifier_method.fit(X_train, y_train)
    score = classifier_method.score(X_test, y_test)

    plot_classifier = plt.subplot(len(datasets), 2, i)
    if ds_index == 0:
        plot_classifier.set_title("Quadratic Discriminant Analysis Classifier")
    # 利用模型预测
    Z = classifier_method.predict_proba(np.c_[x_.ravel(), y_.ravel()])[:, 1]
    # 利用等高线展示预测结果
    Z = Z.reshape(x_.shape)
    cm = plt.cm.RdBu
    plot_classifier.contourf(x_, y_, Z, cmap=cm, alpha=.8)

    # 画点
    plot_classifier.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright)
    plot_classifier.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6)
    plot_classifier.set_xlim(x_.min(), x_.max())
    plot_classifier.set_ylim(y_.min(), y_.max())
    plot_classifier.set_xticks(())
    plot_classifier.set_yticks(())
    # 得分
    plot_classifier.text(x_.max() - .3, y_.min() + .3, score, size=12, horizontalalignment='right')
    i += 1

plt.tight_layout()
plt.show()
