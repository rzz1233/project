# 1. 编写一个程序，该程序从控制台接受一个逗号分隔的数字序列，并生成一个列表和一个包含每个数字的元组。假设向该程序提供了以下输入：34,67,55,33,12,98
# 然后，输出应为：
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# str1 = input("请输入一个逗号分隔数字序列：")
# print(str1.split(","))
# print(tuple(str1.split(",")))

# 2. 编写一个接受句子并计算字母和数字数量的程序。假设将以下输入提供给程序：
# hello world! 123
# 然后，输出应为：
# 字母： 10个
# 数字： 3个

# str1 = input("请输入：")
# str2 = ""
# str3 = ""
# for a in str1:
#     if a.isalpha() == True:
#         str3 += a
# print("字母：",len(str3),"个")
# for i in str1:
#     if i.isdigit() == True:
#         str2 += i
# print("数字：",len(str2),"个")

# 3. 编写一个程序，以给定的数字作为a的值来计算a + aa + aaa + aaaa的值。
# 假设将以下输入提供给程序：
# 9
# 输出的结果应当为：11106
# a = int(input("请输入数字："))
# num1 = int(str(a)+str(a))
# num2 = int(str(a)+str(a)+str(a))
# num3 = int(str(a)+str(a)+str(a)+str(a))
# sum = a+num1+num2+num3
# print(sum)

# 4. 网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码是否有效。
# 以下是检查密码的标准：
# [az]之间至少1个字母
# [0-9]之间至少1个数字
# [AZ]之间至少1个字母
# [$＃@]中的至少1个字符
# 交易密码的最小长度：6
# 交易密码的最大长度：12
# 您的程序应接受逗号分隔的密码序列，并将根据上述条件进行检查。符合条件的密码将被打印，每个密码之间用逗号分隔。
# 例子：如果输入以下密码作为程序输入：ABd1234@1,a F1#,2w3E*,2We3345。 然后，程序的输出应为：ABd1234@1
# str1 = input("请输入密码：")
# lis1 = str1.split(",")
# str2 = "abcdefghijklmnopqrstuvwxyz"
# str3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# str4 = "$＃@"
# for i in lis1:
#     lower = False
#     upper = False
#     num = False
#     spe = False
#     for j in i:
#         if j in "0123456789":
#             num = True
#         elif j in str2:
#             lower = True
#         elif j in str3:
#             upper = True
#         elif j in str4:
#             spe = True
#     if num and lower and upper and spe and len(i)>=6 and len(i)<=12:
#         print(i)


# 5. 根据以下菜单数据，结合用户权限，输出用户对应的菜单列表
#
# menuList = [
#     {"name":"用户管理",'roles':['superAdmin','admin']},
#     {"name":"角色管理",'roles':['superAdmin']},
#     {"name":"菜单管理",'roles':['superAdmin','admin']},
#     {"name":"日志管理",'roles':['superAdmin','admin','user']},
#     {"name":"资产管理",'roles':['admin','user']},
#     {"name":"财务管理",'roles':['admin','user']}
#]
# user_menu = []
# user_menu_dict = {}
# user_menu_res = []
# for menu in menuList:
#     roles_num = len(menu['roles'])
#     for i in range(roles_num):
#         # print(menu['roles'][i], menu['name'])
#         user_menu.append({menu['roles'][i]: menu['name']})
# # print(user_menu)
# for menu in user_menu:
#     for key, value in menu.items():
#         if key in user_menu_dict:
#             user_menu_dict[key].append(value)
#         else:
#             user_menu_dict[key] = [value]
# # print(user_menu_dict)
# user_menu_res.append(user_menu_dict)
# print(user_menu_res)
#


