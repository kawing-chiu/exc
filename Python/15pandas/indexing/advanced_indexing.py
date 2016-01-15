import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### 1. MultiIndex (hierarchical index)
# create multi index
# from tuple
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

# generate 'product' of iterables automatically
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
foo = pd.MultiIndex.from_product(iterables, names=['first', 'second'])
foo.get_values()

# use the index when creating Series/DataFrame
s = pd.Series(np.random.randn(8), index=index)

# specify multi index when creating series or dataframe
arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
          np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]
s = pd.Series(np.random.randn(8), index=arrays)
df = pd.DataFrame(np.random.randn(8, 4), index=arrays)











