# love calculator

# taking the inout from the user and converting them to lower case
person1 = input('Enter teh first person name: ').lower()
person2 = input('Enter teh second person name: ').lower()

combined_names = person1 + person2
print(combined_names)

# let's count the first digit in the love score from person1
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

first_digit = t + r + u + e
print(first_digit)

# let's count the second digit in the love score from person2
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

second_digit = l + o + v + e
print(second_digit)

# To get the score
score = int(str(first_digit) + str(second_digit))

print(f"Your love calculator score is {score}")

