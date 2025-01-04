import pandas as pd

# 读取 users.txt 文件并设置表头，使用 '::' 作为分隔符，并指定 Python 引擎
users_df = pd.read_csv('users.txt', sep='::', engine='python', header=None, names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'])

# 读取 movies.txt 文件并设置表头，使用 '::' 作为分隔符，并指定 Python 引擎
movies_df = pd.read_csv('movies.txt', sep='::', engine='python', header=None, names=['MovieID', 'Title', 'Genres'])

# 读取 ratings.txt 文件并设置表头，使用 '::' 作为分隔符，并指定 Python 引擎
rating_df = pd.read_csv('ratings.txt', sep='::', engine='python', header=None, names=['UserID', 'MovieID', 'Rating','Timestamp'])
# 去掉行索引为 0 的行
rating_df.drop(index=0, inplace=True)
# 如果需要重置索引，可以使用 reset_index 方法
rating_df.reset_index(drop=True, inplace=True)

# 输出前几行数据，查看结果
# print(users_df.head())
# print(movies_df.head())
# print(rating_df.head())


# 将 UserID 列都转换为字符串类型
rating_df['UserID'] = rating_df['UserID'].astype(str)
users_df['UserID'] = users_df['UserID'].astype(str)
# 合并 ratings_df 和 users_df
ratings_users_df = pd.merge(rating_df, users_df, on='UserID',how='outer')
# print(ratings_users_df)

# 将 UserID 列都转换为字符串类型
ratings_users_df['MovieID'] = ratings_users_df['MovieID'].astype(str)
movies_df['MovieID'] = movies_df['MovieID'].astype(str)
# 合并 ratings_users_df 和 movies_df
total_df = pd.merge(ratings_users_df, movies_df, on='MovieID',how='outer')

# 去掉重复的行
total_df = total_df.drop_duplicates()
print(total_df)
#保存
# total_df.to_csv('total_data.csv', index=False)

# 首先确保 Rating 列的数据类型为数值型
total_df['Rating'] = total_df['Rating'].astype(float)
# 显示“电影类别”为'Comedy'且评分>=4的电影名称
result = total_df[(total_df['Genres'] == 'Comedy') & (total_df['Rating'] >= 4)]

# 去掉重复的电影标题
result = result[['Title']].drop_duplicates()
print(result[['Title']])

