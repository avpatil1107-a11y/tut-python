# tuple is unmutable collection of data
# data can be either of same data type, or of different data type
tup = 1,2,3,4,5,6
tup1 = (23,51,63,57,38)
print(type(tup)) # returns the data type, here its 'tuple'
print(type(tup1))
# tuple fuctions identical to list fuctions:
print(tup1[3])
print(tup[1:4])
print(len(tup1))  
print(min(tup1))
print(max(tup1))
print(tup1.count(57))
print(tup.index(3))
# reassignmet for tuple is not possible
# tup[3] = 54 ==> error

# tuple with members of different data types
tup2 = (2,'maki',3.24)
print(tup2)
# unpacking a tuple:
num, string, flt = tup2 # using multiple assignment for storing contents of tuple in indivisual varibles
print(num,string,flt)
# number of variables used for unpacking must be equal to len(tuple)
# error "not enough values to unpack" ==> num,num1,string,flt=tuple 
# error 'too many values to unpack" ==> num,string=tuple

# list inside of a tuple:
tup3 = (52,'jogo',[1,23,45,67,89])
print(tup3)
tup3[2][3] = 76 # list inside of a tuple is mutable
print(tup3)
# check for existance of a value in a tuple/list:
print('jogo' in tup3) # returns "True" as "jogo" is a member of tup3
print(45 in tup3) # returns "True"
print('Jogo' in tup3) # returns "False" as check for existance is case sensitive
list1 = [3,2,1,4,8]
print(list1)
print(1 in list1) # returns "True"
print(69 in list1) # returns "False"

# tuple of one element:
tup4 = (3) # incorrect syntax
print(tup4) # only prints ==> 3
print(type(tup4)) # data-type ==> 'int' i.e. 'integer'
tup4 = (3,) # correct syntax
print(tup4) # prints ==> (3,)
print(type(tup4)) # data-type ==> 'tuple'