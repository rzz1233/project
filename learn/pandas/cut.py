import pandas as pd

data = [1, 5, 10, 15, 20, 25, 30]
bins = [0, 10, 20, 30]
categories = pd.cut(data, bins)
print(categories)

# 输出[(0, 10], (0, 10], (0, 10], (10, 20], (10, 20], (20, 30], (20, 30]]
# Categories (3, interval[int64, right]): [(0, 10] < (10, 20] < (20, 30]]
#
# 例如，1 属于 (0, 10] 区间，15 属于 (10, 20] 区间。
