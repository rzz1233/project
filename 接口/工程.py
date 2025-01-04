import requests


def get_ch_in_data():
    url = "https://olympic-pre.airqualitychina.cn:9998/measures/county-daterange?start_time=2024-12-24&end_time=2024-12-24"
    data = requests.get(url)
    res = data.json().get("result")["table_data"]["data"]
    print(res)


get_ch_in_data()
