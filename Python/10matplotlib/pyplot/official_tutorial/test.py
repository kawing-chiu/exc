import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### 1. simple line segments and points

# line segments
# if only one list is provided, it is used as y values, the x values are the 
# indexes
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
#plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#plt.show()

# points
# if plt.figure() is not called, the following plot will be drawn on the same 
# canvas as the previous plots
plt.figure()
# the default format is 'b-'
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
#plt.show()

# multiple lines at once
plt.figure()
t = np.arange(0., 5.1, 0.05)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()

plt.close('all')


### 2. setting line properties
# using keyword args in plot()
x = t.copy()
plt.plot(x, x**2, linewidth=3.0)

# using setter methods of the line instance
line, = plt.plot(x, x**3, '-')
line.set_antialiased(False)

# use the setp() function
lines = plt.plot(t, t**(-1), t, t**(-0.5))
# will set the properties on all lines
plt.setp(lines, color='r', linewidth=2.0)
plt.axis([0, 5, 0, 20])
#plt.show()

plt.close('all')

### 3. multiple figures and axes
# two subplots
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# first
plt.figure(1)
# numrows, numcols, fignum, where 1 < fignum < numrows*numcols
# the default subplot value is 111
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# second
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#plt.show()

# close() is always needed, closing the pop-up window is not enough
plt.close('all')


### 4. adding text
# a histogram with some text

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
# note the use of latex
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
#plt.show()

plt.close('all')


### 5. annotation
# arrow annotation on simple cosine curve
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
        arrowprops=dict(facecolor='black', shrink=0.05),
    )
plt.ylim(-2, 2)
#plt.show()


