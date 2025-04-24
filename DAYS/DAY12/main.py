# local vs global scope

# global scope
enemies = 33
war_plane = 5

def game():

  def increase_enemies():
    # local scope
    enemies = 2
    print(f'Enemies inside the function: {enemies}, plane status: {war_plane} ')

  increase_enemies()

game()
print(f'enemies outside function is {enemies}')
