# drop_duplicates 是 pandas 中用于去除重复行的方法。

import pandas as pd

# 创建一个包含重复行的 DataFrame
data = {'A': [1, 2, 2, 3, 3],
        'B': [5, 6, 6, 7, 7],
        'C': ['a', 'b', 'b', 'c', 'c']}

df = pd.DataFrame(data)

# 去除完全重复的行
df_cleaned = df.drop_duplicates()
print(df_cleaned)