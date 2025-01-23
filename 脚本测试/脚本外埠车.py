import pymysql
from datetime import datetime

# 数据库连接信息
db_config = {
    "host": "mmservice-06.mysql.hotgrid.cn",  # 数据库地址
    "port": 3306,                             # 数据库端口
    "user": "national_congress",              # 用户名
    "password": "ivr9PrBuqSrReMND",           # 密码
    "database": "national_congress_out_data", # 数据库名称
    "charset": "utf8mb4",                     # 字符编码
}

# 原始数据
raw_data = [
    ("2025/1/3", "75%"),
]

# 数据处理：转换日期格式和百分比为浮点数（除以100）
processed_data = [
    (idx + 1, datetime.strptime(date, "%Y/%m/%d"), float(value.strip('%')) / 100)
    for idx, (date, value) in enumerate(raw_data)
]

# SQL 插入语句
insert_sql = """
INSERT INTO other_city_car (level_0, datetime, `index`) 
VALUES (%s, %s, %s)
"""

# 插入数据的脚本
try:
    # 连接到数据库
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # 插入数据
    cursor.executemany(insert_sql, processed_data)
    connection.commit()  # 提交事务
    print(f"{cursor.rowcount} rows inserted successfully.")

except pymysql.MySQLError as e:
    print(f"Error occurred: {e}")
    if connection:
        connection.rollback()  # 回滚事务

finally:
    # 关闭数据库连接
    if cursor:
        cursor.close()
    if connection:
        connection.close()
