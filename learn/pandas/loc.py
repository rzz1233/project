# loc 是基于标签的索引器
# df.loc[row_indexer, column_indexer]
# row_indexer：表示你要选择的行标签，可以是单个标签、标签列表、切片或布尔值。
# column_indexer：表示你要选择的列标签，同样可以是单个标签、标签列表、切片或布尔值。

import pandas as pd

# 示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['row1', 'row2', 'row3'])

# 选择标签为 'row1' 的行
row1 = df.loc['row1']
print(row1)

# 选择 'row1' 行的 'A' 和 'B' 列
selected_data = df.loc['row1', ['A', 'B']]
print(selected_data)

# 选择 'row1' 和 'row2' 两行
selected_rows = df.loc[['row1', 'row2']]
print(selected_rows)

