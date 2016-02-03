import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



### 1. object creation
print("\n### 1. object creation")
# Series
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

print("-------------")

# DataFrame with date index and column label
dates = pd.date_range('20160101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
print("index:", df.index)
print("columns:", df.columns)
print("values:", df.values)

print("-------------")

# create by using a dict of objects that can be converted to series-like
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print(df2)
print("index2:", df2.index)
print("columns2:", df2.columns)
print("values2:", df2.values)

### 2. basic operations
print("\n### 2. basic operations")

df.head()
df.tail(3)
# summary (mean, std, quantile etc.)
df.describe()
# transpose
df.T

# sort by axis
print(df.sort_index(axis=0, ascending=False))

# sort by values
print(df.sort_values(by='B'))


### 3. indexing
print("\n### 3. indexing")

# using standard python expressions, this is NOT recommended
# selecting column
df['A']
df[['A','C']]
# selecting row
df[0:1]
# the same as above, but note that it is inclusive
df['2016-01-01':'2016-01-01']
# this will not work, rows can only be selected using slice
#df[0]


# df.loc[] selects by index label, it selects rows by default
df.loc[dates[0]]
df.loc[dates]
df.loc['2016-01-03']
df.loc[:, ['A', 'C']]
# both endpoints are INCLUSIVE
print(df.loc['20160102':'20160104', ['A','B']])
# get scalar
df.loc[dates[0],'A']
# get scalar, fast version
df.at[dates[0],'A']


# df.iloc[] selects by position, also selects rows by default
df.iloc[0]
# the same
df.iloc[0,:]
df.iloc[[1,2,4],[0,2]]
# selecting columns
df.iloc[:,1:3]
# however, unlike df.loc[], both the right endpoint is NON-INCLUSIVE
print(df.iloc[1:4,0:2])
# get scalar
df.iloc[1,1]
# get scalar, fast version
df.iat[1,1]


# boolean indexing
# note that this selects rows
df[df.A>0]

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]


### 4. merging
print("\n### 4. merging")

df = pd.DataFrame(np.random.randn(10, 4))

# basic concat (combining columns)
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

# database like joining
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
joined = pd.merge(left, right, on='key')

# append rows
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]
# note the use of ignore_index
df.append(s, ignore_index=True)

### 5. grouping
print("\n### 5. grouping")

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print(df.groupby('A').sum())

### 6. reshaping
print("\n### 6. reshaping")

# stack

# pivot_table
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])


### 7. time series
print("\n### 7. time series")


### 8. plotting
print("\n### 8. plotting")

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
#plt.show()

# DataFrame.plot()
# plot all columns with labels
ts_df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
ts_df = ts_df.cumsum()
ts_df.plot()
plt.legend(loc='best')
plt.show()


