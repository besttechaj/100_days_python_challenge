# bmi calculator

height = float(input('Enter your height (in meter)'))
weight = int(input('Enter your weight (in kg)'))

# using PEMDASLR RULE: parenthesis > exponential > multiplication > division > addition > subtraction
bmi = weight / (height ** 2)

print(" Your calculated Bmi is: ",bmi)

