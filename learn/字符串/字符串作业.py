a = "aAsomr3idd4HGHbigs7Dlsf9YeAF"
# 1. 请将a字符串的大写改为小写，小写改为大写
# print(a.lower())
# print(a.upper())

# 2.将a字符串的数字取出，并输出成一个新的字符串。
# str = ""
# for i in a:
#     str1 = i.isdigit()
#     if str1 == True:
#         str += i
# for b in str:
#     if b in a:
#         a = a.replace(b,"")
# print(a)

#3.反向输出
# str = a[-1:-len(a)-1:-1]
# print(str)

# 4.打印a字符串中所有奇数位上的字符(下标是1，3，5，7…位上的字符)
# for i in range(0,len(a),2):
#     print(a[i],end="")

# 5.将a字符串的所有偶数位上的字符取出，判断是否为回文字符串
# str1 = a[1:len(a):2]
# print(str1)
# for i in range(0,len(str1)//2):
#     if str1[i] != str1[-1-i]:
#         print(str1+"不是回文数")
#         break
# else:
#     print(str1+"是回文数")

# 6.输出a字符串出现频率最高的字母
# max_sum = 0
# for i in range(0,len(a)):
#     sum = a.count(a[i])
#     if sum > max_sum:
#         max_sum = sum
# for i in range(0,len(a)):
#     sum1 = a.count(a[i])
#     if sum1 == max_sum:
#         print(a[i])
# 7.去除a字符串多次出现的字母，仅留最先出现的一个。
# str1 = ""
# str3 = ""
# for i in range(0,len(a)):
#     sum = a.count(a[i])
#     if sum > 1:
#         str1 += a[i]
# str2 = str1.strip(str1[0])
# for b in str2:
#     if b in a:
#         a = a.replace(b,"")
# print(a)

# 去重
# b = ""
# for i in a:
#     if i not in b:
#         b += i
# print(b)

# 8.去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。
# str = ""
# for i in a:
#     str1 = i.isdigit()
#     if str1 == True:
#         str += i
# for b in str:
#     if b in a:
#         a = a.replace(b,"")
# sort = "".join(sorted(a))
# print(sort)

# 9.输出a字符串出现频率最低的字母
# str = ""
# for i in a:
#     str1 = i.isdigit()
#     if str1 == True:
#         str += i
# for b in str:
#     if b in a:
#         a = a.replace(b,"")
#
# min_sum = len(a);
# for i in range(0,len(a)):
#     sum = a.count(a[i])
#     if sum < min_sum:
#         min_sum = sum
# for i in range(0,len(a)):
#     sum1 = a.count(a[i])
#     if sum1 == min_sum:
#         print(a[i],end="")

# 10.输入用户名，判断用户名是否合法(用户名长度6~10位)
# str1 = input("请输入用户名：")
# if len(str1) >6 and len(str1) < 10:
#     print("用户名合法")
# else:
#     print("用户名不合法")

# 11.对字符串的旋转操作描述如下：例如：str = "123456"，str的所有旋转词为：
# "123456"，"234561", "345612", "456123", "561234", "612345"。
#     给定两个字符串 str1 和str2，请判断str1是否是str2的旋转词

# str1 = input("请输入str1：")
# str2 = input("请输入str2：")
# str3 = str2+str2
# if len(str1) != len(str2):
#     print("str1不是str2的旋转词")
# elif str1 in str3:
#     print("str1是str2的旋转词")
# else:
#     print("str1不是str2的旋转词")

str1 = "123456"

str2 = str1+str1
for i in range(len(str1)):
    str = str2[i:i+6]
    print(str)







