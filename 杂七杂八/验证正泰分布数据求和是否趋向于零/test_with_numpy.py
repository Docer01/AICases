"""
author：道客儿
V：Docer01
"""

import numpy as np

print("-----10个数字的均值与和-----")
a = np.random.randn(10)
print(a.mean())
print(a.sum())
print("-----100个数字的均值与和-----")
b = np.random.randn(100)
print(b.mean())
print(b.sum())
print("-----1000个数字的均值与和-----")
c = np.random.randn(1000)
print(c.mean())
print(c.sum())
print("-----10000个数字的均值与和-----")
d = np.random.randn(10000)
print(d.mean())
print(d.sum())
print("-----100000个数字的均值与和-----")
e = np.random.randn(100000)
print(e.mean())
print(e.sum())
print("-----1000000个数字的均值与和-----")
e = np.random.randn(1000000)
print(e.mean())
print(e.sum())

print("********************************")
print("结论：对于均值为0，方差为1的向量，数据量越大，均值越接近0，而和的绝对值越来越大。")
print("********************************")
