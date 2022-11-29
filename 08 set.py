color = ('r', 'g', 'b', 'a', 'g', 'p', 'b')

new_color = set(color)  # 转换为set类型
print(new_color)  # {'r', 'a', 'g', 'b', 'p'}
new_color2 = tuple(new_color)  # 转换为元组类型
print(new_color2)  # ('p', 'a', 'r', 'b', 'g')

# 请使用集合删除列表中重复的元素，并将其转换为元组在命令行进行输出。
# list1 = [ 'r', 'g', 'b', 'g', 'b', 'r', 'g' ]
list1 = ['r', 'g', 'b', 'g', 'b', 'r', 'g']
new_list = tuple(set(list1))
print(new_list)  # ('g', 'b', 'r')
