# 1. 有文件 t1.txt 里面的内容为：
# 1,吴彦祖,22,13812346543,警察
# 2,金城武,23,13698763214,学生
# 3,彭于晏,18,13565478921,运动员
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
    f.write(str(lis4))