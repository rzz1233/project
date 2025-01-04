import pandas as pd

# 导入 Excel 文件
df = pd.read_excel('列表.xlsx')  # 读取 Excel 文件，默认读取第一个工作表

# 将“线索编号”列转换为列表
clue_ids = df['线索编号'].tolist()
print(len(clue_ids))
# 输出列表
print(clue_ids)
