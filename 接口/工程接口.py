import requests


def get_method():
    url = "http://10.18.41.229:18085/service/serviceinterface/search/run.action"
    params = {
        "token": "9bc47b9636af2d76dd3a9ec9168a23d1",
        "interfaceId": "475872ce7c006363e998246f2c309d72",
        "START_TIME": "2024-12-15",
        "END_TIME":"2024-12-16"
    }
    # 请求数据
    resp = requests.get(url, params=params)
    # print(resp.json())
    res = resp.json().get("data", [])
    for i in res:
        print(i.get("DATETIME"))



get_method()