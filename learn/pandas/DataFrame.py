# DataFrame：二维数据表，类似于数据库中的表格，行和列都有标签。

import pandas as pd

# 从字典创建 DataFrame
data = [{'A': [1, 2, 3], 'B': [4, 5, 6]}, {'A': [7, 8, 9], 'B': [10, 11, 12]}, {'A': [13, 14, 15], 'B': [16, 17, 18]}]

df = pd.DataFrame(data)
print(df)


# 从列表/元组创建 DataFrame

df0 = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
s = pd.Series([1, 2, 3])
print(df0)

task_most_county_df = pd.DataFrame({
    'county': [1, 2, 3, 1],
    'clue_num': [150, 200, 120, 180],
    'clue_rank': [2, 1, 4, 3]
})
print(task_most_county_df)