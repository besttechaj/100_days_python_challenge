## Tip Calculator

print('Welcome to the tip calculator')

# converting datatype to float
totalBill = float(input('Please enter your total bill: '))



# converting datatype to int
tip = int(input('How much tip would you like to give (in %): '))


# converting tip (%) to decimal value
new_tip = tip * totalBill / 100

# After giving the tip, now the current bill is
totalBalance = totalBill + new_tip

people = int(input('In how many people you want to split the bill: '))

eachPersonAmount = round(totalBalance / people )

print(f'your total bill is: {totalBalance}$')

print(f"your tip amount is: {new_tip}$")

print(f"Each person should pay: {eachPersonAmount}$")