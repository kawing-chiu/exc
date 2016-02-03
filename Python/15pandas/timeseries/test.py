from datetime import datetime

import numpy as np
import pandas as pd import matplotlib as mpl
import matplotlib.pyplot as plt



### 1. generate sequences of dates or time-spans
##
rng = pd.date_range('1/1/2011', periods=72, freq='H')
rng[:5]

ts = pd.Series(np.random.randn(len(rng)), index=rng)

converted = ts.asfreq('45Min', method='pad')

ts.resample('D', how='mean')


##
dates = [pd.Timestamp('2012-05-01'), pd.Timestamp('2012-05-02'), pd.Timestamp('2012-05-03')]
ts = pd.Series(np.random.randn(3), dates)
pd.Index(dates)


##
pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]))
pd.to_datetime([1349720105, 1349806505, 1349892905,
             1349979305, 1350065705], unit='s')
pd.to_datetime([1349720105100, 1349720105200, 1349720105300,
             1349720105400, 1349720105500 ], unit='ms')

##
index = pd.date_range('2000-1-1', periods=1000, freq='M')

start = datetime(2011, 1, 1)
end = datetime(2012, 1, 1)
rng = pd.date_range(start, end)

# frequencies can be combined
pd.date_range(start, periods=10, freq='2h20min')


### 2. DatetimeIndex
# DatetimeIndex is an index of Timestamps, it is usually created by 
# to_datetime() or date_range()

rng = pd.date_range(start, end, freq='BM')
ts = pd.Series(np.random.randn(len(rng)), index=rng)

ts['1/31/2011']
ts[datetime(2011, 12, 25):]
ts['10/31/2011':'12/31/2011']


##
dft = pd.DataFrame(np.random.randn(100000,1), columns=['A'],
        index=pd.date_range('20130101',periods=100000,freq='T'))

dft['2013-1':'2013-2']
dft.loc['2013-1-15 12:30:00']

##
# unlike when using strings, when using datetime objects, the indexing is 
# always 'exact'
dft[datetime(2013, 1, 1):datetime(2013,2,28)]


##
# special 'datetime' Series:
s = pd.Series(pd.date_range('20130101 09:10:12', periods=4))
s.dt.year
# behave like
ts.index.year
# s does not have a DatetimeIndex
s.index


### 3. DateOffset
# DatetimeIndex
rng = pd.date_range('2012-01-01', '2012-01-03')
# 'special series'
s = pd.Series(rng)

rng + pd.DateOffset(months=2)
s + pd.DateOffset(months=2)


### 4. time series methods
# convert to python datetime
dft.index.to_pydatetime()

# frequency conversion


# date_range(), reindex() and fill_na() are often used together to process 
# time-based data

### 5. resampling
# the 'time-based groupby'
rng = pd.date_range('1/1/2012', periods=1200, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

# default of how is 'mean'
ts.resample('5Min', how='sum')
ts.resample('5Min', how='ohlc')
ts.resample('5Min', how=np.max)

# up sampling
ts[:2].resample('250ms')
ts[:2].resample('250L', fill_method='pad')
ts[:2].resample('250L', fill_method='pad', limit=2)


### 6. time span
# Period represents a span in time rather than a point in time








