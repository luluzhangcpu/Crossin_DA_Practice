import pandas as pd

# task1
df_sh = pd.read_csv('/Users/apple/Desktop/sh.600000.csv')

# task2
print(df_sh.head()) # 查看前5行数据
print(df_sh.tail()) # 查看后5行数据

# task3:描述统计
print(df_sh.index) # 查看行索引
print(df_sh.index.names)
print(df_sh.columns) # 查看列索引
print(df_sh.values)

# task4
print(df_sh.info()) # 查看表字段类型
print(df_sh.describe()) # 查看数值型字段基本描述(含频率、均值、标准差、极值、四分位数)

# task5-1
print(df_sh[:3]) # 查看前3行数据
print(df_sh.loc[0:2]) # 或者用 df.loc[]来查看，前3行数据

# task5-2
print(df_sh.loc[:,'date'],type(df_sh['date'])) # 查看 date列，且查看该列数据类型

# task5-3
print(df_sh.loc[:,['date','open','close']]) # 查看 date,open,close 列数据，及类型
print(type(df_sh[['date','open','close']]))

# task5-4
print(df_sh[df_sh['close'] > 11.08]) # 查看收盘价大于 11.08 数据

# task5-5
df1 = df_sh.set_index('date') # 将 date 列设置为 索引
print(df1.loc['2017-12-11':'2017-12-20']) # 查看 '2017-12-11'至'2017-12-20'的数据

# task5-6
print(df1.loc[:,'open':'close']) # 查看 open 至 close 列的所有列 数据

# task5-7
print(df1.loc['2018-07-01':'2018-07-08','open':'close']) # 查看 '2018-07-01' 至 '2018-07-08'间，ooen 至 close列的所有数据
