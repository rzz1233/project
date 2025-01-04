import requests
import json
import pytest
def get_token():
    url = "http://sanjian-service-api.bjmemc.hotgrid.cn/api/token/"
    data = {
        "username": "lisi",
        "password": "code1234"
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result['access']

def test_clue_statistics_by_county_every_day(self):
        url = "http://sanjian-service-api.bjmemc.hotgrid.cn/clue/api/v2/clue-statistics-by-county/"
        token = get_token()

        headers = {"Authorization": f"Bearer {token}"}
        params = {
            "start_time": "2024-07-01",
            "end_time": "2024-08-02",
            "time_type":1,
            "nested": True,
            "county": [2, 3, 4, 5, 6, 7, 8, 9],
        }
        resp = requests.get(url, headers=headers, params=params)
        print(json.dumps(resp.json(), indent=4, ensure_ascii=False))


