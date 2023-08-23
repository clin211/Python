import json

from tinydb import Query, TinyDB

# 读取文件
with open("./address_book.csv") as f:
    file_data = f.readlines()

f1 = {
    "name": file_data[0].split(",")[0],
    "source": file_data[0].split(",")[1],
    "phone": file_data[0].split(",")[2].strip(),
}
f2 = {
    "name": file_data[1].split(",")[0],
    "source": file_data[1].split(",")[1],
    "phone": file_data[1].split(",")[2].strip(),
}
f3 = {
    "name": file_data[2].split(",")[0],
    "source": file_data[2].split(",")[1],
    "phone": file_data[2].split(",")[2].strip(),
}

"""
问题：
1、假如文件中有更多的行怎么简便处理？
2、怎样知道已经处理完所有行的数据？
3、如果文件格式不规范怎么办？
4、这么写很啰嗦，有没有更优雅的写法？
"""

db = TinyDB("./db.json")

# 将所有数据插入到数据库
db.insert_multiple([f1, f2, f3])


# 查看通讯录中全部好友
print(json.dumps(db.all(), indent=4))


# 根据姓名查电话号码
friend = Query()
friend_info = db.search(friend.name == "张三")

print(friend_info)
print(f"{friend_info[0]['name']}的电话号码是:{friend_info[0]['phone']}")
"""
TinyDB 是纯Python 实现的数据库
它还能支持更新、删除、复杂查询等操作
更多功能请参考官方文档 https://pypi.org/project/tinydb/
"""
