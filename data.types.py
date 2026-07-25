# data type is the type of data a variable is capable of storing:
# integer:
x = 5
print(x)
print(type(x)) # data type ==> 'int"

# float:
pi = 3.14159
print(pi)
print(type(pi)) # data type ==> 'float'

# complex (a+bj):
# in python, 'j' is used as the sqrt(-1) instead of 'i'
c = 3+4j
print(c) # returns ==> (3+4j)
print(type(c)) # data type ==> 'complex'
# initializing a complex variable by using complex():
a = 4
b = 10
com = complex(a,b)
print(com) # returns ==> (4+10j)
print(type(com)) # data type ==> 'complex'

# string:
str1 = 'data'
print(str1)
print(type(str1)) # data type ==> 'str'
# ======================================================================
# respective functions for each data type:
# integer:
d = int(23)
print(d)
print(type(d)) # data type ==> 'int'
e = int(pi) # numbers after the decimal are removed
print(e)
print(type(e)) # data type ==> 'int'

# float:
f = float(2.718)
print(f)
print(type(f)) # data type ==> 'float'
f = float(45)
print(f) # returns ==> '45.0'
print(type(f)) # data type ==> 'float'
k = 67
f = float(k)
print(f) # returns ==> '67.0'
print(type(f)) # data type ==> 'float'

# string:
str2 = str('types')
print(str2)
print(type(str2)) # data type ==> 'str'
# ======================================================================
# boolean:
is_it = True
print(is_it) # returns 'True'
print(type(is_it)) # data type ==> 'bool'
fal = bool(False)
print(fal) # returns 'False'
print(type(fal)) # data type ==> 'bool'
a = 30
b = 10
greater = a > b
print(greater) # returns 'True'
print(type(greater)) # data type ==> 'bool'
smaller = a < b
print(smaller) # returns 'False'
print(type(smaller)) # data type ==> 'bool'
# int equivalent of bool:
k = int(True)
print(k) # returns '1'
print(type(k)) # data type ==> 'int'
l = int(False)
print(l) # returns '0'
print(type(l)) # data type ==> 'int'

# None:
var = None
print(var) # returns 'None'
print(type(var)) # data type ==> 'NoneType'

# Sequences:
# list:
l = [1,2,3,4,5]
print(l)
print(type(l)) # data type ==> 'list'
# tuple:
t = (1,2,3,4,5)
print(t)
print(type(t)) # data type ==> 'tuple'
# set:
s = {1,2,3,4,5,1}
print(s)
print(type(s)) # data type ==> 'set'
# range:
# range(n) is a function which starts at '0' and ends at 'n'
r = range(9)
print(r) # returns (0,9)
print(type(r)) # data type ==> 'range'
# sequences using range:
# starts at '0' at ends just before 'n'
print(list(r))
print(tuple(r))
print(set(r))
# using step size in range() ==> range(initial value, final value, step size)
even_num = range(2,10,2)
print(even_num)
print(list(even_num)) # as '10' is the final value, it will not appear in the list
print(type(list(even_num))) # data type ==> 'list'
print(tuple(range(3,3*11,3))) # table of '3'
print(set(range(5,5*11,5))) # table of '5', but unordered since it is a set