import pandas as pd

# 读取 Excel 文件
df1 = pd.read_excel("光伏电站发电功率及相关数据(数据集三).xlsx")
df2 = pd.read_excel("光伏电站发电功率预测结果(数据集三).xlsx")
# 打印原始数据
print(df1)
# 1. 处理缺失值
# 可以选择删除缺失值的行，或用均值、中位数填充缺失值
# 这里以用【功率(MW)】列的均值来填充缺失值为例
df1["功率(MW)"].fillna(df1["功率(MW)"].mean(), inplace=True)
# 2. 处理重复值
# 删除完全相同的行
df1.drop_duplicates(subset=["功率(MW)"], inplace=True)
# 打印处理后的数据
print(df1)
# 保存结果到 Excel 文件
# df1.to_excel("data_3_1.xlsx", index=False)


