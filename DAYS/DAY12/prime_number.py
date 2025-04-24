import math
program_continue = True

def prime_or_not(num):
      flag = True
      for i in range(2, int ( math.sqrt(num) ) + 1 ): # optimization
        if num % i == 0:
          flag = False
          print(f'{num} is not a prime number')
          break

      if flag == True:
        print(f'{num} is a prime number')


def game_should_continue():
  user_choice = input('Do you want to restart the game. Type \'y\' to restart or type \'n\' to exit. \n').lower()

  if user_choice == 'n':
    return False
  else:
    print('\n'*15)
    return True

while program_continue:
  number = int(input('Enter a number to check whether it is a prime or not. \n'))

  if number == 0 or number == 1:
    print('Not a prime number')
    program_continue = game_should_continue()

  elif number < 1:
    print('please enter a number > 1')
    program_continue = game_should_continue()

  else:
    prime_or_not(number)
    program_continue = game_should_continue()
