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


### 4. merging
print("\n### 4. merging")


### 5. grouping
print("\n### 5. grouping")


### 6. reshaping
print("\n### 6. reshaping")


### 7. time series
print("\n### 7. time series")


### 8. plotting
print("\n### 8. plotting")





