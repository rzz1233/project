# 1.给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

# str = input("请输入数字：")
# list = ['','','abc','def',"ghi","jkl","mno","pqrs","tuv","wxyz"]
# list1 = []
# for i in range(len(str)):
#     for j in range(0,len(list)):
#         if j == int(str[i]):
#             list1.append(list[j])
# str2 = list1[0]
# str3 = list1[1]
# lis2 = []
# for a in str2:
#     for b in str3:
#         lis2.append(a+b)
# print(lis2)

# while True:
#     str = input("请输入数字：")
#     list = ['abc','def',"ghi","jkl","mno","pqrs","tuv","wxyz"]
#     lis1 = []
#     str1 = list[(int(str[0])-2)]
#     str2 = list[(int(str[1])-2)]
#     for i in str1:
#         if int(str[0]) < 2 or int(str[1]) < 2:
#             break
#         else:
#             for j in str2:
#                     # str3 = i+j
#                     lis1.append(i+j)
#     print(lis1)


# 2. 将list中的重复数据去重，lst=[1,3,3,5,6,6,7]
# list = [1,3,3,5,6,6,7]
# list1 = []
# for i in list:
#     if i not in list1:
#         list1.append(i)
# print(list1)

# 3.联系人管理：
# 创建一个简易的联系人管理系统，用列表存储联系人的姓名、电话号码和电子邮件地址。系统需要能够添加新联系人、
# 编辑现有联系人信息、删除联系人，并能够按字母顺序或联系人姓名进行排序展示列表。
import copy

from sympy.abc import q
list = []
while True:
    print("*"*50)
    print("\t\t欢迎来到联系人管理系统，我们有以下操作：\n"
          "\t\t\t1. 添加新的联系人\n"
          "\t\t\t2. 编辑现有联系人的信息\n"
          "\t\t\t3. 删除联系人\n"
          "\t\t\t4. 对联系人进行排序\n"
          "\t\t\t5. 查看所有联系人\n"
          "\t\t\tq. 退出系统")
    print("*"*50)
    choice = input("请输入你要进行的操作：")
    if choice == '1':
        # lis_add = []
        name = input("请输入你的要添加的名字：")
        phone = input("请输入你要添加的电话号码：")
        email_addr = input("请输入你要添加的电子邮箱：")
        lis_add = [name, phone, email_addr]
        # lis_add.append(name)
        # lis_add.append(phone)
        # lis_add.append(email_addr)
        list.append(lis_add)
    elif choice == '2':
        name = input("请输入要修改的联系人的姓名：")
        edit_lis = []
        for i in list:
            if name in i:
                index = list.index(i)
                name = input("请输入修改的联系人的姓名：")
                phone = input("请输入修改的联系人的电话：")
                email_addr = input("请输入修改的联系人的邮箱地址：")
                edit_lis.append(name)
                edit_lis.append(phone)
                edit_lis.append(email_addr)
                list[index] = edit_lis
                break
            else:
                print("输入错误")
    elif choice == '3':
        name = input("请输入要删除的联系人的姓名：")
        for i in list:
            if name in i:
                index = list.index(i)
                del list[index]
                break
    elif choice == '4':
        deep = copy.deepcopy(list)
        list.sort()
        print(list)
    elif choice == '5':
        print(list)
    elif choice == 'q':
        print("再见")
        break
