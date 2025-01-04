import pandas as pd

# 读取 Excel 文件
df = pd.read_excel("市.xlsx")

# 将所有 '--' 替换为 0
df.replace('--', 0, inplace=True)

# 按 devsite_code 分组并合并数据
merged_df = df.groupby('devsite_code', as_index=False).agg({
    'devsite_name': 'first',  # 保留第一个值
    'county_name': 'first',   # 保留第一个值
    'town_name': 'first',     # 保留第一个值
    'address': 'first',       # 保留第一个值
    'longitude': 'first',     # 所有数值列求和
    'latitude': 'first',      # 所有数值列求和
    'pollutant_name': 'first',# 保留第一个值
    'collect_day': 'first',   # 保留第一个值
    'mark': 'sum',            # 对 mark 列求和
    '阈值等级': 'sum',        # 保留第一个值
    '超阈值小时数': 'sum',    # 对 超阈值小时数 列求和
    '超阈值时段均值': 'sum',  # 对 超阈值时段均值 列求和
    '排名': 'sum',            # 对 排名 列求和
    '评分': 'sum',            # 对 评分 列求和
    '峰值前1小时数': 'sum',   # 对 峰值前1小时数 列求和
    '峰值前5小时数': 'sum',   # 对 峰值前5小时数 列求和
    '日浓度': 'sum',         # 对 日浓度 列求和
    '峰值5小时浓度': 'sum',  # 对 峰值5小时浓度 列求和
    '最高时刻浓度': 'sum',   # 对 最高时刻浓度 列求和
    '排名.1': 'sum',         # 对 排名.1 列求和
    '评分.1': 'sum',         # 对 评分.1 列求和
    '超周边0ug小时数': 'sum', # 对 超周边0ug小时数 列求和
    '超周边5ug小时数': 'sum', # 对 超周边5ug小时数 列求和
    '超周边时段与周边差值': 'sum',  # 对 超周边时段与周边差值 列求和
    '超周边时段与周边相对差值': 'sum',  # 对 超周边时段与周边相对差值 列求和
    '超周边时段均值': 'sum',   # 对 超周边时段均值 列求和
    '小时数-浓度相对偏差排名': 'sum',  # 对 小时数-浓度相对偏差排名 列求和
    '浓度-小时数排名': 'sum',   # 对 浓度-小时数排名 列求和
    '评分.2': 'sum',           # 对 评分.2 列求和
    '超周边0ug小时数.1': 'sum',  # 对 超周边0ug小时数.1 列求和
    '超周边5ug小时数.1': 'sum',  # 对 超周边5ug小时数.1 列求和
    '超周边时段与周边差值.1': 'sum',  # 对 超周边时段与周边差值.1 列求和
    '超周边时段与周边相对差值.1': 'sum',  # 对 超周边时段与周边相对差值.1 列求和
    '超周边时段均值.1': 'sum',  # 对 超周边时段均值.1 列求和
    '小时数-浓度相对偏差排名.1': 'sum',  # 对 小时数-浓度相对偏差排名.1 列求和
    '浓度-小时数排名.1': 'sum',  # 对 浓度-小时数排名.1 列求和
    '评分.3': 'sum',           # 对 评分.3 列求和
    '开始时间': 'first',       # 保留第一个值
    '结束时间': 'first',      # 保留第一个值
    '持续时长': 'sum',         # 对 持续时长 列求和
    '过程期间平均浓度': 'sum',  # 对 过程期间平均浓度 列求和
    '过程中与周边差值': 'sum',  # 对 过程中与周边差值 列求和
    '过程中与周边相对差值': 'sum',  # 对 过程中与周边相对差值 列求和
    '过程中与周边差值减历时七天与周边差值': 'sum',  # 对 过程中与周边差值减历时七天与周边差值 列求和
    '排名.2': 'sum',          # 对 排名.2 列求和
    '评分.4': 'sum',          # 对 评分.4 列求和
    '近七天同类过程出现次数': 'sum',  # 对 近七天同类过程出现次数 列求和
    '近七天同类过程平均浓度': 'sum',  # 对 近七天同类过程平均浓度 列求和
    '近七天同类过程与周边差值': 'sum',  # 对 近七天同类过程与周边差值 列求和
    '近七天同类过程与周边差值减历时七天与周边差值': 'sum',  # 对 近七天同类过程与周边差值减历时七天与周边差值 列求和
    '排名.3': 'sum',          # 对 排名.3 列求和
    '评分.5': 'sum',          # 对 评分.5 列求和
    '差值': 'sum',            # 对 差值 列求和
    '排名.4': 'sum',          # 对 排名.4 列求和
    '日浓度.1': 'sum',        # 对 日浓度.1 列求和
    '差值相对值': 'sum',      # 对 差值相对值 列求和
    '上一日日浓度': 'sum',    # 对 上一日日浓度 列求和
    '评分.6': 'sum',          # 对 评分.6 列求和
    '持续时间': 'sum',        # 对 持续时间 列求和
    '过程中每小时平均变化浓度': 'sum',  # 对 过程中每小时平均变化浓度 列求和
    '过程浓度': 'sum',        # 对 过程浓度 列求和
    '排名.5': 'sum',          # 对 排名.5 列求和
    '评分.7': 'sum'           # 对 评分.7 列求和
})

# 将结果中所有的 0 替换为 '--'
merged_df.replace(0, '--', inplace=True)
# 将带有 '评分' 字样的列中的 '--' 替换为 0
for column in merged_df.columns:
    if '评分' in column:
        merged_df[column].replace('--', 0, inplace=True)

def replace_double_dash(val, left_val, right_val):
    if val == '--':
        try:
            # 判断左边和右边是否为数字
            left_is_number = isinstance(float(left_val), (int, float))
            right_is_number = isinstance(float(right_val), (int, float))
            if left_is_number and right_is_number:
                return 0
        except ValueError:
            # 如果转换为数字失败，保持原值
            pass
    return val

# 使用 applymap 遍历 DataFrame 进行替换
for row in range(1, merged_df.shape[0] - 1):  # 遍历行
    for col in range(1, merged_df.shape[1] - 1):  # 遍历列
        left_val = merged_df.iloc[row, col - 1]
        right_val = merged_df.iloc[row, col + 1]
        merged_df.iloc[row, col] = replace_double_dash(merged_df.iloc[row, col], left_val, right_val)

# 打印结果
print(merged_df)

# 保存到新的 Excel 文件（可选）
merged_df.to_excel("12.20pm2.5市数据.xlsx", index=False)
