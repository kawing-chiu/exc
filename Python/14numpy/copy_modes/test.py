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
print("a shape:", a.shape)

# but the underlying data IS shared:
c[0, 3] = 100
print("a:", a)


print("-----------")

# the third is deep copy:
# d is completely not related to a:
d = a.copy()









