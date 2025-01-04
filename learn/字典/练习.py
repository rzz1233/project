# 1.有1,2,3,4,5,6,7,8 八个数字，能组成多少个互不相同且无重复数字的两位数？
import random

# lis1 = [1,2,3,4,5,6,7,8]
# lis2 = []
# for i in lis1:
#     for j in lis1:
#         if i != j:
#             lis2.append(i*10+j)
# print(len(lis2))

# 字典内容如下dic = { 'python': 95, 'java': 99, 'c': 100}
dic = { 'python': 95, 'java': 99, 'c': 100}
# 字典的长度是多少
print(len(dic))
# 请修改'java' 这个key对应的value值为98
dic['java'] = 98
print(dic)
# 删除 c 这个key
del dic['c']
print(dic)
# 增加一个key-value对，key值为 php, value是90
dic.setdefault('php',90)
print(dic)
# 获取所有的key值，存储在列表里
lis1 = dic.keys()
print(lis1)
# 获取所有的value值，存储在列表里
lis2 = dic.values()
print(lis2)
# 判断 javascript 是否在字典中
for i in dic.keys():
    if i == 'javascript':
        print('javascript在dic中')
        break
else:
    print("不存在")
# 获得字典里所有value的和
sum = 0
for i in dic.values():
    sum += i
print(sum)
# 获取字典里最大的value
max_vl = max(dic.values())
print(max_vl)
# 获取字典里最小的value
min_vl = min(dic.values())
print(min_vl)
# 字典dic1 = {'c++': 97}， 将dic1的数据更新到dic中
dic1 = {'c++': 97}
dic.update(dic1)
print(dic)

# 录入学生的名字，如果名字存在则回复人名已存在，无法录入，直到输出空字符串，然后逆序输出
# lis1 =["rzz","eee","www"]
# str1 = input("请输入名字：")
# if str1 in lis1:
#     print("人名已存在，无法录入")
# if str1 == "":
#     print(str1[::-1])
# 写一个列表50个数，将列表中大于30的数据构成一个新的列表
lis3 = []
lis4 = []
for i in range(0,50):
    a = random.randint(0,100)
    lis3.append(a)
for a in lis3:
    if a > 30:
        lis4.append(a)
print(lis4)
# 统计重复单词的次数：此处认为单词之间以空格为分隔符，并且不包含,和.
# a.用户输入一个英文句子
# b.打印出每个单词及其重复的次数
str2 = input("请输入一个英语句子：")
lis5 = str2.split(' ')
lis6 = []
for i in lis5:
   if i not in lis6:
       b = lis5.count(i)
       lis6.append(b)
dic2 = {lis5[i]:lis6[i] for i in range(0,len(lis5))}
print(dic2)



