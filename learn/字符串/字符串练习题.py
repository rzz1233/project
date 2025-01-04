#判断回文数
# a = input("请输入数字：")
# for i in range(0,len(a)//2):
#     if a[i] != a[-1-i]:
#         print(a+"不是回文数")
#         break
# else:
#     print(a+"是回文数")

# a = input("请输入数字：")
# b = a[::-1]
# if a == b:
#     print(f"{a}是一个回文数")
# else:
#     print(f"{a}不是一个回文数")


#判断文件类型
# b = input("请输入文件名：")
# list = b.split(".")
# print(f"这是一个{list[-1]}文件")

# 输入两个字符串，从第一个字符串中删除第二个字符串中所有字符。
str1 = input("请输入第一个字符串：")
str2 = input("请输入第二个字符串：")
for i in str2:
    if i in str1:
        str1 = str1.replace(i, "")
print(str1)


