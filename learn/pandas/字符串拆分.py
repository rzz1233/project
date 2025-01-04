
import pandas as pd

df = pd.DataFrame({
    'text': ['apple-orange-banana', 'dog-cat-mouse', 'car-bus-train']
})

# 使用 '-' 作为分隔符将字符串拆分为列表
df['split_text'] = df['text'].str.split('-')
print(df)

# 将拆分后的列表重新合并为字符串
df['joined_text'] = df['split_text'].str.join('-')
print(df)

