import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### 1. pivoting
df = pd.read_json('{"date":{"0":946857600000,"1":946944000000,"2":947030400000,"3":946857600000,"4":946944000000,"5":947030400000,"6":946857600000,"7":946944000000,"8":947030400000,"9":946857600000,"10":946944000000,"11":947030400000},"type":{"0":"A","1":"A","2":"A","3":"B","4":"B","5":"B","6":"C","7":"C","8":"C","9":"D","10":"D","11":"D"},"value":{"0":0.166165159,"1":0.8822290382,"2":-0.8743071516,"3":1.7505016019,"4":0.355251611,"5":1.022970019,"6":0.3495012092,"7":-0.218052557,"8":-1.4177411645,"9":1.762476698,"10":0.503148668,"11":-1.4409911553}}')

df.pivot(index='date', columns='type', values='value')
df.pivot(index='type', columns='date', values='value')


### 2. stacking


### 3. melting



### 4. pivot table
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                   'B': ['aa', 'bb', 'cc'] * 8,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                   'D': np.random.randn(24),
                   'E': np.random.randn(24),
                   'F': [datetime.datetime(2016, i, 1) for i in range(1, 13)] +
                        [datetime.datetime(2016, i, 15) for i in range(1, 13)]})
pt_df = df

pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

# when values is omited, all remaining columns that can be aggregated will be 
# used
pd.pivot_table(df, values=['D', 'E'], index=['A', 'B'], columns=['C'])
# the same as above:
pd.pivot_table(df, index=['A', 'B'], columns=['C'])

# the default aggregate func is 'mean'
# three-levels MultiIndex on columns
pt = pd.pivot_table(df, values=['D','E'], index=['B'], columns=['A', 'C'], aggfunc=np.sum)
mi = pt.columns


### 5. cross tabulation
foo, bar, dull, shiny, one, two = 'foo', 'bar', 'dull', 'shiny', 'one', 'two'
a = np.array([foo, foo, bar, bar, foo, foo], dtype=object)
b = np.array([one, one, two, one, two, one], dtype=object)
c = np.array([dull, dull, shiny, dull, dull, shiny], dtype=object)
# the first arg is index, the second is columns
pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])



### 6. dummy variable (indicator variable)









