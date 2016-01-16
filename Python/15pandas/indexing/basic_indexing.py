import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


### 1. select by label

### 2. select by position

### 3. boolean indexing

### 4. set/reset index
data = pd.DataFrame({'a': ['bar', 'bar', 'foo', 'foo'],
                    'b': ['one', 'two', 'one', 'two'],
                    'c': ['z', 'y', 'x', 'w'],
                    'd': [1, 2, 3, 4]})
data.set_index('c')
data.set_index(['a', 'b'])

# preserve the index column
data.set_index('c', drop=False)
# combine with existing indexes
data.set_index(['a', 'b'], append=True)


# reset_index() is the inverse operation of set_index()
data = data.set_index(['a', 'b'])
data.reset_index()
data.reset_index(level=1)
data.reset_index(level=1, drop=True)


# reset directly by passing new index to .index attribute
index = pd.Index(list('abcd'))
data.index = index





