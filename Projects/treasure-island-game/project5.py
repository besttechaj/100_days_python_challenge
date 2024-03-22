
print('Welcome to treasure island. Your mission is to find the treasure')
print('You\'re at a crossroad')
choice = input('Whether you want to go left or right ??')

if choice == "left":
  print('You\'ve come to a lake. There is an island in the middle of the lake. Type \'wait\' to wait for the boat. Type \'swim\' to swim across the lake. ')
  print('Horayy! you have selected the right choice, hence moving you to the next level: 1')

  ## moving to next level
  choice = input('Whether you want to swim or wait ??')
  if choice=="swim":
    print('You have made a wrong choice. Your game is over, Better luck next time!')
  elif choice =="wait":
    print('Horayy! you have selected the right choice, hence moving you to the next level: 2 ')
    ### moving to next level
    print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.')
    door = input('Select any one color: red, blue or yellow?? ').lower()

    if door == "yellow":
      print('Horayy! you have selected the right choice. Congratulations, you have won the game!!!')
    elif door == "blue":
      print('You have made a wrong choice. Your game is over by selecting wrong door, Better luck next time!')
    elif door == "red":
      print('You have made a wrong choice. Your game is over by selecting wrong door, Better luck next time!')
    else:
      print(" you have chosen an color which doesn't exist. Game over!!")
  else:
    print(" you have chosen an option which doesn't exist. Game over!!")

else:
  print('You fell into a hole.')
  print("You have made a wrong choice. Your game is over, Better luck next time!")