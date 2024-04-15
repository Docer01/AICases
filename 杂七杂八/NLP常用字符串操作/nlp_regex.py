"""
author：道客儿
V：Docer01
"""

import re

# * ：0个或多次匹配
# + ：1个或多次匹配
# ? ：0个或1次匹配
# {N} : 匹配N次
# {M, N} : 匹配M~N次
# re.search会匹配整个字符串，并返回第一个成功的匹配。如果匹配失败，则返回None
# print(re.search('meng?', 'mengxiaoxin'))
# print(re.search('meng?', 'meng'))
# print(re.search('mang?', 'meng'))
#
# print(re.search('meng*', 'mengxiaoxin'))
# print(re.search('meng*', 'meng'))
# print(re.search('mang*', 'meng'))
#
# print(re.search('meng+', 'mengxiaoxin'))
# print(re.search('meng+', 'meng'))
# print(re.search('mang+', 'meng'))
#
# print(re.search('me{2}', 'meent'))
# print(re.search('me{2,5}', 'meeent'))

# $ ：结尾
# ^ ：开头
# . ：除换行符以外的任何字符
# \w ：字母，数字，下划线
# \d ：数字
# \s ：空格符
# \S ：非空格符
# \b ：空格
# \B ：非空格
# # 匹配以m开头，以g结尾
# print(re.search('^m.*g$', 'meng'))
# # 以文本开始，后面有出现一次或多次的文本
# print(re.search('^\w+', 'meng xiao xin'))
# # 匹配中间含e的单词
# print(re.search('\Be\B', 'meng xiao xin'))

# re.split方法，根据正则表达式分割字符串，可以用户简单的分词
# re.split(pattern, string, maxsplit=0, flags=0)
# pattern：分隔符的意思，可以是字符串，也可以为正则表达式
# string：要进行分割的字符串
# maxsplit：分割的最大次数
# flags默认值为0，表示分割次数无限制，能分几次分几次；取负数，表示不分割；若大于0，表示最多分割maxsplit次；
# s = 'HI, meng xiao xin!'
# print(re.split(r' +', s))
# print(re.split(r'\W+', s))
# print(re.findall(r'\w+|\S\w*', s))
