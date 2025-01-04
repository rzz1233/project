import pandas as pd

# 读取Excel文件
file_path = 'taiyuan.xlsx'
df = pd.read_excel(file_path)

# 尝试将price列转换为浮点数，处理转换错误（例如，无法转换为数字的字符串）
df['price'] = pd.to_numeric(df['price'], errors='coerce')
in_sale_and_price_df = df[(df['price'] >= 5000)]
output_file_path = '太原/ty_cleaned.xlsx'
in_sale_and_price_df.to_excel(output_file_path, index=False)

print(f"价格大于等于5000的数据已另存为 {output_file_path}")