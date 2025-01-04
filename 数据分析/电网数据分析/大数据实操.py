import numpy as np
import pandas as pd

# 读取 Excel 文件
df1 = pd.read_excel("未使用APP交费用户(数据集一).xls")
# print(df1)

# 删除【用户分类】列缺失数据的记录
# 你在使用 dropna 方法时，如果 subset 参数指定了一列或多列，它将只删除这些列中有缺失值的行，而不影响其他列。/
# inplace=True：原数据直接修改，无返回值。
# inplace=False：原数据不变，返回修改后的数据副本
# df1.dropna(subset=["用户分类"], inplace=True)

# 将处理后的数据保存为 Excel 文件
# df1.to_excel("data_1_1.xlsx", index=False)


# 对“data_1_1.xls”进行数据分析，统计每个供电所的【用电类别】有哪些，并计算各【用电类别】的用户数量及绑定微信公众号人数，
# 结果保存为“data_1_2.xls”，表字段包括：供电所、用电类别、用户数量、绑定微信公众号人数
df2 = pd.read_excel("data_1_1.xlsx")
# print(df2)

# 将“绑定微信公众号”列中的“是”转换为1，“否”转换为0
df2["绑定微信公众号"] = df2["绑定微信公众号"].apply(lambda x: x.count("是"))

grouped_df = df2.groupby(["供电所", "用电类别"]).agg(
    用户数量=("用户编号", "count"),  # 统计用户编号的数量，即用户数量
    绑定微信公众号人数=("绑定微信公众号", "sum")  # 统计已绑定微信公众号的人数
).reset_index()
print(grouped_df)
# grouped_df.to_excel("data_1_2.xlsx", index=False)
