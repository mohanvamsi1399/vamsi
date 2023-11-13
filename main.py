#integer expicit bool
num=bool(10)
print(num)
print (type(num))

#integer explicit octal
num = 0o5674
print(num)
print (type(num))

#integer  annotaion
num :int= 10
print(num)
print(type(num))

#float implicit
num=99.99
print(num)
print(type(num))

#float explicit
print(num)
print(type(num))

#float (data annotation)
num : float = 99.99
print(num)
print(type(num))

#exponential implicit
num = float(16.23333e8)
print(num)

#exponential expilcit
num = (3.22e8)
print(num)

#complex impicit
a = 99+98j
b = 98-35j
print(a+b)
print(type(a+b))

#explict
a=complex(34)
print(a)

#annotation
a : complex =99
print(a)