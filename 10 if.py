height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2

# 字符串拼接
print(f'{bmi = :.1f}')

# if语句的最后面有一个:，它是用英文输入法输入的冒号
if 18.5 <= bmi < 24:
    print('你的身材很棒！')

# if else 的应用
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
else:
    print('你的身材不够标准哟！')

# if elif else 的使用
if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')

# if elif else 改造成 match case 的形式
status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
else:
    description = 'Unknown status Code'

print('状态码描述:', description)

# 使用 match 和 case 构造分支结构
status_code = int(input('响应状态码: '))
match status_code:
    case 400:
        description = 'Bad Request'
    case 401:
        description = 'Unauthorized'
    case 403:
        description = 'Forbidden'
    case 404:
        description = 'Not Found'
    case 405:
        description = 'Method Not Allowed'
    case _:
        description = 'Unknown Status Code'

print('状态码描述:', description)

# 合并模式：将多个条件纳入一个分支判断中
status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405:
        description = 'Invalid Request'
    case 401 | 403 | 404:
        description = 'Not Allowed'
    case _:
        description = 'Unknown Status Code'
print('状态码描述:', description)

# 例子2：百分制成绩转换为等级制成绩
# 要求：
# 如果输入的成绩在90分以上（含90分），则输出A；
# 输入的成绩在80分到90分之间（不含90分），则输出B；
# 输入的成绩在70分到80分之间（不含80分），则输出C；
# 输入的成绩在60分到70分之间（不含70分），则输出D；
# 输入的成绩在60分以下，则输出E。

score = float(input("请输入成绩："))
if score >= 90:
    print('A')
elif score >=80:
    print('B')
elif score >= 70:
    print('C')
elif score >=60:
    print('D')
else:
    print('E')


# 计算三角形的周长和面积。
# 要求：输入三条边的长度，如果能构成三角形就计算周长和面积；否则给出“不能构成三角形”的提示。
# 也就是任意两边之和大于第三边，这是构成三角形的必要条件
a = float(input("边长 a 为："))
b = float(input("边长 b 为："))
c = float(input("边长 c 为："))

if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    print(f'周长为： {p}')
    s = p / 2
    area = (s * (s - a) * (s - b) * (s - c)) / 2
    print(f'面积为： {area}')
else:
    print('不能构成三角形！')
