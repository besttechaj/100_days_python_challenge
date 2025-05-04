# How to catch an error using try and except block including use of finally block

try:
  age = int(input('Enter your age\n'))
  if age >= 18:
    print('You are eligible to apply for a driving license')
  else:
    print('You are not eligible')
except ValueError:
  print('Please type a valid numerical response')
finally:
  print('\n'*5)