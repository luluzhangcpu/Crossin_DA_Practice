import pandas as pd

# task1
df1 = pd.read_csv('/Users/apple/Desktop/jobs.csv')
df1.drop_duplicates(inplace=True) # 去除重复值
print(df1.head()) # 展示前 5行数据
print(df1.info()) # 展示 字段信息

# task2
print(df1['source'].value_counts()) # 展示各招聘来源下职位数

# task3
print(df1['experience'].value_counts()) # 展示各工作经验下职位数

# task4
print(df1['education'].value_counts()) # 展示各教育要求下职位数

# task5
print(df1['company_type'].value_counts()) # 展示各公司类型下职位数

# task6
print(df1['salary2'].mean()) # 展示所有职位的平均工资

# task7
print(df1['salary2'].groupby(df1['company']).mean().sort_values(ascending=False).head(10))
# 展示各公司平均薪资，前十位的公司名字及薪资金额

# task8
a = df1['salary'].groupby(df1['company']).count().sort_values(ascending=False).head(10)
print(a)
# 展示各公司发布的职位数，前十位公司名及职位数

# task9
b = df1['salary2'].groupby(df1['company_type']).mean().sort_values(ascending=False).head(10)
print(b)
# 展示各公司类型的平均工资，前十位类型及均资