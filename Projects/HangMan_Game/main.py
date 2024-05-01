### Logic for hangman game: Guess the fruit name

## 1st way to import the module
import random
import hangmanAssets

## 2nd way to import the content inside the module
from hangmanAssets import logo,word_list

print('Welcome to the HANGMAN game')

print(logo)


# select random fruit by computer
chosen_word = random.choice(word_list)

print(f'Word chosen by computer: {chosen_word}')
# creating empty fields
display=[]
players_life = 6

for i in range(len(chosen_word)):
    display.append('_')

print(display)

end_of_game = False
count =0
while not end_of_game:
# checking whether the user's input matched with the chosen_word or not
  user_input = input('Enter the letter : ').lower()


  # acknowledging the user about whether entered letter is already guessed or not
  if user_input in display:
    print(f'The letter has been already guessed: {user_input}')

  for index in range(len(chosen_word)):
    if user_input == chosen_word[index]:
      display[index]=chosen_word[index]
    
  
  # what to do if nothing matches
  if user_input not in chosen_word:
    print('You have made a wrong Guess. Hence we are taking one life from you')
    players_life -=1
    print('Player remaining life is: ',players_life)

    if players_life == 0:
      print('Hangman died because of you')
      print('You have lost the Game!!!!')
      # to exit the while loop and game
      end_of_game = True

  print(display)

  if "_" not in display:
    print('You won the game!!!!!!')
    end_of_game = True
  
  # display the hangman
  print(hangmanAssets.stages[players_life])




