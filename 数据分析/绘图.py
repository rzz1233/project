import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager


matplotlib.use("TkAgg")

font = {
   "family": 'Microsoft Yahei',
    "weight": "bold"
}


matplotlib.rc('font',**font)

fig = plt.figure(figsize=(10,8),dpi=80)

x = range(2,26,2)
y = [13,12,9,5,10,14,18,20,25,16,15,13]
print(x)
# x = [i/2 for i in range(1,11)]
# y = [11,22,33,44,55,66,77,88,99,110]

# 调整刻度
_x_ticks = [f"{i}时" for i in range(2,49)]
print(_x_ticks,type(_x_ticks))
plt.xticks(list(x),_x_ticks[::4],rotation=45)

_y_ticks = (range(min(y),max(y)+1))
plt.yticks(_y_ticks)
plt.xlabel("time")
plt.title("这是郭振业采集的温度数据")
plt.plot(x,y,color="red",alpha=1)  # 折线图
plt.show()
