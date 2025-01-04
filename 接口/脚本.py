import pymysql
from datetime import datetime, date

# 数据库连接配置
db_config = {
    "host": "192.168.195.201",
    "port": 3317,
    "user": "bjmemc_app_assist",
    "password": "lb168e8sLu9PrF0sQ_",
    "database": "bjmemc_app_assist",
    "charset": "utf8mb4"
}

# 8月到12月周期差级数据
district_data = [
    {"county": "东城", "values": [1, 0, 0, 6, 3]},
    {"county": "西城", "values": [1, 0, 0, 1, 0]},
    {"county": "朝阳", "values": [1, 5, 4, 5, 4]},
    {"county": "海淀", "values": [4, 9, 7, 4, 10]},
    {"county": "丰台", "values": [5, 7, 12, 18, 9]},
    {"county": "石景山", "values": [0, 0, 0, 2, 0]},
    {"county": "门头沟", "values": [2, 0, 1, 3, 1]},
    {"county": "房山", "values": [13, 7, 2, 19, 6]},
    {"county": "通州", "values": [2, 2, 0, 1, 4]},
    {"county": "顺义", "values": [5, 3, 3, 2, 3]},
    {"county": "大兴", "values": [3, 2, 4, 5, 1]},
    {"county": "昌平", "values": [5, 2, 6, 7, 3]},
    {"county": "平谷", "values": [4, 5, 2, 2, 3]},
    {"county": "怀柔", "values": [1, 0, 2, 1, 0]},
    {"county": "密云", "values": [0, 1, 1, 2, 1]},
    {"county": "延庆", "values": [0, 0, 0, 0, 1]},
    {"county": "经开区", "values": [0, 1, 0, 1, 0]},
    {"county": "全市", "values": [47, 44, 44, 79, 49]},
]

# 插入数据的函数
def insert_clue_review_cycle_data():
    try:
        # 连接数据库
        connection = pymysql.connect(**db_config)
        cursor = connection.cursor()

        # 插入 SQL 语句
        insert_query = """
        INSERT INTO clue_review_cycle (
            county, emission_type_id, review_cycle_name, review_cycle_target_id,
            value, created_at, updated_at, review_cycle_month, name_type,
            is_deleted, date_string, is_reviewed
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # 当前时间
        now = datetime.now()

        # 循环插入 8 月到 12 月的每一条数据
        for district in district_data:
            for i, value in enumerate(district["values"]):
                review_cycle_month = date(2024, 8 + i, 1).strftime('%Y-%m-%d')
                cursor.execute(
                    insert_query,
                    (
                        district["county"],
                        3,  # emission_type_id 为 3
                        f"{8 + i}月点评周期",  # review_cycle_name 按月命名
                        21,  # review_cycle_target_id 为 21
                        format(value, '.5f'),  # value 保持 5 位小数
                        now.strftime('%Y-%m-%d %H:%M:%S'),
                        now.strftime('%Y-%m-%d %H:%M:%S'),
                        review_cycle_month,
                        1,  # 假设 name_type = 1
                        0,  # 假设 is_deleted = 0
                        None,  # date_string 为空
                        0,  # 假设 is_reviewed = 0
                    )
                )
                print(f"Inserted data for {district['county']} - {8 + i}月点评周期")

        # 提交事务
        connection.commit()
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
    finally:
        # 关闭连接
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# 主函数
if __name__ == "__main__":
    insert_clue_review_cycle_data()
