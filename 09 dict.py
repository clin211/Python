user = {'nickname': 'clin', 'age': 23, 'add': 'cd'}
print(user)  # {'nickname': 'clin', 'age': 23, 'add': 'cd'}

device = dict(name='xiaomi')
print(device)  # {'name':'xiaomi'}

nums = {x: x**2 for x in range(5)}
print(nums)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# 已知有两个列表，分别为: [ 'name1', 'name2', 'name3' ], ['1111', '2222', '3333']; 现需要将这两个列表组成一个如下字典，请编写程序实现：	{ 'name1':'1111', 'name2':'2222', 'name3':'3333' }

key = ['name1', 'name2', 'name3']
value = ['1111', '2222', '3333']
print(dict(zip(key, value)))
print(zip(key, value))
