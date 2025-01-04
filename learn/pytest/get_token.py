import requests
import json
def get_token():
    url = "http://sanjian-service-api.bjmemc.hotgrid.cn/api/token/"
    data = {
        "username": "lisi",
        "password": "code1234"
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result['access']

# 手动调用 get_token() 函数
if __name__ == "__main__":
    token = get_token()
    print(f"获取的 Token: {token}")