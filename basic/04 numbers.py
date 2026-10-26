floatNumber = 1234.56
print(int(floatNumber))  # 1234
# type() 获取当前值的类型
print(type(floatNumber))  # <class 'float'>


num = 1234
print(type(num))  # <class 'int'>

text = "1234"
print(type(text))  # <class 'str'>
text = int(text)
print(type(text))  # <class 'int'>

# 请你编写程序，让用户通过命令行输入两个整数，输入完成后，程序自动计算两个整数的和。

num1 = input("input first number: ")
num2 = input("input second number: ")
print("sum: %d\n", int(num1) + int(num2))
