import requests

def sync_to_population():
    url = "http://192.168.195.24:17202/dataway/api/popInflowOutflow/data"
    param = {
        "start_time": "20241001",
        "end_time": "20241031",
    }
    data =requests.get(url, params=param)
    res = data.json().get("value")
    print(res)


sync_to_population()
