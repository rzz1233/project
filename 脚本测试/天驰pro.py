import os
import requests
import json


def get_token():
    """获取Token"""
    url = "http://10.18.41.73:8080/login"
    data = {"username": "yingshi", "password": "yingshi20210201"}
    try:
        res = requests.post(url, data=data)
        res.raise_for_status()
        result = res.json()
        return result.get("data")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None
    except ValueError as e:
        print(f"解析 JSON 失败: {e}")
        return None


def get_tianchi_data(year):
    """获取天池数据"""
    token = get_token()
    url = "http://10.18.41.73:8080/beijingcity/getQuarterlyDustSave"
    headers = {"token": token}
    param = {"years": year}

    try:
        res = requests.get(url, params=param, headers=headers)
        res.raise_for_status()
        response = res.json().get("data")
        return json.loads(response) if response else []
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return []


def transform_data(entry, response):
    """转换数据"""
    quarter = entry.get("quarter")
    quarter_data = get_quarter_data(quarter, response)
    if not quarter_data:
        raise ValueError(f"缺少季度{quarter}的数据")

    return {
        "last_quarter": {
            "name": "PM25",
            "value": entry.get("thisyearconc"),
            "rate": f"{entry.get('YOY')}%"
        },
        "last_quarter_cumulative": {
            "name": "PM25",
            "value": quarter_data.get("thisyearconc"),
            "rate": f"{quarter_data.get('YOY')}%"
        }
    }


def get_quarter_data(quarter, response):
    """获取对应季度的数据"""
    quarter_map = {
        "1": '1',
        "2": '1~2',
        "3": '1~3',
        "4": '1~4'
    }
    for entry in response:
        if entry.get("quarter") == quarter_map.get(quarter):
            return entry
    return None


def write_to_file(directory, filename, data):
    """将数据写入文件"""
    # 确保目录存在
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 构建完整的文件路径
    file_path = os.path.join(directory, filename)

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"写入 {file_path} 成功！")
    except IOError as e:
        print(f"文件写入失败: {e}")


def process_data_for_year(year, directory):
    """处理并写入数据"""
    response = get_tianchi_data(year)
    if not response:
        print("没有数据返回！")
        return

    # 定义季度与文件名的映射
    quarter_to_filename = {
        "1": f"{year}0401.txt",
        "2": f"{year}0701.txt",
        "3": f"{year}1001.txt",
        "4": f"{year + 1}0101.txt"
    }

    # 按季度分类并写入文件
    for entry in response:
        quarter = entry.get("quarter")
        if quarter in quarter_to_filename.keys():
            filename = f"season_{quarter_to_filename[quarter]}"
            try:
                transformed_entry = transform_data(entry, response)
                write_to_file(directory, filename, transformed_entry)
            except ValueError as e:
                print(f"数据转换失败: {e}")
            except IOError as e:
                print(f"文件写入失败: {e}")


if __name__ == "__main__":
    # 保存路径
    save_directory = "D:/tianchi_data/"

    process_data_for_year(2024, save_directory)
