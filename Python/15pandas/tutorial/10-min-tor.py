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
# however, unlike df.loc[], both endpoints are NON-INCLUSIVE
print(df.iloc[1:4, 0:2])
# get scalar
df.iloc[1,1]
# get scalar, fast version
df.iat[1,1]


# boolean indexing
df[df.A > 0]

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]


### 4. merging
print("\n### 4. merging")


### 5. grouping
print("\n### 5. grouping")


### 6. reshaping
print("\n### 6. reshaping")


### 7. pivot_table


### 8. time series
print("\n### 7. time series")


### 9. plotting
print("\n### 8. plotting")





