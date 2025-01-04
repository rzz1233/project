# apply 是 Pandas 中非常强大的一个函数，用于在 DataFrame 或 Series 上应用一个函数。

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 计算每一列的和
column_sums = df.apply(sum)
print(column_sums)

# 计算每一行的和
row_sums = df.apply(sum, axis=1)
print(row_sums)

# 对每个元素进行平方操作
squared_df = df.apply(lambda x: x ** 2)
print(squared_df)

