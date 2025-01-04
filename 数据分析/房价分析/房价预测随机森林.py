import pandas as pd
import re
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用宋体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 2. 数据加载
file = "bj_data_split.xlsx"
data = pd.read_excel(file)

# 修改列名以匹配示例表格
data.columns = ['title', 'price', 'status', 'size', 'province', 'district', 'area', 'address_detail']

# 3. 数据预处理

# 处理 size 列，将范围数据取平均值或单个面积转换为整数
def process_size(size_str):
    if isinstance(size_str, str):
        # 使用正则表达式提取所有数字并忽略非数字字符
        numbers = re.findall(r'\d+', size_str)
        if len(numbers) == 2:  # 范围格式，如 "128-143㎡"
            low, high = map(int, numbers)
            return (low + high) / 2
        elif len(numbers) == 1:  # 单一面积，如 "138㎡"
            return int(numbers[0])
    return None  # 对无效数据返回 None

data['size'] = data['size'].apply(process_size)

# 删除 size 列中仍然为空的行
data.dropna(subset=['size'], inplace=True)

# 对所有分类变量进行独热编码
data = pd.get_dummies(data, columns=['status', 'province', 'district', 'area', 'address_detail'], drop_first=True)

# 选择特征和目标变量
X = data.drop(columns=['price', 'title'])
y = data['price']

# 4. 数据集拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# 5. 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. 随机森林模型和参数优化
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=42),
                           param_grid=param_grid,
                           cv=5,
                           scoring='neg_mean_squared_error',
                           n_jobs=-1)
grid_search.fit(X_train_scaled, y_train)

# 输出最佳参数
print(f'最佳参数: {grid_search.best_params_}')

# 7. 使用最佳参数训练模型
best_model = grid_search.best_estimator_

# 8. 预测
y_pred = best_model.predict(X_test_scaled)

# 9. 模型评估
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(f'均方根误差 (RMSE): {rmse}')

# 10. 结果可视化
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel('实际价格')
plt.ylabel('预测价格')
plt.title('实际价格与预测价格对比')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')  # y=x 线
# 保存图片
plt.savefig("total_tu.png", dpi=300)  # 设置分辨率为 300 dpi
plt.show()
