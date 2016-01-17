import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy import create_engine


engine = create_engine('sqlite:///test.db')


### 1. MultiIndex (hierarchical index)
# create multi index

# from a list of tuples
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

# or from 'products' of iterables
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
foo = pd.MultiIndex.from_product(iterables, names=['first', 'second'])
foo.get_values()


# use the index when creating Series/DataFrame
s = pd.Series(np.random.randn(8), index=index)
df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)


# specify multi index when creating series or dataframe
arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
          np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]
pd.Series(np.random.randn(8), index=arrays)
pd.DataFrame(np.random.randn(8, 4), index=arrays)


# plain tuples can be used directly as index, too, but it's of course not 
# recommended
pd.Series(np.random.randn(8), index=tuples)


### 2. using multi index
# show names of the index
df.columns.names
# get an array of tuples from the index
df.columns.values
# or list
df.index.tolist()

# get different levels respectively
# by index
index.get_level_values(0)
# by name
index.get_level_values('second')


# basic indexing
s = pd.Series(np.random.randn(8), index=arrays)
df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
bi_df = df
bi_df_T = df.T

s['foo']

df['bar']
df['bar', 'two']
df['bar']['two']

bi_df_T.loc['bar', 'one']
bi_df_T.loc['bar'].loc['one']

# alignment and reindex
# works the same as normal single index
s + s[:-2]
s + s[::2]

s.reindex(index[::2])
s.reindex([('foo', 'two'), ('bar', 'one'), ('qux', 'one'), ('baz', 'one')])


### 3. advanced indexing
df = df.T

df.loc['bar']
df.loc['bar', 'two']

# slicing rows
df.loc['baz':'foo']
df.loc[('baz', 'two'):('qux', 'one')]

# select using list of tuples
df.loc[[('bar', 'two'), ('qux', 'one')]]
# the same
df.ix[[('bar', 'two'), ('qux', 'one')]]



# using slicers
# XXX: when using slicers, the MultiIndex must be sorted MANUALLY beforehand
def mklbl(prefix,n):
    return ["%s%s" % (prefix,i)  for i in range(n)]
miindex = pd.MultiIndex.from_product([mklbl('A',4),
                                      mklbl('B',2),
                                      mklbl('C',4),
                                      mklbl('D',2)])
micolumns = pd.MultiIndex.from_tuples([('a','foo'),('a','bar'),
                                       ('b','foo'),('b','bah')],
                                      names=['lvl0', 'lvl1'])
dfmi = pd.DataFrame(
        np.arange(len(miindex)*len(micolumns)).\
                reshape((len(miindex),len(micolumns))),
        index=miindex,
        columns=micolumns
    )
# shuffling the rows
dfmi = dfmi.iloc[np.random.permutation(len(dfmi))]
# another method
dfmi = dfmi.reindex(np.random.permutation(dfmi.index))

# shuffling the columns
dfmi = dfmi.reindex(columns=np.random.permutation(dfmi.columns))
# or
dfmi = dfmi.iloc[:,np.random.permutation(len(dfmi.columns))]

# SORT IT !
dfmi = dfmi.sort_index().sort_index(axis=1)


# slice(None) selects all rows of that level, levels cannot not be omited in 
# the middle, but can be omited at last
dfmi.loc[(slice('A1','A3'),slice(None),['C1','C3']),:]

# an alternative (better) syntax
idx = pd.IndexSlice
dfmi.loc[idx[:,:,['C1','C3']],idx[:,'foo']]

# can mixed with boolean indexers
mask = dfmi[('a','foo')]>200
dfmi.loc[idx[mask,:,['C1','C3']],idx[:]]


# operate on a single axis
df2 = dfmi.copy()
# and values can be set directly
df2.loc[idx[:,:,['C1','C3']],:] = df2/1000
df2
df2.loc(axis=0)[:,:,['C1','C3']] = -10









