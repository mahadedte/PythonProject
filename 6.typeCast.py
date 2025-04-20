x = 10
print(type(x))
x1 = float(x)
print(x1)
print(type(x1))
x2 = complex(x1)
print(x2)
print(type(x2))

# <class 'int'>
# 10.0
# <class 'float'>
# (10+0j)
# <class 'complex'>

print("next")
a = 10
b = 20
c = complex(a, b)
print(c)
# (10+20j)
d = complex(b, a)
print(d)
# (20+10j)
