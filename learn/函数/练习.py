# 1. 写函数，接收n个数字，求这些参数数字的和
# def sum(*args):
#     num = 0
#     for arg in args:
#         num +=arg
#     print(num)
#     return num
# sum(1, 2, 3,4,8)
# 2. 找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# def jishu(alis1):
#     lis2 = []
#     for i in range(len(alis1)):
#         if i==0 or i%2==0:
#             lis2.append(alis1[i])
#     print(lis2)
#     return lis2
# lis1 = [1,2,3,4,5]
# tuple1 = (1,2,3,4,5)
# jishu(tuple1)
# jishu(lis1)

# 3. 写一个函数，判断用户传入的列表长度是否大于2，如果大于2，只保留前两
# 个，并将新内容返回给调用者
# def li(a):
#     if len(a) > 2:
#         lis1 = a[:2]
#         print(lis1)
# li([1,2,3])

# 4. 写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两
# 个长度的内容，并将新内容返回给调用者
# dic = {"k1":"v1v1","k2":[11,22,33,44]}
# #结果：{'k1': 'v1', 'k2': [11, 22]}
# def  zi(**args):
#     for i in args:
#         if len(args[i]) > 2:
#             args[i] = args[i][:2]
#     print(args)
#     return args
# zi(a="111",b=[1,2,3],c="3")

# 5. 轮盘分为三部分: 一等奖, 二等奖和三等奖;
# 轮盘转的时候是随机的,
# 如果范围在[0,0.08)之间,代表一等奖,
# 如果范围在[0.08,0.3)之间,代表2等奖,
# 如果范围在[0.3, 1.0)之间,代表3等奖,
# 模拟本次活动1000人参加, 模拟游戏时需要准备各等级奖品的个数.
import random
# a = 0
# b = 0
# c = 0
# num_stu = 1000
# for i in range(num_stu):
#     ran_num = random.random()
#     if ran_num < 0.08:
#         a += 1
#     elif ran_num < 0.3:
#         b += 1
#     elif ran_num < 1.0:
#         c += 1
# print(f"一等奖有{a}个")
# print(f"二等奖有{b}个")
# print(f"三等奖有{c}个")
# 函数
# def reward(num_stu):
#     a = 0
#     b = 0
#     c = 0
#     for i in range(num_stu):
#         ran_num = random.random()
#         if ran_num < 0.08:
#             a += 1
#         elif ran_num < 0.3:
#             b += 1
#         elif ran_num < 1.0:
#             c += 1
#     print(f"一等奖有{a}个")
#     print(f"二等奖有{b}个")
#     print(f"三等奖有{c}个")
# reward(1000)

# 作业
# 1. 某种传染病第一天只有一个患者，前五天为潜伏期，不发作也不会传染人 第6天开始发作，从发作到治愈需要5天时间
# ，期间每天传染3个人 求第N天共有多少患者(不会)
def patients(N):
    if 1 <= N <= 5:
        return 1  # 第1天到第5天，只有1个患者
    elif 6 <= N <= 10:
        return 1 + (N - 5) * 3
    else:
        return 15 + (N - 8) * 3  # 第11天及以后，每天新增3个患者，患者数量稳定在13个
N = int(input("请输入天数："))
patients(N)
print(f"第{N}天共有{patients(N)}名患者。")

# 2.编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
# import random
# def shaizi(N):
#     sum = 0
#     for i in range(N):
#         a = random.randint(1,6)
#         sum += a
#     print(sum)
# n = int(input("请输入骰子数："))
# shaizi(n)
# 3.编写一个函数，交换指定字典的key和value
# def dic_jh(dic):
#     s = {v:k for k,v in dic.items()}
#     print(s)
# dic1 = {'a':1,'b':2,'c':3}
# dic_jh(dic1)

# 4.编写一个函数cacluate, 可以接收任意多个数, 返回的是一个元组。
# 元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有元素列表
# def cacluate(*args):
#     lis1 = []
#     lis2 = []
#     sum = 0
#     for i in args:
#         sum += i
#     ping = sum/len(args)
#     lis1.append(ping)
#     for b in args:
#         if b>ping:
#             lis2.append(b)
#     lis1.append(lis2)
#     tuple1=tuple(lis1)
#     print(tuple1)
# cacluate(1,2,3,4,5,6)



