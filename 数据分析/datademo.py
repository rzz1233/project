import pandas as pd

df2 =pd.read_excel("./data.xlsx",sheet_name="Sheet2")
df3 =pd.read_excel("./data.xlsx",sheet_name="Sheet3")
df4 =pd.read_excel("./data.xlsx",sheet_name="Sheet4")
df5 =pd.read_excel("./data.xlsx",sheet_name="Sheet5")

df = pd.merge(df2,df3,"inner",on="手机型号")
print(df)
df1 = pd.merge(df,df4,"inner",on="手机型号")
print(df1)
# print(df2)
# print(df3)
# print(df4)


