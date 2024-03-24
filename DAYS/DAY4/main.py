# Randomisation
# To generate random integer, we have tom import "random module".

# what is a module ?
# Suppose a company make the cars. It is not possible for a single person to create everything by himself. Instead they will create teams to work on different parts of a car. Such teams is like a module which performs different operations. Hence whenever we are writing our code, it can be getting too big or highly complex so to deal with it we are dividing our codes in different module and later point we will integrate any module at any point of time. In this way we are making our code more reliable and easy to understand with less complexity.
# In python there are many numbers of modules present inside it. We can access it at any point to time to use it. to import the module we have to declare like: import module_Name

# we can create our own custom module

# importing module: here random module is a python module
import random
random_integer = random.randint(100,200)# specifying the range
print(random_integer)

# importing custom module
import my_custom_module
print(f"my sister name is {my_custom_module.name}")


# Generating random floating point numbers
## random.random(): returns random floating point number between 0.0 to 1.0
random_float = random.random()
print(random_float)

## How to create a random decimal number between 0 to 5?
decimal_value = random_float * 5
print(decimal_value)
