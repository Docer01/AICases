# 1、大小写转换
# print("meng xiao XIN".upper())       # 字符串转换为大写
# print("meng xiao XIN".lower())       # 字符串转换为小写
# print("meng xiao XIN".swapcase())    # 字符串大小写反转
# print("meng xiao XIN".title())       # 字符串中所有单词首字母大写，其余小写
# print("meng xiao XIN".capitalize())  # 字符串仅第一个单词首字母大写，其余小写

# 2、is判断相关函数
# print("3.14".isdigit())           # 判断字符串是否全为数字字符
# print("3.14".isdecimal())         # 判断字符串是否为十进制数字符
# print("3.14".isnumeric())         # 判断字符串是否所有字符均为数值字符
# print("mengxin123".isalpha())    # 判断字符串是否全为字母
# print("mengxin123".isalnum())    # 判断字符串是否只含有数字和字母
# print("meng xiao XIN".isupper())  # 判断字符串是否是全大写
# print("meng xiao XIN".islower())  # 判断字符串是否是全小写
# print("meng xiao XIN".istitle())  # 判断字符串中所有单词首字母大写，其余小写
# print("n".isspace())             # 判断字符串是否为空白符（空格、换行（n）、制表符（t））
# print("t".isprintable())         # 判断字符串是否可打印字符（只有空格可以，换行和制表符都不可以）
# print("_mengmengda".isidentifier())      # 判断字符串是否符合命名规则（只能字母/_开头，名字只能包含数字、字母和_）

# 3、去掉特定字符
# strip([chars]):删除前导和尾随指定字符串char
# lstrip([chars]):只删字符串左侧（开头）的指定char
# rstrip([chars]):只删字符串右侧（结尾）的指定char
# 示例中增加"-end"是为了显示字符串后面的空格
# text = "     hello      "
# print("before strip:", text + "-end")
# print("after  strip:", text.strip(" ") + "-end")
# print("after lstrip:", text.lstrip(" ") + "-end")
# print("after rstrip:", text.rstrip(" ") + "-end")

# 4、字符串开始与结尾判断
# startswith(prefix[,start[,end]]):判断函数的开始字符串是否为prefix
# endswith(suffix[,start[,end]])：判断函数的结尾字符串是否为suffix
# print("hello".startswith("he"))
# print("hello".startswith("ho"))
# print("hello".endswith("lo"))
# print("hello".endswith("1o"))

# 5、查找字符串
# in 查找字符串中是否有子串
# find(sub[,start[,end]])  ：返回sub第一个字符第一次出现的位置，若无则返回-1
# rfind(sub[,start[,end]]) ：返回从右开始数sub第一个字符第一次出现的位置，无则返-1
# index(sub[,start[,end]]) ：返回sub第一个字符第一次出现的位置，若无则报错
# rindex(sub[,start[,end]])：返回从右开始数sub第一个字符第一次出现的位置，无则报错
# count(sub[,start[,end]]) ：判断指定字符串是否具有子串sub，若有则返回出现次数
# s = "meng xiao XIN"
# print("xiao" in s)
# print(s.find("xiao"))
# print(s.rfind("xiao"))
# print(s.index("xiao"))
# print(s.rindex("xiao"))
# print(s.count("xiao"))

# 6、字符串填充
# center(width，fillchar)：填充物在字符串两边，with为填充后长度
# ljust(width，fillchar)：填充物在字符串左边
# rjust(width,fillchar):填充物在字符串右边
# zfill(width)：居右填充，填充物固定为0，自动识别字符串的正负号，
# print("meng".center(10, "*"))
# print("meng".ljust(10, "*"))
# print("meng".rjust(10, "*"))
# print("66".zfill(10))
# print("-66".zfill(10))
# print("+66".zfill(10))

# 7、字符串拆分
# partition(sep）：将string分为sep前、sep、sep后三部分
# split(sep,maxsplit)：将string按sep拆分成数组，maxsplit可选参数，用于指定拆分的次数
# s = "mengxiaoxin"
# print(s.partition("xiao"))
# print(s.split("xiao"))

# 8、字符串连接
# +连接
# join()：将可迭代数据用字符串连接起来
# s1 = "123"
# s2 = "abc"
# print(s1 + s2)
# s = "mengxin"  # 字符串类型
# print('_'.join(s))
# t = ('meng', 'xiao', 'xin')  # tuple类型
# print('-'.join(t))
# e = {'meng', 'xiao', 'xin'}  # set类型
# print(".".join(e))  # 注意打印顺序不一定是meng.xiao.xin

# 9、字符串替换
# replace(old,new[,count]):# old为旧string，new为新string，count可选代表更改个数
# s = "mengxiaoxin"
# print(s.replace("xiao", "da"))

# 10、组合多个字符串
# a1 = ["meng", "xiao", "xin"]
# a2 = ["bang", "bang", "da"]
# for x, y in zip(a1, a2):
#     print(x, y)

# 11、字符串反转
# python没有反转方法，可以先将字符串切片成列表，然后利用列表的反转方法进行反转。
# s = "mengxiaoxin"
# print(s[::-1])

# 12、回文(正反读都一样的词语)识别。例如，level就是回文
def is_palindrome(s):
    reverse = s[::-1]
    if reverse == s:
        return True
    return False
print(is_palindrome("level"))
print(is_palindrome("meng"))
