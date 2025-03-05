#! python arithmetic operators
'''
#? Priority for arithmetic operations: known as P_E_M_D_A_S_L_R (parenthesis > exponential [consider ypu are having sequence of exponential :Exponentiation (**) follows Right to Left order] > multiplication || division || floor division || modulus ) based on traversing from LEFT TO RIGHT, whichever comes first > ( addition || subtraction ) left to right
parenthesis: ()
exponents: base ** exponents
multiplication: *
division: /
addition: +
subtraction: -

'''

# division: Return type of division is "float"
print(6/3,type(6/3)) # 2.0, class float

# power: base ** exponential
print(3**2, type(3**2)) #class int

print(3 * (3 + 3) /  3 - 3); # 3.0


#! Exception: Exponentiation (**) follows Right to Left order
result = 2 ** 3 ** 2
# Right to left: (3 ** 2) = 9, then 2 ** 9 = 512
print(result)  # 512