# - 定义字符串可以使用一下三种方式：
#   - 单引号''
#   - 双引号 ""
#   - 三重引号""" """ 或者 ''' '''

print('name')  # name
print("name")  # name
print("""name""")  # name

# 转义
print('hello \'Python\'')  # hello 'Python'
print("hello \"Python\"")  # hello "Python"
print("""hello 'Python'""")  # hello 'Python'

# 字符串中使用变量
# 需要再字符串中插入变量的值时，可以使用 f-string
# f-string 的用法

# f"{variable}" f-string  需要再Python3.6 以上版本

age = 23
print(f"age: {age}")  # age: 23

# in 关键字 在某个字符串中是否包含某个字符
print("x" in "1324X4321")  # False
print("x" in "1324x4321")  # True


print("x" not in "1234")  # true


str1 = "abc"
str2 = "xyz"
print(str1 + str2)  # abcxyz
print(str1 * 3)  # abcabcabc
print(str1)
print(str1[-1])  # c -1获取最后一个字符
print(str1[0])  # b
print(str1[0:2])  # ab
print(str1[0:2:1])  # ab
name = 'forest'
print(name[0:-1:1])


address = 'chengdu city'
print(address.count('c'))  # 2

email = '767425412@qq.com'
print(email.isalnum())  # False

chars = "abcdefg"
print(chars.isalnum())  # True
print(",".join(chars))  # a,b,c,d,e,f,g

strs = "a,b,c,d,e,f,g"
print(strs.split(","))  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']


print(chars.startswith('a'))  # True

# 统计一下文章中单词 better 出现的次数，并进行输出。
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
p = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex."""
print(p.count('better'))

# 请编写程序，在程序运行后提示用户输入自己的名字，并将名字的首字母改为大写并输出 Hello 用户名
nickname = input("input your name: \n")
joinNickname = f"Hello {nickname[0].upper()}{nickname[1:]}"
joinNickname = f"Hello {nickname.capitalize()}"
print(joinNickname)
