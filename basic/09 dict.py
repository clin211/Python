import json

user = {'nickname': 'clin', 'age': 23, 'add': 'cd'}
print(user)  # {'nickname': 'clin', 'age': 23, 'add': 'cd'}

device = dict(name='xiaomi')
print(device)  # {'name':'xiaomi'}

nums = {x: x ** 2 for x in range(5)}
print(nums)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 已知有两个列表，分别为: [ 'name1', 'name2', 'name3' ], ['1111', '2222', '3333']; 现需要将这两个列表组成一个如下字典，请编写程序实现：	{ 'name1':'1111',
# 'name2':'2222', 'name3':'3333' }
key = ['name1', 'name2', 'name3']
value = ['1111', '2222', '3333']

print(dict(zip(key, value)))
print(zip(key, value))

mail_list = {'tom': 'tom@gmail.com',
             'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}

# 访问列表里的所有元素
mail_list.items()
print('get list items:', mail_list.items())

# 获取所有的key
print('get keys:', mail_list.keys())

# 获取所有的values

# get values: dict_values(['tom@gmail.com', 'jerry@foxmail.com', 'john@163.com'])
print('get values:', mail_list.values())

print('get only value:', mail_list.get('tom'))  # get only value: tom@gmail.com
print('mail list tom:', mail_list['tom'])  # mail list tom: tom@gmail.com

for key, value in mail_list.items():
    print('key:', key)
    print('value:', value)

tom_mail = mail_list.setdefault('tom2')
print(tom_mail)
print(mail_list)

mail_list['tom2'] = 'tom2@gamil.com'

# {'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'tom2': 'tom2@gamil.com'}
print(mail_list)

print('length:', len(mail_list))  # 4
mail_list.pop('tom')
# {'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'tom2': 'tom2@gamil.com'}
print(mail_list)

# 移除字典中的最后一个元素
popItem = mail_list.popitem()
print(popItem)  # ('tom2', 'tom2@gamil.com')

# 设置默认值
tom_mail = mail_list.setdefault('tom')
print(tom_mail)  # tom@gmail.com
print(mail_list)  # {'tom': 'tom@gmail.com', 'jerry': 'jerry@foxmail.com', 'john': 'john@163.com'}

tom_mail = mail_list.setdefault('tom2', 'abc.@abc.com')
print(tom_mail)  # abc.@abc.com
print(mail_list)  # {'jerry': 'jerry@foxmail.com', 'john': 'john@163.com', 'tom2': 'abc.@abc.com'}

# 设计一个字典数据类型用于存储通讯录，通讯录中包含：必须填写的姓名、可以为空的备注名、1 个邮箱，至少 2 个手机号码，并尝试增加和删除联系人。
address_book = [
    {'name': 'John Smith', 'nickname': 'Johnny', 'email': 'john.smith@example.com',
     'phone_number': ['+1 555-123-4567', '+1 555-987-6543']},
    {'name': 'Emily Davis', 'nickname': 'Em', 'email': 'emily.davis@example.com',
     'phone_number': ['+1 555-777-8888']}
]
# create
new_user = {'name': 'Bob Johnson', 'nickname': 'Bobby', 'email': 'bob.johnson@example.com', 'phone_number': ['+1 555-333-4444', '+1 555-555-5555']}
address_book.append(new_user)
print(json.dumps(address_book, indent=4))

# delete
for item in address_book:
    if item.get('nickname') == 'Andrew':
        address_book.remove(item)
print(json.dumps(address_book, indent=4))

# update
for index, item in enumerate(address_book):
    if item['nickname'] == 'Em':
        address_book[index]['phone_number'][0] = '+2 222-1234-1234'
print(json.dumps(address_book, indent=4))
