import pandas as pd
import numpy as np

# task1
df1 = pd.read_csv('/Users/apple/Desktop/task6_1.csv')

# task2
print(pd.pivot_table(df1,index=['id','date'],values=['sales'],fill_value=0,aggfunc=np.sum))
# 每人每天金额之和

# task3
print(pd.pivot_table(df1,index=['id'],values=['sales'],columns=['date'],fill_value=0,margins=True,aggfunc=np.sum))
# 透视表新增，每人总金额

# task4
df2 = pd.read_csv('/Users/apple/Desktop/task6_2.csv')

# task5
print(pd.pivot_table(df2,index=['sex'],columns=['smoke'],values=['age','height'],aggfunc=np.mean))
# 按性别分组，查看各组平均年龄及身高

# task6
print(pd.crosstab(index=df2['sex'],columns=df2['smoke'],margins=True))
# 按性别分组，查看各组抽烟与否人数分布

# task7
print(pd.crosstab(index = df2['age'],columns=df2['smoke'],margins=True))
# 按年龄分组，查看各组抽烟与否人数分布