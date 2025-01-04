# 断言的作用是验证某个条件是否为真，如果条件为假，程序会引发一个错误（通常是 AssertionError），以便开发者发现并修复问题。

x = 5
assert x > 0  # 条件为真，程序继续执行
print("断言通过！")


x = -1
assert x > 0, "x 必须为正数"  # 条件为假，程序会引发 AssertionError: x 必须为正数

