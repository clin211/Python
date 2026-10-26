import time

from adbutils.shell import is_percent

# 重复打印 3600 次 hello  world，每隔1秒打印一次
"""
    for in 循环
"""
# for-in
# for i in range(3600):
#     print('hello, world')
#     time.sleep(1)

# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。

# 空白标识符 _
# for _ in range(3600):
#     print('hello, world')
#     time.sleep(1)

# 用for-in循环实现从1到100的整数求和
total = 0
for i in range(1, 101):
    total += i

print(total)

# 从1到100的偶数求和
total1 = 0
for i in range(2, 101, 2):
    total1 += i
print(total1)  # 2550

# Python 内置了 sum 函数
print(sum(range(2, 101, 2)))  # 2550

"""
    while 循环：不能确定循环重复的次数，我们推荐使用while循环，while循环通过布尔值或能产生布尔值的表达式来控制循环，当布尔值或表达式的值为True时，循环体（while语句下方保持相同缩进的代码块）中的语句就会被重复执行，当表达式的值为False时，结束循环。
"""

# 用while循环来实现从1到100的整数求和
total = 0
i = 0
while i <= 100:
    total += i
    i += 1

print(total)  # 5050

# break 和 continue
# break只能终止它所在的那个循环
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break  # 当 i 大于 100 的时候，终止循环结构的执行
print(total)  # 2550

# continue 则是用来放弃本次循环，直接进入下一轮循环
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue  # 使用 continue 关键字跳过了 i 是奇数的情况，只有在 i 是偶数的前提下，才会执行到 total += i。
    total += i
print(total)

# 嵌套的循环结构
# 通过嵌套的循环来输出一个乘法口诀表（九九 乘法表）
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i * j}", end='\t')
    print("")

# 输入一个大于1的正整数判断它是不是素数；素数指的是只能被1和自身整除的大于1的整数
num = int(input("请输入一个正整数："))
end = int(num ** 0.5)  # 获取平方根
print(f'end：{end}')

is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')


# 最大公约数
# 要求：输入两个大于0的正整数，求两个数的最大公约数。
#
# 提示：两个数的最大公约数是两个数的公共因子中最大的那个数。
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')