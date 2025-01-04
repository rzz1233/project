import requests

def test_device_site_data():
    url = "http://sanjian-service-api.bjmemc.hotgrid.cn/transfer/device-site-data/"
    token = "025603d57dfb0864fa8f0096b00a8655ce66d010"
    headers = {"Content-Type": "application/json", "Authorization": f"Token {token}"}
    params = {
        "start_time": "2024-12-09 01:00:00",
        "end_time": "2024-12-10 01:00:00",
        "time_type": "1h",
        "pollutant_code": "tsp,tvoc"
    }
    resp = requests.get(url, headers=headers, params=params)
    print(resp.json())

# 调用函数
test_device_site_data()
