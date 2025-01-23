import requests
import pandas as pd


def device_site_data():
    # API 信息
    # url = "http://127.0.0.1:8000/transfer/device-site-data/"   #本地
    url = "http://sanjian-service-api.bjmemc.hotgrid.cn/transfer/device-site-data/"
    # token = "025603d57dfb0864fa8f0096b00a8655ce66d010"
    # headers = {"Content-Type": "application/json", "Authorization": f"Token {token}"}
    params = {
        "start_time": "2025-01-16 00:00:00",
        "end_time": "2025-01-20 23:59:59",
        "time_type": "1h",
        "pollutant_code":"no2"
    }

    # 请求数据
    print("请求 URL:", url)
    resp = requests.get(url, params=params)
    # print(resp.json())
    # 检查响应
    if resp.status_code == 200:
        print("请求成功，正在处理数据...")
        try:
            data = resp.json().get("data", [])
            if not data:
                print("未返回任何数据")
                return

            # 将数据转换为 Pandas DataFrame
            df = pd.DataFrame(data)

            # 保存为 Excel 文件
            output_file = "no2_data2.xlsx"
            df.to_excel(output_file, index=False)
            print(f"数据已成功保存为文件：{output_file}")
        except Exception as e:
            print("处理数据时发生错误:", e)
    else:
        print(f"请求失败，HTTP 状态码: {resp.status_code}, 响应内容: {resp.text}")


# 调用函数
device_site_data()
