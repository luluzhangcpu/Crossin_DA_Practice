import pandas as pd
import numpy as np

# task1
df_company = pd.DataFrame({'marketcap':[449,371,237,21313,1369,823],\
                           'pe':[8.31,15.36,16.01,7.16,7.59,6.3],\
                          'code':['600926','002958','601128','601398','601229','600919']},\
    index = ['杭州银行','青农商行','常熟银行','工商银行','上海银行','江苏银行'])

# task2
print(df_company[df_company['marketcap'] < 2000]) # 选取市值低于 2000亿的所有公司

# task3
print(df_company[(df_company['marketcap'] < 2000) & (df_company['pe'] < 10)])
# 选取市值低于 2000亿，且市盈率<10 的所有公司

# task4
dr = pd.date_range(start='2019-01-02',periods=100)
data = np.random.randn(100).cumsum()
close = data - np.min(data)
df = pd.DataFrame({'close':close},index=dr)
df['av_close'] = df['close'].rolling(5).mean() # 新增1列，5日平均数据

# task5
df2 = pd.DataFrame(np.arange(1,17).reshape(4,4),index = list('abcd'),columns=['第1列','第2列','第3列','第4列'])

# task6
print(df2.apply(lambda x:x.sum(),axis=1)) # 应用 apply函数，统计每行总和

# task7
df2['tj'] = df2.apply(lambda x:x['第1列'] + x['第2列'] if x['第3列'] > 10 else x['第3列'],axis=1)
print(df2)
# 应用 apply函数，按条件新生第5列数据
