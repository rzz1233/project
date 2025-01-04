

import requests

def get_dianwei_data():
    # 定义你的 start_time 和 end_time 值
    start_time = '2025-01-01 00:00:00'
    end_time = '2025-01-02 00:00:00'

    # 插入实际的 token 并格式化 URL
    token = 'tAFuWeewk-ojwVPoNP9PCQnrrV-w8MsU4V2ua6dK9q-nEQqTzqW8EXN7nviGpWAVtG9A4Ep8BojFy_SP3rA3YkgbOlM36yxkwDiIaJp8hdS51OErpEE-agaDbAzvT3GGE7hWbC1xmmkv-5o1vkL4VdpL6zxfwdQfUjByV6gqjG8_eS3AqDClAHIn_azgGEq2guZj8G9scUbmS8JPu0IqQs_B4Fn26ToXm6YUbMjXl32XLciIFVZ3JqkYiiDcvVB9TnC3TUH1UooAmjhk3AH2wQ=='

    url = f'https://api-adm-data-service.airqualitychina.cn/adm/certain-time-avg?json={{"token":"{token}","rankid":"7","startTime":"{start_time}","endTime":"{end_time}","timeType":"2","is_round":"True","auditflag":"0","roundNum":"2","order":"desc","keyword":"","countyid":""}}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果返回状态码不是 200，将抛出异常
        data = response.json()  # 将返回的 JSON 数据解析为字典
        print(data)  # 输出返回的数据
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


get_dianwei_data()