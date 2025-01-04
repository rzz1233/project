# def pri():
#    print("www")
# pri()
# def add(a,b):
#    sum = a+b
#    return sum
# add(1,2)
# print("输出为：",add(1,2))
# def stri(a,b,sex='男'):
#    print(f"我叫{a},今年{b}岁,性别是{sex}")
#    print(3)
#
# stri('rzz',21)
# stri(b='23',a='szy')
# stri('gzy',18,'女')

# def a(list):
#    list.append(1)
#    print(list)
# def b(str1):
#    str1+='a'
#    print(str1)
# lis1 = [1,2,3]
# str = '123'
# a(lis1)
# b(str)
# print(lis1,str)
# 写函数,判断用户传入的对象(string,list,tuple)长度是否大于5
# def dx(str,list,tuple):
#    if len(str) > 5:
#       print(f"{str}长度大于5")
#    else:
#       print(f"{str}长度小于5")
#    if len(list) > 5:
#       print(f"{list}长度大于5")
#    else:
#       print(f"{list}长度小于5")
#    if len(tuple) > 5:
#       print(f"{tuple}长度大于5")
#    else:
#       print(f"{tuple}长度小于5")
# dx('123',[1,2,3,6],(1,2,3))

# lambda
sum = lambda a,b: a+b
print(sum(1,2))

def fun(a,b,func):
   return func(a,b)
print(fun(1,2,lambda a,b: a+b))

f1 = lambda a,b: a if a > b else b
print(f1(1,2))
#lambda排序
lis1 = [{'age':15},{'age':16}]
dic2 = sorted(lis1,key=lambda x:x['age'])
print(dic2)







