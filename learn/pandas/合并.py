# merge
# pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False)
# how：连接方式，默认是 inner。常用选项有：
# 'inner'：内连接，只保留在两个表中都有的行。
# 'outer'：外连接，保留两个表中所有的行，缺失值填充 NaN。
# 'left'：左连接，保留左侧 DataFrame 的所有行。
# 'right'：右连接，保留右侧 DataFrame 的所有行。

# on：要连接的列名，要求在两个 DataFrame 中都存在。如果没有指定，Pandas 会自动寻找共享的列。
# left_on 和 right_on：如果列名不相同，可以分别指定左侧和右侧的连接列名。


import pandas as pd

# 创建两个 DataFrame
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})

# 基于 'key' 列进行内连接
merged_df = pd.merge(df1, df2, on='key', how='inner')
print(merged_df)
