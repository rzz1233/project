# 1. 有文件 t1.txt 里面的内容为：
# 1,吴彦祖,22,13812346543,警察
# 2,金城武,23,13698763214,学生
# 3,彭于晏,18,13565478921,运动员
# 利用文件操作，将其构造成如下数据类型。输出到文件t2.txt中。
# [
# {'id':'1','name':'吴彦祖','age':'22','phone':'13812346543','job':'警察'},
# {'id':'2','name':'金城武','age':'23','phone':'13698763214','job':'学生'},
# ... ...
# ]
import json
lis1 = ['id','name','age','phone','job']
with open("t1.txt","r",encoding="utf-8") as f:
    lis4 = []
    res = f.read()
    lis2 = res.split("\n")
    for i in lis2:
        lis3 = i.split(",")
        dic1 = {lis1[s]: lis3[s] for s in range(len(lis1))}
        lis4.append(dic1)
print(lis4)
with open("t2.txt","w",encoding="utf-8") as f:
    json.dump(lis4,f,ensure_ascii=False)

# 2. 读取一个python源码文件，显示除了以#号开头的行以外的所有行。并打印输出#号开头的行数。
# with open("test_shuju.py","r",encoding="utf-8") as f:
#     sum = 0
#     for i in f:
#         if i.startswith("#") != True:
#             print(i)
#         else:
#             sum += +1
#             print(f"#开头有：第{sum}行")

# 3.【综合练习】
# 完成用户注册/登陆功能。
#
# 注册:
# (1)提示用户输入，用户名和密码，其中密码需要输入2次。
# 提示用户名只能为字母、下划线和数字；密码不能超过8位，密码只能为数字或大小写字母
# (2)注册成功后,账户密码记录在文件中 (user.txt)
# 内容格式可以为 {姓名：密码}
# (3)用户名不能重复。输入用户名重复，需要提示用户重新输入。
# (4)检测两次密码如果不同,提示两次密码不一致，检测两次密码如果相同,确认注册成功。
#
# 登陆:
# （1）用户登录时,进行三次校验,都不对,记录黑名单。黑名单保存在文件中：blacklist.txt
# （2）如果是黑名单的用户,则禁止再次登录

# def login(dic1,user):
#     for i in user:
#         if i == "_" or i.isalnum() == True:
#             continue
#         else:
#             print("用户名错误")
#             break
#
#     pw = input("请输入密码：")
#     for p in pw:
#         if int(p) > 8 or p.isalnum() == False:
#             print("密码错误")
#             break
#     if user not in dic1.keys():
#         dic1[user] = pw
#         with open("user.txt", "w") as f:
#             json.dump(dic1,f,ensure_ascii=False)
#     else:
#         print("用户名不能重复")
#
#     pw2 = input("请确认密码")
#     if pw == pw2:
#         print("注册成功")
#     else:
#         print("两次密码不一致")
# def log(user):
#     i = 3
#     while i>0:
#         pw = input("请输入密码:")
#         if user in dic1.keys():
#             with open("blacklist.txt", "r") as f1:
#                 if user in f1.read():
#                     print("该用户在黑名单，无法登录")
#                     break
#             if dic1[user] == pw:
#                 print("登录成功")
#                 break
#             else:
#                 i -= 1
#                 print(f"密码错误你还有{i}次机会")
#         else:
#             print("该用户还没有注册")
#             break
#     else:
#         print("该用户已被加入黑名单")
#         with open("blacklist.txt", "a") as f:
#             json.dump(user,f,ensure_ascii=False)
#
# def main(choice,dic1):
#     user = input("请输入用户名：")
#
#     if choice == '1':
#         login(dic1,user,)
#     if choice == '2':
#         log(user,)
#
# if __name__ == '__main__':
#     dic1 = {}
#     while True:
#         print("**" * 50)
#         print("\t\t注册/登陆:\n"
#               "\t\t\t1.注册\n"
#               "\t\t\t2.登录")
#         print("**" * 50)
#         choice = input("请输入你的选择：")
#         main(choice,dic1)


















