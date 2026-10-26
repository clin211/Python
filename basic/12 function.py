import string

from module import one, two, three
"""
def function_name(arg1, arg2):
    return "something"

- def 是声明函数的关键字
- function_name 是函数名
- arg1，arg2 传入的是参数，是形参
- return 是这个函数返回的关键字
- "something" 就是被返回的结果
"""


# 通过关键字 def 定义求阶乘的函数
# 自变量（参数）num是一个非负整数
# 因变量（返回值）是num的阶乘
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 计算阶乘的时候不需要写重复的代码而是直接调用函数
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
# print(fac(m) // fac(n) // fac(m - n))

# Python 标准库的 math 模块中，已经有一个名为 factorial 的函数实现了求阶乘的功能，我们可以直接用 import math 导入 math 模块，然后使用 math.factorial 来调用求阶乘的函数
from math import factorial

m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))

"""
函数的参数
"""


# 判断三条边的长度能否构成三角形
def make_judgement(a, b, c):
    return a + b > c and b + c > a and a + c > b  # 任意两边之和大于第三边


# 参数的默认值
from random import randrange, random, choices


# 定义摇色子的函数
# 函数的自变量（参数）n表示色子的个数，默认值为2
# 函数的因变量（返回值）表示摇n颗色子得到的点数
def roll_dice(number=2):
    total = 0
    for _ in range(number):
        total += randrange(1, 7)
    return total


# 如果没有指定参数，那么n使用默认值2，表示摇两个骰子
print(roll_dice())

# 传入参数3，变量n被赋值为3，表示摇三个骰子获得点数
print(roll_dice(3))

"""
带默认值的参数必须放在不带默认值的参数之后，否则将产生 SyntaxError 错误
"""


def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c


# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())  # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))  # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))  # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6

# 可变参数
"""
Python 语言中可以通过星号表达式语法让函数支持可变参数。所谓可变参数指的是在调用函数时，可以向函数传入0个或任意多个参数
"""


# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n 元组 赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 因为会被组装成一个元组，所以就直接通过索引的方式获取
    if len(args): print('获取传入的第一个参数', args[0])
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())  # 0
print(add(1))  # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45


# 如果我们希望通过“参数名=参数值”的形式传入若干个参数，具体有多少个参数也是不确定的，我们还可以给函数添加可变关键字参数，把传入的关键字参数组装到一个字典中
# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)
# 执行后结果如下：
# (3, 2.1, True)
# {'name': '骆昊', 'age': 43, 'gpa': 4.95}

# 用模块管理函数
one.func()
two.func()
three.func()


all_chars =string.digits + string.ascii_letters

def generate_verification_code(*, code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度（默认4个字符）
    :return: 有大小写英文字母和数字组成的随机验证码字符串
    """
    return ''.join(choices(all_chars, k=code_len)) # k是一个命名关键字参数，在传参时必须指定参数名

for _ in range(5):
    print(generate_verification_code())
