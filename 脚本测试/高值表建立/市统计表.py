import pandas as pd
import requests
from datetime import datetime

def shi_data():
    url = 'http://127.0.0.1:9020/high_value_analysis/get_analysis_value?json={"start_time":"2024-12-20","end_time":"2024-12-20","pollutant_id":134004,"site_type":2,"audit_type":"0,1,2,3","column_type":0}'
    try:
        # 发送请求
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        print("原始数据：", data)

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
                for nested_key in ['超阈值', '峰值小时数', '超周边小时', '超周边浓度', '时段突高', '规律高值', '日变幅',
                                   '小时变幅']:
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

            # 转换为 DataFrame
            df = pd.DataFrame(flat_data)

            # 修改列名为中文
            column_mapping = {
                'devsite_code': '点位编号',
                'devsite_name': '点位名称',
                'county_name': '区县',
                'town_name': '乡镇街道',
                'address': '详细地址',
                'longitude': '经度',
                'latitude': '纬度',
                'pollutant_name': '污染物名称',
                'collect_day': '日期',
                'mark': '评分',
            }
            df.rename(columns=column_mapping, inplace=True)

            # 删除不需要的列
            columns_to_drop = ['pollutant_id', 'pollutant_value', 'image', 'audit_type', 'index']
            df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

            # 按照 '点位编号' 升序排序
            if '点位编号' in df.columns:
                df.sort_values(by='点位编号', ascending=True, inplace=True)

            # 保存为 Excel 文件
            file_name = f"12.20pm2.5市统计.xlsx"
            df.to_excel(file_name, index=False)
            print(f"数据已保存到 {file_name}")
        else:
            print("返回的数据格式不符合预期，期望是列表，但收到的是：", type(data))

    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
    except ValueError:
        print("返回的不是有效的JSON格式数据")
    except Exception as e:
        print(f"发生错误: {e}")

# 调用函数
shi_data()
