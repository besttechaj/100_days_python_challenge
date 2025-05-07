# Object-oriented programming: attributes | methods | object

# The turtle library in Python is a graphics module that helps beginners learn programming through visual feedback — by controlling a turtle on the screen to draw shapes, patterns, and more.
# class
# from turtle import Turtle, Screen
# created an object from turtle class
# timmy = Turtle()
# timmy.color('blue','red')
# timmy.shape('turtle')
# print(timmy.circle(100))
# timmy.forward(150)

# my_screen = Screen()
# my_screen.bgcolor('black')
# accessing the attribute
# print(my_screen.canvheight)

# we will exit the popup window once we close it
# my_screen.exitonclick()

# displaying table using prettyTable package ( you need to install this 3rd party package )
# class
from prettytable import  PrettyTable
# object
table = PrettyTable()
# methods
table.add_column('POKEMON NAME',['pikachu','squirtle','charmander'])
table.add_column('TYPE',['electric','water','fire'])
# attributes
table.align='l'
print(table)