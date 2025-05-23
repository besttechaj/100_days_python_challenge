import random

## below two lines are for debugging purpose
user_score = -1
computer_score = -1

# fetching random card from the list
def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def calculate_score(cards):
  # ace (11) + 10 = 21
  if sum(cards) == 21 and len(cards) == 2:
    return 0 ## blackjack(0)
  
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)



def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_a_game():

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
        '''adding 2 cards in each list'''
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

  # user control logic
  while not is_game_over: # run until it sets to True.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards are {user_cards}, current score is {user_score}")
    print(f"Computer's first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_choice = input('Type \'y\' to get another card, type \'n\' to pass \n').lower()

      if user_choice == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
    


  # computer control logic
  while  computer_score != 0 and  computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


  print(f"\nYour final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  # comparing score
  print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack ? Type 'y' or 'n' :" ) == 'y':
   print('\n'*20)
   play_a_game()




