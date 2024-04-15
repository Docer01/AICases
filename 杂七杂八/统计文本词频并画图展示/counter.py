"""
作者：道客儿
V：Docer01
"""

# Counter 可用来统计文本中每个字的数量
from collections import Counter

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

f = open('data/济南的冬天.txt', encoding='utf8')  # encoding 要使用和这个文件对应的编码
txt = f.read()  # 读取全部字符
f.close()

counter = Counter(txt)  # 得到每个字符的出现次数
print(len(counter))

ccc_list = []  # 定义空的列表
for ccc in counter:
    if ccc in "\u3000\n 。,:!！“?…”《》，；—（）-：？^~`[]|":  # 过滤掉常见的标点和空白字符
        continue
    ccc_list.append([counter[ccc], ccc])  # 把字符和字符出现的次数加入列表

ccc_list.sort(reverse=True)  # 降序排序

# 以下代码打印前100的字符和出现次数
for ccc in ccc_list:
    print(ccc[0], ccc[1])

# 图表展示
x = []
y = []
for i, char_cnt in enumerate(ccc_list):
    x.append(i)
    y.append(char_cnt[0])
plt.axis((0, 100, 0, max(y)))
plt.bar(x[:100], y[:100], width=1)
plt.show()