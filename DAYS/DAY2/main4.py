# Number manipulation and F strings in python

## Number manipulation in python
# rounding the number
print(8/3) # 2.666666666.. 
print(round(8/3)) # 3 (Round off to the nearest integer)
print(round(8/3,2)) # 2.67 (Providing precision value(literal after decimal), hence we are rounding it to 2 decimal places)

# floor division: "//", floor means rounding off to the lowest nearest whole number and also we got the integer datatype.

print(8 // 3) # 2  int data type
print(type (8 / 3) ) #2.0 " float " datatype
print(type (4 / 2) ) #2.0 " float " datatype


# some shortcuts
score = 0;

score +=2
print(score)# 2 

score *=10
print(score)# 20

score /=2
print(score) # 10.0

score -=100 
print(score) # -90.0

## F-String in python

## problem in python: we can't concat the string with any other datatype hence to overcome it we have to convert the result datatype into string to concat it. example
# print('your score is '+ score) ERROR
print('your score is '+ str(score))


## Instead of converting the result datatype to string datatype, we can overcome this problem by using " F- Strings ".
score += 1000
height = 1.8
isWinning = True

print(f"your current score is {score}, your height is {height}, you are winning is {isWinning}")

