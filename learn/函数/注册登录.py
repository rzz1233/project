menuList = [
    {"name":"用户管理",'roles':['superAdmin','admin']},
    {"name":"角色管理",'roles':['superAdmin']},
    {"name":"菜单管理",'roles':['superAdmin','admin']},
    {"name":"日志管理",'roles':['superAdmin','admin','user']},
    {"name":"资产管理",'roles':['admin','user']},
    {"name":"财务管理",'roles':['admin','user']}
]
userList = [
    {"username":"zhangsan","password":"123456","roles":['user']},
    {"username":"lisi","password":"123456","roles":['superAdmin','user']},
    {"username":"wangwu","password":"123456","roles":['user','admin']},
    {"username":"zhaoliu","password":"123456","roles":['superAdmin','admin']},
]
def fun1():
    print("注册")
    str4 = input("请输入注册的角色：")
    str1 = input("请输入手机号：")
    password = input("请输入密码：")
    str3 = input("请输入权限：")
    lis3 = str3.split(",")
    lis2 = ["username", "password", "roles"]
    num = True
    for j in str1:
        if j not in "0123456789":
            num = False
    if num and len(str1) == 11:
        lis1 = [str4, password, lis3]
        result_dict = {lis2[i]: lis1[i] for i in range(len(lis2))}
        userList.append(result_dict)
        print("注册成功")
    else:
        print("手机号格式不正确")
def fun2():
    print("请登录")
    a = 5
    while a > 0:
        print(f"你还有 {a} 次机会")
        username = input("输入username: ")
        password = input("输入password: ")
        bool = False
        for user in userList:
            if user["username"] == username and user["password"] == password:
                print(f"欢迎你{username}!")
                print(f"你的身份是: {', '.join(user['roles'])}")
                bool = True
                break
        if bool:
            break
        else:
            a -= 1
    if a == 0:
        print("你已经没有机会输入")
def fun3():
    print("查找菜单列表")
    str1 = input("请输入username：")
    for menu in menuList:
        for user in userList:
            if user["username"] == str1:
                for role in user["roles"]:
                    if role in menu["roles"]:
                        print(menu)
                        break
def fun4():
    print("退出")

print("**" * 50)
print("\t\t欢迎进入注册登录查找界面：\n"
          "\t\t\t1. 注册\n"
          "\t\t\t2. 登录\n"
          "\t\t\t3. 查找菜单\n"
          "\t\t\tq. 退出")
print("**" * 50)

while True:
    choice = input("请选择你的操作：")
    if choice == "1":
        fun1()
    if choice == "2":
        fun2()
    if choice == "3":
        fun3()
    if choice == "q":
        fun4()
        break