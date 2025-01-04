import numpy as np

# # 创建一维数组
# arr1 = np.array([1, 2, 3, 4]) #数据类型一致
# arr11 = np.array([5, 6, "555", 8])  #优先级（字符串>浮点型>数字）
#
# # 创建二维数组
# # arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# arr2 = np.array([[i for i in range(3)], [4, 5, 6]])
#
# print(arr1)
# print(arr11)
# print(arr2)
#
# print(arr2.shape)  # 数组形状(几行几列)
# print(arr2.ndim)   # 数组维度
# print(arr2.size)   # 数组中的元素数量
# print(arr2.dtype)  # 数组的数据类型

# arr = np.array([np.arange(10,20),np.arange(10,20)])

# arr = np.array([[1,2,3,4,5,6,7,8]])  #一维数组变二维数组时每行元素数量相同
# arr1 = arr.reshape((2,4)).reshape((8,1))  # 变形
# print(arr1)
# arr2 = arr.reshape((1,-1)) # 一行八列
# arr3 = arr.reshape((-1,1)) # 八行一列
# print("arr2:",arr2)
# print("arr3",arr3)

# arr = np.random.rand(3, 4) #生成指定维度大小（3行4列）的随机多维浮点型数据（二维）
# print(arr)

# 生成指定维度大小（3行4列）的随机多维整型数据（二维），randint()可以指定区间（-1, 5）
# arr = np.random.randint(-1, 5, size = (3, 4))
# print(arr)
# np.random.shuffle(arr)  #乱序

# 索引
# arr = np.array([[11,22,33],[44,55,66],[444,555,666]])
# print(arr[1][1]) #55
#
# 切片
# print(arr[:2,1:2])  # 逗号之前取行，之后取列 区间都是前闭后开
# print(arr[::-1,::-1])  #反向（上下左右）



# arr = np.array([[11,22,33],[44,55,66],[444,555,666]])
#
# print(np.any(arr > 30)) # np.any(): 至少有一个元素满足指定条件，返回True
# print(np.all(arr > 30)) #np.all(): 所有的元素满足指定条件，返回True
#
# arr2 = np.sort(arr)
# print(arr2)


# 例1：m=np.ones((2.3)) a =np.arange(3) 求 m+a
# m=np.array([[1,2,3],[4,5,6]])
# a =np.arange(3)
# print(a)
# print(m+a)  #[[1 3 5][4 6 8]]


m=np.array([[1],[1]])
a = np.arange(3)
print(a)
print(m+a) #[[1 2 3] [1 2 3]]
