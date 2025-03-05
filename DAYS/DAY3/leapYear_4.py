
#? write a program to check whether year is leap or not
# leap year: Normal year has 365 days whereas leap year has 366 days.

year = int(input('ENTER YOUR YEAR: \n'))

if year % 4 ==0:
  if year % 100 ==0:
        if year % 400 ==0:
          print('Leap year')
        else:
          print('Not a leap year')
  else:
        print('leap year')
else:
  print('Not a leap year')





