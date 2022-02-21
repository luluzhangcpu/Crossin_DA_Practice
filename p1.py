import numpy as np
import matplotlib.pyplot as plt

# task1
arr1 = np.arange(4,dtype=float).reshape((2,2)) #创建2*2数组，指定float
print(arr1)
print('-'*30)

# task2
arr2 = np.zeros(shape=(6,6)) #创建6*6数组，元素全为0
arr3 = np.ones(shape=(6,6)) #创建6*6数组，元素全为1
arr4 = np.eye(6) #创建6*6数组，对角线为1，其他为0
print(arr2)
print(arr3)
print(arr4)
print('-'*30)

# task3
arr5 = np.arange(10,step=2) #创建 [0,10)，步长为2 的整数序列
print(arr5)
print('-'*30)

# task4
arr6 = np.linspace(0,10,6) #创建 [0,10)，等差数列，个数为6 的序列
print(arr6)
print('-'*30)

# task5
arr7 = np.random.randint(1,10,(10,))
print(arr7)
arr7[arr7.argmax()] = 0
print(arr7)
print('-'*30)

# task6
x = np.array([1,2,3,2,3,4,3,4,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])
dist1 = round(np.sqrt(np.sum(np.power((x - y),2))),5)
print(dist1)

# task7
a = np.random.seed(1)
values = np.random.randn(1000).cumsum(a)
plt.title('资金价值曲线图')
plt.plot(values,color = 'blue')
plt.show()

# task8
max_drawdown = np.max(np.maximum.accumulate(values) - values)
print(max_drawdown)
