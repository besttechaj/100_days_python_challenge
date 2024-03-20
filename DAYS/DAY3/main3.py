# nested if else condition and    if elif condition

height = float(input('Enter your height in cm: \n'))

if height >= 120:
  print('you can ride')
  age = int(input('Enter your age in years: \n'))
  if age >= 18:
    print('total price is 15$')
  elif age >= 12:
    print('Total price is 10$')
  else:
    print('Total price is 5$')
else:
  print('you cannot ride')