# userList = [
#     {"username":"zhangsan","password":"123456","roles":['user']},
#     {"username":"lisi","password":"123456","roles":['superAdmin','user']},
#     {"username":"wangwu","password":"123456","roles":['user','admin']},
#     {"username":"zhaoliu","password":"123456","roles":['superAdmin','admin']},
# ]
# str1 = input("请输入username：")
# for menu in menuList:
#     for user in userList:
#         if user["username"] == str1:
#             for role in user["roles"]:
#                 if role in menu["roles"]:
#                     print(menu)
#                     break
# 6. 模拟登录,要求实现 限制密码输错5次，每输错一次，提醒剩余次数
# userList = [
#     {"username":"zhangsan","password":"123456","roles":['user']},
#     {"username":"lisi","password":"123456","roles":['superAdmin','user']},
#     {"username":"wangwu","password":"123456","roles":['user','admin']},
#     {"username":"zhaoliu","password":"123456","roles":['superAdmin','admin']},
# ]
# a = 5
# while a > 0:
#     print(f"你有 {a} 次机会")
#     username = input("输入username: ")
#     password = input("输入password: ")
#     bool = False
#     for user in userList:
#         if user["username"] == username and user["password"] == password:
#             print(f"欢迎你{username}!")
#             print(f"你的身份是: {', '.join(user['roles'])}")
#             bool = True
#             break
#     if bool:
#         break
#     else:
#         a -= 1
# if a == 0:
#     print("你已经没有机会输入")

# 7.模拟注册输入手机号 / 密码 / 角色， 要求判断手机号的格式问题（简单判断长度与类型即可）userList = []
# userList = [
#     {"username":"zhangsan","password":"123456","roles":['user']},
#     {"username":"lisi","password":"123456","roles":['superAdmin','user']},
#     {"username":"wangwu","password":"123456","roles":['user','admin']},
#     {"username":"zhaoliu","password":"123456","roles":['superAdmin','admin']},
# ]
# str4 = input("请输入注册的角色：")
# str1 = input("请输入手机号：")
# password = input("请输入密码：")
# str3 = input("请输入权限：")
# lis3 = []
# lis2 = ["username","password","roles"]
# lis3.append(str3)
# num = False
# for j in str1:
#     if j in "0123456789":
#         num = True
# if num and len(str1) == 11:
#     lis1 = [str4,password,lis3]
#     result_dict = {lis2[i]: lis1[i] for i in range(len(lis2))}
#     userList.append(result_dict)
#     print("注册成功")
# else:
#     print("手机号格式不正确")

# 8.将5~7三个题目整合  注册/登录/查看拥有的菜单列表
# 自有数据：
# menuList = [
#     {"name":"用户管理",'roles':['superAdmin','admin']},
#     {"name":"角色管理",'roles':['superAdmin']},
#     {"name":"菜单管理",'roles':['superAdmin','admin']},
#     {"name":"日志管理",'roles':['superAdmin','admin','user']},
#     {"name":"资产管理",'roles':['admin','user']},
#     {"name":"财务管理",'roles':['admin','user']}
# ]
# userList = [
#     {"username":"zhangsan","password":"123456","roles":['user']},
#     {"username":"lisi","password":"123456","roles":['superAdmin','user']},
#     {"username":"wangwu","password":"123456","roles":['user','admin']},
#     {"username":"zhaoliu","password":"123456","roles":['superAdmin','admin']},
# ]
# while True:
#     print("**" * 50)
#     print("\t\t欢迎进入注册登录查找界面：\n"
#           "\t\t\t1. 注册\n"
#           "\t\t\t2. 登录\n"
#           "\t\t\t3. 查找菜单\n"
#           "\t\t\tq. 退出")
#     print("**" * 50)
#     choice = input("请选择你的操作：")
#     if choice == "1":
#         print("注册")
#         str4 = input("请输入注册的角色：")
#         str1 = input("请输入手机号：")
#         password = input("请输入密码：")
#         str3 = input("请输入权限：")
#         lis3 = str3.split(",")
#         lis2 = ["username","password","roles"]
#         num = False
#         for j in str1:
#             if j in "0123456789":
#                 num = True
#         if num and len(str1) == 11:
#             lis1 = [str4,password,lis3]
#             result_dict = {lis2[i]: lis1[i] for i in range(len(lis2))}
#             userList.append(result_dict)
#             print("注册成功")
#         else:
#             print("手机号格式不正确")
#
#     if choice == "2":
#         print("请登录")
#         a = 5
#         while a > 0:
#             print(f"你还有 {a} 次机会")
#             username = input("输入username: ")
#             password = input("输入password: ")
#             bool = False
#             for user in userList:
#                 if user["username"] == username and user["password"] == password:
#                     print(f"欢迎你{username}!")
#                     print(f"你的身份是: {', '.join(user['roles'])}")
#                     bool = True
#                     break
#             if bool:
#                 break
#             else:
#                 a -= 1
#         if a == 0:
#             print("你已经没有机会输入")
#
#     if choice == "3":
#         print("查找菜单列表")
#         str1 = input("请输入username：")
#         for menu in menuList:
#             for user in userList:
#                 if user["username"] == str1:
#                     for role in user["roles"]:
#                         if role in menu["roles"]:
#                             print(menu)
#                             break
#     if choice == "q":
#         print("已退出")
#         break
# 9. '''
# 模拟购物车，准备一个列表 goodList = [{'name':'笔记本电脑','price':8000}, {'name':'鼠标', 'price':100}]
# 5个函数 1.加入购物车 2.收藏商品 3.去结算 4.删除购物车商品 5.清空购物车
# 购物车 cartList = []
# 收藏列表 collectSet = {'笔记本电脑','鼠标'}  数据示例
# 去结算计算出总价即可
# 假如购物车的时候，添加number为可变的 如果不输入，默认为1
# 结算功能  单独结算一个商品的所有数量/固定数量，数量不输入，默认结算全部 如果商品名称也不写，直接结算购物车全部商品
# 添加新功能，添加新的商品
goodList = [{'name':'笔记本电脑','price':8000}, {'name':'鼠标', 'price':100}]
cartList = []
collectSet = set()
print("**" * 50)
print("\t\t购物车，有以下操作：\n"
      "\t\t\t1. 加入购物车\n"
      "\t\t\t2. 收藏商品\n"
      "\t\t\t3. 删除购物车商品\n"
      "\t\t\t4. 去结算\n"
      "\t\t\t5. 清空购物车\n"
      "\t\t\t6. 查看购物车\n"
      "\t\t\t7. 添加新商品\n"
      "\t\t\tq. 退出")
