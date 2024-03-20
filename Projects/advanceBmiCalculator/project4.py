# bmi calculator

# converting height's unit from cm to meter
height = float(input('Enter your height (in cm)'))/100

weight = int(input('Enter your weight (in kg)'))


# using PEMDASLR RULE: parenthesis > exponential > multiplication > division > addition > subtraction
bmi = weight / (height ** 2)

print(" Your calculated Bmi is: ",bmi)


if bmi >= 35:
  print(f'Your bmi is {bmi}, you are clinically obese')
elif bmi >= 30:
  print(f'Your bmi is {bmi}, you are obese')
elif bmi >= 25:
  print(f'Your bmi is {bmi}, your are slightly overweight')
elif bmi >= 18.5:
  print(f'Your bmi is {bmi}, your have a normal weight')
else:
  print(f'Your bmi is {bmi}, you are underweight')