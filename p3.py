import numpy as np
import pandas as pd

# task1
data1 = np.random.randint(3,10,(5,))
s1 = pd.Series(data1,index= list('abcde'))
print(s1)

# task2
a = s1.iloc[-3:]
b = s1.loc['c':]

# task3
df1 = pd.DataFrame({'year':[2017,2018,2019],'price':[10,20,30]})

# task4
data2 = np.random.randint(5,15,(5,3))
df_test = pd.DataFrame(data2,index = list('acefh'),columns=['one','two','three'])

# task5
df_test.loc['a','one'] = np.nan
df_test.loc['c','two'] = -99
df_test.loc['c','three'] = -99
df_test.loc['a','two'] = -100
df_test['four'] = 'test'
df_change = df_test.reindex(list('abcdefgh')) # 重置索引

# task6
df1 = df_change.dropna() # 删除存在缺失值的行

# task7
df2 = df_change.dropna(how='all') # 删除所有值均为缺失值的行

# task8
df3 = df_change.fillna(0) # 将缺失值补充为 0

# task9
df4 = df_change.drop_duplicates() # 删除重复行

