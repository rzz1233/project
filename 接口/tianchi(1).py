import requests
import json
import datetime


class Quarter:
    def __init__(self):
        self.token = None
        self.data = None

    def init_token(self,token=None):
        url = 'http://10.18.41.73:8080/login'
        payload = {
            "username": "yingshi",
            "password": "yingshi20210201"
        }
        if token:
            self.token = token
        try:
            res = requests.post(url, data=payload)
            result = res.json()
            self.token = result.get("data")
        except Exception as e:
            raise ValueError('获取token失败')


    def get_data(self):
        if not self.token:
            raise ValueError('token required!')
        try:
            url = "http://10.18.41.73:8080/beijingcity/getQuarterlyDustSave"
            headers = {"token": self.token}
            cur_time = datetime.datetime.now()
            year = cur_time.year
            if cur_time.month == 1:
                year = year - 1
            param = {"years": year}
            resp = requests.get(url, params=param, headers=headers)
            data = resp.json().get("data")
            data = json.loads(data)
            self.data = data
            return data
        except Exception as e:
            raise ValueError('获取数据失败！')


    def get_data_by_quarter(self,quarter=None):
        result = {}
        if not self.data:
            self.data = self.get_data()
        # 默认获取当前时间的上个季度
        if not quarter:
            current_time = datetime.datetime.now()
            quarter = (current_time.month - 1) // 3

        for item in self.data:
            if item.get("quarter") == quarter:
                result["last_quarter"] =  {
                    "name": "PM25",
                    "value": item.get("thisyearconc"),
                    "rate": f"{item.get('YOY')}%"
                }
                if item.get("quarter") == '1':
                    result["last_quarter_cumulative"] = {
                        "name": "PM25",
                        "value": item.get("thisyearconc"),
                        "rate": f"{item.get('YOY')}%"
                    }

            if item.get("quarter") == f'1~{quarter}':
                result["last_quarter_cumulative"] = {
                    "name": "PM25",
                    "value": item.get("thisyearconc"),
                    "rate": f"{item.get('YOY')}%"
                }

        return result

def main():
    quarter = Quarter()
    quarter.init_token()
    data = quarter.get_data_by_quarter('1')
    filename = '20240401.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()

