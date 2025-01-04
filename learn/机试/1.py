# 一、定义一个函数，向函数内传入形参num, num1, num2，如果num小于100，则计算num1 和 num2的积并打印；否则计算num1和num2的和，然后打印输出；
#
# 1、定义函数名为oper的函数
# 2、当num值小于100时，求两数的乘积，反之求两数的和
# 3、调用函数，向函数内传入1314, 52, 0和5, 2, 0两组数据测试结果

def oper(num,num1,num2):
    sum = 0
    if num < 100:
        sum = num1 * num2
        print(sum)
    else:
        sum = num1 + num2
        print(sum)

oper(1314,52,0)
oper(5,2,0)

