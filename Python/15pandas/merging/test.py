import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


### 1. concatenating
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                     index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])
frames = [df1, df2, df3]

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                 'D': ['D2', 'D3', 'D6', 'D7'],
                 'F': ['F2', 'F3', 'F6', 'F7']},
                index=[2, 3, 6, 7])

## concat
# note that concat() and append() make full copy of the data, so don't call 
# them many times
res_concat = pd.concat(frames)
res_concat_withkey = pd.concat(frames, keys=['x', 'y', 'z'])

# ignore index
pd.concat([df1, df4], ignore_index=True)

# add series as new column
s1 = pd.Series(['X0', 'X1', 'X2', 'X3'], name='X')
pd.concat([df1, s1], axis=1)


## append
# if there are many dataframes to append, a better approach is apend them all 
# in a list and then use pd.concat()
res_append = df1.append(df2)
res_append_overlap = df1.append(df4)
res_append_overlap_ignore_index = df1.append(df4, ignore_index=True)

# append series
s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
df1.append(s2, ignore_index=True)



### 2. database-like joining
## pd.merge()
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# inner join
res_inner = pd.merge(left, right, on=['key1', 'key2'])
# left join
res_left = pd.merge(left, right, how='left', on=['key1', 'key2'])
# outer join
res_outer = pd.merge(left, right, how='outer', on=['key1', 'key2'])



## DataFrame.join()
# DataFrame.join() can be used to join on index, it uses pd.merge() internally
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


# unlike pd.merge(), by default, this is a left join
df_join_left = left.join(right)













