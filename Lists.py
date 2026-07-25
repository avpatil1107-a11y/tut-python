# tuple = unmutable i.e unchageable list
# synatx ==> tuple = mem1,mem2,... (or) tuple = (mem1,mem2,...)
nums = 1,2,3,4,5
nums0 = (6,5,7,8,9)
print(type(nums)) # type() = returns the data type of the variable
print(type(nums0))
# list = mutable linear collection of data.
# syntax ==> list = [mem1, mem2,...]
print(nums)
x = [34,32,4,56,39]
print(type(x))
print(x)
print(nums[4])
print(x[-2])
# slicing = using a specific section/range of a string/list
print(nums[2:5])
print(nums[1:10])
print(nums[3:])
print(x[:4])
print(x[-2:])
print(x[-3:-1])
print(x[-4:4])
print(x[-1:2])
# list of strings:
name = ['yuji','megumi','nobara','gojo','Geto']
print(name)
# list of values of mutiple data-types
mix = ['mei',67,9.6,'utahime']
print(mix)
# list of lists(similar to a matrix):
mix2 = [name,mix,x]
len(mix2) # length will be only "3"
print(mix2)
print(mix2[1]) # each list acts as a member of the bigger list
# for using a specific member of the list(here its "utahime")
print(mix2[1][3])
# combining lists:
mix3 = name + x + mix # forms a list consisting of members of the used lists in order
print(mix3)
# list functions
print(x)
x.append(69) # append = adding a member of given value at the end of the list
print(x)
print(x.count(34)) # count = number of times a member appears in a list
x.insert(3,45) # insert = adding a member at a particular index, syntax ==> list.insert(index,value)
print(x)
x.extend([56,46,73,89]) # extend = appending multiple values
x.remove(39) # remove = removing a member from the list
x.pop(2) # pop = removing a member at a particular index from the list
print(x)
x.pop() # using pop() without specifing the index results in the removal of the very last member, similar to stack data structure
print(x)
del x[2:5] # del = deletion of members from initial to final index mentioned in []
print(x)
x[1:4] = [29,38,47] # reassigning values for given index range as list is mutable
print(x)
x.reverse() # reverse = reversing the order of members of a list
print(x)
x.sort() # sort = sorting a list in ascending order
print(x)
print(min(x)) # min = returns minimum value from the list
print(max(x)) # max = return maximum
print(sum(x)) # sum = returns sum of all members
print(min(name)) # for list for strings, min returns the very first member when all the members are arranged in alphabetical order 
print(max(name)) # max returns member last in the alphabetical order 
# print(sum(name)) ==> results in error as sum of strings cannot be found
# print(min(mix)) ==> error as strings,int,float cannot be compaired. Same applies for fuctions max(), sum(), sort()
mix.reverse()
print(mix)