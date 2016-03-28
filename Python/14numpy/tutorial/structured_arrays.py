import numpy as np


### 1. simple example
# create with list argument
# in the tuple it is (name, type, (optional)shape)
x = np.array([(1,2.,'Hello'), (2,3.,'World')],
             dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])


# access structured array by field name
y = x['foo']
# y is a view
# the following also changes the underlying data in x
y[:] = 2*y
x[1] = (-1,-1.,'Master')


### 2. other creation methods
# create with dictionary argument, type 1
# optional keys are 'offsets' and 'titles' (titles are just metadata)
x1 = np.zeros(3, dtype={'names':['col1', 'col2'], 'formats':['i4','f4']})

# create with dictionary argument, type 2
# in the tuple it is (type, offset, title)
x2 = np.zeros(3, dtype={'col1':('i1',0,'title 1'), 'col2':('f4',1,'title 2')})


# there are still other creation methods, but not so useful, refer to
# http://docs.scipy.org/doc/numpy/user/basics.rec.html
#x3 = np.zeros(3, dtype='3int8, float32, (2,3)float64')


### 3. accessing
x = np.zeros(3, dtype={'col1':('i1',0,'title 1'), 'col2':('f4',1,'title 2')})

# field names
x.dtype.names
x.dtype.names = ('x', 'y')

# field titles
x.dtype.fields['x'][2]

# multiple fields at once
x = np.array([(1.5,2.5,(1.0,2.0)),(3.,4.,(4.,5.)),(1.,3.,(2.,6.))],
                dtype=[('x','f4'),('y',np.float32),('value','f4',(2,2))])
x[['x','y']]
x[['x','value']]
x[['y','x']]


### 4. filling



















