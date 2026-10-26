# 输入两个数字后输入运算符，然后根据输入的运算符输出结果
first = int(input('input first number: '))
second = int(input('input second number: '))

os = input("enter the operation symbol(+、-、*、/): ")
print(eval(f"{first}{os}{second}"))
