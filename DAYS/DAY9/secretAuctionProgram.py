bidder_chart= {}
continue_bid = True

# comparing bids in dictionary
def find_highest_bidder(bidder_chart):
  highest_bid = 0
  winner = ""
  for bidder in bidder_chart:
    bid_current = bidder_chart[bidder]
    if bid_current > highest_bid:
      highest_bid = bid_current
      winner = bidder
  print(f'The highest secret bidder winner is {winner}:{bidder_chart[winner]}')


while continue_bid:
    name = input('What your name ?\n')
    bid_amount = int(input(' \'What\'s your bid ? \n'))
    bidder_chart[name] = bid_amount
    other_bidder = input('Are there any other bidders ? \'yes\' or \'no\'.\n').lower()
    if other_bidder == 'no':
      continue_bid = False
      find_highest_bidder(bidder_chart)
    elif other_bidder == 'yes':
      print("\n"*20) ## escaping lines so that other bidder can't see previous bid






