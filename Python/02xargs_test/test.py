
import sys

# In the following command line, '{}' has not effect:
# $ find ../ -print0 | xargs -0 -L 20 python test.py '{}'
#
# To insert arguments in the middle of the command line, -I must be used, 
# however, using -I implies -L 1, which means only one argument is processed a 
# time. This seems to be a limitation of xargs.
print(sys.argv)
