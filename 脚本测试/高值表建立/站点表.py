import pandas as pd
import requests


def station_data():
    url = 'http://10.18.41.53:8000/high_value_analysis/get_std_analysis_value?json={"start_time":"2025-01-06","end_time":"2025-01-06","pollutant_id":134004,"site_type":0,"audit_type":"0,1,2,3","column_type":0}'
    try:
        res = requests.get(url)
        # 检查响应状态码
        res.raise_for_status()  # 如果响应码不是2xx，抛出异常
        data = res.json()  # 尝试解析JSON响应
        print(data)

        # 假设返回的数据是一个列表，包含多个站点的数据
        if isinstance(data, list):
            # 扁平化嵌套的字典结构，展开嵌套的字段
            flat_data = []
            for item in data:
                # 合并每个字段，避免嵌套字典
                flat_item = item.copy()

                # 用来记录已存在的列名
                existing_columns = set(flat_item.keys())

                # 将每个嵌套字段拆开，变为独立列
                for nested_key in ['超阈值', '峰值小时数', '超周边小时', '超周边浓度', '时段突高', '规律高值', '日变幅', '小时变幅']:
                    if nested_key in item:
                        for sub_key, sub_value in item[nested_key].items():
                            new_column_name = sub_key
                            # 如果列名重复，添加后缀
                            count = 1
                            while new_column_name in existing_columns:
                                new_column_name = f"{sub_key}_{count}"
                                count += 1
                            flat_item[new_column_name] = sub_value
                            existing_columns.add(new_column_name)

                        # 删除嵌套字段
                        del flat_item[nested_key]

                flat_data.append(flat_item)

            # 将数据转换为DataFrame
            df = pd.DataFrame(flat_data)
            # 修改列名为中文
            column_mapping = {
                'station_id': '站点编号',
                'station_name': '站点名称',
                'county_name': '区县名称',
                'longitude': '经度',
                'latitude': '纬度',
                'pollutant_id': '污染物编号',
                'pollutant_name': '污染物名称',
                'pollutant_value': '污染物值',
                'collect_day': '采集日期',
                'mark': '标记',
                'image': '图片',
                'audit_type': '审核类型',
                'index': '索引'
            }
            df.rename(columns=column_mapping, inplace=True)
            # 按照 '站点编号' 升序排序
            df.sort_values(by='站点编号', ascending=True, inplace=True)

            # 保存为Excel文件
            df.to_excel('station_data.xlsx', index=False)
            print("数据已保存到 station_data.xlsx")
        else:
            print("返回的数据格式不符合预期")

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
    except ValueError:
        print("返回的不是有效的JSON格式数据")
    except Exception as e:
        print(f"发生错误: {e}")


# 调用函数
station_data()
