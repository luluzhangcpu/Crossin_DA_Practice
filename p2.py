import numpy as np

# task1
iris = np.genfromtxt('/Users/apple/Desktop/iris.csv',encoding='utf-8',dtype='float')
print(iris,type(iris))

# task2
zd = iris.argmax() # 原数组中最大值所在位置
zx = iris.argmin() # 原数组中最小值所在位置

# task3
value_zd = iris.max() # 原数组中最大值
value_zx = iris.min() # 原数组中最小值

# task4
iris = sorted(iris) # 从小到大排序数据
iris = np.array(iris)

# task5
i = np.unique(iris) # 去除重复值

# task6
pj = iris.mean() # 数组平均值

# task7
bzc = iris.std() # 该组数据标准差
fc = iris.var() # 该组数据方差

# task8
zh = iris.sum() # 该组数据总和

# task9
lj = iris.cumsum() # 该组数据累积求和运算

# task10
cnt = (iris > pj).sum() # 该组数据中高于均值的个数
