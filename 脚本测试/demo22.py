import requests
import pandas as pd


def device_site_data():
    # API 信息
    # url = "http://127.0.0.1:8000/transfer/device-site-data/"   #本地
    url = "https://national-congress-midservice.airqualitychina.cn/air_quality/map_data/qc-data-api?token=qiYrxXEv5mJPW6-dU5_wQRI-PR9kst_qrORUjRNuf9omXjG98bE4NHg2o1NSyIIa1yXqWDSDVvwhUnPAt2gMWpOGxnty576cXBCZwI7OlUpd0HlEtkE0gczq2P-pFKLOfjnSVy7TNQocKSIU5m_x4aqytYzvAV7OWBcSrQB_WOWBMh7-bbMEq5ycWk8uJpfmTFCc4pyCu9o83oGvOKBOsk71dHNmoU1XJU0fDxef9BQ%3D"
    # token = "025603d57dfb0864fa8f0096b00a8655ce66d010"
    # headers = {"Content-Type": "application/json", "Authorization": f"Token {token}"}
    # params = {
    #     "start_time": "2024-12-08 01:00:00",
    #     "end_time": "2024-12-08 01:00:00",
    #     "time_type": "1h",
    #     "pollutant_code":"tsp,tvoc"
    # }

    # 请求数据
    print("请求 URL:", url)
    resp = requests.get(url)
    print(resp.json())
    # 检查响应
    if resp.status_code == 200:
        print("请求成功，正在处理数据...")
        try:
            data = resp.json().get("result", [])
            if not data:
                print("未返回任何数据")
                return

            # 将数据转换为 Pandas DataFrame
            df = pd.DataFrame(data)

            # 保存为 Excel 文件
            output_file = "station1_data.xlsx"
            df.to_excel(output_file, index=False)
            print(f"数据已成功保存为文件：{output_file}")
        except Exception as e:
            print("处理数据时发生错误:", e)
    else:
        print(f"请求失败，HTTP 状态码: {resp.status_code}, 响应内容: {resp.text}")


# 调用函数
device_site_data()
