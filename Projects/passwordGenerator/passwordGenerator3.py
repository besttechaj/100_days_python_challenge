# importing random module


### Hard logic and strongest password generator

import random
print('Welcome to the password Generator')

password_length = int(input('How many letters would you like in your password?'))

symbols_length = int(input('How many symbol would you like in your password?'))

numbers_length = int(input('How many numbers would you like in your password?'))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

password=[]
count =0

# Selecting random symbols
for i in range(1,  symbols_length + 1):
    password.append(random.choice(symbols))

# Selecting random letters
for j in range(1, password_length + 1):
    password.append(random.choice(letters))

# Selecting random numbers
for j in range(1, numbers_length + 1):
    password.append(random.choice(numbers))

# Now to shuffle or re-order your list, we need random.shuffle() method
random.shuffle(password)

finalPassword = ""
for char in password:
  finalPassword += char

print(f'Your Generated password is : {finalPassword} and the length is {len(password)}')



