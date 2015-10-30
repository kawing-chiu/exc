
adders = [0,1,2,3]
for i in [0,1,2,3]:
   adders[i] = lambda a: i+a

print(adders[1](3))
