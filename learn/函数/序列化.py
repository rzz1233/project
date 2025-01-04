import json
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = json.dumps(dic) #序列化：将一个字典转换成一个字符串
print(type(str_dic),str_dic)
dic2 = json.loads(str_dic)#反序列化：将一个字符串格式的字典转换成一个字典
print(type(dic2),dic2)

f = open("test.txt","w")
json.dump(dic2,f)#dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
f.close()

f = open("test.txt","r")
dic3 = json.load(f)#load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
print(dic3)
f.close()