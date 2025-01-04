
# astype
import pandas as pd
#
df = pd.DataFrame({'A': [1.5, 2.6, 3.1], 'B': [4.5, 5.1, 6.2]})
#
#
# df['A'] = df['A'].astype(int)  # 将列 A 转换为整数类型
# print(df)
#
# # 转换多列的数据类型
# df = pd.DataFrame({'A': [1.5, 2.6, 3.1], 'B': [4.5, 5.1, 6.2]})
#
#
# df = df.astype({'A': 'int32', 'B': 'int32'})  # 同时转换 A 列为 int32 类型，B 列为 float64 类型
# print(df)



# 注意事项
# 缺失值（NaN）：如果列中有 NaN，转换为整数时会出错，因为整数类型不能表示缺失值。可以先填充缺失值，或者将数据转换为 float 类型。
