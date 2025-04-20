from sys import getsizeof

var1=100
import sys
print(sys.getsizeof(var1))
# 28
# will output the size (in bytes) of the integer object var1 using Python’s sys.getsizeof() function.
# var1 = 100: Assigns the integer value 100 to the variable var1.
# import sys: Imports the sys module.
# sys.getsizeof(var1): Returns the size in bytes of the object var1, which includes the overhead for Python’s object management.


var="hello python"
print(getsizeof(var))
# 53

