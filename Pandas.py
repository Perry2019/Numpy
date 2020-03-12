import numpy as np
import pandas as pd

# 1. 属性
s = pd.Series([1,3,6,8,np.nan,22,1])
print(s)

dates = pd.date_range('20200311',periods=6)
print(dates)

# DataFrame生成
# 数据由numpy生成，行索引由dates生成，列索引由a~d生成
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['a','b','c','d'])
print(df)

# DataFrame的列索引
print(df.index)
# DataFrame的行索引
print(df.columns)
# DataFrame的元素
print(df.values)
# DataFrame的列索引排序
print(df.sort_index(axis=1, ascending=False))

# 2. 选择数据
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
# 行选择
print(df.a)
print(df['a'])
# 列选择
print(df[0:3])
# 高级行选择
print(df)
print(df.loc['20200312'])
print(df.loc[:,'a'])
# 位置选择
print(df.iloc[3:4,1:2])
# 位置和标签的混合选择
##print(df.ix[1:4,['a','c']])

# 3. 设置值
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
# 通过位置改动
a = df.iloc[2,2] = 111
print(a)
# 通过标签改动
aa = df.loc['20200301','b'] = 55
print(aa)
# 部分赋值改动
df[df.a>4] = 0
print(df)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
df.a[df.a>4] = 0
print(df)
# 增加一列
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
df['f'] = np.nan
print(df)
# 增加与行标签对应的一列
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
df['f'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20200311',periods=6))
print(df)

# 4. 缺失数据处理
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
# 丢弃
print(df.dropna(axis=0,how='any'))     # 只要有缺失数据就丢弃
print(df.dropna(axis=0,how='all'))     # 全是缺失数据才丢弃
# 填充
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
print(df.fillna(value=0))              # 0填充
print(df.isnull())                     # 检查是否有缺失

# 5. 数据合并
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
# 上下合并（行、列标签相同）
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)
# 上下合并（行、列标签不同）
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)
res = pd.concat([df1,df2],join='inner',ignore_index=True)
print(res)
# 左右合并（行、列标签不同）
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'],index=[2,3,4])
print(df1)
print(df2)
res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])
print(res)
# append添加
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
res = df1.append(df2,ignore_index=True)
print(res)
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res = df1.append(s1,ignore_index=True)
print(res)

# 6. merge合并(处理字典数据)
left = pd.DataFrame({'Key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'Key':['K0','K1','K2','K3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3']})
print(left)
print(right)
res = pd.merge(left,right,on='Key')
print(res)
# 含有相同字段的合并
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K1','K2'],'age':[4,5,6]})
res = pd.merge(boys,girls,on='k',suffixes=['_boy','girl'],how='inner')
print(boys)
print(girls)
print(res)