# 至少有一个字符并且所有字符都是字母则返回 True
str1 = "qwertas"
print(str1.isalpha())
# 如果 string 只包含数字则返回 True，全角数字
str2 = "1234567890"
print(str2.isdigit())
# 如果 string 中只包含空格（换行、制表符），则返回 True
str3 = " \n\t"
print(str3.isspace())
