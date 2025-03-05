# MINI PROJECT ON PIZZA DELIVERY

print('Welcome to pizza delivering service')

size =  input('Select your pizza Size: (S, M, L) ? ').upper()

if size == "S":
  bill = 15
  add_pepperoni_smallPizza = input('Do you want pepperoni: (Y or N) ').upper()
  if add_pepperoni_smallPizza == "Y":
    bill += 2
  add_extraCheese_anyPizza = input('Do you want extra cheese: (Y or N) ').upper()
  if add_extraCheese_anyPizza == "Y":
    bill += 1


if size == "M":
  bill = 20
  add_pepperoni_mediumOrLargePizza = input('Do you want pepperoni: (Y or N) ').upper()
  if add_pepperoni_mediumOrLargePizza == "Y":
    bill += 3
  add_extraCheese_anyPizza = input('Do you want extra cheese: (Y or N) ').upper()
  if add_extraCheese_anyPizza == "Y":
    bill += 1

if size == "L":
  bill = 25
  add_pepperoni_mediumOrLargePizza = input('Do you want pepperoni: (Y or N) ').upper()
  if add_pepperoni_mediumOrLargePizza == "Y":
    bill += 3
  add_extraCheese_anyPizza = input('Do you want extra cheese: (Y or N) ').upper()
  if add_extraCheese_anyPizza == "Y":
    bill += 1

print(f" Your final bill is {bill}$")

print("Thankyou for choosing domino's pizza, enjoy your meal")