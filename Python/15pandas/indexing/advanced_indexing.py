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

s['foo']

df['bar']
df['bar', 'two']
df['bar']['two']

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












