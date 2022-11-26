
nums = [1, 2, 3, 4, 5, 6, 7]
chars = ['aa', 'bb', 'cc']
mixture = [1, 'a', True, 3.14]

numbers = [x for x in range(1, 10)]
print(numbers)


lists = ['a', 'b', [1, 2, 3, 4]]
print(lists[2][0])  # 1

# 删除下标为0的元素
del lists[0]
print(lists)  # ['b', [1, 2, 3, 4]]

# 删除lists这个列表
del lists

list_number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_number)


colors = ['red', 'blue', 'green']
print(colors)  # ['red', 'blue', 'green']
print(type(colors))  # <class 'list'>
print(colors[1])  # blue
print(colors[-1])  # green

# colors.insert(0, 'skyblue')
# colors.insert(-1, 'yellow')
# print(colors)  # ['skyblue', 'red', 'blue', 'yellow', 'green']

colors = ['red', 'blue', 'green']
colors.append('white')
print(colors)  # ['red', 'blue', 'green', 'white']

colors = ['red', 'blue', 'green']
colors.extend(['black'])
print(colors)  # ['red', 'blue', 'green', 'black']


colors = ['red', 'blue', 'green']
colors.remove('green')
print(colors)  # ['red', 'blue']

colors = ['red', 'blue', 'green']
colors.reverse()
print(colors)  # ['green', 'blue', 'red']

colors = ['red', 'blue', 'green']
result = colors.pop()
print(f"list is {colors}")  # list is ['red', 'blue']
print(f"result is {result}")  # result is green

colors = ['red', 'blue', 'green']
color = colors.copy()
print(color)  # ['red', 'blue', 'green']

colors = ['red', 'blue', 'green']
colors.clear()
print(colors)  # []

colors = ['red', 'blue', 'green']

print(len(colors))  # 3
print(len(colors[1]))  # 4
print(colors.count('green'))  # 1

l = ['a', 'c', 'c', 'b', 'd']
new_list = sorted(l)
l.sort()
print(new_list)
print(l)
lists = ['a', 1, 'b', 2, 'c', 'c', 3]
while lists.count('c'):
    lists.remove('c')
print(lists)  # ['a', 1, 'b', 2, 3]
