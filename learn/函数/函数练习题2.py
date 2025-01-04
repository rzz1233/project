# 1. 某种传染病第一天只有一个患者，前五天为潜伏期，不发作也不会传染人 第6天开始发作，从发作到治愈需要5天时间
# ，期间每天传染3个人 求第N天共有多少患者
# def patients(N):
#     if 1 <= N <= 5:
#         return 1  # 第1天到第5天，只有1个患者
#     elif 6 <= N <= 10:
#         return 1 + (N - 5) * 3
#     else:
#         return 15 + (N - 8) * 3  # 第11天及以后，每天新增3个患者，患者数量稳定在13个
# N = int(input("请输入天数："))
# patients(N)
# print(f"第{N}天共有{patients(N)}名患者。")
def patients_on_day(N):
    if N < 1:
        return 0
    elif N == 1:
        return 1
    elif N <= 5:
        return 1
    else:
        # Starting from day 6
        patients = 1  # Initial patient count
        for day in range(6, N + 1):
            patients += 2  # Each day adds 2 patients
        return patients

# Example usage:
N = 7
total_patients = patients_on_day(N)
print(f"Total patients on day {N}: {total_patients}")
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

