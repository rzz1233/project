import pandas as pd

# 读取 Excel 文件
file_path = 'year1.csv'
df = pd.read_excel(file_path, engine='openpyxl')

# 分离年份和地区
df['year_only'] = df['year'].str.extract(r'(\d{4})').astype(int)
df['region'] = df['year'].str.extract(r'年(.*?)房价')

# 删除原始 'year' 列并重新排列列顺序
df = df[['year_only', 'region', 'price']]

# 保存为新的 Excel 文件
output_path = 'processed_housing_prices.xlsx'
df.to_excel(output_path, index=False)

print(f"处理后的文件已保存为 {output_path}")
