# 装饰器本质上还是函数，让其它的函数在不做任何代码修改的情况
# 下，增加额外的功能

# def f2(func):
#     def f1():
#         x = func()
#         return x + 1
#     return f1
# @f2   # ==> func = f2(func)
# def func():
#     print("这是主函数")
#     return 1
# # 不改变原有代码。增加新的功能
# @f2
# def func2():
#     print("主函数2")
#     return 3
# print(func())
# print(func2())



# def f2(func):
#     def f1():
#         x = func()
#         return x + 1
#     return f1
# # # 原始功能
# def func():
#     print("这是主函数")
#     return 1
# # 函数名([参数列表])
#
# func = f2(func)
# print(func())

import time
def f2(func):
    def f1():
        stat_time = time.time()
        func()
        end_time = time.time()
        print(end_time - stat_time)
    return f1
@f2
def fun1():
    time.sleep(1)
    print("函数1执行完毕")
@f2
def fun2():
    time.sleep(2)
    print("函数2执行完毕")
@f2
def fun3():
    time.sleep(3)
    print("函数3执行完毕")
fun1()
fun2()
fun3()
# stat_time = time.time()
# fun1()
# end_time = time.time()
# print(end_time - stat_time)