import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置字体以支持中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取 Excel 文件
df1 = pd.read_excel("data_3_1.xlsx")

# 确保时间列为 datetime 类型
df1["时间"] = pd.to_datetime(df1["时间"])

# 筛选时间范围（2019-06-01 00:00 至 2019-08-30 13:00）
start_date = "2019-06-01 00:00"
end_date = "2019-08-30 13:00"

# 过滤数据
df_filtered = df1[(df1["时间"] >= start_date) & (df1["时间"] <= end_date)]

# 分别提取两个光伏电站的数据
df_station_1001 = df_filtered[df_filtered["光伏电站编号"] == 1001]
df_station_1002 = df_filtered[df_filtered["光伏电站编号"] == 1002]

# 绘制功率时序折线图
plt.figure(figsize=(12, 6))
plt.plot(df_station_1001["时间"], df_station_1001["功率(MW)"], label="光伏电站 1001", color='blue')
plt.plot(df_station_1002["时间"], df_station_1002["功率(MW)"], label="光伏电站 1002", color='orange')

# 设置图表标题和标签
plt.title("光伏电站功率时序图 (2019-06-01 至 2019-08-30)")
plt.xlabel("时间")
plt.ylabel("功率 (MW)")
plt.xticks(rotation=45)  # 旋转日期标签以便更好显示
plt.legend()
plt.grid()

# 保存图表
plt.savefig("image_3_2_1.png", bbox_inches='tight')

# 显示图表
plt.show()
