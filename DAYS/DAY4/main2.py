# virtual coin toss program

import random

result = random.randint(0,1)

if result ==1:
  print('Head')
elif result == 0:
  print('tail')
else:
  print('Not a valid number')