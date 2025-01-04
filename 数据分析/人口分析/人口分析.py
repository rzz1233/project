import numpy as np
import pandas as pd

df_pop = pd.read_csv("state-population.csv")
print(df_pop)   # state/region 州的简称  ages 年龄  year年份 population：人口数
df_abb = pd.read_csv("state-abbrevs.csv")
print(df_abb)  # state 州的全称  abbreviation 州的简称
df_areas = pd.read_csv("state-areas.csv")
print(df_areas)  # state州的全称   area (sq. mi)州面积

# 将人口数据和各州简称数据进行合并
abb_pop = pd.merge(df_abb,df_pop,left_on="abbreviation",right_on="state/region",how="outer")
# print(abb_pop)

# 将合并的数据中重复的abbreviation列进行删除
abb_pop.drop(labels="abbreviation",axis=1,inplace=True)
print(abb_pop)

# 查看存在缺失数据的列
# 第一种
buf = abb_pop.isnull().any(axis=0)
print(buf)
# 第二种
print(abb_pop.info())


# 找到有哪些state/region使得state的值为NaN，进行去重操作
# 首先找到哪些Nan
buf2 = abb_pop["state"].isnull()
print(buf2)
# 去重
buf3 = abb_pop.loc[buf2]["state/region"].unique()
print(buf3)  # ['PR' 'USA'] 存在缺失值


# 为找到的这些state/region的state项补上正确的值，从而去除掉state这一列的所有NaN
# ‘USA'
buf4 = abb_pop["state/region"] == "USA"
print("*"*40)
# print(buf4)
buf5 = abb_pop.loc[buf4]  # 过滤数据
# print(buf5)
indexs = buf5.index
# print(indexs)
abb_pop.loc[indexs,"state"] = "United States of America"
# print(abb_pop)

# PR  ==》Puerto Rico
indexs_2 = abb_pop.loc[abb_pop['state/region']=="PR"].index
abb_pop.loc[indexs_2,'state'] = "Puerto Rico"
print(abb_pop)
# 合并各州面积数据areas
abb_pop_areas = pd.merge(abb_pop,df_areas,how="outer")
print(abb_pop_areas)
indexs_3 = abb_pop_areas.loc[abb_pop_areas['area (sq. mi)'].isnull()].index
abb_pop_areas.drop(labels=indexs_3,axis=0,inplace=True)
print(abb_pop_areas)

# 找出2010年的全民人口数据
pop_num = abb_pop_areas.query('ages == "total" & year==2010')
# print(pop_num)
print(pop_num["population"].sum())

abb_pop_areas["density"] = abb_pop_areas["population"] / abb_pop_areas["area (sq. mi)"]
print(abb_pop_areas)

# 排序，并找出人口密度最高的五个州
buf6 = abb_pop_areas.sort_values(by="density",axis=0,ascending=False).iloc[0]["state"]
print(buf6)






