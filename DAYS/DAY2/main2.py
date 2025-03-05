# Type conversion

# In python we can't concat numbers with string, it will throw you one error

#? multi line comment in python
'''for multi line comment use 3*' or 3*", but don't assign multiline to a variable else it will not be treated as comment

name = len(input('Enter your name : \n'))
print(type(name), name)
#print('total no. of characters present inside the name is '+ name) --> TypeError, can't concatenate number with string using + operator
# performing type conversion to concat string data "converting integer to string"
new_name = str(name)
print('total no. of characters present inside the name is '+ new_name)

'''

a = 79
print(a,type(a))

# let's convert the number to float
b = float(a)
print(b,type(b))

# converting string to float then concatenating it with number
print(1000 + float("999"), type(1000 + float("999")))

# concatenation string conversion with another string conversion
print(str(10000_00)+str(99_999))# string data type


