# Below code is to check multiple all if conditions whereas In case of if elif only must condition must satisfied

height = float(input('Enter your height in cm: \n'))
photo_cost = 3

# verifying their height
if height >= 120:
  print('you can ride')

  # conditions to check their age
  age = int(input('Enter your age in years: \n'))
  if age >= 18:
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




