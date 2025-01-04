import pandas as pd


# 从字典创建 DataFrame
data = [{'A': [1, 2, 3], 'B': [4, 5, 6]}, {'A': [7, 8, 9], 'B': [10, 11, 12]}, {'A': [13, 14, 15], 'B': [16, 17, 18]}]

df = pd.DataFrame(data)
print(df.columns)