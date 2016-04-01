import numpy as np


### 1. get normal array from masked array
# create array with mask
x = np.ma.array([1, 100, 2, 3], mask=[False, True, False, False],
                dtype=int)
print("The input integer masked array is:")
print(x)

# fill with np.nan
xnan = np.ma.filled(x.astype(float), np.nan)
print("Converted to double precision, with nan:")
print(xnan)


print("--------------")


### 2. convert to masked array
x = np.array([1.0, 2.5, np.nan, 1.3, np.inf, 7.2])
print("input array with bad values:")
print(x)

xm = np.ma.masked_invalid(x)
print("masked version:")
print(xm)

# count valid (unmasked) entries
xm.count()


# get the 'mask' array
x = np.arange(12).reshape(3, 4)
np.ma.getmaskarray(x)
xm = np.ma.arange(6).reshape(2, 3)
np.ma.getmaskarray(x)
xm.mask


print("--------------")


### 3. mask values in array
x = np.arange(10)
xm = np.ma.masked_greater(x, 5)
xm[[0,2]] = np.ma.masked




### 4. using masked array in computation
x = np.ma.array([1, 2, 3], mask=[False, False, True])
y = np.ma.array([1, 0, 1])

# divide by 0 yields a masked value
x/y

# the same for function with argument outside the domain
np.ma.arcsin([0.8, 1, 100])













