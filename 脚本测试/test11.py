import requests
from datetime import datetime, timedelta
def get_token():
    url = "http://sanjian-service-api.bjmemc.hotgrid.cn/api/token/"
    data = {"username": "yuyu", "password": "u4du4xzw"}
    response = requests.post(url, json=data)
    result = response.json()
    return result["access"]
def get_county_id(county):
    if county == "北京市":
        return 1
    url = "http://sanjian-service-api.bjmemc.hotgrid.cn/clue/api/v2/counties/"
    token = get_token()
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(url, headers=headers)
    result = response.json()

    for item in result:
        # print(item)
        if item["name"] == county:
            # print(item["id"])
            return item["id"]
    # print(result)


def generate_report():
    yesterday = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    url = "http://10.18.41.229:18085/service/serviceinterface/search/run.action"
    params = {
        "token": "9bc47b9636af2d76dd3a9ec9168a23d1",
        "interfaceId": "475872ce7c006363e998246f2c309d72",
        "START_TIME": yesterday,
        "END_TIME": yesterday
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json().get("data", [])
    print(yesterday)
    for item in data:
        county_id = get_county_id(item.get("REGION_NAME"))
        print(f'区id:{item.get("REGION_NAME")}:{county_id}')

# get_county_id("西城区")
generate_report()