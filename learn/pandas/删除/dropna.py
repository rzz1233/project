# dropna 是 pandas 中的一个方法，用于删除包含缺失值（NaN）的行或列。
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# how:
# 'any'：只要有一个缺失值，就删除该行或列（默认值）。
# 'all'：只有当所有值都是缺失时，才删除该行或列。

# subset:
# 用于指定检查缺失值的特定行或列。可以传入一个列名列表，dropna 会仅在这些列中检查缺失值。
import pandas as pd
import numpy as np

# 创建包含缺失值的 DataFrame
data = {'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': [9, 10, 11, 12]}

df = pd.DataFrame(data)

# 删除包含缺失值的行
df_cleaned = df.dropna(axis=0)
print(df_cleaned)

# 删除包含缺失值的列
df_cleaned2 = df.dropna(axis=1)
print(df_cleaned2)
