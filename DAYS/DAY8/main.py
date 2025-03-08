# Function in python

## What is a function ?
# It is a block of code which is used to perform some particular task.
# Function can take arguments
# We can call one function inside another function
# We can call the function n no. of times

"""def functionName( // parameter){
  // code or return value
}
function calling
functionName(// arguments)"""

outside_weather="rain"

def greet(name, temp, weather):
  print(f'Good Morning {name}. Today\'s temperature is {temp} deg celsius. Maybe it will "{weather}"')

greet("ajay",35, outside_weather)

print('')

## Position vs keyword arguments

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in \"{location}\"")

greet_with(location="mount fuji", name="angela")

## paint calc

h=int(input('Enter the height: '))
w=int(input('Enter the width: '))

def paintCalc(height, width, coverage):
  cansRequired=(height*width)/coverage
  print(f'The total number of cans required to cover the wall is "{cansRequired}"')

paintCalc(width=w, height=h, coverage=5)