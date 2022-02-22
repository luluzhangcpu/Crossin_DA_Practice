import pandas as pd

# task1
df_house = pd.read_csv('/Users/apple/Desktop/houses.csv',encoding='gbk')
df_house.drop_duplicates(inplace=True) # 去除重复行
print(df_house.info()) # 查看字段类型

# task2
print(len(df_house['title'])) # 查看房源总数
print(len(df_house['xiaoqu_name'].unique())) # 查看不同小区数量
print(len(df_house['sub_district_name'].unique())) # 查看不同板块数量

# task3
print(df_house['huxing'].unique()) # 查看有哪些不同户型
print(df_house['zhuangxiu'].unique()) # 查看哪些不同装修
print(df_house['buildyear'].unique()) # 查看哪些不同年份

# task4
print(df_house['up_price'].mean())

# task5
a = df_house['size'].groupby(by=df_house['huxing']).agg({'count','mean'}).sort_values(by='count',ascending=False)
print(a)
# 按户型分组，查看不同户型的房源数，及，平均面积，并按房源数降序排列

# task6
b = df_house['title'].groupby(df_house['xiaoqu_name']).count().sort_values(ascending=False)
print(b)
# 按小区分组，查看不同小区房源数，并降序排列

# task7
c = df_house['up_price'].groupby(df_house['xiaoqu_name']).mean()
print(c)
# 按小区分组，查看不同小区，每平米均价

# task8
d = df_house.sort_values(by='price',ascending=False).head()
print(d)
# 按房价降序排列，取前5行数据

# task9
df_house['buildyear'] = pd.to_datetime(df_house['buildyear'],format='%Y') # 先将时间转为时间序列
e = df_house['title'].groupby(df_house['buildyear']).count() # 再按 groupby 统计各年度房源数
print(e.resample('10A').sum()) # 以resample 来统计每10年的房源总数
