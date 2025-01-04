#1. 用闭包的形式，写出能打印如下结果的函数
# 期末成绩公布了：
# 小吕：语文：90
# 期末成绩公布了：
# 王哥：语文：95
# 王哥：数学：89
def fun1(str1):
    print(str1)
    def fun2():
        print('小吕：语文：90')
        print(str1)
        print('王哥：语文：95')
        print('王哥：数学：89')
    return fun2

a = fun1("期末成绩公布了：")
a()

# 2.请使用lambda表达式将下边函数转变为匿名函数？
# def fun_A(x,y=3):
# return x*y

# sum = lambda x,y: x*y
# print(sum(3,3))

# 请将下边的匿名函数转变为普通函数？
# lambda x:x if x%2 else None
# def fun1(x):
#     if x%2==0:
#         print(x)
#     else:
#         print("None")
# fun1(1)

# 请目测以下表达式会打印什么？
# def make_repeat(n):
#     return lambda s:s*n
# double = make_repeat(2)
# print(double(8))
# print(double("FISHC"))

# 16
# FISHCFISHC

#  5.编写一个函数, 接收字符串参数, 返回一个元组,
# 元组的第一个值为大写字母的个数, 第二个值为小写字母个数.
# def fun1(str):
#     count = 0
#     sum = 0
#     tuple1 = tuple()
#     for i in str:
#         if ord(i)>=97 and ord(i)<=122:
#             sum += 1
#         elif ord(i)>=65 and ord(i)<=90:
#             count += 1
#     tuple1 = (count,sum,str)
#     return tuple1
# str1 = "Strive"
# print(fun1(str1))

# 登录
# 原始函数：只判断长度 6~12位
# 增加的功能：你们自己填   判断里面有没有特殊字符
def f2(func):
    def f1(str1):
        str2 = "@#$&"

        for i in range(0,len(str1)):
            if str1[i] in str2:
                func(str1)
                break
        else:
            print("密码格式不对，没有特殊字符。")
    return f1
def f3(func):
    def f4(str1):
        for i in range(0,len(str1)):
            if ord(str1[i]) >= 65 and ord(str1[i]) <= 90:
                func(str1)
                break
        else:
            print("密码格式不对，没有大写字母。")
    return f4
@f2
@f3
def fun(str1):
    if len(str1) >6 and len(str1) <12:
        print("登录成功")
    else:
        print("密码错误，长度不对")
pw = input("请输入你的密码：")
fun(pw)