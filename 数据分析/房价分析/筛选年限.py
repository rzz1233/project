import pandas as pd

# 读取Excel文件
file = "processed_year1.xlsx"
sheets = pd.read_excel(file, sheet_name=None)

# 创建一个空的DataFrame用于存储2019年的数据
df_2019 = pd.DataFrame()

# 遍历每个工作表
for sheet_name, df in sheets.items():
    # 筛选出2019年的数据
    df_2019_sheet = df[df['Year'] == 2024]

    # 如果当前工作表有2019年的数据，合并到总的DataFrame中
    df_2019 = pd.concat([df_2019, df_2019_sheet], ignore_index=True)

# 查看2019年的数据
print(df_2019)
df_2019.to_excel('2024.xlsx', index=False)
