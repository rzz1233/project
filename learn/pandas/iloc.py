# iloc 是基于位置的索引器

import pandas as pd

# 示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# 打印第一行
first_row = df.iloc[0:1]
print(first_row)
