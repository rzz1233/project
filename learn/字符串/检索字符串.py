str = "rZz,rQz,gzy"
#count()检索
sum1 = str.count("z",2,6)
print(sum1)
#find()检索
sum2 = str.find("v")
print(str.find("g"))
print(sum2)
#startswith()判断开头
print(str.startswith('z'))
#startswith()判断结尾
print(str.endswith('y'))
# 转换大小写
print(str.lower())
print(str.upper())
# 清除空格和特殊字符
str1 = "@#$rzz\n\t\r"
print(str1.strip())
print(str1.upper())

# 把 string 中的 old_str 替换成 new_str，
str2 = "rzz"
str3 = str.replace("gzy",str2)
print(str3)

