"""
制作样本数据方法。
author：道客儿
V：Docer01
"""

import numpy as np
from sklearn.datasets import make_moons, make_circles, make_classification


def make_classifier_data(n_samples=100):
    """
    获取三种分类数据，用于分类算法，分别是线性数据、半月形样本数据、环形样本数据
    Parameters
        n_samples：样本数
    Returns
        三种数据样本
    """
    # 制造线性样本数据
    # n_samples：样本数量，默认值为100
    # n_features：特征总数
    # n_redundant：冗余特征的数量，这些特征是作为信息特征的随机线性组合生成的
    # n_informative：信息特征的数量
    # n_repeated：从信息特征和冗余特征中随机抽取的重复特征的数量
    # n_classes：分类问题的标签分类数,默认为2
    # random_state：类似随机种子，复现随机数
    # n_clusters_per_class：每个类的集群数
    X, y = make_classification(n_samples=n_samples, n_features=2, n_redundant=0, n_informative=2,
                               n_classes=2, random_state=1, n_clusters_per_class=1)

    rng = np.random.RandomState(2)
    X += 2 * rng.uniform(size=X.shape)
    linearly_data = (X, y)

    # 制造半月形样本数据
    # n_numbers：生成样本数量
    # shuffle：是否打乱，类似于将数据集random一下
    # noise：默认是false，数据集是否加入高斯噪声
    # random_state：生成随机种子，给定一个int型数据，能够保证每次生成数据相同
    moon_data = make_moons(n_samples=n_samples, noise=0.3, random_state=0)

    # 制造环形样本数据
    # n_samples：设置样本数量
    # noise：设置噪声，小的话比较集中
    # factor：内外圆之间的比例因子，默认值0.8
    # random_state：设置随机参数 （部分）
    circle_data = make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1)

    return [linearly_data,
            moon_data,
            circle_data
            ]


if __name__ == '__main__':
    datasets = make_classifier_data()
    print(datasets)
