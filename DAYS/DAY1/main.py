# Write your code below this line 👇
print('hello world')

#?  string
print("this is lesson 1")
print("this is 'python' tutorial")
print(' this is "python" tutorial')
# Using Triple Quotes (""" or ''') :for Multi-line Strings
print("""triple quotes example""")
print('''triple quotes example''')

#? escape character
# to acknowledge the written content as a string, we can use the escape character \"
print("hello coder this is day-1 of \"python\" tutorial")

#? to print multiple lines in a single print statement, we can use \n (\n is a newline character, which moves the text after it to the next line.)
print("hello developers......\n this is day-1 of \"python\" tutorial")

# string concatenation
print("introvert:" + " shy")
print("extrovert:" + " " + "sociable")

#? multi-line string in python
# way-01
print("""hare krishna hare krishna
krishna krishna hare hare""")

# way-02 : using \n is a newline character, backslash
print("hare rama hare rama\n rama rama hare hare")

#? IndentationError: In python we should write the code from beginning of the line else it will throw you one indentation Error if you give some space before the beginning of the code
#__print('don\'t give any space')
print('don\'t give any space')

## code intelligence: make sure it is enabled. Code intelligence gives you autocomplete, as well as hints as you type.

#? input function: The input() function is used to take user input in Python. It always returns the input as a string unless explicitly converted to another type.
# input('Enter your name')
# input("Hello, " + input("Enter your name"))

#? Multiple Inputs in One Line: Use split() to take multiple inputs at once.
x, y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)

#? Using eval() for Direct Conversion: Instead of int() or float(), you can use eval() to automatically convert numbers.
x = eval(input("Enter a number: "))
print("You entered:", x)


# len() function: It is used to get the length of the string.
# print(len(input("Enter your name")))

# variables in python: It is used to store the data.Hence we can use the variable to refer the data.
# data = input("Enter your name: ")
# print(data)