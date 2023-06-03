#  Task
# 1、统计文件行数
# 2、统计不包含空行的行数
# 3、统计单词 I 出现的次数
# 4、统计单词 you 和 You 出现的次数
import pprint

with open("./text.txt") as file:
    file_data = file.readlines()
    pprint.pprint(file_data)

    # 统计文件行数
    row_number = len(file_data)
    print('统计文件行数:', row_number)

    # 统计不包含空行的行数
    print('统计非空行的行数：', len(file_data) - file_data.count("\n"))
    print('统计非空行的行数：', len(set(file_data)) - 1)

    # 统计单词 I 出现的次数
    print('统计单词 I 出现的次数:', str(file_data).split(" ").count("I"))

    # 统计单词 you 和 You 出现的次数
    you_count = int(str(file_data).split(" ").count("you"))
    You_count = int(str(file_data).split(" ").count("You"))
    print('统计单词 you 和 You 出现的次数:', you_count + You_count)

    print(set(file_data))

