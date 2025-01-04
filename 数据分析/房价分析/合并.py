import pandas as pd




df1 = pd.read_excel('bj_cleaned.xlsx')  # 替换为你的文件路径
df2 = pd.read_excel('sh_cleaned.xlsx')
df3 = pd.read_excel('gz_cleaned.xlsx')
df4 = pd.read_excel('sz_cleaned.xlsx')
df5 = pd.read_excel('ty_cleaned.xlsx')

# 2. 合并这五个表格
combined_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# 3. 保存为一个新的 Excel 文件
combined_df.to_excel('combined_table.xlsx', index=False)