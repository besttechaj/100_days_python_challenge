# importing random module
import random



###  easy level


print('Welcome to the password Generator')

password_length = int(input('How many letters would you like in your password?'))

symbols_length = int(input('How many symbol would you like in your password?'))

numbers_length = int(input('How many numbers would you like in your password?'))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

password=""
count =0

# Selecting random symbols
for i in range(1,  symbols_length + 1):
    temp = random.randint(0, symbols_length)
    password += symbols[temp]

print('stage 1: ',password)

# Selecting random letters
for j in range(1, password_length + 1):
    temp = random.randint(0, password_length + 1)
    password += letters[temp]

print('stage 2: ',password)

# Selecting random numbers
for j in range(1, numbers_length + 1):
    temp = random.randint(0, numbers_length + 1)
    password += numbers[temp]

print('stage 3: ',password)

print(f'Your Generated password is : {password} and the length is {len(password)}')



