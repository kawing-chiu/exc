import numpy as np


# there are three modes of copy in np

a = np.arange(12)

# the first is "no copy":
b = a
print("b is a:", b is a)

print("-----------")

# the second is "view" (or "shallow copy")
c = a.view()
print("c.base is a:", c.base is a)

# shape is not shared:
c.shape = (2, 6)
print("a's shape:", a.shape)

# but the underlying data IS shared:
c[0, 3] = 100
print("a:", a)

# slicing also return a view:
print("a[0:3].base is a:", a[0:3].base is a)
# however indexing using an array is a different story


print("-----------")

# the third is deep copy:
d = a.copy()
# d is completely not related to a

# note that the built-in list.copy() (since Python 3.3) is shallow copy, NOT
# deep copy! However, since np.array contains only simple (immutable) data, the
# result is the same.
l = [1, [1, 3], 5]
ll = l.copy()
ll[1][0] = 300
print(l)

print("-----------")

# unlike slicing, indexing using another array or list is a deep copy:
e = a[np.array([5, 7, 9])]
# the same
#e = a[ [5, 7, 9] ]
print("e.base is a:", e.base is a)
e[0] = 500
print("e:", e)
print("a:", a)






