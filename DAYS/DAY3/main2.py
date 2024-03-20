# Program to check whether the number is even or odd

number = int(input('Enter your number here: \n'))

## note: " % " modulus operator gives remainder whereas " / " division gives quotient

if number % 2 ==0:
  print('Even number')
else:
  print('Odd number')