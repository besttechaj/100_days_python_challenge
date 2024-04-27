# Loops in python

# For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is “for in” loop which is similar to foreach loop in other languages.
"""
fruits = ["apple", "grapes", "banana", "papaya"]

for fruit in fruits:
  print(fruit)"""


### WAP TO CALCULATE AVERAGE HEIGHT OF STUDENT PRESENT INSIDE A CLASS
# Return a list of the substrings in the string, using sep as the separator string.
"""students_height= input().split()

print(students_height)

totalHeight=0

for student in students_height:
  print(student)
  print(type(student))
  totalHeight += int(student)

print(f" The total heights of all the student is: {totalHeight}")

## to get the number of students inside a list
n = 0
for stud in students_height:
  n+=1

print(f" The total number of all the students present in a class is: {n}")

## to get the average height of a class
result = round(totalHeight/n)

print(f" The average height in a class: {result}")"""

### WAP TO CALCULATE HIGHEST SCORE FROM A LIST OF SCORES

"""scores = input().split()

print(scores)

# converting the list data's datatype from string to int

for n in range(0, len(scores)):
  scores[n]=int(scores[n])

high=0

for score in scores:
  if score > high:
    high = score

print(f" The highest score in the class is: {high}")"""


### Range function: Generates number to loop through.
"""# It will take 3 parameters ie., starting index, ending index -1 and when the step is given, it specifies the increment.

# without giving 3rd parameter
for i in range(1,5):
  print(i)

# using 3rd parameter ie. increment by +3
for i in range(1,10,2) :
  print(i)"""

### to add all the number between 1 to 100.
"""sum =0
for i in range(1,101):
  sum+=i
print(f"The addition of number from 1 - 100 is: {sum}")"""


### to add all the even numbers between 1 to x
#! way 1: writing the logic for even number
"""x = int(input('Enter the last range: \n'))
even_number =0
for n in range(1, x):
  if n % 2 ==0:
    even_number += n
print(f"The addition of all the even numbers is: {even_number}")"""

#! way 2: by passing 3rd argument inside range function that is "step means increment_value"
"""x = int(input('Enter the last range: \n'))
even_number =0
for n in range(1, x, 2):
    even_number += n
print(f"The addition of all the even numbers is: {even_number}")"""

### WAP to create fizzBuzz game

"""for n in range(1,100 + 1):
  if n % 3 == 0 and n % 5 != 0:
    print('fizz')
  elif n % 5 == 0 and n % 3 != 0:
    print('buzz')
  elif n % 3 == 0 and n % 5 == 0:
    print('fizzBuzz')
  else:
      print(n)"""