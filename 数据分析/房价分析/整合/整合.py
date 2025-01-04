import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib

# 设置支持中文的字体为宋体
matplotlib.rcParams['font.family'] = 'SimSun'  # 宋体

# 文件路径列表
file_paths = [
    "bj_cleaned.xlsx",
    "sh_cleaned.xlsx",
    "gz_cleaned.xlsx",
    "sz_cleaned.xlsx",
    "ty_cleaned.xlsx"
]

# 创建一个空的 DataFrame 用于存储结果
average_prices = pd.DataFrame(columns=['City', 'Average Price'])

# 城市名称列表
cities = ['北京', '上海', '广州', '深圳', '太原']

# 遍历每个文件，计算平均价格
for file_path, city in zip(file_paths, cities):
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        # 处理缺失值，确保只计算有效价格
        df.dropna(subset=['price'], inplace=True)
        # 计算平均价格
        avg_price = df['price'].mean()
        # 创建一个新的 DataFrame 用于保存结果
        new_row = pd.DataFrame({'City': [city], 'Average Price': [avg_price]})
        # 使用 pd.concat() 添加新行
        average_prices = pd.concat([average_prices, new_row], ignore_index=True)
    else:
        print(f"文件 {file_path} 不存在，请检查路径。")

# 打印结果
print(average_prices)

# 保存结果到 Excel 文件
# average_prices.to_excel('average_prices.xlsx', index=False)

# 绘制平均价格条形图
plt.figure(figsize=(10, 6))
plt.bar(average_prices['City'], average_prices['Average Price'], color='skyblue')
plt.title('各城市平均价格')  # 中文标题
plt.xlabel('城市')  # 中文x轴标签
plt.ylabel('平均价格')  # 中文y轴标签
plt.xticks(rotation=45)  # 旋转x轴标签以便更好地显示
plt.grid(axis='y')

# 保存图表
plt.tight_layout()
plt.savefig('average_prices_chart.png', dpi=300)  # 设置DPI为300
plt.show()  # 显示图表
