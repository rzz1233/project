import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 1. 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用宋体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 2. 数据加载
data = pd.read_excel('bj_cleaned.xlsx')  # 替换为你的数据文件路径

# 3. 数据预处理
data.columns = ['title', 'price', 'address', 'status', 'size', 'province']

# 处理缺失值
data.dropna(inplace=True)  # 删除含有缺失值的行

# 提取 size 的数值部分（取平均值）
def process_size(size_str):
    if '-' in size_str:  # 处理范围，例如 '128-143㎡'
        low, high = map(int, size_str.replace('㎡', '').split('-'))
        return (low + high) / 2
    else:
        return int(size_str.replace('㎡', ''))

data['size'] = data['size'].apply(process_size)

# 对所有分类变量进行独热编码
data = pd.get_dummies(data, columns=['status', 'province', 'address'], drop_first=True)

# 选择特征和目标变量
X = data.drop(columns=['price', 'title'])  # 特征
y = data['price']  # 目标变量

# 4. 数据集拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 模型训练
model = LinearRegression()
model.fit(X_train, y_train)

# 6. 预测
y_pred = model.predict(X_test)

# 7. 模型评估
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(f'均方根误差 (RMSE): {rmse}')

# 8. 结果可视化
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel('实际价格')
plt.ylabel('预测价格')
plt.title('实际价格与预测价格对比')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')  # y=x 线
plt.show()
