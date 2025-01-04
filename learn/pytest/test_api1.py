import pytest
import requests
import json

# 使用pytest的标记功能，将该测试标记为'test_feedback_overview'，以便运行时进行筛选
@pytest.mark.test_feedback_overview
def test_clue_feedback_overview():
    # API接口的URL
    url = "http://sanjian-service-api.bjmemc.hotgrid.cn/clue/api/v2/clue-feedback-overview/"

    # 获取token，这里假设get_token()是一个函数，返回一个有效的访问令牌
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMzMzA2MjIyLCJpYXQiOjE3MzMzMDU5MjIsImp0aSI6ImM5NWRiOGJiMTIwOTRmYjg4Y2RmMjc1MWJmYWFiNTA2IiwidXNlcl9pZCI6M30.vmLUhx1-J3N72N2fJJLV9_MovjpQ3n91njIowFFHmNk"

    # 设置请求头，包含Authorization字段，使用Bearer token进行认证
    headers = {"Authorization": f"Bearer {token}"}

    # 设置请求参数，包含查询的时间范围、环境元素和问题目标
    params = {
        'assign_time_start': '2024-08-13',  # 指定开始时间
        'assign_time_end': '2024-08-20',    # 指定结束时间
        'environment_element': [1],         # 环境元素的筛选条件
        'issue_target': 2,                  # 问题目标的筛选条件
    }

    # 发送GET请求，传递headers和params作为参数
    resp = requests.get(url, headers=headers, params=params)

    # 将返回的JSON数据格式化并打印输出（调试时使用）
    print(json.dumps(resp.json(), indent=4, ensure_ascii=False))

    # 这里可以添加断言，以验证响应是否符合预期
    # 例如：检查状态码是否为200，响应数据是否包含必要的字段等
