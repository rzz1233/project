# zip()
# 两个列表
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
#
# zipped = zip(list1, list2)
# print(list(zipped))  # 输出：[(1, 'a'), (2, 'b'), (3, 'c')]

# map() 是 Python 的一个内置函数，用于将指定的函数依次作用于一个或多个可迭代对象（如列表、元组等）中的每个元素，并返回一个迭代器，
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
# 使用 map() 将 square 函数应用于 numbers 列表的每个元素
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # 输出：[1, 4, 9, 16, 25]



