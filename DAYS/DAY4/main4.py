import random

# friend names
friend_names = "vishal, prashant, ajay, roshini";

# splitting the string into array using string's built-in split() method
# split() : takes one separator
friends = friend_names.split(', ');

total_length = len(friends)

target = random.randint(0, total_length - 1)

print(f"{friends[target]} is going to buy the meal during meetup!")