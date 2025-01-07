import requests
import time


def data_get():
    url = "https://national-congress-midservice.airqualitychina.cn/air_quality/map_data/qc-data-high-value-api?token=qiYrxXEv5mJPW6-dU5_wQRI-PR9kst_qrORUjRNuf9omXjG98bE4NHg2o1NSyIIa1yXqWDSDVvwhUnPAt2gMWpOGxnty576cXBCZwI7OlUpd0HlEtkE0gczq2P-pFKLOfjnSVy7TNQocKSIU5m_x4aqytYzvAV7OWBcSrQB_WOWBMh7-bbMEq5ycWk8uJpfmTFCc4pyCu9o83oGvOKBOsk71dHNmoU1XJU0fDxef9BQ%3D&pollutant_id=134004&time_type=1&start_time=2025-01-06+09:00:00&end_time=2025-01-06+09:00:00&level=7&min_value=0&max_value=99999&ranking=9999"
    start_time = time.time()  # 记录开始时间

    data = requests.get(url)

    end_time = time.time()  # 记录结束时间

    res = data.json()

    duration = end_time - start_time  # 计算响应时间
    print(f"接口请求时间: {duration:.2f}秒")


data_get()
