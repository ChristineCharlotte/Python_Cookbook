from collections import ChainMap

# 将多个映射合并为单个映射

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
# print(c)
#
# print(c['x'])
# print(c['y'])
# print(c['z'])
# print(len(c))

c['z'] = 10
c['w'] = 40

del c['y']

print('c', c)

