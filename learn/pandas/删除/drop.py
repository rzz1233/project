# DataFrame.drop(labels, axis=0, index=None, columns=None, inplace=False, errors='raise')




import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# 删除第二行（索引为1的行）
df_dropped = df.drop(1)
print(df_dropped)






