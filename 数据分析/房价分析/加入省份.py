import pandas as pd

# 读取 Excel 文件
file_path = '太原/ty_cleaned.xlsx'
df = pd.read_excel(file_path)

# 删除 huxing 列
# df = df.drop(columns=['huxing'])

# 增加 province 列，并将所有值填为 "上海"
df['province'] = '太原'

# 将修改后的数据保存回 Excel 文件
df.to_excel('ty_cleaned.xlsx', index=False)

print("数据已保存至 'sh_cleaned.xlsx'")
