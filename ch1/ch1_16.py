import math

myList = [1, 4, -5, 10, -7, 2, 3, 1]
filtered_myList = [n for n in myList if n > 0]
print(filtered_myList)

sqrt_myList = [math.sqrt(n) for n in myList if n > 0]
print(sqrt_myList)

# 对于筛选数据，另一种情况是用新值替换掉不满足标准的值
clip_neg = [n if n > 0 else 0 for n in myList]
print(clip_neg)

# itertools.compress() 压缩 把对一个序列的筛选结果施加到另一个相关的序列上。
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]

print(more5)

compressed_list = list(compress(addresses, more5))
print(compressed_list)

