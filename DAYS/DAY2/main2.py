# Type conversion



# In python we can't concat numbers with string, it will throw you one error

'''for multi line comment use ' or ", but don't assign multiline to a variable else it will not be treated as comment

name = len(input('Enter your name : \n'))
print(type(name), name)
# performing type conversion to concat integer to string
new_name = str(name)
print('Your name has ' + ' ' + 'and total characters inside name is '+ new_name)
'''

a = 79
print(type(a))
# let's convert the number to float
b = float(a)
print(type(b))

# converting string to float then concatenating it with number
print(1000 + float("999"))

# concatenation string conversion with another string conversion
print(str(10000_00)+str(99_999))


