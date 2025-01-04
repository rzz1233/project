import pandas as pd

# 读取 Excel 文件
df1 = pd.read_excel("光伏用户发电量(数据集二).xls")

# 计算每个供电所每月的总发电量、总上网电量以及用户数量
grouped_df = df1.groupby(["供电所", "电费年月"]).agg(
    总发电量=("总发电量", "sum"),  # 统计总发电量
    总上网电量=("总上网电量", "sum"),  # 统计总上网电量
    用户数量=("用户编号", "count")  # 统计用户数量
).reset_index()

# 计算户均总发电量和户均总上网电量
grouped_df["户均总发电量"] = grouped_df["总发电量"] / grouped_df["用户数量"]
grouped_df["户均总上网电量"] = grouped_df["总上网电量"] / grouped_df["用户数量"]

# 删除不再需要的列
# grouped_df.drop(labels=["总发电量", "总上网电量", "用户数量"],axis=1,inplace=True)
# drop_row = [1,2,3,4,5,6]
# grouped_df.drop(index=drop_row,inplace=True)
# grouped_df1 = grouped_df[grouped_df["供电所"] != '南屯供电所']
grouped_df.drop(columns=["总发电量", "总上网电量", "用户数量"],inplace=True)

# 打印分组后的结果
print(grouped_df)

# 将结果保存为新的 Excel 文件
# grouped_df.to_excel("data_2_1.xlsx", index=False)