print("**" * 50)
while True:
    choice = input("选择你要进行的操作：")
#添加
    if choice == '1':
        goods = {}
        name = input("请选择你添加的商品：")
        for good in goodList:
            if name == good['name']:
                number = input("请输入你要该添加商品的数量：")
                if number == "":
                    goods['name'] = good['name']
                    goods['price'] = good['price']
                    goods['number'] = 1
                else:
                    goods['name'] = good['name']
                    goods['price'] = good['price']
                    goods['number'] =int(number)
        cartList.append(goods)
# 收藏
    if choice == '2':
        name = input("请选择你收藏的商品：")
        for good in goodList:
            if name == good['name']:
                collectSet.add(name)
        print("收藏：",collectSet)
# 删除
    if choice == '3':
        name = input("请选择要删除的商品：")
        if len(cartList) == 0:
            print("购物车为空。")
        for cart in cartList:
            if cart['name'] == name:
                cartList.remove(cart)
#结算
    if choice == '4':
        sum = 0
        name = input("请输入你要结算的商品：")
        if len(cartList) == 0:
            print("购物车是空的，快去添加吧。")
        else:
            for good in cartList:
                if name == good['name']:
                    number = input("请输入你要结算的数量：")
                    if number == "":
                        sum += good['price'] * good['number']
                    elif int(number) >0 and int(number) <= int(good['number']):
                        sum += good['price'] * int(number)
                        a = good['number']- int(number)
                        good['number'] = a
                        print(sum)
                        if good['number'] == 0:
                            cartList.remove(good)
                elif name == "":
                    for good in cartList:
                        price = good["price"]
                        number = good["number"]
                        sum += price * number
                    print(sum)
                    cartList.clear()
# 清空
    if choice == '5':
        cartList.clear()
# 查看
    if choice == '6':
        print(cartList)
# 添加商品
    if choice == '7':
        goods = {}
        name = input("请输入要添加的新商品名称：")
        price = input("请输入要添加的新商品价格：")
        goods['name'] = name
        goods['price'] = price
        goodList.append(goods)
        print("商品列表：",goodList)
    if choice == 'q':
        print("再见")
        break








