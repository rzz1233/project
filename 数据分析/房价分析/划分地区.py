import pandas as pd

# 读取 Excel 文件
file = '太原/ty_cleaned.xlsx'
df = pd.read_excel(file)

# 分割 address 列，将其分为三列：district、area、address_detail
df[['district', 'area', 'address_detail']] = df['address'].str.extract(r'\[\s*([^\s]+)\s+([^\s]+)\s*\]\s*(.*)')

# 删除原 address 列
df = df.drop(columns=['address'])

# 保存分割后的表格为新的 Excel 文件
df.to_excel("ty_split.xlsx", index=False)

print(df)
