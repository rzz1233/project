import requests

# 定义查询参数
params = {
    "page": 1,
    "start_time": "2024-08-13 06:00:00",
    "end_time": "2024-08-13 14:00:00",
}

# 发送 GET 请求
response = requests.get('http://localhost:9100/navication/tasks/', params=params)

# 打印响应内容
print(response.url)  # 打印最终的请求 URL  /navication/tasks/?page=1&start_time=2024-08-13+06%3A00%3A00&end_time=2024-08-13+14%3A00%3A00
# print(response.json())  # 打印响应的 JSON 数据
