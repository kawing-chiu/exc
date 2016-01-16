import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


### 1. creating groups
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})

# specify columns directly
df.groupby(['A', 'B'])


# use a mapper function, or a dict providing the label -> group name mapping
def get_letter_type(label):
    if label.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'
# by columns (axis=1)
grouped_by_cols = df.groupby(get_letter_type, axis=1)
grouped_by_cols.groups
grouped_by_cols.axis

# by row
def greater_than_5(label):
    print(label)
    if label > 5:
        return 'big'
    else:
        return 'small'
grouped_by_rows = df.groupby(greater_than_5)


# groupby with multi index
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
s = pd.Series(np.random.randn(8), index=index)

s.groupby(level=1).sum()
s.groupby(level='second').mean()
s.groupby(level=['first', 'second'])



### 2. iterate and select groups
grouped = df.groupby('A')
for name, group in grouped:
    print("group:", name)
    print(group)

grouped_multi = df.groupby(['A', 'B'])
for name, group in grouped_multi:
    print("\ngroup", name)
    print(group)

for name, group in grouped_by_cols:
    print("\ngroup", name)
    print(group)

# select groups
grouped.get_group('bar')
grouped_multi.get_group(('foo', 'one'))
# not working, must use tuple
#grouped_multi.get_group(['bar', 'one'])

# list all groups
grouped.groups
len(grouped)


### 3. select target columns of groupby
grouped = df.groupby('A')
grouped['C'].sum()
grouped[['D', 'C']].mean()
# all columns
grouped.mean()



### 4. aggregation
grouped = df.groupby('A')
grouped.aggregate(np.sum)

# don't use the group-by columns as the index of the result DataFrame
df.groupby('A', as_index=False).sum()

grouped.size()
grouped.describe()

# get the n-th item of each group
grouped.nth(0)
grouped.nth(0, dropna='any')


# a aggregate function that returns the first element
def first(x):
    print("\ngot:", type(x))
    print(x)
    return x.iloc[0]
grouped.aggregate(first)


# apply multiple functions for a single column
grouped['C'].agg([np.sum, np.mean, np.std])
# name the output columns
grouped['D'].agg({'sum_result' : np.sum,
                  'mean_result' : np.mean})

# use different functions for different columns
# note that a dictionary argument of aggregate() can have different meaning 
# depending on whether operating on a single column or multiple columns
grouped.agg({'C' : np.sum,
             'D' : lambda x: np.std(x)})


### 5. transformation
# Quote from official docs: "The transform method returns an object that is 
# indexed the same (same size) as the one being grouped. Thus, the passed 
# transform function should return a result that is the same size as the group 
# chunk."

# example: standardize the data within each group
index = pd.date_range('10/1/1999', periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
ts = pd.rolling_mean(ts, 100, 100).dropna()

# group by year
key = lambda x: x.year
zscore = lambda x: (x - x.mean()) / x.std()
#def zscore(x):
#    print(x)
#    return (x - x.mean()) / x.std()
transformed = ts.groupby(key).transform(zscore)

# check that the result has 0 mean and unit sd
group = ts.groupby(key)
group.mean()
group.std()

group_trans = transformed.groupby(key)
group_trans.mean()
group_trans.std()

# compare the original data and the transformed data visually
compare = pd.DataFrame({'Original': ts, 'Transformed': transformed})
compare.plot()


### 6. filtration




### 7. apply







