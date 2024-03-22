# LOGICAL OPERATORS: TO CHECK MULTIPLE CONDITION ON THE SAME LINE OF CODE

## "and" operator: all conditions must be true to get True else it return False.

## "or" operator: any one condition must be true to get True else it return False.

## "not" operator: if the condition is true, it becomes false and vice versa.


# updating previous code logics using logical operators to perform some optimization.


height = float(input('Enter your height in cm: \n'))
photo_cost = 3

# verifying their height
if height >= 100:
  print('you can ride')

  # conditions to check their age
  age = int(input('Enter your age in years: \n'))

  
  ## new line using logical "and" operator
  if age >=40 and age <= 50:
    ticket_price = 0
    print(f'total price is ${ticket_price}$')


  elif age >= 18:
    ticket_price = 15
    print(f'total price is ${ticket_price}$')
  elif age >= 12:
    ticket_price = 10
    print(f'Total price is ${ticket_price}$')

  else:
    ticket_price = 5
    print(f'Total price is ${ticket_price}$')
  
  # want to take photo or not???
  want_photo = input('Do you want a photo taken? Y or N.')
  if want_photo == "Y":
      ticket_price += photo_cost
  print(f"your total bill is ${ticket_price}")
else:
  print('you cannot ride')




